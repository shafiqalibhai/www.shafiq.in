---
title: Hardening Procedure for Solaris Systems
author: Shafiq Alibhai
date: 2012-12-01T16:27:52+00:00
publicize_twitter_user:
  - shafiqalibhai
draft: true
categories:
  - Development
tags:
  - AWK
  - Browser
  - copy
  - cp
  - Database
  - database server
  - ERP
  - Grep
  - Harden
  - History
  - HTML
  - implementation
  - intel
  - IP
  - Management
  - Networks
  - Requirement
  - Requirements
  - sed
  - shell
  - Solaris
  - Sun
  - Sun Microsystems
  - Development
  - tens
  - Tools
  - XML

---
# DOWNLOAD - Hardening Procedure for Solaris Systems {.western}

<table width="590" cellspacing="0" cellpadding="7">
  <tr valign="TOP">
    <td style="border: none; padding: 0;" width="137">
      <p style="margin-top: .21cm;">
        <a name="ProcedureStatement"></a><span style="font-size: small;"><b>Procedure Statement</b>

    </td>
    
    <td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: none; border-right: none; padding: 0;" width="425">
      <p class="western" style="margin-top: .21cm;">
        <span style="font-size: small;">The hardening policies are defined as follows:
      
      
      <ul>
        <li>
          <p style="margin-bottom: .11cm;">
            <span style="font-size: small;">Database server hardening procedure.
          
        </li>
        
        <li>
          <p style="margin-bottom: .11cm;">
            <span style="font-size: small;">Web server hardening procedure
          
        </li>
        
        <li>
          <p style="margin-bottom: .11cm;">
            <span style="font-size: small;">Application server hardening procedure
          
        </li>
        
        <li>
          <p style="margin-bottom: .11cm;">
            <span style="font-size: small;">Utility server hardening procedure
          
          
          <p style="margin-bottom: .11cm;">
            <span style="font-size: small;">On every case, 4 security components are involved:
          
        </li>
      </ul>
      
      <ul>
        <li>
          <p style="margin-bottom: .11cm;">
            <span style="font-size: small;">JASS
          
        </li>
        
        <li>
          <p style="margin-bottom: .11cm;">
            <span style="font-size: small;">BSM
          
        </li>
        
        <li>
          <p style="margin-bottom: .11cm;">
            <span style="font-size: small;">RSA
          
        </li>
        
        <li>
          <p style="margin-bottom: .11cm;">
            <span style="font-size: small;">Tripwire
          
        </li>
      </ul>
      
      
        <span style="font-size: small;">In those cases where Solaris Containers are implemented, the same security mechanisms are utilized with the virtualized instances of the operating system.  
        
        
           
        
        
        
           
        
        
        <table width="590" cellspacing="0" cellpadding="7">
          <tr valign="TOP">
            <td style="border: none; padding: 0;" width="137">
              <p style="margin-top: .21cm;">
                <a name="TOC"></a><span style="font-size: small;"><b>Table of Contents</b>
              
            </td>
            
            <td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: none; border-right: none; padding: 0;" width="425">
              <p style="margin-top: .21cm;">
                <span style="font-size: medium;"><span style="color: #0000ff;"><span style="text-decoration: underline;"><a class="western" href="#ProcedureStatement"><span style="font-size: small;">Procedure Statement………………………………………………………1</a>
              
              
              <p class="western" style="margin-top: .21cm;">
                <span style="color: #0000ff;"><span style="text-decoration: underline;"><a class="western" href="#TOC"><span style="font-size: small;">Table of Contents………………………………………………………….1</a>
              
              
              <p class="western" style="margin-top: .21cm;">
                <span style="color: #0000ff;"><span style="text-decoration: underline;"><a class="western" href="#JASS"><span style="font-size: small;">JASS Implementation……………………………………………………..2</a>
              
              
              <p class="western" style="margin-top: .21cm;">
                <span style="color: #0000ff;"><span style="text-decoration: underline;"><a class="western" href="#Driver"><span style="font-size: small;">Driver……………………………………………………………………...2</a>
              
              
              <p class="western" style="margin-top: .21cm;">
                <span style="color: #0000ff;"><span style="text-decoration: underline;"><a class="western" href="#BSM"><span style="font-size: small;">BSM Implementation……………………………………………………...5</a>
              
              
              <p class="western" style="margin-top: .21cm;">
                <span style="color: #0000ff;"><span style="text-decoration: underline;"><a class="western" href="#Audit"><span style="font-size: small;">Audit Configuration……………………………………………………….5</a>
              
              
              <p class="western" style="margin-top: .21cm;">
                <span style="color: #0000ff;"><span style="text-decoration: underline;"><a class="western" href="#RSA"><span style="font-size: small;">RSA Implementation………………………………………………………6</a>
              
              
              <p class="western" style="margin-top: .21cm;">
                <span style="color: #0000ff;"><span style="text-decoration: underline;"><a class="western" href="#Tripwire"><span style="font-size: small;">Tripwire Implementation………………………………………………….6</a>
              
              
              <p class="western" style="margin-top: .21cm;">
                <span style="color: #0000ff;"><span style="text-decoration: underline;"><a class="western" href="#SolarisContainers"><span style="font-size: small;">Solaris Containers (Virtualization)………………………………………..7</a>
              
              
              <p class="western" style="margin-top: .21cm;">
                <span style="color: #0000ff;"><span style="text-decoration: underline;"><a class="western" href="#Bibliography"><span style="font-size: small;">Bibliography………………………………………………………………11</a>
              
              
              <p class="western" style="margin-top: .21cm;">
                <span style="color: #0000ff;"><span style="text-decoration: underline;"><a class="western" href="#Revision"><span style="font-size: small;">Revision References……………………………………………………….11</a>
              
              
              <p class="western" style="margin-top: .21cm;">
                <span style="color: #0000ff;"><span style="text-decoration: underline;"><a class="western" href="#Appendix"><span style="font-size: small;">Appendix A: Examples……………………………………………………12</a>
              
              
              <p class="western" style="margin-left: 1.24cm; text-indent: -1.24cm; margin-top: .21cm;">
                <span style="color: #0000ff;"><span style="text-decoration: underline;"><a class="western" href="#Scripts"><span style="font-size: small;">Scripts..………………………………………..………………..12</a>
              
              
              <p class="western" style="margin-left: 1.56cm; text-indent: -1.56cm; margin-top: .21cm;">
                <span style="color: #0000ff;"><span style="text-decoration: underline;"><a class="western" href="#Password"><span style="font-size: small;">Password……………………………………………………..…17</a>
              
              
              <p class="western" style="margin-left: 1.56cm; text-indent: -1.56cm; margin-top: .21cm;">
                <span style="color: #0000ff;"><span style="text-decoration: underline;"><a class="western" href="#Audit"><span style="font-size: small;">Audit…………….…………………………………………..….21</a>
              
              
              <p class="western" style="margin-top: .21cm;">
                
                
                <tr valign="TOP">
                  <td style="border: none; padding: 0;" width="137">
                    <p style="margin-bottom: .11cm;">
                      <a name="JASS"></a> <span style="font-size: small;"><b>JASS Implementation:</b>
                    
                    
                    <p style="margin-top: .21cm;">
                      </td> 
                      
                      <td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: none; border-right: none; padding: 0;" width="425">
                        <span style="font-size: small;">The Solaris Security Toolkit, formerly known as the JumpStart Architecture and Security Scripts (JASS) toolkit, provides a flexible and extensible mechanism to harden and audit Solaris Operating Systems (OSs). The Solaris Security Toolkit simplifies and automates the process of securing Solaris Operating Systems and is based on proven security best practices and practical customer site experience gathered over many years. This toolkit can be used to secure SPARC-based and x86/x64-based systems.
                      </td></tr>   
                      
                      
                         
                      
                      
                      
                         
                      
                      
                      <table width="590" cellspacing="0" cellpadding="7">
                        <tr valign="TOP">
                          <td style="border: none; padding: 0;" width="137">
                            <p style="margin-top: .21cm; text-decoration: none;">
                              <a name="Driver"></a> <span style="font-size: small;"><b>Driver</b>
                            
                          </td>
                          
                          <td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: none; border-right: none; padding: 0;" width="425">
                            <p style="margin-bottom: .11cm;">
                              <span style="font-size: small;">JASS provides a set of templates to customize the security profiles. The one utilized is <i>secure.driver</i>.
                            
                            
                            <p style="margin-bottom: .11cm;">
                              <span style="font-size: small;">No scripts are customized (user.init) but some of the scripts in the hardening.driver file, are disabled or enabled to fit the requirements in the environment. 
                            
                            
                            
                              <span style="font-size: small;">Below are the template being used and a brief description of which scripts are intentionally disabled/enabled.  
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm;">
                                <span style="font-size: xx-small;"><i>JASS_SCRIPTS="
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-ab2.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-apache.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-apache2.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-appserv.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-asppp.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-autoinst.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-automount.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-dhcpd.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-directory.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-dmi.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-dtlogin.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-face-log.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-ipv6.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-IIim.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-kdc.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-keyboard-abort.fin <b>### This script was intentionally enabled.</b>
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-keyserv-uid-nobody.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-ldap-client.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-lp.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-mipagent.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-named.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-nfs-client.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-nfs-server.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-nscd-caching.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i># disable-picld.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-ppp.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-preserve.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-power-mgmt.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-remote-root-login.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-rhosts.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-routing.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-rpc.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-samba.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-sendmail.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-slp.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-sma.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-smcwebserver.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-snmp.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-spc.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-ssh-root-login.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-syslogd-listen.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-system-accounts.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-uucp.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-vold.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-wbem.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-xfs.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>disable-xserver-listen.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>enable-account-lockout.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>enable-coreadm.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i># enable-ftpaccess.fin <b>### This script was intentionally disabled.</b>
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>enable-ftp-syslog.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>enable-inetd-syslog.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i># enable-ipfilter.fin <b>### This script was intentionally disabled.</b>
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>enable-password-history.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>enable-priv-nfs-ports.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i># enable-process-accounting.fin <b>### This script was intentionally disabled.</b>
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>enable-rfc1948.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>enable-stack-protection.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>enable-tcpwrappers.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>install-at-allow.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>install-ftpusers.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>install-loginlog.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>install-md5.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>install-nddconfig.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>install-newaliases.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>install-sadmind-options.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>install-security-mode.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>install-shells.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>install-sulog.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>print-rhosts.fin <b>### This script was intentionally enabled.</b>
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>remove-unneeded-accounts.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>set-banner-dtlogin.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>set-banner-ftpd.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>set-banner-sendmail.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>set-banner-sshd.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>set-banner-telnetd.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>set-flexible-crypt.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>set-ftpd-umask.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>set-login-retries.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>set-power-restrictions.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>set-rmmount-nosuid.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>set-root-group.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>set-strict-password-checks.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>set-sys-suspend-restrictions.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>set-system-umask.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>set-tmpfs-limit.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>set-user-password-reqs.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>set-user-umask.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>update-at-deny.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>update-cron-allow.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>update-cron-deny.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>update-cron-log-size.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>update-inetd-conf.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>enable-bsm.fin <b>### This script was intentionally enabled.</b>
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>install-fix-modes.fin
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i>install-strong-permissions.fin <b>### This script was intentionally enabled.</b>
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i># enable-bart.fin <b>### This script was intentionally disabled.</b>
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i># print-sgid-files
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i># print-suid-files
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 2.54cm; text-indent: 1.27cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i># print-unowned-objects
                              
                              
                              
                                 
                              
                              
                              <p class="western" style="margin-left: 3.81cm; margin-top: .21cm; margin-bottom: 0;">
                                <span style="font-size: xx-small;"><i># print-world-writable-objects
                              
                              
                              
                                 
                              
                              
                              
                                 
                              
                              
                              <table width="590" cellspacing="0" cellpadding="7">
                                <tr valign="TOP">
                                  <td style="border: none; padding: 0;" width="137">
                                    <p style="margin-top: .21cm;">
                                      </td> 
                                      
                                      <td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: none; border-right: none; padding: 0;" width="425">
                                        <p class="western" style="margin-top: .21cm;">
                                          <span style="font-size: small;">The scripts which are commented out won't be executed.
                                        
                                      </td></tr>   
                                      
                                      
                                         
                                      
                                      
                                      <p class="western" style="margin-left: 2.54cm; text-indent: 1.27cm; margin-top: .21cm;">
                                        <span style="font-size: small;">Brief description of some outstanding scripts:
                                      
                                      
                                      
                                         
                                      
                                      
                                      <p class="western" style="margin-left: 3.81cm; margin-top: .21cm;">
                                        <span style="font-size: small;"><b>enable-account-lockout.fin:</b> This is to enable lock accounting. 
                                      
                                      
                                      
                                         
                                      
                                      
                                      <p class="western" style="margin-left: 3.81cm; margin-top: .21cm;">
                                        <span style="font-size: small;"><b>enable-coreadm.fin:</b> This enable the core environment. 
                                      
                                      
                                      
                                         
                                      
                                      
                                      <p class="western" style="margin-left: 3.81cm; margin-top: .21cm;">
                                        <span style="font-size: small;"><b>enable-ftpaccess.fin:</b> We set the ftp access disabled, also blocked on IPFilters.
                                      
                                      
                                      
                                         
                                      
                                      
                                      <p class="western" style="margin-left: 3.81cm; margin-top: .21cm;">
                                        <span style="font-size: small;"><b>enable-ftp-syslog.fin:</b> Also trace ftp activity in syslog.
                                      
                                      
                                      
                                         
                                      
                                      
                                      <p class="western" style="margin-left: 3.81cm; margin-top: .21cm;">
                                        <span style="font-size: small;"><b>enable-inetd-syslog.fin:</b> This script configures the Internet Services Daemon (INETD) to log all incoming connections.
                                      
                                      
                                      
                                         
                                      
                                      
                                      <p class="western" style="margin-left: 3.81cm; margin-top: .21cm;">
                                        <span style="font-size: small;"><b>enable-ipfilter.fin:</b> This enable IPFilters environment (with no active rules by default).
                                      
                                      
                                      
                                         
                                      
                                      
                                      <p class="western" style="margin-left: 3.81cm; margin-top: .21cm;">
                                        <span style="font-size: small;"><b>enable-password-history.fin:</b> Enable password history. 
                                      
                                      
                                      
                                         
                                      
                                      
                                      <p class="western" style="margin-left: 3.81cm; margin-top: .21cm;">
                                        <span style="font-size: small;"><b>enable-priv-nfs-ports.fin:</b> This is to allow NFS to accept connections from privileged ports only (below port 1024).
                                      
                                      
                                      
                                         
                                      
                                      
                                      <p class="western" style="margin-left: 3.81cm; margin-top: .21cm;">
                                        <span style="font-size: small;"><b>enable-process-accounting.fin:</b> We don't enable process accounting as it is not useful in our environment. 
                                      
                                      
                                      
                                         
                                      
                                      
                                      <p class="western" style="margin-left: 3.81cm; margin-top: .21cm;">
                                        <span style="font-size: small;"><b>enable-rfc1948.fin:</b> This script will create/modify the /etc/default/inetinit file to enable support of RFC 1948. This RFC defines unique-per-connection ID sequence number generation. For more information, refer to # http://RF.Cx/rfc1948.html.
                                      
                                      
                                      
                                         
                                      
                                      
                                      <p class="western" style="margin-left: 3.81cm; margin-top: .21cm;">
                                        <span style="font-size: small;"><b>enable-stack-protection.fin:</b> Enable stack and logging protection.
                                      
                                      
                                      
                                         
                                      
                                      
                                      <p class="western" style="margin-left: 3.81cm; margin-top: .21cm;">
                                        <span style="font-size: small;"><b>enable-tcpwrappers.fin:</b> Create hosts.allow and hosts.deny files to wrap all TCP connections.
                                      
                                      
                                      
                                         
                                      
                                      
                                      <table width="590" cellspacing="0" cellpadding="7">
                                        <tr valign="TOP">
                                          <td style="border: none; padding: 0;" width="137">
                                            <p style="margin-top: .21cm;">
                                              </td> 
                                              
                                              <td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: none; border-right: none; padding: 0;" width="425">
                                                <p class="western" style="margin-top: .21cm;">
                                                  
                                                  
                                                  <tr valign="TOP">
                                                    <td style="border: none; padding: 0;" width="137">
                                                      <p style="margin-top: .21cm; text-decoration: none;">
                                                        <a name="BSM"></a> <span style="font-size: small;"><b>BSM Implementation </b>
                                                      
                                                      
                                                      <p style="margin-top: .21cm; text-decoration: none;">
                                                        <span style="font-size: small;"><b>Audit Configuration</b>
                                                      
                                                    </td>
                                                    
                                                    <td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: none; border-right: none; padding: 0;" width="425">
                                                      <p class="western" style="margin-top: .21cm;">
                                                        <span style="font-size: small;">The Basic Security Module (BSM) provides two security features. The first feature is an auditing mechanism, which includes tools to assist with the analysis of the auditing data. The second feature is a device-allocation mechanism, which provides the required object-reuse characteristics for removable devices or assignable devices.
                                                      
                                                      
                                                      <p class="western" style="margin-top: .21cm;">
                                                        <span style="font-size: small;">The auditing mechanism helps you detect potential security breaches by revealing suspicious or abnormal patterns of system usage. The auditing mechanism also provides a means to trace suspect actions back to a particular user, thus serving as a deterrent. If users know that their activities are likely to be audited, they might be less likely to attempt malicious activities.
                                                      
                                                      
                                                      <p class="western" style="margin-top: .21cm;">
                                                        <span style="font-size: small;">The audit subsystem is configured to log the audit activity locally and in a remote Syslog server.
                                                      
                                                      
                                                      <p class="western" style="margin-top: .21cm;">
                                                        <span style="font-size: small;">Audit Control file:
                                                      
                                                      
                                                      <p class="western" style="margin-top: .21cm;">
                                                        <span style="font-size: small;"><i>dir:/var/audit
                                                      
                                                      
                                                      <p class="western" style="margin-top: .21cm;">
                                                        <span style="font-size: small;"><i>flags:lo,ex
                                                      
                                                      
                                                      <p class="western" style="margin-top: .21cm;">
                                                        <span style="font-size: small;"><i>minfree:20
                                                      
                                                      
                                                      <p class="western" style="margin-top: .21cm;">
                                                        <span style="font-size: small;"><i>naflags:lo,ex
                                                      
                                                      
                                                      <p class="western" style="margin-top: .21cm;">
                                                        <span style="font-size: small;"><i>plugin: name=audit_syslog.so;p_flags=lo,ex
                                                      
                                                      
                                                      <p class="western" style="margin-top: .21cm;">
                                                        <span style="font-size: small;">Audit Startup file:
                                                      
                                                      
                                                      <p class="western" style="margin-top: .21cm;">
                                                        <span style="font-size: small;"><i>/usr/sbin/auditconfig -setpolicy +cnt
                                                      
                                                      
                                                      <p class="western" style="margin-top: .21cm;">
                                                        <span style="font-size: small;"><i>/usr/sbin/auditconfig -setpolicy +zonename
                                                      
                                                      
                                                      <p class="western" style="margin-top: .21cm;">
                                                        <span style="font-size: small;"><i>/usr/sbin/auditconfig -setpolicy +argv
                                                      
                                                      
                                                      <p class="western" style="margin-top: .21cm;">
                                                        <span style="font-size: small;"><i>/usr/sbin/auditconfig -conf
                                                      
                                                      
                                                      <p class="western" style="margin-top: .21cm;">
                                                        <span style="font-size: small;"><i>/usr/sbin/auditconfig -aconf
                                                      
                                                      
                                                      <p class="western" style="margin-top: .21cm;">
                                                        <span style="font-size: small;">Entry on the /etc/syslog.conf
                                                      
                                                      
                                                      <p class="western" style="margin-top: .21cm;">
                                                        <span style="font-size: small;"><i>audit.notice;auth.debug @dc5sfsecsyslog01
                                                      
                                                      
                                                      <p class="western" style="margin-top: .21cm;">
                                                        
                                                        
                                                        <tr valign="TOP">
                                                          <td style="border: none; padding: 0;" width="137">
                                                            <p style="margin-top: .21cm; text-decoration: none;">
                                                              <a name="RSA"></a> <span style="font-size: small;"><b>RSA Implementation</b>
                                                            
                                                          </td>
                                                          
                                                          <td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: none; border-right: none; padding: 0;" width="425">
                                                            <p class="western" style="margin-top: .21cm; margin-bottom: 0;">
                                                              <span style="font-size: small;">Authentication is only provided in the Solaris box is by using RSA. Steps to be followed for implementing RSA is as following:
                                                            
                                                            
                                                            <ul>
                                                              <li>
                                                                <p class="western" style="margin-top: .21cm; margin-bottom: 0;">
                                                                  <span style="font-size: small;">Get latest sdconf.rec file 
                                                                
                                                              </li>
                                                              
                                                              <li>
                                                                <p class="western" style="margin-top: .21cm; margin-bottom: 0;">
                                                                  <span style="font-size: small;">Download the latest RSA Agent software 
                                                                
                                                              </li>
                                                              
                                                              <li>
                                                                <p class="western" style="margin-top: .21cm; margin-bottom: 0;">
                                                                  <span style="font-size: small;">Copy sdconf.rec file under /var/ace 
                                                                
                                                              </li>
                                                              
                                                              <li>
                                                                <p class="western" style="margin-top: .21cm; margin-bottom: 0;">
                                                                  <span style="font-size: small;">Unzip RSA Agent software 
                                                                
                                                              </li>
                                                              
                                                              <li>
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  <span style="font-size: small;">Run the script install.sh (from the tar file) > Accept > Enter
                                                                
                                                              </li>
                                                            </ul>
                                                          </td>
                                                        </tr>  
                                                        
                                                        
                                                           
                                                        
                                                        
                                                        
                                                           
                                                        
                                                        
                                                        <table width="590" cellspacing="0" cellpadding="7">
                                                          <tr valign="TOP">
                                                            <td style="border: none; padding: 0;" width="137">
                                                              <p style="margin-top: .21cm; text-decoration: none;">
                                                                <a name="Tripwire"></a><a name="Implementation"></a> <span style="font-size: small;"><b>Tripwire Implementation</b>
                                                              
                                                            </td>
                                                            
                                                            <td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: none; border-right: none; padding: 0;" width="425">
                                                              <p style="margin-bottom: .49cm; widows: 2; orphans: 2;">
                                                                <span style="font-size: small;">Tripwire is a browser-based configuration audit and control tool which monitors file servers. It baseline's the files using a set of rules that specify what directories, files should be monitored. The data collected as a result of running the rules becomes the benchmark against which future checks are measured.
                                                              
                                                              
                                                              <p style="margin-top: .49cm; margin-bottom: .49cm; widows: 2; orphans: 2;">
                                                                <span style="font-size: small;">Steps to install <i>TWeagent  </i>(Tripwire Enterprise Agent   (INTEL) 7.1.0) in Solaris box are as following:
                                                              
                                                              
                                                              <ul>
                                                                <li>
                                                                  <p style="margin-top: .49cm; margin-bottom: 0; widows: 2; orphans: 2;">
                                                                    <span style="font-size: small;">Copy the files from tomcat:/backup (SPARC or x86) to the proper servers
                                                                  
                                                                </li>
                                                                
                                                                <li>
                                                                  <p style="margin-bottom: .49cm; widows: 2; orphans: 2;">
                                                                    <span style="font-size: small;">Log into the server and uncompress the file
                                                                  
                                                                </li>
                                                                
                                                                <li>
                                                                  <p style="margin-bottom: .49cm; widows: 2; orphans: 2;">
                                                                    <span style="font-size: small;">Install the package
                                                                  
                                                                </li>
                                                                
                                                                <li>
                                                                  <p style="margin-top: .49cm; widows: 2; orphans: 2;">
                                                                    <span style="font-size: small;">Start the agent
                                                                  
                                                                </li>
                                                              </ul>
                                                            </td>
                                                          </tr>
                                                        
                                                        
                                                        
                                                           
                                                        
                                                        
                                                        
                                                           
                                                        
                                                        
                                                        
                                                           
                                                        
                                                        
                                                        <table width="590" cellspacing="0" cellpadding="7">
                                                          <tr valign="TOP">
                                                            <td style="border: none; padding: 0;" width="109">
                                                              <p style="margin-top: .21cm;">
                                                                <a name="SolarisContainers"></a><span style="font-size: small;"><b>Solaris Containers</b>
                                                              
                                                            </td>
                                                            
                                                            <td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: none; border-right: none; padding: 0;" width="454">
                                                              <p class="western" style="margin-top: .21cm; widows: 0; orphans: 0;">
                                                                A zone is a single instance of the Solaris Operating System, in which processes are isolated from the rest of the system.
                                                              
                                                              
                                                              <p class="western" style="margin-top: .21cm;">
                                                                There are two types of zones: global zone and non-global zone. Every Solaris system contains a global zone. The global zone is the only zone from which a non-global zone can be configured, installed, managed, or uninstalled. Only the global zone is bootable from the system hardware.
                                                              
                                                              
                                                              <p class="western" style="margin-top: .21cm;">
                                                                A non-global zone can be thought of as a box. To enforce basic process isolation, a process can see only those processes that exist in the same zone. Basic communication between zones is accomplished by giving each zone at least one logical network interface. An application running in one zone cannot observe the network traffic of another zone. This isolation is maintained even though the respective streams of packets travel through the same physical interface.
                                                              
                                                              
                                                              <p class="western" style="margin-top: .21cm;">
                                                                Each zone is given a portion of the file system hierarchy. Because each zone is confined to its subtree of the file system hierarchy, a workload running in a particular zone cannot access the on-disk data of another workload running in a different zone.
                                                              
                                                              
                                                              <p class="western" style="margin-top: .21cm;">
                                                                There are two types of non-global zone root file system models: sparse and whole root. The whole root zone model provides the maximum configurability. All of the required and any selected optional Solaris packages are installed into the private file systems of the zone. The sparse root zone model has only a subset of the root packages are installed
                                                              
                                                              
                                                              <p class="western" style="margin-top: .21cm;">
                                                                We run most applications in non-global zones except the databases. Zones are hardened to ensure high-level security. The practices are:
                                                              
                                                              
                                                              <ol>
                                                                <li>
                                                                  <p class="western" style="margin-bottom: .35cm; widows: 2; orphans: 2;">
                                                                    Whole root zones(Non-global) with shared network interface
                                                                  
                                                                </li>
                                                              </ol>
                                                              
                                                              <p class="western" style="margin-left: 1.27cm; margin-top: .21cm;">
                                                                We will apply the hardening methods to the zones accordingly
                                                              
                                                              
                                                              <ol>
                                                                <li>
                                                                  <p class="western" style="margin-bottom: .35cm; widows: 2; orphans: 2;">
                                                                    JASS: global zone 0, zone1, zone2
                                                                  
                                                                </li>
                                                                
                                                                <li>
                                                                  <p class="western" style="margin-bottom: .35cm; widows: 2; orphans: 2;">
                                                                    RSA: global zone 0, zone1, zone2
                                                                  
                                                                </li>
                                                                
                                                                <li>
                                                                  <p class="western" style="margin-bottom: .35cm; widows: 2; orphans: 2;">
                                                                    BSM: global zone 0
                                                                  
                                                                </li>
                                                              </ol>
                                                              
                                                              <ol start="2">
                                                                <li>
                                                                  <p class="western" style="margin-bottom: .35cm; widows: 2; orphans: 2;">
                                                                    Whole root zones(Non-global) with exclusive network interface
                                                                  
                                                                </li>
                                                              </ol>
                                                              
                                                              <p class="western" style="margin-left: 1.27cm; margin-top: .21cm;">
                                                                We will apply the hardening methods to the zones accordingly
                                                              
                                                              
                                                              <ol>
                                                                <li>
                                                                  <p class="western" style="margin-bottom: .35cm; widows: 2; orphans: 2;">
                                                                    JASS: global zone 0, zone1, zone2
                                                                  
                                                                </li>
                                                                
                                                                <li>
                                                                  <p class="western" style="margin-bottom: .35cm; widows: 2; orphans: 2;">
                                                                    RSA: global zone 0, zone1, zone2
                                                                  
                                                                </li>
                                                                
                                                                <li>
                                                                  <p class="western" style="margin-bottom: .35cm; widows: 2; orphans: 2;">
                                                                    BSM: global zone 0
                                                                  
                                                                </li>
                                                              </ol>
                                                              
                                                              <ol start="3">
                                                                <li>
                                                                  <p class="western" style="margin-bottom: .35cm; widows: 2; orphans: 2;">
                                                                    Sparse root zones(Non-global) with shared network interface
                                                                  
                                                                </li>
                                                              </ol>
                                                              
                                                              <p class="western" style="margin-left: 1.27cm; margin-top: .21cm;">
                                                                We will apply the hardening methods to the zones accordingly
                                                              
                                                              
                                                              <ol>
                                                                <li>
                                                                  <p class="western" style="margin-bottom: .35cm; widows: 2; orphans: 2;">
                                                                    JASS: global zone 0, zone1, zone2
                                                                  
                                                                </li>
                                                                
                                                                <li>
                                                                  <p class="western" style="margin-bottom: .35cm; widows: 2; orphans: 2;">
                                                                    RSA: global zone 0, zone1, zone2
                                                                  
                                                                </li>
                                                                
                                                                <li>
                                                                  <p class="western" style="margin-bottom: .35cm; widows: 2; orphans: 2;">
                                                                    BSM: global zone 0
                                                                  
                                                                </li>
                                                              </ol>
                                                              
                                                              <ol start="4">
                                                                <li>
                                                                  <p class="western" style="margin-bottom: .35cm; widows: 2; orphans: 2;">
                                                                    Sparse root zones(Non-global) with exclusive network interface
                                                                  
                                                                </li>
                                                              </ol>
                                                              
                                                              <p class="western" style="margin-left: 1.27cm; margin-top: .21cm;">
                                                                We will apply the hardening methods to the zones accordingly
                                                              
                                                              
                                                              <ol>
                                                                <li>
                                                                  <p class="western" style="margin-bottom: .35cm; widows: 2; orphans: 2;">
                                                                    JASS: global zone 0, zone1, zone2
                                                                  
                                                                </li>
                                                                
                                                                <li>
                                                                  <p class="western" style="margin-bottom: .35cm; widows: 2; orphans: 2;">
                                                                    RSA: global zone 0, zone1, zone2
                                                                  
                                                                </li>
                                                                
                                                                <li>
                                                                  <p class="western" style="margin-bottom: .35cm; widows: 2; orphans: 2;">
                                                                    BSM: global zone 0
                                                                  
                                                                </li>
                                                              </ol>
                                                              
                                                              <ul>
                                                                <li>
                                                                  <p style="margin-top: .49cm; margin-bottom: .49cm; widows: 2; orphans: 2;">
                                                                    <span style="font-size: small;">Example of a zone configuration file from a sparse zone with shared network.
                                                                  
                                                                </li>
                                                              </ul>
                                                              
                                                              <p style="margin-bottom: 0;">
                                                                <span style="font-size: xx-small;"><i><?xml version="1.0&#8243; encoding="UTF-8&#8243;?>
                                                              
                                                              
                                                              <p style="margin-bottom: 0;">
                                                                <span style="font-size: xx-small;"><i><!DOCTYPE zone PUBLIC "-//Sun Microsystems Inc//DTD Zones//EN" "file:///usr/share/lib/xml/dtd/zonecfg.dtd.1">
                                                              
                                                              
                                                              <p style="margin-bottom: 0;">
                                                                <span style="font-size: xx-small;"><i><!-
                                                              
                                                              
                                                              <p style="margin-bottom: 0;">
                                                                <span style="font-size: xx-small;"><i>DO NOT EDIT THIS FILE. Use zonecfg(1M) instead.
                                                              
                                                              
                                                              <p style="margin-bottom: 0;">
                                                                <span style="font-size: xx-small;"><i>->
                                                              
                                                              
                                                              <p style="margin-bottom: 0;">
                                                                <span style="font-size: xx-small;"><i><zone name="dc5sfapp01a" zonepath="/zones/dc5sfapp01a" autoboot="true">
                                                              
                                                              
                                                              <p style="margin-bottom: 0;">
                                                                <span style="font-size: xx-small;"><i><inherited-pkg-dir directory="/lib"/>
                                                              
                                                              
                                                              <p style="margin-bottom: 0;">
                                                                <span style="font-size: xx-small;"><i><inherited-pkg-dir directory="/platform"/>
                                                              
                                                              
                                                              <p style="margin-bottom: 0;">
                                                                <span style="font-size: xx-small;"><i><inherited-pkg-dir directory="/sbin"/>
                                                              
                                                              
                                                              <p style="margin-bottom: 0;">
                                                                <span style="font-size: xx-small;"><i><inherited-pkg-dir directory="/usr"/>
                                                              
                                                              
                                                              <p style="margin-bottom: 0;">
                                                                <span style="font-size: xx-small;"><i><inherited-pkg-dir directory="/usr/sfw"/>
                                                              
                                                              
                                                              <p style="margin-bottom: 0;">
                                                                <span style="font-size: xx-small;"><i><inherited-pkg-dir directory="/export/home/apache-ant-1.6.1&#8243;/>
                                                              
                                                              
                                                              <p style="margin-bottom: 0;">
                                                                <span style="font-size: xx-small;"><i><inherited-pkg-dir directory="/export/home/jdk1.6.0_13&#8243;/>
                                                              
                                                              
                                                              <p style="margin-bottom: 0;">
                                                                <span style="font-size: xx-small;"><i><network address="10.5.30.14&#8243; physical="nge0&#8243;/>
                                                              
                                                              
                                                              <p style="margin-bottom: 0;">
                                                                <span style="font-size: xx-small;"><i></zone>
                                                              
                                                              
                                                              <ul>
                                                                <li>
                                                                  <p style="margin-top: .49cm; margin-bottom: .49cm; widows: 2; orphans: 2;">
                                                                    <span style="font-size: small;">Example of a zone configuration file from a root zone with shared network.
                                                                  
                                                                </li>
                                                              </ul>
                                                              
                                                              <p style="margin-bottom: 0;">
                                                                <span style="font-size: xx-small;"><i><?xml version="1.0&#8243; encoding="UTF-8&#8243;?>
                                                              
                                                              
                                                              <p style="margin-bottom: 0;">
                                                                <span style="font-size: xx-small;"><i><!DOCTYPE zone PUBLIC "-//Sun Microsystems Inc//DTD Zones//EN" "file:///usr/share/lib/xml/dtd/zonecfg.dtd.1">
                                                              
                                                              
                                                              <p style="margin-bottom: 0;">
                                                                <span style="font-size: xx-small;"><i><!-
                                                              
                                                              
                                                              <p style="margin-bottom: 0;">
                                                                <span style="font-size: xx-small;"><i>DO NOT EDIT THIS FILE. Use zonecfg(1M) instead.
                                                              
                                                              
                                                              <p style="margin-bottom: 0;">
                                                                <span style="font-size: xx-small;"><i>->
                                                              
                                                              
                                                              <p style="margin-bottom: 0;">
                                                                <span style="font-size: xx-small;"><i><zone name="dc5sfsmnsageapp01&#8243; zonepath="/zones/dc5sfsmnsageapp01&#8243; autoboot="true">
                                                              
                                                              
                                                              <p style="margin-bottom: 0;">
                                                                <span style="font-size: xx-small;"><i><network address="10.5.35.14&#8243; physical="nge0&#8243;/>
                                                              
                                                              
                                                              <p style="margin-top: .49cm; margin-bottom: .49cm; widows: 2; orphans: 2;">
                                                                <span style="font-size: xx-small;"><i></zone>
                                                              
                                                              
                                                              <ul>
                                                                <li>
                                                                  <p style="margin-top: .49cm; margin-bottom: .49cm; widows: 2; orphans: 2;">
                                                                    <span style="font-size: small;">Example of a zone configuration file from a root zone with a dedicated network interface.
                                                                  
                                                                </li>
                                                              </ul>
                                                              
                                                              <p style="margin-bottom: 0;">
                                                                <span style="font-size: xx-small;"><i><?xml version="1.0&#8243; encoding="UTF-8&#8243;?>
                                                              
                                                              
                                                              <p style="margin-bottom: 0;">
                                                                <span style="font-size: xx-small;"><i><!DOCTYPE zone PUBLIC "-//Sun Microsystems Inc//DTD Zones//EN" "file:///usr/share/lib/xml/dtd/zonecfg.dtd.1">
                                                              
                                                              
                                                              <p style="margin-bottom: 0;">
                                                                <span style="font-size: xx-small;"><i><!-
                                                              
                                                              
                                                              <p style="margin-bottom: 0;">
                                                                <span style="font-size: xx-small;"><i>DO NOT EDIT THIS FILE. Use zonecfg(1M) instead.
                                                              
                                                              
                                                              <p style="margin-bottom: 0;">
                                                                <span style="font-size: xx-small;"><i>->
                                                              
                                                              
                                                              <p style="margin-bottom: 0;">
                                                                <span style="font-size: xx-small;"><i><zone name="dc5sfsmnsageweb01&#8243; zonepath="/zones/dc5sfsmnsageweb01&#8243; autoboot="true" ip-type="exclusive">
                                                              
                                                              
                                                              <p style="margin-bottom: 0;">
                                                                <span style="font-size: xx-small;"><i><network address="" physical="nge2&#8243;/>
                                                              
                                                              
                                                              <p style="margin-top: .49cm; margin-bottom: .49cm; widows: 2; orphans: 2;">
                                                                <span style="font-size: xx-small;"><i></zone>
                                                              
                                                              
                                                              <p style="margin-top: .49cm; widows: 2; orphans: 2;">
                                                                
                                                                
                                                                <tr valign="TOP">
                                                                  <td style="border: none; padding: 0;" width="109">
                                                                    <p style="margin-top: .21cm;">
                                                                      <a name="Bibliography"></a><span style="font-size: small;"><b>Bibliography</b>
                                                                    
                                                                  </td>
                                                                  
                                                                  <td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: none; border-right: none; padding: 0;" width="454">
                                                                    <p class="western" style="margin-top: .21cm;">
                                                                      <span style="font-size: small;">International Standard ISO/IEC 17799
                                                                    
                                                                    
                                                                    <p class="western" style="margin-left: 1.27cm; margin-top: .21cm;">
                                                                      <span style="font-size: small;">Information Technology – Security Techniques – Code Of Practice For Information Security Management
                                                                    
                                                                  </td>
                                                                </tr>  
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  <a name="Appendix"></a><b>Appendix A: Examples</b>
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  <a name="Scripts"></a><b>Scripts </b>
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  /opt/SUNWjass/Finish # ls -lrt
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  total 834
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 697 Jul 26 2005 disable-ab2.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 892 Jul 26 2005 disable-IIim.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1103 Jul 26 2005 disable-directory.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1560 Jul 26 2005 disable-dhcpd.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 888 Jul 26 2005 disable-automount.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1023 Jul 26 2005 disable-asppp.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 566 Jul 26 2005 disable-appserv.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 532 Jul 26 2005 disable-apache2.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1159 Jul 26 2005 disable-apache.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 644 Jul 26 2005 disable-named.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1013 Jul 26 2005 disable-mipagent.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 999 Jul 26 2005 disable-ldap-client.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 2460 Jul 26 2005 disable-keyserv-uid-nobody.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1850 Jul 26 2005 disable-kdc.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 797 Jul 26 2005 disable-ipv6.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 935 Jul 26 2005 disable-face-log.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1869 Jul 26 2005 disable-routing.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1454 Jul 26 2005 disable-rhosts.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1361 Jul 26 2005 disable-preserve.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1070 Jul 26 2005 disable-ppp.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 2229 Jul 26 2005 disable-power-mgmt.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 847 Jul 26 2005 disable-picld.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1865 Jul 26 2005 disable-nscd-caching.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 984 Jul 26 2005 disable-nfs-server.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 825 Jul 26 2005 disable-spc.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 949 Jul 26 2005 disable-slp.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1854 Jul 26 2005 enable-password-history.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 2823 Jul 26 2005 enable-inetd-syslog.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1352 Jul 26 2005 enable-ftpaccess.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1124 Jul 26 2005 enable-ftp-syslog.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 2166 Jul 26 2005 enable-bart.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 2639 Jul 26 2005 enable-account-lockout.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1165 Jul 26 2005 enable-32bit-kernel.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 434 Jul 26 2005 disable-xfs.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 2253 Jul 26 2005 install-ftpusers.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 4418 Jul 26 2005 install-fix-modes.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1570 Jul 26 2005 install-at-allow.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1290 Jul 26 2005 install-Sun_ONE-WS.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 2104 Jul 26 2005 enable-tcpwrappers.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1572 Jul 26 2005 enable-priv-nfs-ports.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1374 Jul 26 2005 install-shells.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1965 Jul 26 2005 install-sadmind-options.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1959 Jul 26 2005 install-recommended-patches.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1911 Jul 26 2005 install-openssh.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1040 Jul 26 2005 install-newaliases.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 3073 Jul 26 2005 install-md5.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1330 Jul 26 2005 print-unowned-objects.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1188 Jul 26 2005 print-suid-files.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1188 Jul 26 2005 print-sgid-files.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 3942 Jul 26 2005 minimize-Sun_ONE-WS.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 570 Jul 26 2005 install-templates.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 2329 Jul 26 2005 set-banner-dtlogin.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1122 Jul 26 2005 remove-unneeded-accounts.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1564 Jul 26 2005 print-world-writable-objects.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1877 Jul 26 2005 set-term-type.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1699 Jul 26 2005 set-system-umask.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 4421 Jul 26 2005 set-strict-password-checks.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1086 Jul 26 2005 set-root-group.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 2266 Jul 26 2005 set-rmmount-nosuid.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1380 Jul 26 2005 set-login-retries.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 2087 Jul 26 2005 update-cron-deny.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1740 Jul 26 2005 update-cron-allow.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1225 Jul 26 2005 suncluster3x-set-nsswitch-conf.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 2084 Jul 26 2005 set-tmpfs-limit.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 2048 Aug 22 2008 disable-dtlogin.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1286 Aug 22 2008 disable-dmi.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1155 Aug 22 2008 disable-autoinst.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 678 Aug 22 2008 disable-serial-login.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 6428 Aug 22 2008 disable-sendmail.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1102 Aug 22 2008 disable-samba.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1636 Aug 22 2008 disable-rpc.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1174 Aug 22 2008 disable-remote-root-login.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 451 Aug 22 2008 disable-nis-client.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1369 Aug 22 2008 disable-nfs-client.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1018 Aug 22 2008 disable-mesg.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 2149 Aug 22 2008 disable-lp.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1400 Aug 22 2008 disable-keyboard-abort.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1948 Aug 22 2008 enable-ssh-root-login.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1774 Aug 22 2008 enable-sar.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1555 Aug 22 2008 enable-rfc1948.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 3804 Aug 22 2008 enable-process-accounting.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 2031 Aug 22 2008 enable-password-changes.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 690 Aug 22 2008 enable-ldmd.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 3805 Aug 22 2008 enable-ipfilter.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1122 Aug 22 2008 enable-ftp-debuglog.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1217 Aug 22 2008 enable-cronlog.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 3368 Aug 22 2008 enable-coreadm.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 6862 Aug 22 2008 enable-bsm.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 2118 Aug 22 2008 disable-xserver-listen.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 4306 Aug 22 2008 disable-xdmcp.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 997 Aug 22 2008 disable-wbem.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1461 Aug 22 2008 disable-vold.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1608 Aug 22 2008 disable-uucp.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 3851 Aug 22 2008 disable-system-accounts.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 2986 Aug 22 2008 disable-syslogd-listen.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1938 Aug 22 2008 disable-ssh-root-login.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1324 Aug 22 2008 disable-snmp.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 535 Aug 22 2008 disable-smcwebserver.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1237 Aug 22 2008 disable-sma.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1292 Aug 22 2008 install-loginlog.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 2084 Aug 22 2008 install-local-syslog.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 2563 Aug 22 2008 install-ldm.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 2904 Aug 22 2008 install-jass.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1527 Aug 22 2008 install-connlog.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1573 Aug 22 2008 install-authlog.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 3095 Aug 22 2008 enable-xscreensaver.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 3773 Aug 22 2008 enable-stack-protection.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1080 Aug 22 2008 print-rhosts.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 765 Aug 22 2008 print-package-files.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 2281 Aug 22 2008 print-jumpstart-environment.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 3758 Aug 22 2008 print-jass-environment.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1151 Aug 22 2008 install-sulog.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1384 Aug 22 2008 install-strong-permissions.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1897 Aug 22 2008 install-security-mode.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1347 Aug 22 2008 install-nddconfig.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 2089 Aug 22 2008 set-power-restrictions.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1642 Aug 22 2008 set-oem-banner.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 768 Aug 22 2008 set-lp-open.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 2774 Aug 22 2008 set-lp-localonly.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1202 Aug 22 2008 set-log-file-permissions.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 3144 Aug 22 2008 set-grub-password.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 4738 Aug 22 2008 set-greeter-warning.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 2803 Aug 22 2008 set-ftpd-umask.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 4147 Aug 22 2008 set-flexible-crypt.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 3437 Aug 22 2008 set-failed-logins.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1664 Aug 22 2008 set-dtlogin-open.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 2642 Aug 22 2008 set-dtlogin-localonly.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 961 Aug 22 2008 set-calendar-open.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1810 Aug 22 2008 set-calendar-localonly.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1307 Aug 22 2008 set-banner-telnetd.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1829 Aug 22 2008 set-banner-sshd.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 2027 Aug 22 2008 set-banner-sendmail.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 4350 Aug 22 2008 set-banner-ftpd.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 6560 Aug 22 2008 s15k-static-arp.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 3460 Aug 22 2008 s15k-sms-secure-failover.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1329 Aug 22 2008 s15k-sms-override.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 2010 Aug 22 2008 s15k-exclude-domains.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 10195 Aug 22 2008 update-inetd-conf.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 4944 Aug 22 2008 update-cron-log-size.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1909 Aug 22 2008 update-at-deny.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 663 Aug 22 2008 set-wbem-open.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1323 Aug 22 2008 set-wbem-localonly.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 3352 Aug 22 2008 set-user-umask.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 3049 Aug 22 2008 set-user-password-reqs.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 974 Aug 22 2008 set-ttdb-open.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1635 Aug 22 2008 set-ttdb-localonly.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1558 Aug 22 2008 set-sys-suspend-restrictions.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 2584 Aug 22 2008 set-ssh-config.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 672 Aug 22 2008 set-smcwebserver-open.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 910 Aug 22 2008 set-smcwebserver-localonly.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 909 Aug 22 2008 set-rpc-open.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 2060 Aug 22 2008 set-rpc-localonly.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 1673 Aug 22 2008 set-root-password.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  -r-r-r- 1 root root 4734 Aug 22 2008 set-root-home-dir.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  <a name="Password"></a><b>Password</b>
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  opt/SUNWjass/Finish # pwd
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  [/opt/SUNWjass/Finish # cat set-user-password-reqs.fin
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  #!/bin/sh
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  #
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  # Copyright 2006 Sun Microsystems, Inc. All rights reserved.
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  # Use is subject to license terms.
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  #
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  # ident "@(#)set-user-password-reqs.fin 3.10 06/10/30 SMI"
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  #
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  # This script installs some basic password requirements for users. Note
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  # that this effects local password policy only.
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  logMessage "Installing user password requirements."
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  echo ""
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  PASSWD=${JASS_ROOT_DIR}etc/default/passwd
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  if [ ! -f ${PASSWD} ]; then
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  create_a_file -m 0444 -o root:sys ${PASSWD}
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  echo ""
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  fi
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  changeToBeMade="0&#8243;
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  # Determine the values to be used. If values are
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  # already in place, then use them. Otherwise, use the
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  # defaults that are included below.
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  minWeeks=`nawk -F= '$1==keyword { print $2 }' keyword="MINWEEKS" ${PASSWD}`
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  if [ ! -z "${JASS_AGING_MINWEEKS}" ]; then
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  if [ "${JASS_AGING_MINWEEKS}" != "${minWeeks}" ]; then
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  changeToBeMade="1&#8243;
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  if [ -z "${minWeeks}" ]; then
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  minWeeks="NONE"
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  fi
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  logMessage 'Changing MINWEEKS setting from ${minWeeks} to ${JASS_AGING_MINWEEKS}.'
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  fi
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  minWeeks="${JASS_AGING_MINWEEKS}"
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  fi
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  maxWeeks=`nawk -F= '$1==keyword { print $2 }' keyword="MAXWEEKS" ${PASSWD}`
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  if [ ! -z "${JASS_AGING_MAXWEEKS}" ]; then
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  if [ "${JASS_AGING_MAXWEEKS}" != "${maxWeeks}" ]; then
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  changeToBeMade="1&#8243;
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  if [ -z "${maxWeeks}" ]; then
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  maxWeeks="NONE"
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  fi
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  logMessage 'Changing MAXWEEKS setting from ${maxWeeks} to ${JASS_AGING_MAXWEEKS}.'
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  fi
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  maxWeeks="${JASS_AGING_MAXWEEKS}"
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  fi
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  warnWeeks=`nawk -F= '$1==keyword { print $2 }' keyword="WARNWEEKS" ${PASSWD}`
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  if [ ! -z "${JASS_AGING_WARNWEEKS}" ]; then
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  if [ "${JASS_AGING_WARNWEEKS}" != "${warnWeeks}" ]; then
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  changeToBeMade="1&#8243;
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  if [ -z "${warnWeeks}" ]; then
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  warnWeeks="NONE"
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  fi
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  logMessage 'Changing WARNWEEKS setting from ${warnWeeks} to ${JASS_AGING_WARNWEEKS}.'
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  fi
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  warnWeeks="${JASS_AGING_WARNWEEKS}"
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  fi
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  passLength=`nawk -F= '$1==keyword { print $2 }' keyword="PASSLENGTH" ${PASSWD}`
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  if [ ! -z "${JASS_PASS_LENGTH}" ]; then
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  if [ "${JASS_PASS_LENGTH}" != "${passLength}" ]; then
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  changeToBeMade="1&#8243;
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  if [ -z "${passLength}" ]; then
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  passLength="NONE"
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  fi
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  logMessage 'Changing PASSLENGTH setting from ${passLength} to ${JASS_PASS_LENGTH}.'
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  fi
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  passLength="${JASS_PASS_LENGTH}"
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  fi
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  if [ "${changeToBeMade}" = "1" ]; then
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  echo ""
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  backup_file ${PASSWD}
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  # Remove the old entries and insert the new ones.
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  cat ${PASSWD}.${JASS_SUFFIX} |\
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  egrep -v '^MINWEEKS=|^MAXWEEKS=|^WARNWEEKS=|^PASSLENGTH=' > ${PASSWD}
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  if [ ! -z "${JASS_AGING_MINWEEKS}" ]; then
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  echo "MINWEEKS=${minWeeks}" >> ${PASSWD}
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  fi
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  if [ ! -z "${JASS_AGING_MAXWEEKS}" ]; then
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  echo "MAXWEEKS=${maxWeeks}" >> ${PASSWD}
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  fi
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  if [ ! -z "${JASS_AGING_WARNWEEKS}" ]; then
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  echo "WARNWEEKS=${warnWeeks}" >> ${PASSWD}
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  fi
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  if [ ! -z "${JASS_PASS_LENGTH}" ]; then
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  echo "PASSLENGTH=${passLength}" >> ${PASSWD}
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  fi
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  change_owner root:sys ${PASSWD}
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  change_default_perms ${PASSWD}
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  fi
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm;">
                                                                  [ ?0 dc5sfshrapp01 root 1 !542 0 22:47:39 ]
                                                                
                                                                
                                                                
                                                                   
                                                                
                                                                
                                                                <p class="western" style="margin-top: .21cm; widows: 0; orphans: 0;">
                                                                  /opt/SUNWjass/Finish #
