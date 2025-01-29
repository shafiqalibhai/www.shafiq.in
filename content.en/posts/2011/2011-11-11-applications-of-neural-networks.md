---
title: Applications of Neural Networks
author: Shafiq Alibhai
draft: true
date: 2011-11-11T05:48:11+00:00
categories:
  - Uncategorized

---

  **Download Link : <a href="/wp-content/uploads/2011/11/2-appliations.doc">Appliations</a>**

Chapter 1. Introduction

  1.
      **Introduction to neural networks**

  **1.1 What is a Neural Network?**

  An <a class="zem_slink" title="Artificial neural network" href="http://en.wikipedia.org/wiki/Artificial_neural_network" rel="wikipedia">Artificial Neural Network</a> (ANN) is an <a class="zem_slink" title="Information processing" href="http://en.wikipedia.org/wiki/Information_processing" rel="wikipedia">information processing</a> paradigm that is inspired by the way biological <a class="zem_slink" title="Nervous system" href="http://en.wikipedia.org/wiki/Nervous_system" rel="wikipedia">nervous systems</a>, such as the brain, process information. The key element of this paradigm is the novel structure of the information processing system. It is composed of a <a class="zem_slink" title="Large numbers" href="http://en.wikipedia.org/wiki/Large_numbers" rel="wikipedia">large number</a> of highly interconnected processing elements (neurons) working in unison to solve specific problems. ANNs, like people, learn by example. An ANN is configured for a specific application, such as pattern recognition or data classification, through a <a class="zem_slink" title="Learning" href="http://en.wikipedia.org/wiki/Learning" rel="wikipedia">learning process</a>. Learning in biological systems involves adjustments to the synaptic connections that exist between the neurons. This is true of ANNs as well.

  **1.2 Why use neural networks?**

  <a class="zem_slink" title="Neural network" href="http://en.wikipedia.org/wiki/Neural_network" rel="wikipedia">Neural networks</a>, with their remarkable ability to derive meaning from complicated or imprecise data, can be used to extract patterns and detect trends that are too complex to be noticed by either humans or other computer techniques. A trained neural network can be thought of as an "expert" in the category of information it has been given to analyze. This expert can then be used to provide projections given new situations of interest and answer "what if" questions.

 Other advantages include:

  Adaptive learning: An ability to learn how to do tasks based on the data given for training or initial experience.

  <a class="zem_slink" title="Self-organization" href="http://en.wikipedia.org/wiki/Self-organization" rel="wikipedia">Self-Organization</a>: An ANN can create its own organization or representation of the information it receives during learning time.

  Real Time Operation: ANN computations may be carried out in parallel, and special hardware devices are being designed and manufactured which take advantage of this capability.

  <a class="zem_slink" title="Fault-tolerant system" href="http://en.wikipedia.org/wiki/Fault-tolerant_system" rel="wikipedia">Fault Tolerance</a> via Redundant Information Coding: Partial destruction of a network leads to the corresponding degradation of performance. However, some network capabilities may be retained even with major network damage.

  **1.3 Neural networks versus conventional computers**

  Neural networks take a different approach to <a class="zem_slink" title="Problem solving" href="http://en.wikipedia.org/wiki/Problem_solving" rel="wikipedia">problem solving</a> than that of conventional computers. Conventional computers use an algorithmic approach i.e. the computer follows a set of instructions in order to solve a problem. Unless the specific steps that the computer needs to follow are known the computer cannot solve the problem. That restricts the problem solving capability of conventional computers to problems that we already understand and know how to solve. But computers would be so much more useful if they could do things that we don't exactly know how to do.

  Neural networks process information in a similar way the human brain does. The network is composed of a large number of highly interconnected processing elements (neurons) working in parallel to solve a specific problem. Neural networks learn by example. They cannot be programmed to perform a specific task. The examples must be selected carefully otherwise useful time is wasted or even worse the network might be functioning incorrectly. The disadvantage is that because the network finds out how to solve the problem by itself, its operation can be unpredictable.

  On the other hand, conventional computers use a cognitive approach to problem solving; the way the problem is to solved must be known and stated in small unambiguous instructions. These instructions are then converted to a high level language program and then into machine code that the computer can understand. These machines are totally predictable; if anything goes wrong is due to a software or hardware fault.

  Neural networks and conventional algorithmic computers are not in competition but complement each other. There are tasks are more suited to an algorithmic approach like arithmetic operations and tasks that are more suited to neural networks. Even more, a large number of tasks, require systems that use a combination of the two approaches (normally a conventional computer is used to supervise the neural network) in order to perform at maximum efficiency.

  Neural networks do not perform miracles. But if used sensibly they can produce some amazing results.

