# Computational Geometry

......

<!--more-->

https://alatown.com/spline-history-architecture/

https://pages.mtu.edu/~shene/COURSES/cs3621/NOTES/spline/de-Boor.html

https://github.com/caadxyz/DeBoorAlgorithmNurbs

======

https://mitocw.ups.edu.ec/courses/mechanical-engineering/2-158j-computational-geometry-spring-2003

https://www3.cs.stonybrook.edu/~gu/selected_publications/books.html

# CAE_isogeometric

https://en.wikipedia.org/wiki/Isogeometric_analysis

https://coreform.com/

<!--more-->

https://www.cee.ed.tum.de/en/st/research/finite-element-technology/isogeometric-analysis/

https://link.springer.com/article/10.1007/s11831-022-09752-5 2022

https://www.sciencedirect.com/science/article/abs/pii/S0378475415001214 2015

https://www.sciencedirect.com/science/article/abs/pii/S0045782504005171 2005

https://view.inews.qq.com/a/20240129A00QI800

......

------

https://www.ams.org/journals/notices/201508/201508-full-issue.pdf

August 2016

1–5 XVI International Conference on Hyperbolic Problems: Theory, Numerics, Applications, RWTH Aachen University, Aachen, Germany.

The objective of the conference is to bring together scientists with interests in the theoretical, applied, and computational aspects of hyperbolic partial differential equations and of related mathematical models appearing in the area of applied sciences.

Information: www.hyp2016.de

https://arxiv.org/abs/1705.02151

------

Use of surface descriptions, especially in such fields as computer aided design and manufacturing, **isogeometric** analysis, computer graphics, computer vision and computer animation ... is also of interest in geographic information systems, multimedia, and many other areas of science and medicine.

Information: www.ima.org.uk/conferences/conferences_calendar15th_maths_of_surfaces.html


------


https://news.ycombinator.com/item?id=27517503


/ 1. 

/> Another blocker is that CAD is a relatively small part of mechanical engineering. Pretty much all software engineers use version control, but depending on subfield/company, maybe 20-50% of mechanical engineers will use CAD significantly. Mostly the design guys. The engineers in test, analysis, materials will barely touch it.

/ 2. 

/> On the other hand, CAD software is much more complicated than most systems I interact with. CAD platforms are one of the few remaining software systems that are written for experts. Experienced practioners are very productive [2]. So programming these systems will also be complicated.
[2] https://www.youtube.com/watch?v=G3rho-24DWQ&t=184s

/ 3. 

/ >> How are you handling the fact that it seems like none of the computational geometry algorithms parallelize?

/ >> Even something as fundamental as line segment intersection doesn't seem to have any good parallel algorithms.

/ > We don't need parallel algorithms at the lowest level. A NURBS model consists of a large number of surfaces and trim curves. You'll be hard pressed to find "standard" algorithms for NURBS boolean operations, but jwesthues (creator of solvespace) chose a fairly good process for handling them. To combine 2 NURBS shells we compute intersections of each curve from A against each surface from B as one step in the process. Finding all those intersections can be done in parallel. Each step in the boolean process can similarly be done in parallel at either the curve or surface level.

/ > We also do triangle mesh creation in parallel now, as each surface patch is triangulated separately it was easy to run them in parallel. This was a huge win for things like a torus where there are many surface patches with compound curvature and lots of triangles.

/ > We had one nasty bug where dragging some geometry around would start to distort a couple surfaces. Turns out there is a function to intersect a ray with a NURBS surface that recursively subdivides the surface. The recursive subdivision was altering the weights of the original surface control points and then putting them back. Running that on multiple threads at once could lead to corruption. I don't recall how I tracked that down, but the fix was to simply make a copy of the surface and discard it when done rather than changing the original. This whole ray-surface intersection thing is another example of an algorithm that doesn't really benefit from parallelization for a single call, but there's no reason we can't go up a level and have multiple threads calling that function with different ray/surface combination.

/ > I was really pleased that most of the complicated code in Solvespace is written in a functional style - meaning it doesn't mutate data. Another part of the NURBS boolean process is to create a BSP-tree for each surface, which is then discarded after the operation is complete. Once again, that can be done in parallel over all the surfaces even though it'd be hard to create a single BSP-tree using parallel code.