<table width="608" cellspacing="0" cellpadding="1">
  <tr valign="TOP">
    <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="577" height="13">
      <p class="western" style="margin-bottom:.21cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
        **2****.1 Co Evolution of Neural Networks for Control of Pursuit & Evasion**

    </td>
    
    <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" colspan="3" width="27">

  <tr valign="TOP">
    <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" colspan="2" width="582">
      <p class="western" style="margin-bottom:.35cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
        The following MPEG movie sequences illustrate behavior generated by dynamical recurrent neural network controllers co-evolved for pursuit and evasion capabilities. From an initial population of random network designs, successful designs in each generation are selected for reproduction with recombination, mutation, and gene duplication. Selection is based on measures of how well each controller performs in a number of pursuit-evasion contests. In each contest a pursuer controller and an evader controller are pitched against each other, controlling simple "visually guided" 2-dimensional autonomous virtual agents. Both the pursuer and the evader have limited amounts of energy, which is used up in movement, so they have to evolve to move economically. Each contest results in a time-series of position and orientation data for the two agents.

      <p style="margin-bottom:.18cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
        These time-series are then fed into a custom 3-D movie generator. It is important to note that, although the chase behaviors are genuine data, the 3D structures, surface physics, and shading are all purely for illustrative effect.
      
      
      <p style="margin-bottom:.18cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="CENTER">
        
      
      
      <table width="464" cellspacing="0" cellpadding="0">
        <col width="464" /> <tr>
          <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="464">
            <p class="western" style="margin-bottom:.35cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
              <span style="font-size:x-small;">1. The pursuer is not very good at pursuing, and the evader is not very good at evading.
            
            
            <p style="margin-bottom:.18cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
              <span style="font-size:x-small;">2. Pursuer chases evader, but soon runs out of energy, allowing the evader to escape.
            
            
            <p style="margin-bottom:.18cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
              <span style="font-size:x-small;">3. Pursuer chases evader, but uses up all its energy just before the evader runs out of energy.
            
            
            <p style="margin-bottom:.21cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
              <span style="font-size:x-small;">4. After a couple of close shaves, the pursuer finally catches the evader.
            
          
      
      
      <p class="western" style="margin-bottom:.35cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
        </td> 
        
        <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" colspan="2" width="22">
        </td></tr>   
        
        
          
            <table style="font-family:'Times New Roman';" width="552" cellspacing="0" cellpadding="2">
              <col width="22" /> <col width="522" /> <tr valign="TOP">
                <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="22" height="20">
                  <p class="western" style="margin-bottom:.21cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                    **2.2**
                  
                </td>
                
                <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="522">
                  <p class="western" style="margin-bottom:.21cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                    **Learning the Distribution of Object Trajectories for Event Recognition**
                  
                </td>
              </tr>
            
            
            
              
                <div style="font-family:'Times New Roman';line-height:normal;font-size:medium;" align="RIGHT">
                  <table width="652" cellspacing="0" cellpadding="2">
                    <col width="316" /> <col width="2" /> <col width="322" /> <tr>
                      <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" colspan="3" valign="TOP" width="648" height="205">
                        <p class="western" style="margin-bottom:.21cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;margin-left:1.23cm;" lang="en-US" align="JUSTIFY">
                          This research work is about the modeling of object behaviors using detailed, learnt statistical models. The techniques being developed will allow models of characteristic object behaviors to be learnt from the continuous observation of long image sequences. It is hoped that these models of characteristic behaviors will have a number of uses, particularly in automated surveillance and event recognition, allowing the surveillance problem to be approached from a lower level, without the need for high-level scene/behavioral knowledge. Other possible uses include the random generation of realistic looking object behavior for use in Virtual Reality, and long-term prediction of object behaviors to aid occlusion reasoning in object tracking. 
                        
                      </td>
                    </tr>
                    
                    <tr valign="TOP">
                      <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="316">
                        <p class="western" style="margin-bottom:.35cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                          <span style="font-size:x-small;">1. The model is learnt in an unsupervised manner by tracking objects over long image sequences, and is based on a combination of a neural network implementing Vector <span style="font-size:x-small;">Quantization and a type of neuron with short-term memory capabilities.
                        
                        
                        <p style="margin-bottom:.21cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                          <a style="color:#0000ff;" href="http://tralvex.com/pub/nap/video/jn-learn.mpg" target="_blank"></a><span style="font-size:x-small;">
 <a style="color:#0000ff;" href="http://tralvex.com/pub/nap/video/jn-learn.mpg" target="_blank">1. Learning mode</a>

                      </td>
                      
                      <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="2">
                      </td>
                      
                      <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="322">
                        <p style="margin-bottom:.18cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                          <span style="font-size:x-small;">2. Models of the trajectories of pedestrians have been generated and used to assess the typicality of new trajectories (allowing the identification of `incidents of interest' within the scene), predict future object trajectories, and randomly generate new trajectories.
                        
                        
                        <p style="margin-bottom:.21cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                          <a style="color:#0000ff;" href="http://tralvex.com/pub/nap/video/jn-pred.mpg" target="_blank"></a><span style="font-size:x-small;">
 <a style="color:#0000ff;" href="http://tralvex.com/pub/nap/video/jn-pred.mpg" target="_blank">2. Predict mode</a>

                      </td>
                    </tr>
                  
                
                
                
                  
                    <table style="font-family:'Times New Roman';" width="626" cellspacing="0" cellpadding="2">
                      <col width="36" /> <col width="276" /> <col width="86" /> <col width="212" /> <tr valign="TOP">
                        <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="36" height="15">
                          <p class="western" style="margin-bottom:.21cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                             **2.3**
                          
                        </td>
                        
                        <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" colspan="2" width="366">
                          <p class="western" style="margin-bottom:.21cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                            **Radiosity for Virtual Reality Systems (ROVER)**
                          
                        </td>
                        
                        <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="212">
                        </td>
                      </tr>
                      
                      <tr>
                        <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" colspan="4" valign="TOP" width="622">
                          <p class="western" style="margin-bottom:.35cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                            The synthesis of actual and computer generated photo-realistic images has been the aim of artists and graphic designers for many decades. Some of the most realistic images (see <a style="color:#0000ff;" href="http://tralvex.com/pub/rover/gg0.htm">Graphics Gallery</a> - simulated steel mill) were generated using radiosity techniques. Unlike ray tracing, radiosity models the actual interaction between the lights and the environment. In photo realistic Virtual Reality (VR) environments, the need for quick feedback based on user actions is crucial. It is generally recognised that traditional implementation of radiosity is computationally very expensive and therefore not feasible for use in VR systems where practical data sets are of huge complexity. In the original thesis, we introduce two new methods and several hybrid techniques to the radiosity research community on using radiosity in VR applications.
                          
                          
                          <p style="margin-bottom:.18cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                            On the left column, flyby, walkthrough and a virtual space are first introduced and on the left. On the right, we showcase one of the two novel methods which were proposed using Neural Network technology.
                          
                          
                          <p style="margin-bottom:.18cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                            
                            
                            <tr valign="TOP">
                              <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" colspan="2" width="316">
                                <p style="margin-bottom:.18cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                                  <a name="Flyby"></a><span style="font-size:x-small;">Introduction to Flyby, Walkthrough and Virtual Space
                                
                                
                                <p style="margin-bottom:.18cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                                  <a style="color:#0000ff;" href="http://tralvex.com/pub/nap/video/ty-flyby.mpg" target="_blank"><span style="font-size:x-small;">
 Flyby</a>

                                <p style="margin-bottom:.18cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                                  <a style="color:#0000ff;" href="http://tralvex.com/pub/nap/video/ty-walk.avi" target="_blank"></a><span style="font-size:x-small;">
 <a style="color:#0000ff;" href="http://tralvex.com/pub/nap/video/ty-walk.avi" target="_blank">3D Walkthrough</a>

                                <p style="margin-bottom:.21cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                                  <a style="color:#0000ff;" href="http://tralvex.com/pub/nap/video/ty-offvr.mov" target="_blank"></a><span style="font-size:x-small;">
 <a style="color:#0000ff;" href="http://tralvex.com/pub/nap/video/ty-offvr.mov" target="_blank">Virtual Space</a>

                              </td>
                              
                              <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" colspan="2" width="302">
                                <p style="margin-bottom:.18cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                                  <a name="ROVER_Learning"></a><span style="font-size:x-small;">(A) ROVER Learning from Examples
                                
                                
                                <p style="margin-bottom:.18cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                                  
                                
                                
                                <p style="margin-bottom:.18cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                                  <a style="color:#0000ff;" href="http://tralvex.com/pub/nap/video/ty-walk1.mov" target="_blank"><span style="font-size:x-small;">Sequence 1</a>
                                
                                
                                <p style="margin-bottom:.18cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                                  <a style="color:#0000ff;" href="http://tralvex.com/pub/nap/video/ty-walk5.mov" target="_blank"><span style="font-size:x-small;">Sequence 5</a>
                                
                                
                                <p style="margin-bottom:.18cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                                  <a style="color:#0000ff;" href="http://tralvex.com/pub/nap/video/ty-walk8.mov" target="_blank"><span style="font-size:x-small;">Sequence 8</a>
                                
                                
                                <p class="western" style="margin-bottom:.35cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                                  <p style="margin-bottom:.18cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                                    <span style="font-size:x-small;">(B) ROVER Modeling
                                  
                                  
                                  <p style="margin-bottom:.18cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                                    
                                  
                                  
                                  <p class="western" style="margin-bottom:.35cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                                    <p style="margin-bottom:.18cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                                      <span style="font-size:x-small;">(C) ROVER Prediction
                                    
                                    
                                    <p style="margin-bottom:.21cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                                      
                                      
                                    
                                    
                                      
                                        
                                          <table style="font-family:'Times New Roman';" width="469" cellspacing="0" cellpadding="2">
                                            <col width="35" /> <col width="427" /> <tr valign="TOP">
                                              <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="35" height="1">
                                                <p class="western" style="margin-bottom:.21cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                                                  **2.4**
                                                
                                              </td>
                                              
                                              <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="427">
                                                <p class="western" style="margin-bottom:.21cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                                                  <a name="Autonomous_Walker_&_Swimming_Eel"></a>**Autonomous Walker & Swimming Eel**
                                                
                                              </td>
                                            </tr>
                                          
                                          
                                          
                                            
                                              <div style="font-family:'Times New Roman';line-height:normal;font-size:medium;" align="RIGHT">
                                                <table width="626" cellspacing="0" cellpadding="2">
                                                  <col width="311" /> <col width="2" /> <col width="302" /> <tr valign="TOP">
                                                    <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="311">
                                                      <p class="western" style="margin-bottom:.35cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                                                        <span style="font-size:x-small;">(A) The research in this area involves combining biology, mechanical engineering and information technology in order to develop the techniques necessary to build a dynamically stable legged vehicle controlled by a neural network. This would incorporate command signals, sensory feedback and reflex circuitry in order to produce the desired movement.
                                                      
                                                      
                                                      <p style="margin-bottom:.21cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                                                        <a style="color:#0000ff;" href="http://tralvex.com/pub/nap/video/al-climb.mpg" target="_blank"></a><span style="font-size:x-small;">
 <a style="color:#0000ff;" href="http://tralvex.com/pub/nap/video/al-climb.mpg" target="_blank">Walker</a>

                                                    </td>
                                                    
                                                    <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="2">
                                                    </td>
                                                    
                                                    <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="302">
                                                      <p class="western" style="margin-bottom:.35cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                                                        <span style="font-size:x-small;">(B) Simulation of the swimming lamprey (eel-like sea creature), driven by a neural network.
                                                      
                                                      
                                                      <p style="margin-bottom:.21cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                                                        <a style="color:#0000ff;" href="http://tralvex.com/pub/nap/video/al-lamp.mpg" target="_blank"></a><span style="font-size:x-small;">
 <a style="color:#0000ff;" href="http://tralvex.com/pub/nap/video/al-lamp.mpg" target="_blank">Swimming Lamprey</a>

                                                    </td>
                                                  </tr>
                                                
                                              
                                              
                                              
                                                <p class="western" style="margin-bottom:.35cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                                                  
                                                    
                                                      <table style="font-family:'Times New Roman';" width="594" cellspacing="0" cellpadding="2">
                                                        <col width="75" /> <col width="511" /> <tr valign="TOP">
                                                          <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="75" height="15">
                                                            <p class="western" style="margin-bottom:.21cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                                                              **2.5**
                                                            
                                                          </td>
                                                          
                                                          <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="511">
                                                            <p class="western" style="margin-bottom:.21cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                                                              <a name="Robocup:_Robot_World_Cup"></a>**Robocup: Robot World Cup**
                                                            
                                                          </td>
                                                        </tr>
                                                        
                                                        <tr>
                                                          <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" colspan="2" valign="TOP" width="590">
                                                            <p class="western" style="margin-bottom:.35cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                                                              The RoboCup Competition pits robots (real and virtual) against each other in a simulated soccer tournament. The aim of the RoboCup competition is to foster an interdisciplinary approach to robotics and agent-based AI by presenting a domain that requires large-scale coorperation and coordination in a dynamic, noisy, complex environment.
                                                            
                                                            
                                                            
                                                              RoboCup has three different leagues to-date. The Small and Middle-Size Leagues involved physical robots; the Simulation League is for virtual, synthetic teams. This work focus on building softbots for the Simulation League.
                                                            
                                                            
                                                            <p style="margin-bottom:.18cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                                                              Machine Learning for Robocup involves:
                                                            
                                                            
                                                            <ol>
                                                              <li>
                                                                <p class="western" style="margin-bottom:.18cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                                                                  The training of player in the process of making the decision of whether (a) to dribble the ball; (b) to pass it on to another team-mate; (c) to shoot into the net.
                                                                
                                                              </li>
                                                              
                                                              <li>
                                                                <p class="western" style="margin-bottom:.18cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                                                                  The training of the goalkeeper in process of intelligent guessing of how the ball is going to be kick by the opponents. Complexities arise when one opponent decides to pass the ball to another player instead of attempting a score.
                                                                
                                                              </li>
                                                              
                                                              <li>
                                                                <p class="western" style="margin-bottom:.18cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                                                                  Evolution of a co-operative and perhaps unpredictable team.
                                                                
                                                              </li>
                                                            </ol>
                                                            
                                                            <p style="margin-bottom:.18cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                                                              Common AI methods used are variants of Neural Networks and Genetic Algorithms.
                                                            
                                                            
                                                            <p style="margin-bottom:.21cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                                                              
                                                              
                                                              <tr>
                                                                <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" colspan="2" valign="TOP" width="590">
                                                                  <p style="margin-bottom:.21cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                                                                    <a style="color:#0000ff;" href="http://tralvex.com/pub/nap/video/sp-robo.avi" target="_blank"></a>
 <a style="color:#0000ff;" href="http://tralvex.com/pub/nap/video/sp-robo.avi" target="_blank">KRDL Soccer Softbots</a> (3.1mb, AVI)

                                                                </td>
                                                              </tr>  
                                                              
                                                              
                                                                <p class="western" style="margin-bottom:.35cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                                                                  
                                                                    
                                                                      <table style="font-family:'Times New Roman';" width="487" cellspacing="0" cellpadding="2">
                                                                        <col width="30" /> <col width="449" /> <tr valign="TOP">
                                                                          <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="30" height="8">
                                                                            <p class="western" style="margin-bottom:.21cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                                                                              **2.6**
                                                                            
                                                                          </td>
                                                                          
                                                                          <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="449">
                                                                            <p class="western" style="margin-bottom:.21cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                                                                              <a name="Using_HMM's_for_Audio-to-Visual_Conversi"></a>**Using HMM's for Audio-to-Visual Conversion**
                                                                            
                                                                          </td>
                                                                        </tr>
                                                                      
                                                                      
                                                                      
                                                                        
                                                                          <div style="font-family:'Times New Roman';line-height:normal;font-size:medium;" align="RIGHT">
                                                                            <table width="594" cellspacing="0" cellpadding="2">
                                                                              <col width="278" /> <col width="2" /> <col width="302" /> <tr>
                                                                                <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" colspan="3" valign="TOP" width="590">
                                                                                  <p class="western" style="margin-bottom:.35cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                                                                                    One emerging application which exploits the correlation between audio and video is speech-driven facial animation. The goal of speech-driven facial animation is to synthesize realistic video sequences from acoustic speech. Much of the previous research has implemented this audio-to-visual conversion strategy with existing techniques such as vector quantization and neural networks. Here, they examine how this conversion process can be accomplished with hidden Markov models (HMM).
                                                                                  
                                                                                  
                                                                                  <p style="margin-bottom:.18cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                                                                                    
                                                                                    
                                                                                    <tr valign="TOP">
                                                                                      <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="278">
                                                                                        <p class="western" style="margin-bottom:.35cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                                                                                          <span style="font-size:x-small;">(A) Tracking Demo: The parabolic contour is fit to each frame of the video sequence using a modified deformable template algorithm. The height between the two contours, and the width between the corners of the mouth can be extracted from the templates to form our visual parameter sets.
                                                                                        
                                                                                        
                                                                                        <p style="margin-bottom:.21cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                                                                                          <a style="color:#0000ff;" href="http://tralvex.com/pub/nap/video/rr-track.avi" target="_blank"></a><span style="font-size:x-small;">
 <a style="color:#0000ff;" href="http://tralvex.com/pub/nap/video/rr-track.avi" target="_blank">Tracking</a>

                                                                                      </td>
                                                                                      
                                                                                      <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="2">
                                                                                      </td>
                                                                                      
                                                                                      <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="302">
                                                                                        <p style="margin-bottom:.18cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                                                                                          <span style="font-size:x-small;">(B) Morphing Demo: Another important piece of the speech-driven facial animation system is a visual synthesis module. Here we are attempting to synthesize the word "wow" from a single image. Each frame in the video sequence is morphed from the first frame shown below. The parameters used to morph these images were obtained by hand.
                                                                                        
                                                                                        
                                                                                        <p style="margin-bottom:.21cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                                                                                          <a style="color:#0000ff;" href="http://tralvex.com/pub/nap/video/rr-morph.avi" target="_blank"></a><span style="font-size:x-small;">
 <a style="color:#0000ff;" href="http://tralvex.com/pub/nap/video/rr-morph.avi" target="_blank">Morphing</a>

                                                                                      </td>
                                                                                    </tr>   
                                                                                    
                                                                                    
                                                                                      <p class="western" style="margin-bottom:.35cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                                                                                        
                                                                                          
                                                                                            <table style="font-family:'Times New Roman';" width="594" cellspacing="0" cellpadding="2">
                                                                                              <col width="265" /> <col width="321" /> <tr valign="TOP">
                                                                                                <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="265" height="15">
                                                                                                  <p class="western" style="margin-bottom:.21cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                                                                                                    <a name="Artifical_Life:_Galapagos"></a>**2.7 Artificial Life: Galapagos**
                                                                                                  
                                                                                                </td>
                                                                                                
                                                                                                <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="321">
                                                                                                </td>
                                                                                              </tr>
                                                                                              
                                                                                              <tr>
                                                                                                <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" colspan="2" valign="TOP" width="590">
                                                                                                  <p class="western" style="margin-bottom:.35cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                                                                                                    Galapagos is a fantastic and dangerous place where up and down have no meaning, where rivers of iridescent acid and high-energy laser mines are beautiful but deadly artifacts of some other time. Through spatially twisted puzzles and bewildering cyber-landscapes, the artificial creature called Mendel struggles to survive, and you must help him.
                                                                                                  
                                                                                                  
                                                                                                  
                                                                                                    Mendel is a synthetic organism that can sense infrared radiation and tactile stimulus. His mind is an advanced adaptive controller featuring Non-stationary Entropic Reduction Mapping - a new form of artificial life technology developed by Anark. He can learn like your dog, he can adapt to hostile environments like a cockroach, but he can't solve the puzzles that prevent his escape from Galapagos.
                                                                                                  
                                                                                                  
                                                                                                  <p style="margin-bottom:.21cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                                                                                                    
                                                                                                    
                                                                                                    <tr valign="TOP">
                                                                                                      <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="265">
                                                                                                        <p class="western" style="margin-bottom:.21cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                                                                                                          <span style="font-size:x-small;">Galapagos features rich, 3D texture-mapped worlds, with continuous-motion graphics and 6 degrees of freedom. Dramatic camera movement and incredible lighting effects make your passage through Galapagos breathtaking. Explosions and other chilling effects will make you fear for your synthetic friend. Active panning 3D stereo sound will draw you into the exotic worlds of Galapagos.
                                                                                                        
                                                                                                      </td>
                                                                                                      
                                                                                                      <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="321">
                                                                                                        <p style="margin-bottom:.21cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                                                                                                          <a style="color:#0000ff;" href="http://tralvex.com/pub/nap/video/galapago.mov" target="_blank"></a>
 <a style="color:#0000ff;" href="http://tralvex.com/pub/nap/video/galapago.mov" target="_blank"><span style="font-size:x-small;">Galapagos</a>

                                                                                                      </td>
                                                                                                    </tr>  
                                                                                                    
                                                                                                    
                                                                                                      <p class="western" style="margin-bottom:.35cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                                                                                                        
                                                                                                          <table style="font-family:'Times New Roman';" width="615" cellspacing="0" cellpadding="2">
                                                                                                            <col width="294" /> <col width="4" /> <col width="2" /> <col width="299" /> <tr valign="TOP">
                                                                                                              <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="294">
                                                                                                                <p class="western" style="margin-bottom:.21cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                                                                                                                  <a name="Speechreading_(Lipreading)"></a> **2.8 Speechreading (Lipreading)**
                                                                                                                
                                                                                                              </td>
                                                                                                              
                                                                                                              <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="4">
                                                                                                              </td>
                                                                                                              
                                                                                                              <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" colspan="2" width="305">
                                                                                                              </td>
                                                                                                            </tr>
                                                                                                            
                                                                                                            <tr>
                                                                                                              <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" colspan="4" valign="TOP" width="611">
                                                                                                                <p class="western" style="margin-bottom:.35cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                                                                                                                  As part of the research program Neuroinformatik the IPVR develops a neural speechreading system as part of a user interface for a workstation. The three main parts of the system include a face tracker (done by Marco Sommerau), lip modeling and speech processing (done by Michael Vogt) and the development and application of SNNS for neural network training (done by Günter Mamier).
                                                                                                                
                                                                                                                
                                                                                                                <p style="margin-bottom:.18cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                                                                                                                  Automatic speechreading is based on a robust lip image analysis. In this approach, no special illumination or lip make-up is used. The analysis is based on true color video images. The system allows for realtime tracking and storage of the lip region and robust off-line lip model matching. The proposed model is based on cubic outline curves. A neural classifier detects visibility of teeth edges and other attributes. At this stage of the approach the edge between the closed lips is automatically modeled if applicable, based on a neural network's decision.
                                                                                                                
                                                                                                                
                                                                                                                
                                                                                                                  To achieve high flexibility during lip-model development, a model description language has been defined and implemented. The language allows the definition of edge models (in general) based on knots and edge functions. Inner model forces stabilize the overall model shape. User defined image processing functions may be applied along the model edges. These functions and the inner forces contribute to an overall energy function. Adaptation of the model is done by gradient descent or simulated annealing like algorithms. The figure shows one configuration of the lip model, consisting of an upper lip edge and a lower lip edge. The model edges are defined by Bezier-functions. Outer control knots stabilize the position of the corners of the mouth.
                                                                                                                
                                                                                                                
                                                                                                                <p style="margin-bottom:.21cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                                                                                                                  
                                                                                                                  
                                                                                                                  <tr valign="TOP">
                                                                                                                    <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" colspan="2" width="302">
                                                                                                                      <table width="302" cellspacing="0" cellpadding="0">
                                                                                                                        <col width="302" /> <tr>
                                                                                                                          <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="302">
                                                                                                                            <p style="margin-bottom:.21cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                                                                                                                              
                                                                                                                            
                                                                                                                          </td>
                                                                                                                        </tr>
                                                                                                                        
                                                                                                                        <tr>
                                                                                                                          <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="302">
                                                                                                                            <p class="western" style="margin-bottom:.21cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                                                                                                                              <span style="font-size:x-small;">Fig 2.8.1 The model interpreter enables a permanent measurement of model knot positions and color blends along model edges during adaptation to an utterance. The resulting parameters may be used for speech recognition tasks in further steps.
                                                                                                                            
                                                                                                                          </td>
                                                                                                                        </tr>
                                                                                                                      
                                                                                                                      
                                                                                                                      <p class="western" style="margin-bottom:.35cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                                                                                                                        </td> 
                                                                                                                        
                                                                                                                        <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="2">
                                                                                                                        </td>
                                                                                                                        
                                                                                                                        <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="299">
                                                                                                                          <p style="margin-bottom:.18cm;direction:ltr;line-height:16px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                                                                                                                            <a style="color:#0000ff;" href="http://tralvex.com/pub/nap/video/gm-lip.mpg" target="_blank"></a>
 <a style="color:#0000ff;" href="http://tralvex.com/pub/nap/video/gm-lip.mpg" target="_blank"><span style="font-size:x-small;">Lipread</a>

                                                                                                                        </td></tr>   
                                                                                                                        
                                                                                                                        
                                                                                                                          <p class="western" style="margin-bottom:.35cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                                                                                                                            
                                                                                                                              
                                                                                                                                <table style="font-family:'Times New Roman';" width="606" cellspacing="0" cellpadding="2">
                                                                                                                                  <col width="591" /> <col width="7" /> <tr valign="TOP">
                                                                                                                                    <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="591">
                                                                                                                                      <p class="western" style="margin-bottom:.21cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                                                                                                                                        <a name="Detection_and_Tracking_of_Moving_Targets"></a>**2.9 Detection and Tracking of Moving Targets**
                                                                                                                                      
                                                                                                                                    </td>
                                                                                                                                    
                                                                                                                                    <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="7">
                                                                                                                                    </td>
                                                                                                                                  </tr>
                                                                                                                                  
                                                                                                                                  <tr>
                                                                                                                                    <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" colspan="2" valign="TOP" width="602">
                                                                                                                                      <p class="western" style="margin-bottom:.21cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                                                                                                                                        The moving target detection and track methods here are "track before detect" methods. They correlate sensor data versus time and location, based on the nature of actual tracks. The track statistics are "learned" based on artificial neural network (ANN) training with prior real or simulated data. Effects of different clutter backgrounds are partially compensated based on space-time-adaptive processing of the sensor inputs, and further compensated based on the ANN training. Specific processing structures are adapted to the target track statistics and sensor characteristics of interest. Fusion of data over multiple wavelengths and sensors is also supported.
                                                                                                                                      
                                                                                                                                      
                                                                                                                                      
                                                                                                                                        Compared to conventional fixed matched filter techniques, these methods have been shown to reduce false alarm rates by up to a factor of 1000 based on simulated SBIRS data for very weak ICBM targets against cloud and nuclear backgrounds, with photon, quantization, and thermal noise, and sensor jitter included. Examples of the backgrounds, and processing results, are given below.
                                                                                                                                      
                                                                                                                                      
                                                                                                                                      
                                                                                                                                        The methods are designed to overcome the weaknesses of other advanced track-before-detect methods, such as 3+-D (space, time, etc.) matched filtering, dynamic programming (DP), and multi-hypothesis tracking (MHT). Loosely speaking, 3+-D matched filtering requires too many filters in practice for long-term track correlation; DP cannot realistically exploit the non-Markovian nature of real tracks, and strong targets mask out weak targets; and MHT cannot support the low pre-detection thresholds required for very weak targets in high clutter. They have developed and tested versions of the above (and other) methods in their research, as well as Kalman-filter probabilistic data association (KF/PDA) methods, which they use for post-detection tracking.
                                                                                                                                      
                                                                                                                                      
                                                                                                                                      
                                                                                                                                        Space-time-adaptive methods are used to deal with correlated, non-stationary, non-Gaussian clutter, followed by a multi-stage filter sequence and soft-thresholding units that combine current and prior sensor data, plus feed back of prior outputs, to estimate the probability of target presence. The details are optimized by adaptive "training" over very large data sets, and special methods are used to maximize the efficiency of this training.
                                                                                                                                        
                                                                                                                                        <tr>
                                                                                                                                          <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" colspan="2" valign="TOP" width="602">
                                                                                                                                            <p style="margin-bottom:.21cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                                                                                                                                              <a style="color:#0000ff;" href="http://tralvex.com/pub/nap/video/dgi-trk.mpg" target="_blank"></a>
 Figure 2.9 (a) Raw input backgrounds with weak targets included,
 (b) Detected target sequence at the ANN processing output,
 post-detection tracking not included. <a style="color:#0000ff;" href="http://tralvex.com/pub/nap/video/dgi-trk.mpg" target="_blank">Video Clip</a>

                                                                                                                                          </td>
                                                                                                                                        </tr>  
                                                                                                                                        
                                                                                                                                        
                                                                                                                                          
                                                                                                                                            <table style="font-family:'Times New Roman';" width="594" cellspacing="0" cellpadding="2">
                                                                                                                                              <col width="291" /> <col width="2" /> <col width="117" /> <col width="135" /> <col width="30" /> <tr valign="TOP">
                                                                                                                                                <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" colspan="3" width="417" height="15">
                                                                                                                                                  <p class="western" style="margin-bottom:.21cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                                                                                                                                                    <a name="Real-time_Target_Identification_for_Secu"></a>**2.10 Real-time Target Identification for Security Applications**
                                                                                                                                                  
                                                                                                                                                </td>
                                                                                                                                                
                                                                                                                                                <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="135">
                                                                                                                                                </td>
                                                                                                                                                
                                                                                                                                                <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="30">
                                                                                                                                                </td>
                                                                                                                                              </tr>
                                                                                                                                              
                                                                                                                                              <tr>
                                                                                                                                                <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" colspan="5" valign="TOP" width="590">
                                                                                                                                                  <p class="western" style="margin-bottom:.35cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                                                                                                                                                    The system localizes and tracks peoples' faces as they move through a scene. It integrates the following techniques:
                                                                                                                                                  
                                                                                                                                                  
                                                                                                                                                  <ul>
                                                                                                                                                    <li>
                                                                                                                                                      <p class="western" style="margin-bottom:.18cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                                                                                                                                                        Motion detection
                                                                                                                                                      
                                                                                                                                                    </li>
                                                                                                                                                    
                                                                                                                                                    <li>
                                                                                                                                                      <p class="western" style="margin-bottom:.18cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                                                                                                                                                        Tracking people based upon motion
                                                                                                                                                      
                                                                                                                                                    </li>
                                                                                                                                                    
                                                                                                                                                    <li>
                                                                                                                                                      <p class="western" style="margin-bottom:.18cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                                                                                                                                                        Tracking faces using an appearance model
                                                                                                                                                      
                                                                                                                                                    </li>
                                                                                                                                                  </ul>
                                                                                                                                                  
                                                                                                                                                  <p style="margin-bottom:.18cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                                                                                                                                                    Faces are tracked robustly by integrating motion and model-based tracking.
                                                                                                                                                  
                                                                                                                                                  
                                                                                                                                                  <p style="margin-bottom:.21cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                                                                                                                                                    
                                                                                                                                                    
                                                                                                                                                    <tr valign="TOP">
                                                                                                                                                      <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="291">
                                                                                                                                                        <p style="margin-bottom:.18cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                                                                                                                                                          (A) Tracking in low resolution and poor lighting conditions
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        <p style="margin-bottom:.21cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                                                                                                                                                          <a style="color:#0000ff;" href="http://tralvex.com/pub/nap/video/sm-jon.mpg" target="_blank"></a>
 <span style="font-size:x-small;"><a style="color:#0000ff;" href="http://tralvex.com/pub/nap/video/sm-jon.mpg" target="_blank">Jon</a>

                                                                                                                                                      </td>
                                                                                                                                                      
                                                                                                                                                      <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="2">
                                                                                                                                                      </td>
                                                                                                                                                      
                                                                                                                                                      <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" colspan="3" width="290">
                                                                                                                                                        <p style="margin-bottom:.18cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                                                                                                                                                          (B) Tracking two people simultaneously: lock is maintained on the faces despite unreliable motion-based body tracking.
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        <p style="margin-bottom:.21cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                                                                                                                                                          <a style="color:#0000ff;" href="http://tralvex.com/pub/nap/video/sm-2ppl.mpg"></a>
 <a style="color:#0000ff;" href="http://tralvex.com/pub/nap/video/sm-2ppl.mpg" target="_blank"><span style="font-size:x-small;">Double Tracking</a>

                                                                                                                                                      </td>
                                                                                                                                                    </tr>  
                                                                                                                                                    
                                                                                                                                                    
                                                                                                                                                      
                                                                                                                                                        
                                                                                                                                                          <table style="font-family:'Times New Roman';" width="606" cellspacing="0" cellpadding="2">
                                                                                                                                                            <col width="57" /> <col width="541" /> <tr valign="TOP">
                                                                                                                                                              <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="57">
                                                                                                                                                                <p class="western" style="margin-bottom:.21cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                                                                                                                                                                  **2.11**
                                                                                                                                                                
                                                                                                                                                              </td>
                                                                                                                                                              
                                                                                                                                                              <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="541">
                                                                                                                                                                <p class="western" style="margin-bottom:.21cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                                                                                                                                                                  <a name="Facial_Animation"></a>**Facial Animation**
                                                                                                                                                                
                                                                                                                                                              </td>
                                                                                                                                                            </tr>
                                                                                                                                                            
                                                                                                                                                            <tr>
                                                                                                                                                              <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" colspan="2" valign="TOP" width="602">
                                                                                                                                                                <p style="margin-bottom:.18cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                                                                                                                                                                  Facial animations created using hierarchical B-spline as the underlying surface representation. Neural networks could be use for learning of each variation in the face expressions for animated sequences.
                                                                                                                                                                
                                                                                                                                                                
                                                                                                                                                                <p style="margin-bottom:.18cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                                                                                                                                                                  The (mask) model was created in SoftImage, and is an early prototype for the character "Mouse" in the YTV/ABC televisions series "ReBoot" (They do not use hierarchical splines for Reboot!). The original standard bicubic B-spline was imported to the "Dragon" editor and a hierarchy automatically constructed. The surface was attached to a jaw to allow it to open and close the mouth. Groups of control vertices were then moved around to created various facial expressions. Three of these expressions were chosen as key shapes, the spline surface was exported back to SoftImage, and the key shapes were interpolated to create the final animation.
                                                                                                                                                                
                                                                                                                                                                
                                                                                                                                                                <table width="542" cellspacing="0" cellpadding="0">
                                                                                                                                                                  <col width="271" /> <col width="271" /> <tr>
                                                                                                                                                                    <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="271">
                                                                                                                                                                      <p class="western" style="margin-bottom:.21cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                                                                                                                                                                        <a style="color:#0000ff;" href="http://tralvex.com/pub/nap/video/df-mask.mpg" target="_blank"></a><span style="font-size:x-small;">
 <a style="color:#0000ff;" href="http://tralvex.com/pub/nap/video/df-mask.mpg" target="_blank">Mask</a>

                                                                                                                                                                    </td>
                                                                                                                                                                    
                                                                                                                                                                    <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="271">
                                                                                                                                                                      <p class="western" style="margin-bottom:.21cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                                                                                                                                                                        <a style="color:#0000ff;" href="http://tralvex.com/pub/nap/video/df-haida.mpg" target="_blank"></a><span style="font-size:x-small;">
 Haida

                                                                                                                                                                    </td>
                                                                                                                                                                  </tr>
                                                                                                                                                                
                                                                                                                                                                
                                                                                                                                                                <p class="western" style="margin-bottom:.35cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                                                                                                                                                                    
                                                                                                                                                                  
                                                                                                                                                                  
                                                                                                                                                                    
                                                                                                                                                                      <table style="font-family:'Times New Roman';" width="646" cellspacing="0" cellpadding="2">
                                                                                                                                                                        <col width="40" /> <col width="106" /> <col width="150" /> <col width="150" /> <col width="135" /> <col width="41" /> <tr valign="TOP">
                                                                                                                                                                          <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="40">
                                                                                                                                                                            <p class="western" style="margin-bottom:.21cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                                                                                                                                                                              **2.12**
                                                                                                                                                                            
                                                                                                                                                                          </td>
                                                                                                                                                                          
                                                                                                                                                                          <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" colspan="4" width="553">
                                                                                                                                                                            <p class="western" style="margin-bottom:.21cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                                                                                                                                                                              <a name="Artificial_Life_for_Graphics,_Animation,"></a>**Artificial Life for Graphics, Animation, Multimedia, and Virtual Reality**
                                                                                                                                                                            
                                                                                                                                                                          </td>
                                                                                                                                                                          
                                                                                                                                                                          <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="41">
                                                                                                                                                                          </td>
                                                                                                                                                                        </tr>
                                                                                                                                                                        
                                                                                                                                                                        <tr>
                                                                                                                                                                          <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" colspan="6" valign="TOP" width="642">
                                                                                                                                                                            <p class="western" style="margin-bottom:.35cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                                                                                                                                                                              Some graphics researchers have begun to explore a new frontier-a world of objects of enormously greater complexity than is typically accessible through physical modeling alone-objects that are alive. The modeling and simulation of living systems for computer graphics resonates with the burgeoning field of scientific inquiry called Artificial Life. Conceptually, artificial life transcends the traditional boundaries of computer science and biological science. The natural synergy between computer graphics and artificial life can be potentially beneficial to both disciplines. As some of the demos here demonstrate, potential is becoming fulfillment.
                                                                                                                                                                            
                                                                                                                                                                            
                                                                                                                                                                            
                                                                                                                                                                              The demos demonstrate and elucidate new models that realistically emulate a broad variety of living things-both plants and animals-from lower animals all the way up the evolutionary ladder to humans. Typically, these models inhabit virtual worlds in which they are subject to physical laws. Consequently, they often make use of physics-based modeling techniques. More significantly, however, they must also simulate many of the natural processes that uniquely characterize living systems-such as birth and death, growth, natural selection, evolution, perception, locomotion, manipulation, adaptive behavior, intelligence, and learning. The challenge is to develop sophisticated graphics models that are self-creating, self-evolving, self-controlling, and/or self-animating by simulating the natural mechanisms fundamental to life.
                                                                                                                                                                            
                                                                                                                                                                            
                                                                                                                                                                            <p style="margin-bottom:.21cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="JUSTIFY">
                                                                                                                                                                              
                                                                                                                                                                              
                                                                                                                                                                              <tr valign="TOP">
                                                                                                                                                                                <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" colspan="2" width="150">
                                                                                                                                                                                  <p style="margin-bottom:.21cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="CENTER">
                                                                                                                                                                                    <a style="color:#0000ff;" href="http://tralvex.com/pub/nap/video/sg95-dog.mov" target="_blank"></a><span style="font-size:x-small;">
 <a style="color:#0000ff;" href="http://tralvex.com/pub/nap/video/sg95-dog.mov" target="_blank">A.Dog</a>

                                                                                                                                                                                </td>
                                                                                                                                                                                
                                                                                                                                                                                <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="150">
                                                                                                                                                                                  <p class="western" style="margin-bottom:.21cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="CENTER">
                                                                                                                                                                                    <a style="color:#0000ff;" href="http://tralvex.com/pub/nap/video/sg95-evc.mpg" target="_blank"></a><span style="font-size:x-small;">
 <a style="color:#0000ff;" href="http://tralvex.com/pub/nap/video/sg95-evc.mpg" target="_blank">Evolved Virtual Creatures</a>

                                                                                                                                                                                </td>
                                                                                                                                                                                
                                                                                                                                                                                <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="150">
                                                                                                                                                                                  <p class="western" style="margin-bottom:.21cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="CENTER">
                                                                                                                                                                                    <a style="color:#0000ff;" href="http://tralvex.com/pub/nap/video/sg95-sac.mov" target="_blank"></a><span style="font-size:x-small;">
 <a style="color:#0000ff;" href="http://tralvex.com/pub/nap/video/sg95-sac.mov" target="_blank">Sensor-Based Autonomous Creatures</a>

                                                                                                                                                                                </td>
                                                                                                                                                                                
                                                                                                                                                                                <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" colspan="2" width="179">
                                                                                                                                                                                  <p class="western" style="margin-bottom:.21cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="CENTER">
                                                                                                                                                                                    <a style="color:#0000ff;" href="http://tralvex.com/pub/nap/video/sg95-af.mov" target="_blank"></a><span style="font-size:x-small;">
 <a style="color:#0000ff;" href="http://tralvex.com/pub/nap/video/sg95-af.mov" target="_blank">A. Fish</a>

                                                                                                                                                                                </td>
                                                                                                                                                                              </tr>  
                                                                                                                                                                              
                                                                                                                                                                              
                                                                                                                                                                                <p class="western" style="margin-bottom:.35cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                                                                                                                                                                                  
                                                                                                                                                                                    
                                                                                                                                                                                      <table style="font-family:'Times New Roman';" width="606" cellspacing="0" cellpadding="2">
                                                                                                                                                                                        <col width="324" /> <col width="274" /> <tr>
                                                                                                                                                                                          <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" colspan="2" valign="TOP" width="602">
                                                                                                                                                                                            <p class="western" style="margin-bottom:.21cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                                                                                                                                                                                              <a name="Creatures:_The_World_Most_Advanced_Artif"></a>**2.13 Creatures: The World Most Advanced Artificial Life!**
                                                                                                                                                                                            
                                                                                                                                                                                          </td>
                                                                                                                                                                                        </tr>
                                                                                                                                                                                        
                                                                                                                                                                                        <tr valign="TOP">
                                                                                                                                                                                          <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="324" height="225">
                                                                                                                                                                                            <p class="western" style="margin-bottom:.21cm;direction:ltr;line-height:17px;font-family:Calibri, sans-serif;font-size:11pt;" lang="en-US" align="JUSTIFY">
                                                                                                                                                                                              Creatures is the most entertaining computer game you'll ever play which offers nothing to shoot, no puzzles to solve or difficult controls to master. And yet it is mesmerizing entertainment.
 One has to raise, teach, breed and love computer pets that are really alive. They are so alive that if it is not taken care of, they will die. Creatures' features the most advanced, genuine Artificial Life software ever developed in a commercial product, technology that has blown the imaginations of scientists world-wide. This is a look into the future where new species of life emerge from ordinary home and office PCs.

                                                                                                                                                                                          </td>
                                                                                                                                                                                          
                                                                                                                                                                                          <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="274">
                                                                                                                                                                                            <p style="margin-bottom:.21cm;direction:ltr;line-height:18px;margin-top:.18cm;" lang="en-US" align="CENTER">
                                                                                                                                                                                              <a style="color:#0000ff;" href="http://tralvex.com/pub/nap/video/creature.avi" target="_blank">
 Creatures</a>

                                                                                                                                                                                          </td>
                                                                                                                                                                                        </tr>
                                                                                                                                                                                        
                                                                                                                                                                                        <tr valign="TOP">
                                                                                                                                                                                          <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="324">
                                                                                                                                                                                          </td>
                                                                                                                                                                                          
                                                                                                                                                                                          <td style="border-color:initial;border-style:none;border-width:initial;padding:0;" width="274">
                                                                                                                                                                                          </td>
                                                                                                                                                                                        </tr>
                                                                                                                                                                                      
                                                                                                                                                                                      
                                                                                                                                                                                      
                                                                                                                                                                                         
                                                                                                                                                                                      
                                                                                                                                                                                      
                                                                                                                                                                                      <p style="margin-bottom:0;" align="JUSTIFY">
                                                                                                                                                                                        The following MPEG movie sequences illustrate behavior generated by dynamical recurrent neural network controllers co-evolved for pursuit and evasion capabilities. From an initial population of random network designs, successful designs in each generation are selected for reproduction with recombination, mutation, and gene duplication. Selection is based on measures of how well each controller performs in a number of pursuit-evasion contests. In each contest a pursuer controller and an evader controller are pitched against each other, controlling simple "visually guided" 2-dimensional autonomous virtual agents. Both the pursuer and the evader have limited amounts of energy, which is used up in movement, so they have to evolve to move economically. Each contest results in a time-series of position and orientation data for the two agents. 
                                                                                                                                                                                      
                                                                                                                                                                                      
                                                                                                                                                                                      <p style="margin-top:.18cm;margin-bottom:.18cm;line-height:100%;" align="JUSTIFY">
                                                                                                                                                                                        These time-series are then fed into a custom 3-D movie generator. It is important to note that, although the chase behaviors are genuine data, the 3D structures, surface physics, and shading are all purely for illustrative effect. 
                                                                                                                                                                                      
                                                                                                                                                                                      
                                                                                                                                                                                      <table width="464" cellspacing="0" cellpadding="0">
                                                                                                                                                                                        <col width="464" /> <tr>
                                                                                                                                                                                          <td style="border:none;padding:0;" width="464">
                                                                                                                                                                                            <p style="margin-bottom:0;" align="JUSTIFY">
                                                                                                                                                                                              <span style="font-size:x-small;">1. The pursuer is not very good at pursuing, and the evader is not very good at evading. 
                                                                                                                                                                                            
                                                                                                                                                                                            
                                                                                                                                                                                            <p style="margin-top:.18cm;margin-bottom:.18cm;" align="JUSTIFY">
                                                                                                                                                                                              <span style="font-size:x-small;">2. Pursuer chases evader, but soon runs out of energy, allowing the evader to escape. 
                                                                                                                                                                                            
                                                                                                                                                                                            
                                                                                                                                                                                            <p style="margin-top:.18cm;margin-bottom:.18cm;" align="JUSTIFY">
                                                                                                                                                                                              <span style="font-size:x-small;">3. Pursuer chases evader, but uses up all its energy just before the evader runs out of energy. 
                                                                                                                                                                                            
                                                                                                                                                                                            
                                                                                                                                                                                            <p style="margin-top:.18cm;" align="JUSTIFY">
                                                                                                                                                                                              <span style="font-size:x-small;">4. After a couple of close shaves, the pursuer finally catches the evader. 
                                                                                                                                                                                            
                                                                                                                                                                                          </td>
                                                                                                                                                                                        </tr>
