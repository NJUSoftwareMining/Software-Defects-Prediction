<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<!DOCTYPE bugzilla SYSTEM "https://bugs.eclipse.org/bugs/page.cgi?id=bugzilla.dtd">

<bugzilla version="4.4.7"
          urlbase="https://bugs.eclipse.org/bugs/"
          
          maintainer="webmaster@eclipse.org"
          exporter="463808243@qq.com"
>

    <bug>
          <bug_id>420116</bug_id>
          
          <creation_ts>2013-10-22 16:40:00 -0400</creation_ts>
          <short_desc>[1.8] Add implemented methods should consider type annotations</short_desc>
          <delta_ts>2014-04-07 08:41:16 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>enhancement</bug_severity>
          <target_milestone>4.4 M7</target_milestone>
          <dependson>417937</dependson>
    
    <dependson>426094</dependson>
    
    <dependson>431963</dependson>
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Stephan Herrmann">stephan.herrmann@berlin.de</reporter>
          <assigned_to name="Manju Mathew">manju656@gmail.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>jarthana@in.ibm.com</cc>
    
    <cc>manju656@gmail.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
    
    <cc>noopur_gupta@in.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706886-bjr70vDDudnDVIQ7Q_Pxn0Ua6vVJV9sCFiBKJ_b1Etk</token>

      

      <flag name="review"
          id="61981"
          type_id="1"
          status="-"
          setter="noopur_gupta@in.ibm.com"
    />

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2321887</commentid>
    <comment_count>0</comment_count>
    <who name="Stephan Herrmann">stephan.herrmann@berlin.de</who>
    <bug_when>2013-10-22 16:40:17 -0400</bug_when>
    <thetext>Preparing to speak about JSR 308 at ECE I see that &quot;Add implemented methods&quot; nicely copies old annotations, but ignores type annotations.

While the implementation looks straight-forward, I&apos;m not sure what&apos;s the plan regarding ASTProvider.SHARED_AST_LEVEL. Is it still at JLS4 because some operations are still used that only exist below JLS8?</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2321888</commentid>
    <comment_count>1</comment_count>
      <attachid>236787</attachid>
    <who name="Stephan Herrmann">stephan.herrmann@berlin.de</who>
    <bug_when>2013-10-22 16:43:37 -0400</bug_when>
    <thetext>Created attachment 236787
Implementation sketch

This patch succeeds during smoke testing :)

But as mentioned, it&apos;s probably too early to switch to JLS8, right?</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2349239</commentid>
    <comment_count>2</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2014-01-14 02:02:40 -0500</bug_when>
    <thetext>Thanks Stephan for the patch, I have applied the patch and it works in normal cases.

Consider the below interface:

package typeAnnotation;

import java.awt.List;

import org.eclipse.jdt.annotation.NonNull;
import org.eclipse.jdt.annotation.Nullable;

interface A {

	int foo1(@Nullable Object[] o1, Object @Nullable [] o2);

	int foo2(Object @Nullable... o1);

	int foo3(Object @Nullable [] o1, @Nullable Object... o2);

	void foo4(@Nullable String s1, @NonNull String... s2);

	void foo5(@Nullable List l1, java.util.@NonNull List&lt;String&gt; l2);
}

Implementing the above interface leaves the user with multiple errors.
@Markus/ @Stephan : Can one of you point to valid and invalid cases in the above example.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2349351</commentid>
    <comment_count>3</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2014-01-14 07:09:04 -0500</bug_when>
    <thetext>Bug 386410 contains pre-Java-8 discussions about when to copy annotations, and bug 386410 comment 4 the current conclusion for declaration annotations.

In JDT UI, we use the helper method StubUtility2#isCopyOnInheritAnnotation(..) to decide whether an annotation should be copied or not.

In BETA_JAVA8, TYPE_USE annotations are now part of a method parameter&apos;s ITypeBinding. They no longer appear in IMethodBinding#getParameterAnnotations(int), and that&apos;s why StubUtility2#createParameters(..) doesn&apos;t copy them any more.

I think most cases will work fine after bug 417937 is fixed. We may have to fix the special case for varargs (copy type annotations as well).</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2351501</commentid>
    <comment_count>4</comment_count>
    <who name="Stephan Herrmann">stephan.herrmann@berlin.de</who>
    <bug_when>2014-01-18 12:44:16 -0500</bug_when>
    <thetext>(In reply to Manju Mathew from comment #2)
&gt; Implementing the above interface leaves the user with multiple errors.
&gt; @Markus/ @Stephan : Can one of you point to valid and invalid cases in the
&gt; above example.

Is this still relevant? If so, please also show the implementing class. If all annotations are directly copied, I wouldn&apos;t expect any error.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2351631</commentid>
    <comment_count>5</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2014-01-19 20:35:29 -0500</bug_when>
    <thetext>(In reply to Stephan Herrmann from comment #4)
&gt; Is this still relevant? If so, please also show the implementing class.

import java.awt.List;

import org.eclipse.jdt.annotation.NonNull;
import org.eclipse.jdt.annotation.Nullable;

public class AImplemented implements A {

	@Override
	public int foo1(Object[] o1, @Nullable Object[] o2) { //Error1: annotation not copied to right location
		// TODO Auto-generated method stub
		return 0;
	}

	@Override
	public int foo2(Object... o1) { //Error2: annotation is not copied
		// TODO Auto-generated method stub
		return 0;
	}

	@Override
	public int foo3(@Nullable Object[] o1, @Nullable Object... o2) { //Error3: Same as Error1
		// TODO Auto-generated method stub
		return 0;
	}

	@Override
	public void foo4(@Nullable String s1, @NonNull String... s2) {
		// TODO Auto-generated method stub

	}

	@Override
	public void foo5(@Nullable List l1, @NonNull java.util.List&lt;String&gt; l2) { //Error4: annotation not in right location
		// TODO Auto-generated method stub

	}

}</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2352781</commentid>
    <comment_count>6</comment_count>
      <attachid>239210</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2014-01-21 20:44:57 -0500</bug_when>
    <thetext>Created attachment 239210
Updated Patch + Testcases

With the fix for bug 417937, most of the cases are taken care off with out any changes in UI code. Bug 426094 handles annotation on dimentions. As Markus mentioned, we need to explicity take care of varargs in UI. I have updated the patch and also added few testcases. For the testcase to execute properly we need org.eclipse.jdt.annotation 2.o</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2383864</commentid>
    <comment_count>7</comment_count>
      <attachid>241534</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2014-04-02 21:52:29 -0400</bug_when>
    <thetext>Created attachment 241534
Patch+Tests

Created the patch against master. Noopur, now you should be able to apply the patch neatly.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2383875</commentid>
    <comment_count>8</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2014-04-02 22:51:43 -0400</bug_when>
    <thetext>(In reply to Manju Mathew from comment #6)
&gt; Created attachment 239210 [details] [diff]
&gt; For the testcase to execute
&gt; properly we need org.eclipse.jdt.annotation 2.0

This dependency is removed now.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2383984</commentid>
    <comment_count>9</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2014-04-03 05:18:37 -0400</bug_when>
    <thetext>1. The fix does not handle the type annotations on array dimensions with varargs.
Example - a class implementing the following interface gets incorrect annotations on the method parameter:

interface A {
	int foo2C(@NonNull Object @NonNull [] @Nullable... o2);
}

Results in:

class C implements A {

	@Override
	public int foo2C(@NonNull Object[] @NonNull... o2) {
		// TODO Auto-generated method stub
		return 0;
	}
}
-----------------------------------------------------------------------------

2. When the type annotations are not compiler&apos;s null annotations, the type annotations are still copied to the methods in the implementing class except the ones on a varargs parameter, which looks wrong. Either all non-compiler type annotations (including the ones on varargs) should be copied or none.

Example:

@Target({ TYPE_USE }) @interface N1 { }
@Target({ TYPE_USE }) @interface N2 { }

interface A {
	int foo2(@N1 String @N2 [] s1, @N1 String @N2... s2);
}

Results in:

class C implements A {

	@Override
	public int foo2(@N1 String @N2 [] s1, String... s2) {
		// TODO Auto-generated method stub
		return 0;
	}

}</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2384494</commentid>
    <comment_count>10</comment_count>
      <attachid>241597</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2014-04-03 23:50:35 -0400</bug_when>
    <thetext>Created attachment 241597
Patch+Tests

(In reply to Noopur Gupta from comment #9)
Thanks Noopur.
&gt; 1. The fix does not handle the type annotations on array dimensions with
&gt; varargs.
Filed bug 431963 for this as the model does not return all the annotation in this case. Added a testcase which will be red till bug 431963 is fixed.

&gt; 2. When the type annotations are not compiler&apos;s null annotations, 
I had uploaded the wrong patch which didn&apos;t consider comment 3. While copying type use annotation we need not check StubUtility2#isCopyOnInheritAnnotation. Added a testcase for this scenario.

We will wait for bug 431963 to see if anything else has to be handled in UI for this issue.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2384500</commentid>
    <comment_count>11</comment_count>
    <who name="Jay Arthanareeswaran">jarthana@in.ibm.com</who>
    <bug_when>2014-04-04 00:02:18 -0400</bug_when>
    <thetext>BETA_J8 is no longer a valid target. Can we adjust/reset the target please?</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2385191</commentid>
    <comment_count>12</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2014-04-06 17:16:17 -0400</bug_when>
    <thetext>The bug in StubUtility2#createParameters(..) is that it calls getElementType() and then manually adds array dimensions again, thereby losing all type annotations on intermediate dimensions.

Since type annotations on varargs are so special, we also can&apos;t simply use imports.addImport(type, ast, context) as in the normal case, because we have to copy all but the last dimension.

Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=a42a1e1d629f0534edd86fd2b249cbfbce432b77 and released Manju&apos;s tests with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=95f8397468004b3e0efb0321ba636831af5c03a4

I&apos;ve extracted the fetching of the org.eclipse.jdt.annotations path into
Java18ProjectTestSetup.getJdtAnnotations20Path(), since that may also be interesting in other tests. Fixed the implementation so that it also works when running with a 1.6 or 1.7 JRE.
I&apos;ve also added a few more annotated dimensions to testUnimplementedMethods5 and fixed a typo in testUnimplementedMethods3.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2385480</commentid>
    <comment_count>13</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2014-04-07 08:41:16 -0400</bug_when>
    <thetext>Forgot to actually import/set the type in the &quot;if (!is50OrHigher)&quot; branch. This triggered bug 432132. Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=ea49c237d51a679a569c4069eac0a514f2bc8b1f</thetext>
  </long_desc>
      
          <attachment
              isobsolete="1"
              ispatch="1"
              isprivate="0"
          >
            <attachid>236787</attachid>
            <date>2013-10-22 16:43:00 -0400</date>
            <delta_ts>2014-01-21 20:44:57 -0500</delta_ts>
            <desc>Implementation sketch</desc>
            <filename>eclipse.jdt.ui.patch</filename>
            <type>text/plain</type>
            <size>4628</size>
            <attacher name="Stephan Herrmann">stephan.herrmann@berlin.de</attacher>
            
              <token>1425706887-s5TKpH1Smuf0gL8jn-y7762fzl67m7PMhxwEznOOiPQ</token>

          </attachment>
          <attachment
              isobsolete="1"
              ispatch="1"
              isprivate="0"
          >
            <attachid>239210</attachid>
            <date>2014-01-21 20:44:00 -0500</date>
            <delta_ts>2014-04-02 21:52:29 -0400</delta_ts>
            <desc>Updated Patch + Testcases</desc>
            <filename>Fix-for-bug-420116--18-Add-implemented-methods-shoul.patch</filename>
            <type>text/plain</type>
            <size>10143</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706887-5cfTmwwWUlhdeIvc4tTE2dEA1sqmX5KEIksRDGyJwhY</token>

          </attachment>
          <attachment
              isobsolete="1"
              ispatch="1"
              isprivate="0"
          >
            <attachid>241534</attachid>
            <date>2014-04-02 21:52:00 -0400</date>
            <delta_ts>2014-04-03 23:50:35 -0400</delta_ts>
            <desc>Patch+Tests</desc>
            <filename>Fixed-Bug-420116-18-Add-implemented-methods-should-v3.patch</filename>
            <type>text/plain</type>
            <size>9701</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706887-iEdgBiQ-tsxDLhj6PDSRVMyzfUeIZOWc7fhP_mSFH4A</token>

          </attachment>
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>241597</attachid>
            <date>2014-04-03 23:50:00 -0400</date>
            <delta_ts>2014-04-03 23:50:35 -0400</delta_ts>
            <desc>Patch+Tests</desc>
            <filename>Fixed-Bug-420116-18-Add-implemented-methods-should-v4.patch</filename>
            <type>text/plain</type>
            <size>12852</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706887-wVy0ngeKoVE9Guc92iyW4U-2rjuEVeigJ5EFcg-CS9A</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>418692</bug_id>
          
          <creation_ts>2013-10-04 11:22:00 -0400</creation_ts>
          <short_desc>[extract method] Does not replace duplicates that span the whole method body</short_desc>
          <delta_ts>2013-10-11 07:33:14 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>PC</rep_platform>
          <op_sys>Windows 7</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>normal</bug_severity>
          <target_milestone>4.4 M3</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Frank Neblung">f.neblung@gis-systemhaus.de</reporter>
          <assigned_to name="Manju Mathew">manju656@gmail.com</assigned_to>
          <cc>channingwalton@mac.com</cc>
    
    <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>manju656@gmail.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
    
    <cc>samrat.dhillon@gmail.com</cc>
          
          <votes>0</votes>

      
          <token>1425706887-1eh8lCAc1drOz7Som7ELXIhRHFU9H5mxMWzi2L2mejM</token>

      

      <flag name="review"
          id="59572"
          type_id="1"
          status="-"
          setter="manju656@gmail.com"
    />

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2314422</commentid>
    <comment_count>0</comment_count>
      <attachid>236121</attachid>
    <who name="Frank Neblung">f.neblung@gis-systemhaus.de</who>
    <bug_when>2013-10-04 11:22:27 -0400</bug_when>
    <thetext>Created attachment 236121
the semicolon makes the difference

The result of detecting so called &apos;additional occurences&apos; depends on whether or not the selection includes the semicolon.

See Screenshot.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2314621</commentid>
    <comment_count>1</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-10-05 01:47:02 -0400</bug_when>
    <thetext>Tested using Eclipse Version: 4.4.0 and Build: I20130916-0900. The issue is not reproducible. With the given sample code snippet, whether semicolon is included or not, i could see all the 3 occurrences of s.length() replaced after the refactoring. 

Closing the bug as it is not reproducible in the latest Eclipse build. Let us know the Eclipse build you have used for testing this scenario. We can open the bug if you are able to reproduce the bug in one of the latest Eclipse builds.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2314908</commentid>
    <comment_count>2</comment_count>
    <who name="Frank Neblung">f.neblung@gis-systemhaus.de</who>
    <bug_when>2013-10-07 03:30:31 -0400</bug_when>
    <thetext>I observe the behavior of the screenshot with rcp-kepler-win32 and rcp-kepler-sr1-win32 as well as with standard-luna-M2-win32 (Version: Luna Release Build id: 20131003-0825)

I did the following to reproduce it with luna:
 * download http://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/luna/M2/eclipse-standard-luna-M2-win32.zip
 * unpack the downloaded zip
 * doubleclick the unzipped eclipse/eclipse.exe
 * choose a new folder when prompted for workspace directory
 * paste the code snippet (see below) into package explorer
 * highlight the code &apos;s.length();&apos; within m1()  !include the semicolon!
 * open the refactoring dialog with shortcut &lt;Alt&gt;+&lt;Shift&gt;+M

&gt;&gt;&gt;BEGIN snippet
package pck;

public class Foo {
    String s;
    int i;

    void m1() {
        s.length();
    }

    void m2() {
        s.length();
    }

    void m3() {
        if (i &gt; 0) {
            s.length();
        }
    }
}
&lt;&lt;&lt;END snippet

The extract-method-dialog informs one that only 1 additional occurence will be replaced.

 * choose &apos;x&apos; as the method name
 * confirm the dialog

As a result of the refactoring the content is changed to:
&gt;&gt;&gt;BEGIN refactored code
package pck;

public class Foo {
    String s;
    int i;

    void m1() {
        x();
    }

	private void x() {
		s.length();
	}

    void m2() {
        s.length();
    }

    void m3() {
        if (i &gt; 0) {
            x();
        }
    }
}
&lt;&lt;&lt;END refactored code</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2314920</commentid>
    <comment_count>3</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-10-07 04:35:41 -0400</bug_when>
    <thetext>With the test data you have provided, the issue is now reproducible. In #m2() if there is an executable statement before s.length(); then it reports the right number of occurrences.
void m2() {
		System.out.println();
		s.length();
	}</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2315925</commentid>
    <comment_count>4</comment_count>
      <attachid>236247</attachid>
    <who name="Samrat Dhillon">samrat.dhillon@gmail.com</who>
    <bug_when>2013-10-08 21:24:03 -0400</bug_when>
    <thetext>Created attachment 236247
Proposed patch

Here is another variation of this bug using the snippet below:

class Test{
	public void foo1(){
		System.out.println(&quot;Hello world&quot;);
	}
	
	public void foo2(){
		//Select from here
		{
			System.out.println(&quot;Hello world&quot;);
		}
		//Select till here and execute extract method refactoring and name the new method x
	}
}

The resulting refactoring results in compilation failure

class Test{
	public void foo1()x();
	
	public void foo2(){
		//Select from here
		x();
		//Select till here and execute extract method refactoring
	}

	private void x() {
		{
			System.out.println(&quot;Hello world&quot;);
		}
	}
}

The proposed patch fixes both the scenarios, but it will break two tests in ExtractMethodTests test652() and test800(). It was not very clear as to what conditions were being tested/guarded by these tests. In my opinion its safe to remove these tests. 

If the patch looks fine and the failure of test652() and test800() is acceptable, then I can add tests for this change.

This contribution complies with http://www.eclipse.org/legal/CoO.php</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2317028</commentid>
    <comment_count>5</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-10-11 01:34:31 -0400</bug_when>
    <thetext>With your patch SnippetFinder#isMethodBody() will return true only for the scenario mentioned in comment #5. Below scenario will fail.
public void foo1(){
		System.out.println(&quot;Hello world&quot;);
                System.err.println();
	}
	
	public void foo2(){
		//Select from here
		{
			System.out.println(&quot;Hello world&quot;);
                        System.err.println();
		}
		//Select till here and execute extract method refactoring and name the new method x
	}
}

Also it will leave garbage code and also a wrong Javadoc. I took your change, modified the code, modified the test, added a new test case and updated Javadoc and released the fix as: http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=baf1e0ecfb36327ff5288cd2beec9ef03936d3b1</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2317029</commentid>
    <comment_count>6</comment_count>
      <attachid>236247</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-10-11 01:39:06 -0400</bug_when>
    <thetext>Comment on attachment 236247
Proposed patch

I meant comment #4 in my previous comment.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2317165</commentid>
    <comment_count>7</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-10-11 07:33:14 -0400</bug_when>
    <thetext>*** Bug 71575 has been marked as a duplicate of this bug. ***</thetext>
  </long_desc>
      
          <attachment
              isobsolete="0"
              ispatch="0"
              isprivate="0"
          >
            <attachid>236121</attachid>
            <date>2013-10-04 11:22:00 -0400</date>
            <delta_ts>2013-10-04 11:22:27 -0400</delta_ts>
            <desc>the semicolon makes the difference</desc>
            <filename>screenshots.png</filename>
            <type>image/png</type>
            <size>113658</size>
            <attacher name="Frank Neblung">f.neblung@gis-systemhaus.de</attacher>
            
              <token>1425706887-BQ83o-UJ1faLXLhEAT4oXKvHq6xhkZRDOH_sBHHo5ag</token>

          </attachment>
          <attachment
              isobsolete="1"
              ispatch="1"
              isprivate="0"
          >
            <attachid>236247</attachid>
            <date>2013-10-08 21:24:00 -0400</date>
            <delta_ts>2013-10-11 01:39:06 -0400</delta_ts>
            <desc>Proposed patch</desc>
            <filename>Bug 418692.patch</filename>
            <type>text/plain</type>
            <size>1482</size>
            <attacher name="Samrat Dhillon">samrat.dhillon@gmail.com</attacher>
            
              <token>1425706887-iJ7pVuoiLuhVHvTVvJfBxVwk-M81grEo8-PhUSz0_xM</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>416935</bug_id>
          
          <creation_ts>2013-09-10 10:43:00 -0400</creation_ts>
          <short_desc>[JUnit] Initialize JUnit container &amp; JUNIT_HOME doesn&apos;t work when there is no bundle.info</short_desc>
          <delta_ts>2013-12-09 14:25:21 -0500</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          <see_also>https://bugs.eclipse.org/bugs/show_bug.cgi?id=416982</see_also>
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>normal</bug_severity>
          <target_milestone>4.4 M4</target_milestone>
          
          <blocked>416915</blocked>
          <everconfirmed>1</everconfirmed>
          <reporter name="Mickael Istria">mistria@redhat.com</reporter>
          <assigned_to name="Mickael Istria">mistria@redhat.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706887-2DGlmkkhZCSYvQHf2Z3klcW_0Co8I3AFLjCYtAnvXRs</token>

      

      

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2304935</commentid>
    <comment_count>0</comment_count>
    <who name="Mickael Istria">mistria@redhat.com</who>
    <bug_when>2013-09-10 10:43:39 -0400</bug_when>
    <thetext>In the context of running JDT tests with Tycho, I noticed that the implementation of JUnitHomeInitializer relies on SimpleConfigurator and assumes that the product uses a bundles.info file to work.
However, it&apos;s not the case with Tycho Surefire tests, bundles are instead passed in the config.ini file, using the &quot;osgi.bundles&quot; property.

So it seems like current implementation is based on the wrong assumption that all RCP products use a bundles.info.
Instead, it should leverage the OSGi APIs, as we can more safely assume that any application using JDT is started in an OSGi container.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2305245</commentid>
    <comment_count>1</comment_count>
    <who name="Mickael Istria">mistria@redhat.com</who>
    <bug_when>2013-09-11 02:55:50 -0400</bug_when>
    <thetext>In a general way, I think JDT should not have a dependency on p2 or the way application is configured at all. It seems safer and more portable to rely on OSGi runtime and Platform.getBundles().</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2305266</commentid>
    <comment_count>2</comment_count>
    <who name="Mickael Istria">mistria@redhat.com</who>
    <bug_when>2013-09-11 03:50:15 -0400</bug_when>
    <thetext>Additionally to the limitation caused by using SimpleConfigurator, there is also a bug on Tycho side that seems to make it a bit difficult to get tycho-surefire-plugin able to run tests related to JDT/junit integration.
Both issues make it hard to set a good value to the JUNIT_HOME variable in test environments with Tycho.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2305336</commentid>
    <comment_count>3</comment_count>
    <who name="Mickael Istria">mistria@redhat.com</who>
    <bug_when>2013-09-11 06:41:47 -0400</bug_when>
    <thetext>Suggested Gerrit patch: https://git.eclipse.org/r/#/c/16312/</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2306471</commentid>
    <comment_count>4</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-09-13 08:02:33 -0400</bug_when>
    <thetext>Setting target tentatively to M3. Markus is on vacation and Java 8 work has highest priority when he comes back.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2337733</commentid>
    <comment_count>5</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-12-04 13:00:59 -0500</bug_when>
    <thetext>(In reply to Mickael Istria from comment #3)
&gt; Suggested Gerrit patch: https://git.eclipse.org/r/#/c/16312/

Unfortunately, Platform.getBundles(..) doesn&apos;t work for all our use cases, see bug 225594, which introduced the P2Utils class.

If you don&apos;t have the JUnit bundles in your workspace (including source), then the JUnit library container and the JUNIT_SRC_HOME classpath variable won&apos;t find the source bundles, since they are not available in the OSGi instance that is running the platform.

A solution could be to make the dependency on SimpleConfigurator optional, and then skip source bundle lookup via P2Utils if the SimpleConfigurator is not available.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2337744</commentid>
    <comment_count>6</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-12-04 13:25:58 -0500</bug_when>
    <thetext>There&apos;s also a problem with resolving the org.hamcrest.core entry in the JUnit 4 classpath container. Probably because org.hamcrest.core is Jar&apos;d, but org.junit is installed as a folder.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2337950</commentid>
    <comment_count>7</comment_count>
    <who name="Mickael Istria">mistria@redhat.com</who>
    <bug_when>2013-12-05 02:23:39 -0500</bug_when>
    <thetext>Ok, so would it make sense to write an implementation that search with Platform.getBundle() and in case it&apos;s not found, fail back to p2 to resolve it?
This would work better in both cases (p2-enabled application or not)</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2338015</commentid>
    <comment_count>8</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-12-05 06:01:02 -0500</bug_when>
    <thetext>&gt; Ok, so would it make sense to write an implementation that search with
&gt; Platform.getBundle() and in case it&apos;s not found, fail back to p2 to resolve
&gt; it?

Yes, but I&apos;d prefer the other direction: First try p2, and only fall back to Platform.getBundles(..) if the simpleconfigurator didn&apos;t work out. For the normal case (running in IDE), this saves one lookup that is guaranteed to fail. And it takes less time to review, since we normally keep the current code that is well-tested.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2339494</commentid>
    <comment_count>9</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-12-09 14:25:21 -0500</bug_when>
    <thetext>Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=47c871e94543c7ab24a3b061491c8494d161d6d6 (rebased Mickael&apos;s patch) and http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=baed3657b4b5e42e534be45cb1ca3474cdfd2178 :

- fixed source bundle resolution (was broken unless from workspace)
- fixed implementation of getSourceBundleLocation()
- code cleanup

Filed bug 423622 for broken Gerrit workflow. I&apos;ll abandon the Gerrit change set.</thetext>
  </long_desc>
      
      

    </bug>
    <bug>
          <bug_id>416914</bug_id>
          
          <creation_ts>2013-09-10 08:16:00 -0400</creation_ts>
          <short_desc>Get rid of nested jars for tests</short_desc>
          <delta_ts>2013-10-03 08:36:15 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>enhancement</bug_severity>
          <target_milestone>4.4 M3</target_milestone>
          
          <blocked>416915</blocked>
    
    <blocked>416740</blocked>
          <everconfirmed>1</everconfirmed>
          <reporter name="Mickael Istria">mistria@redhat.com</reporter>
          <assigned_to name="Mickael Istria">mistria@redhat.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>david_williams@us.ibm.com</cc>
    
    <cc>jarthana@in.ibm.com</cc>
    
    <cc>Michael_Rennie@ca.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706887-QXlJB7VPcbQ4TGih4c-xy3t6hYw-4dsibkfOdLizsgo</token>

      

      <flag name="review"
          id="59357"
          type_id="1"
          status="+"
          setter="daniel_megert@ch.ibm.com"
    />

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2304831</commentid>
    <comment_count>0</comment_count>
    <who name="Mickael Istria">mistria@redhat.com</who>
    <bug_when>2013-09-10 08:16:55 -0400</bug_when>
    <thetext>+++ This bug was initially created as a clone of Bug #416740 +++

In order to be able to use the tycho-surefire-plugin, it would be nice to get rid of the nested jars in test bundles which confuse surefire.

Why are there some nested jars? Here is the answer from Dani (Megert):
&quot;&quot;&quot;
Almost all our (Platform, JDT, PDE) test bundles have their class files inside a JAR that&apos;s inside the JARed bundle. This is simply for historical reasons: back in the old days, each bundle was in a directory with a JAR that contained the class files. When we started to JAR most of our bundles, we converted them to have the class files directly in the bundle JAR. We did not do this for the test bundles just because there was neither a reason nor a benefit. We can accept patches that fix this, but each patch must fix all test projects inside the same repository for consistency and of course you must verify that all tests are still green before submitting the patch. 
&quot;&quot;&quot;
Cf http://dev.eclipse.org/mhonarc/lists/platform-releng-dev/msg21603.html</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2304973</commentid>
    <comment_count>1</comment_count>
    <who name="Mickael Istria">mistria@redhat.com</who>
    <bug_when>2013-09-10 11:35:04 -0400</bug_when>
    <thetext>Submitted Gerrit patch: https://git.eclipse.org/r/16290</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2306466</commentid>
    <comment_count>2</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-09-13 07:57:51 -0400</bug_when>
    <thetext>Setting target to M3. We have M2 next week and we should not destabilize the current build.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2313805</commentid>
    <comment_count>3</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-10-03 08:36:15 -0400</bug_when>
    <thetext>Submitted with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=6ab6993eaa428b3a730cfb2e733cccd5532cf142

Sorry it took so long. There was M2 and then I was on vacation.</thetext>
  </long_desc>
      
      

    </bug>
    <bug>
          <bug_id>414084</bug_id>
          
          <creation_ts>2013-07-31 00:39:00 -0400</creation_ts>
          <short_desc>[1.8][quick fix] Add more quick fix proposals for implicit abstract method with body in interface</short_desc>
          <delta_ts>2014-04-17 08:55:16 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>enhancement</bug_severity>
          <target_milestone>4.4 M7</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Manju Mathew">manju656@gmail.com</reporter>
          <assigned_to name="Manju Mathew">manju656@gmail.com</assigned_to>
          <cc>manju656@gmail.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
    
    <cc>noopur_gupta@in.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706887-5MgxhzM6Pi8FMpkhr3Z-MervM28MQLgxYRhpGZ1DIWo</token>

      

      

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2290010</commentid>
    <comment_count>0</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-07-31 00:39:09 -0400</bug_when>
    <thetext>Consider the below code:
	interface test{
		public void m1(){
	}
For m1(), currently user is provided with a single Quick Fix proposal which will remove the body of the method. Ideally from Java 1.8, the method can be either default or static, hence we need to provide 2 new proposals here.
The Quick Fix proposals will be:
1. Remove method body
2. Add &apos;default&apos; modifier
3. Add &apos;static&apos; modifier</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2290686</commentid>
    <comment_count>1</comment_count>
      <attachid>234028</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-08-01 12:58:21 -0400</bug_when>
    <thetext>Created attachment 234028
Patch with testcases.

As discussed, for abstract methods in interface new quick fix proposals are added. Testcases are also attached.

Markus, please review.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2303525</commentid>
    <comment_count>2</comment_count>
      <attachid>235220</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-09-06 02:38:20 -0400</bug_when>
    <thetext>Created attachment 235220
Updated Patch with tests

Created fresh patch from the newly created remote branch after removing duplicates.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2386674</commentid>
    <comment_count>3</comment_count>
      <attachid>241760</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2014-04-09 02:34:00 -0400</bug_when>
    <thetext>Created attachment 241760
Patch+Tests

Updated patch against master.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2386807</commentid>
    <comment_count>4</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2014-04-09 07:01:26 -0400</bug_when>
    <thetext>- When we have explicit &apos;abstract&apos; modifier:
interface Test {
	public abstract void m1() {
	}
}
the proposals say: &quot;Add &apos;default&apos; modifier&quot;, &quot;Add &apos;static&apos; modifier&quot;.
They actually replace the &apos;abstract&apos; modifier rather than adding one.
Shouldn&apos;t these be &quot;Change modifier of {0} to &apos;static&apos; / &apos;default&apos;&quot; (like bug 414100)?

- All calls to ASTNodes.findModifierNode in ModifierCorrectionSubProcessor where we remove the returned modifier can be replaced with the new ModifierCorrectionSubProcessor.removeModifier method.

- ModifierChangeCorrectionProposal can be used instead of LinkedCorrectionProposal like other places in ModifierCorrectionSubProcessor.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2386846</commentid>
    <comment_count>5</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2014-04-09 07:50:36 -0400</bug_when>
    <thetext>(In reply to Noopur Gupta from comment #4)
&gt; - When we have explicit &apos;abstract&apos; modifier:
&gt; interface Test {
&gt; 	public abstract void m1() {
&gt; 	}
&gt; }
&gt; the proposals say: &quot;Add &apos;default&apos; modifier&quot;, &quot;Add &apos;static&apos; modifier&quot;.
&gt; They actually replace the &apos;abstract&apos; modifier rather than adding one.
&gt; Shouldn&apos;t these be &quot;Change modifier of {0} to &apos;static&apos; / &apos;default&apos;&quot; (like
&gt; bug 414100)?

We already have the following cases where the proposal text is not exactly same as what the proposal does:

interface I {
	 static int bar(); // [1] - Add &apos;abstract&apos; modifier
}
class C {
	static int i= foo(); // [2] - Change modifier of &apos;foo()&apos; to &apos;static&apos;
	int foo() {
		return 0;
	}
}

Markus, is this OK or should all these be updated?</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2387233</commentid>
    <comment_count>6</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2014-04-10 01:02:06 -0400</bug_when>
    <thetext>The problem that we are handling here is &quot;IProblem.BodyForAbstractMethod&quot;. The confusion happens when the method is explicitly qualified with Abstract modifier and user is shown &quot;Add &apos;static&apos; / &apos;default&apos; modifier&quot; quick fix. Since this message does not literally fit all situation, how about &quot;Convert to &apos;static&apos; / &apos;default&apos; method&quot;?</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2387794</commentid>
    <comment_count>7</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2014-04-10 17:01:34 -0400</bug_when>
    <thetext>Yes, please fix inexact messages and use e.g. ModifierCorrectionSubProcessor_changemodifiertostatic_description=
Change modifier of &apos;&apos;{0}&apos;&apos; to &apos;&apos;static&apos;&apos;

In case we do more than changing a modifier, use:
Change method &apos;&apos;{0}&apos;&apos; to &apos;&apos;static&apos;&apos;
... or:
Change to &apos;&apos;static&apos;&apos;

Please don&apos;t use &quot;Convert&quot;. We commonly use &quot;Change&quot; for small/localized changes and &quot;Convert&quot; for larger-scale conversions that apply more than 1 or 2 changes.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2389024</commentid>
    <comment_count>8</comment_count>
      <attachid>241993</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2014-04-15 01:27:50 -0400</bug_when>
    <thetext>Created attachment 241993
Patch+Tests

Updated the patch after modifying the quick fix message from &quot;Add modifier..&quot; to &quot;Change modifier...&quot;. When the quick fix is invoked on methods with implicit abstract modifier, the &quot;Change modifier ..&quot; message might not be the exact message, but it is better than showing &quot;Add modifier..&quot; when there is explicit abstract modifier associated to a method.
Noopur, let me know if this change is fine.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2389918</commentid>
    <comment_count>9</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2014-04-16 14:05:57 -0400</bug_when>
    <thetext>(In reply to Manju Mathew from comment #8)
&gt; Created attachment 241993 [details] [diff]
&gt; Patch+Tests

Is this the updated patch? 
It does not contain the changes requested in comment #4. Also, the early draft declaration is still present in the files.
You can release the patch once those changes and correct messages are updated.

&gt; Updated the patch after modifying the quick fix message from &quot;Add
&gt; modifier..&quot; to &quot;Change modifier...&quot;. When the quick fix is invoked on
&gt; methods with implicit abstract modifier, the &quot;Change modifier ..&quot; message
&gt; might not be the exact message, but it is better than showing &quot;Add
&gt; modifier..&quot; when there is explicit abstract modifier associated to a method.
&gt; Noopur, let me know if this change is fine.

Markus, please have a look at the above message and share your thoughts.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2390038</commentid>
    <comment_count>10</comment_count>
      <attachid>242076</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2014-04-16 18:58:13 -0400</bug_when>
    <thetext>Created attachment 242076
Updated patch

Accidentally uploaded the wrong patch earlier.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2390041</commentid>
    <comment_count>11</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2014-04-16 19:06:45 -0400</bug_when>
    <thetext>Released the patch to master with : http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=ca371620e0f1b5ed39c5d47afe00e11db3f3eaea

Markus, have a look at the quick fix messages.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2390193</commentid>
    <comment_count>12</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2014-04-17 08:55:16 -0400</bug_when>
    <thetext>interface I {
    default void bar();
    void foo() { }
}

Fixed first quick fix to avoid adding a redundant &apos;abstract&apos; modifier. Removed the word &quot;modifier&quot; from the messages to include the cases where modifiers are added/deleted, not changed (comment 7): http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=ed8bda6dc0617d173cd3b5b770fdc3e6432ed402</thetext>
  </long_desc>
      
          <attachment
              isobsolete="1"
              ispatch="1"
              isprivate="0"
          >
            <attachid>234028</attachid>
            <date>2013-08-01 12:58:00 -0400</date>
            <delta_ts>2013-09-06 02:38:20 -0400</delta_ts>
            <desc>Patch with testcases.</desc>
            <filename>eclipse.jdt.ui.patch</filename>
            <type>text/plain</type>
            <size>14305</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706887-IHc7hBxksO5usXcw_r4CHAl6J7iqhkkLRlHNbsqm9ic</token>

          </attachment>
          <attachment
              isobsolete="1"
              ispatch="1"
              isprivate="0"
          >
            <attachid>235220</attachid>
            <date>2013-09-06 02:38:00 -0400</date>
            <delta_ts>2014-04-09 02:34:00 -0400</delta_ts>
            <desc>Updated Patch with tests</desc>
            <filename>Fix-for-bug-414084-18quick-fix-Add-more-quick-fix-pr.patch</filename>
            <type>text/plain</type>
            <size>12125</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706887-6skNqTjQTFTLGg12v6IreCshE3cxX2Avghs85NtQCCo</token>

          </attachment>
          <attachment
              isobsolete="1"
              ispatch="1"
              isprivate="0"
          >
            <attachid>241760</attachid>
            <date>2014-04-09 02:34:00 -0400</date>
            <delta_ts>2014-04-15 01:27:50 -0400</delta_ts>
            <desc>Patch+Tests</desc>
            <filename>Fix-for-bug-414084-18quick-fix-Add-more-quick-fix-v3.patch</filename>
            <type>text/plain</type>
            <size>11437</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706887-uZjJWdp0u0mOErtj93wCzoWHIUY5KpOTJp1Le1Vi3S4</token>

          </attachment>
          <attachment
              isobsolete="1"
              ispatch="1"
              isprivate="0"
          >
            <attachid>241993</attachid>
            <date>2014-04-15 01:27:00 -0400</date>
            <delta_ts>2014-04-16 18:58:13 -0400</delta_ts>
            <desc>Patch+Tests</desc>
            <filename>Fix-for-bug-414084-18quick-fix-Add-more-quick-fix-pr.patch</filename>
            <type>text/plain</type>
            <size>12125</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706887-toV__g8XGXF2ICnsZPX1pwsYhCQFgIVf6Si2txOkjlU</token>

          </attachment>
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>242076</attachid>
            <date>2014-04-16 18:58:00 -0400</date>
            <delta_ts>2014-04-16 18:58:13 -0400</delta_ts>
            <desc>Updated patch</desc>
            <filename>Fix-for-bug-414084-18quick-fix-Add-more-quick-fix-v3.patch</filename>
            <type>text/plain</type>
            <size>14865</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706887-KckqsbyA7pDx0FrtIqKMia-aTjyka3bTM6GqsMuUDR4</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>413583</bug_id>
          
          <creation_ts>2013-07-23 18:39:00 -0400</creation_ts>
          <short_desc>Setup of null annotations in plug-in project does not work with headless PDE/Build</short_desc>
          <delta_ts>2014-06-05 07:17:16 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>PC</rep_platform>
          <op_sys>Linux</op_sys>
          <bug_status>VERIFIED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>major</bug_severity>
          <target_milestone>4.4 RC4</target_milestone>
          <dependson>436469</dependson>
          <blocked>434307</blocked>
          <everconfirmed>1</everconfirmed>
          <reporter name="Stephan Herrmann">stephan.herrmann@berlin.de</reporter>
          <assigned_to name="Markus Keller">markus_keller@ch.ibm.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>ed@willink.me.uk</cc>
    
    <cc>jarthana@in.ibm.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
    
    <cc>noopur_gupta@in.ibm.com</cc>
    
    <cc>shankhba@in.ibm.com</cc>
    
    <cc>srikanth_sankaran@in.ibm.com</cc>
    
    <cc>stephan.herrmann@berlin.de</cc>
    
    <cc>tom.schindl@bestsolution.at</cc>
          
          <votes>0</votes>

      
          <token>1425706887-HZb1uB5NZUkFXKsAZiGX2hKdYJbeu05i0KybeRGwhXY</token>

      

      <flag name="review"
          id="62854"
          type_id="1"
          status="+"
          setter="jarthana@in.ibm.com"
    />
    <flag name="review"
          id="62855"
          type_id="1"
          status="+"
          setter="noopur_gupta@in.ibm.com"
    />
    <flag name="review"
          id="62856"
          type_id="1"
          status="+"
          setter="daniel_megert@ch.ibm.com"
    />

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2287636</commentid>
    <comment_count>0</comment_count>
    <who name="Stephan Herrmann">stephan.herrmann@berlin.de</who>
    <bug_when>2013-07-23 18:39:16 -0400</bug_when>
    <thetext>Bug 366014 added support for automatically configuring projects for the use of
null annotations. For plug-in projects it inserts an additional.bundles stanza
into build.properties.

I never fully understood the effect, but today I ran my first headless PDE-build
on a bundle with null annotations, which failed due to bug 354724.
If I understand that bug correctly, it is actually a &quot;works-as-designed&quot;:

  &quot;The fact that PDE Build does not consider the additional.bundles property can lead 
   to a slightly different issue.  The property is not intended to add anything to the
   build classpath, but instead allow the workspace to build when there are indirect
   dependencies.  Another bundle should be adding the additional bundle as a real
   (manifest) dependency.&quot;

Thus I propose to change the mechanism from bug 366014 (and the documentation)
to use an optional import instead (I tried Require-Bundle, which worked, not sure
if Import-Package would work and be more appropriate, or not).

As an extra data point I may want to check if/how tycho interprets these settings ...</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2344457</commentid>
    <comment_count>1</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-12-20 18:43:31 -0500</bug_when>
    <thetext>Yes, bug 354724 looks like a real blocker.

And since additional.bundles doesn&apos;t support version ranges (bug 414444 comment 20), I agree we can&apos;t keep going with that solution.


Unfortunately, there&apos;s nothing in OSGi that represents build-time dependencies. The next best hack I know is to use ...

Require-Bundle: org.eclipse.jdt.annotation;bundle-version=&quot;[2.0.0,3.0.0)&quot;;resolution:=optional

... which is wrong (since the bundle is never required at run time), but it often works out (except that p2 may install it and the runtime may load it unnecessarily).</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2344466</commentid>
    <comment_count>2</comment_count>
    <who name="Stephan Herrmann">stephan.herrmann@berlin.de</who>
    <bug_when>2013-12-20 20:35:06 -0500</bug_when>
    <thetext>Yes, I think that&apos;s the best we can do.

Given the bundle is part of JDT everybody compiling in the IDE will find the bundle at compile time.

For headless builds it works if you provide the annotation bundle as part of the target platform.

And no application will be broken by not shipping the bundle. In this specific case unintentionally pulling in those few bytes (if they are available at install time) shouldn&apos;t really hurt anybody.

And: we can specify the version.

Unless s.o. strongly votes for Import-Package rather than Require-Bundle we seem to have a solution, right?</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2357438</commentid>
    <comment_count>3</comment_count>
    <who name="Thomas Schindl">tom.schindl@bestsolution.at</who>
    <bug_when>2014-01-31 19:50:21 -0500</bug_when>
    <thetext>just a minor remark - the current p2 repo does only install version 2.0.0 but both 1.0.0 and 2.0.0 have to be installed</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2357508</commentid>
    <comment_count>4</comment_count>
    <who name="Stephan Herrmann">stephan.herrmann@berlin.de</who>
    <bug_when>2014-02-01 09:56:29 -0500</bug_when>
    <thetext>(In reply to Thomas Schindl from comment #3)
&gt; just a minor remark - the current p2 repo does only install version 2.0.0
&gt; but both 1.0.0 and 2.0.0 have to be installed

Looking closer at the repo this is a problem of unintended metadata generated for the patch feature: it declares both versions as replacements, so 2.0.0 overrides 1.0.0. Instead the metadata should declare one version as a regular new dependency (&lt;required&gt;).

To avoid the need for changes in p2 metadata generation, I&apos;ll propose a workaround via bug 414444.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2365172</commentid>
    <comment_count>5</comment_count>
    <who name="Stephan Herrmann">stephan.herrmann@berlin.de</who>
    <bug_when>2014-02-18 17:15:04 -0500</bug_when>
    <thetext>Can we schedule this for BETA_J8? 
Should I (try to) prepare a patch?</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2411844</commentid>
    <comment_count>6</comment_count>
    <who name="Stephan Herrmann">stephan.herrmann@berlin.de</who>
    <bug_when>2014-06-03 04:57:41 -0400</bug_when>
    <thetext>While updating the documentation I just realized that the quickfix has not been updated.

This means that Luna will still propose to add the annotation bundle to additional.bundles in build.properties.

Given that this approach is strongly discouraged going forward, we should at least remove this quickfix (or better: change it to adding the recommended optional require bundle).

Can this please be considered for Luna?</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2411868</commentid>
    <comment_count>7</comment_count>
    <who name="Ed Willink">ed@willink.me.uk</who>
    <bug_when>2014-06-03 05:09:04 -0400</bug_when>
    <thetext>(In reply to Stephan Herrmann from comment #6)
&gt; Given that this approach is strongly discouraged going forward

Prohibited. Anyone requiring a BREE &lt; 8 must not use the additional classpath. There should a ManifestBuilder warning if it is in use.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2411879</commentid>
    <comment_count>8</comment_count>
    <who name="Stephan Herrmann">stephan.herrmann@berlin.de</who>
    <bug_when>2014-06-03 05:17:25 -0400</bug_when>
    <thetext>(In reply to Ed Willink from comment #7)
&gt; (In reply to Stephan Herrmann from comment #6)
&gt; &gt; Given that this approach is strongly discouraged going forward
&gt; 
&gt; Prohibited. Anyone requiring a BREE &lt; 8 must not use the additional
&gt; classpath. There should a ManifestBuilder warning if it is in use.

Ed, I&apos;m trying to put your critique to action. I&apos;m trying to prevent that JDT/UI proposes the situation that caused so much grief in your cases and for others.

I don&apos;t understand what you are trying to prohibit?

Are you expressing objection to my request in comment 6, or are you saying &quot;discouraged&quot; is still too weak?

Which approach are you referring to when saying &quot;additional classpath&quot;?</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2411892</commentid>
    <comment_count>9</comment_count>
    <who name="Ed Willink">ed@willink.me.uk</who>
    <bug_when>2014-06-03 05:37:37 -0400</bug_when>
    <thetext>Hi.

Yes &quot;discouraged&quot; is too weak.

Unfortunately the Kepler best practice proved unsuitable for Java 8, so as much assistance as possible needs to be given to those who followed it and have long since forgotten why.

If you don&apos;t het a warning into the manifest (and/or source message/quick fix) expect many users complaining that their Kepler @NonNull files don&apos;t compile on Luna.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2412165</commentid>
    <comment_count>10</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2014-06-03 11:56:30 -0400</bug_when>
    <thetext>I just filed bug 436469 as a request for proper compile-time dependencies in the manifest.

It&apos;s too late for a fix for 4.4. Given that we don&apos;t have any good solution at this time, the best we can do is to give some advice in the N&amp;N.

AFAIK, the best advice we have at this time is to use ...

- ... for projects with a JavaSE-1.7 or earlier execution environment:

Require-Bundle: org.eclipse.jdt.annotation;bundle-version=&quot;[1.1.0,2.0.0)&quot;;resolution:=optional

- ... for projects with a JavaSE-1.8 or later execution environment:

Require-Bundle: org.eclipse.jdt.annotation;bundle-version=&quot;[2.0.0,3.0.0)&quot;;resolution:=optional


Note that this is not a unique problem with null annotations. PDE in general is very weak in handling versioned bundles. E.g. the quick fix
&quot;Add &apos;org.eclipse.jdt.annotation&apos; to required bundles&quot; also doesn&apos;t ask about version constraints, so users have to understand their dependencies in other situations as well.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2412181</commentid>
    <comment_count>11</comment_count>
    <who name="Ed Willink">ed@willink.me.uk</who>
    <bug_when>2014-06-03 12:08:46 -0400</bug_when>
    <thetext>(In reply to Markus Keller from comment #10)
&gt; Require-Bundle:
&gt; org.eclipse.jdt.annotation;bundle-version=&quot;[1.1.0,2.0.0)&quot;;resolution:
&gt; =optional

NB it really must be optional. If any plugin is non-optional, e.g. using a tests plugin to force Hudson to load jdt.annotation, that plugin gets the you-must-use-Java-8 error treatment.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2412196</commentid>
    <comment_count>12</comment_count>
    <who name="Stephan Herrmann">stephan.herrmann@berlin.de</who>
    <bug_when>2014-06-03 12:24:05 -0400</bug_when>
    <thetext>(In reply to Markus Keller from comment #10)
&gt; I just filed bug 436469 as a request for proper compile-time dependencies in
&gt; the manifest.
&gt; 
&gt; It&apos;s too late for a fix for 4.4.

I know - if you are speaking of a *real fix*.

&gt; AFAIK, the best advice we have at this time is to use ...

Yes, these are the recommendations that we all agreed upon.

&gt; Given that we don&apos;t have any good solution
&gt; at this time, the best we can do is to give some advice in the N&amp;N.

I have some notes in help and N&amp;N, to be released shortly.

But shouldn&apos;t we just disable the quickfix that seems to create more grief than really fixing anything?

Wouldn&apos;t it look strange if N&amp;N needs to say: JDT/UI offers a quickfix for ... but PLEASE DON&apos;T USE IT!</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2412219</commentid>
    <comment_count>13</comment_count>
      <attachid>243899</attachid>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2014-06-03 13:26:28 -0400</bug_when>
    <thetext>Created attachment 243899
Remove quick fix &quot;Add library with default null annotations to build path&quot;

OK, we can just remove the bundle-specific quick fix.

I think we should only offer the &quot;copy ... to build path&quot; quick fix for non-bundle projects, since it would just cause pain later when people try to use PDE build or Tycho to build the bundle.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2412224</commentid>
    <comment_count>14</comment_count>
    <who name="Stephan Herrmann">stephan.herrmann@berlin.de</who>
    <bug_when>2014-06-03 13:51:22 -0400</bug_when>
    <thetext>(In reply to Markus Keller from comment #13)

Makes perfect sense to me, thanks!</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2412306</commentid>
    <comment_count>15</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2014-06-03 16:12:42 -0400</bug_when>
    <thetext>Markus, do you plan do fix this for RC4? If so, please add reviewers.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2412328</commentid>
    <comment_count>16</comment_count>
    <who name="Stephan Herrmann">stephan.herrmann@berlin.de</who>
    <bug_when>2014-06-03 17:06:28 -0400</bug_when>
    <thetext>FYI: I removed mentioning of the bogus quick fix from the help document[1], and replaced it with recommendations along the lines of comment 10. (I wouldn&apos;t be reliably available on short notice before RC4 goes final).

[1] http://git.eclipse.org/c/platform/eclipse.platform.common.git/commit/?id=a24df834b818100666397f4e801a61cf8878161d</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2412553</commentid>
    <comment_count>17</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2014-06-04 07:38:58 -0400</bug_when>
    <thetext>+1 for RC4.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2412671</commentid>
    <comment_count>18</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2014-06-04 09:42:33 -0400</bug_when>
    <thetext>Looks good. +1 for RC4.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2412702</commentid>
    <comment_count>19</comment_count>
    <who name="Jay Arthanareeswaran">jarthana@in.ibm.com</who>
    <bug_when>2014-06-04 10:07:00 -0400</bug_when>
    <thetext>Looks good to me.

Markus, I am not sure if Stephan can get to this today. I have verified that his document changes are in line with the reversal.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2412703</commentid>
    <comment_count>20</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2014-06-04 10:08:39 -0400</bug_when>
    <thetext>Thanks, fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=d255e0bd45d3058af3070c6787a98ffb36e7aa28

I take Stephan&apos;s comment 14 as another committer+1, so we should be well-covered here.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2413428</commentid>
    <comment_count>21</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2014-06-05 07:17:16 -0400</bug_when>
    <thetext>Verified in I20140604-2000.</thetext>
  </long_desc>
      
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>243899</attachid>
            <date>2014-06-03 13:26:00 -0400</date>
            <delta_ts>2014-06-03 13:26:28 -0400</delta_ts>
            <desc>Remove quick fix &quot;Add library with default null annotations to build path&quot;</desc>
            <filename>eclipse.jdt.ui.patch</filename>
            <type>text/plain</type>
            <size>8638</size>
            <attacher name="Markus Keller">markus_keller@ch.ibm.com</attacher>
            
              <token>1425706887-piXQS0Pmp-MC6DxeT3hg2I7sCATZ5KghwDFkZIM0TdY</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>412139</bug_id>
          
          <creation_ts>2013-07-02 15:23:00 -0400</creation_ts>
          <short_desc>[hovering] Links in Javadoc hover/view headers don&apos;t resolve fully-qualified types correctly</short_desc>
          <delta_ts>2014-04-04 15:56:57 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>normal</bug_severity>
          <target_milestone>4.4 M7</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Markus Keller">markus_keller@ch.ibm.com</reporter>
          <assigned_to name="Markus Keller">markus_keller@ch.ibm.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>manju656@gmail.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706887-iva5zrmYTqAjuPXbF5ESFSUbdDEntElILdp7rMLtzGo</token>

      

      

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2279928</commentid>
    <comment_count>0</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-07-02 15:23:07 -0400</bug_when>
    <thetext>Links in Javadoc hover/view headers don&apos;t resolve fully-qualified types correctly.

Many examples can be found in org.eclipse.jdt.core.dom.ASTConverter, e.g. recordNodes(ASTNode node, org.eclipse.jdt.internal.compiler.ast.ASTNode oldASTNode).

The Javadoc tool generates title attributes like &quot;class or interface in org.eclipse.jdt.internal.compiler.ast&quot; for links to types. We could also generate titles, but we better just use &quot;in &lt;package&gt;&quot; syntax.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2292715</commentid>
    <comment_count>1</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-08-08 08:15:28 -0400</bug_when>
    <thetext>&gt; The Javadoc tool generates title attributes like &quot;class or interface in
&gt; org.eclipse.jdt.internal.compiler.ast&quot; for links to types. We could also
&gt; generate titles, but we better just use &quot;in &lt;package&gt;&quot; syntax.

Usually, the full qualification is not that interesting, so the Javadoc hover should keep showing just the simple name. But even if the links are fixed and lead to the right type, seeing the full name is still tedious (click the link, read the name, go back). Therefore, we should also add a &quot;title&quot; attribute to the &lt;a href=&quot;...&quot;&gt; element, so that the qualifier can be seen without following the link.

The Javadoc tool&apos;s &quot;class or interface in &lt;qualifier&gt;&quot; is a bit clumsy. A better title text is just &quot;in &lt;qualifier&gt;&quot;. The &quot;title&quot; attribute is only to be generated if a qualifier is actually available.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2294008</commentid>
    <comment_count>2</comment_count>
      <attachid>234338</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-08-13 00:41:10 -0400</bug_when>
    <thetext>Created attachment 234338
Proposed patch

With this patch, links in Javadoc view/hover resolve fully qualified types correctly. &apos;title&apos; attribute is generated if the method parameter is qualified, which the user can see while hovering over the parameter link in the Javadoc. Manually tested with different combination of method parameters both in source and binary. Also tested java.util.Map.Entry, my.pack.Map.Entry and my.pack.Outer.Entry.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2294167</commentid>
    <comment_count>3</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-08-13 08:20:30 -0400</bug_when>
    <thetext>The variable &quot;qualifiedTypeName&quot; has a wrong name. It doesn&apos;t contain a qualified type name.

The lastIndexOf(..) and the string concatenation &quot;Signature.C_DOT + typeName&quot; are unnecessary.

The &quot;createHeaderWithTitleLink&quot; method name sounds strange. It&apos;s not a &quot;header with title&quot; or a &quot;title link&quot;, but it&apos;s a HeaderLinkWithTitle. Or just overload createHeaderLink(..).

The title text message &quot;in {0}&quot; needs to be externalized.

The new link is missing &quot;class=&apos;header&apos;&quot;. Write the implementation in a way that &quot;class=&apos;header&apos;&quot; only appears once in the source code.

Example (in source):
	void foo(Thread.State s) {}
	void foo(Map.Entry&lt;String, Date&gt; e) {}

Why does &quot;State&quot; have an &quot;in Thread&quot; title, but &quot;Entry&quot; doesn&apos;t have an &quot;in Map&quot; title? I would expect the second title as well.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2295476</commentid>
    <comment_count>4</comment_count>
      <attachid>234472</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-08-16 02:46:38 -0400</bug_when>
    <thetext>Created attachment 234472
Updated Patch

(In reply to comment #3)
&gt; The variable &quot;qualifiedTypeName&quot; has a wrong name.
modified to signatureSimpleName.

&gt; The lastIndexOf(..) and the string concatenation &quot;Signature.C_DOT +
&gt; typeName&quot; are unnecessary.
I have modified the logic to find the package name. When the method is from a binary with parameter type signature: &lt;Ljava.util.Map$Entry;&gt;, then: typeName=&quot;Entry&quot;; signatureQualifier=&quot;java.util&quot;; signatureSimpleName=&quot;Map.Entry&quot;;  The title to be generated is &quot;java.util.Map&quot;. In this case i have to use indexof and string concatenation to derive the package name. Let me know how to make it better.

&gt; The &quot;createHeaderWithTitleLink&quot; method name 
overloaded createHeaderLink(..).
 
&gt; The title text message &quot;in {0}&quot; needs to be externalized.
Externalized &lt;title=&apos;in {0}&apos;&gt;

&gt; The new link is missing &quot;class=&apos;header&apos;&quot;. Write the implementation in a way
&gt; that &quot;class=&apos;header&apos;&quot; only appears once in the source code.
Done

&gt; Example (in source):
&gt; 	void foo(Thread.State s) {}
Done

Markus, please have a look.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2384937</commentid>
    <comment_count>5</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2014-04-04 15:56:57 -0400</bug_when>
    <thetext>(In reply to Manju Mathew from comment #4)
&gt; &gt; The lastIndexOf(..) and the string concatenation &quot;Signature.C_DOT +
&gt; &gt; typeName&quot; are unnecessary.

Such magic indexOf(..) calls are hard to read and can often be broken by devious input. Better go the safe way and only call substring with arguments where you can guarantee that they won&apos;t fail.

For the refTypeName, better just use the full typeSig (rather than splitting it up and concatenating it again).

&gt; &gt; The title text message &quot;in {0}&quot; needs to be externalized.
&gt; Externalized &lt;title=&apos;in {0}&apos;&gt;

No, avoid externalizing HTML (translators should not have to realize that &quot;title&quot; is not something to translate).

Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=19200f37a9b0059f19993e5bc4ae3a9b8d0390c7</thetext>
  </long_desc>
      
          <attachment
              isobsolete="1"
              ispatch="1"
              isprivate="0"
          >
            <attachid>234338</attachid>
            <date>2013-08-13 00:41:00 -0400</date>
            <delta_ts>2013-08-16 02:46:38 -0400</delta_ts>
            <desc>Proposed patch</desc>
            <filename>eclipse.jdt.ui.patch</filename>
            <type>text/plain</type>
            <size>2145</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706887-58NkFHeJlTmXq_sQzgsG5VGmCs6VeAcm8l1BZacGPjo</token>

          </attachment>
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>234472</attachid>
            <date>2013-08-16 02:46:00 -0400</date>
            <delta_ts>2013-08-16 02:46:38 -0400</delta_ts>
            <desc>Updated Patch</desc>
            <filename>eclipse.jdt.ui.v2.patch</filename>
            <type>text/plain</type>
            <size>4809</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706887-BCddjmprMBfgNpjPmks3wweLcSn9EOLLEwSGFHCgZwE</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>411841</bug_id>
          
          <creation_ts>2013-06-27 19:03:00 -0400</creation_ts>
          <short_desc>Rerunning a test from JUnit results view is launching the test on UI thread.</short_desc>
          <delta_ts>2013-07-02 13:55:03 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>normal</bug_severity>
          <target_milestone>4.4 M1</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Thirumala Reddy Mutchukota">thirumala@google.com</reporter>
          <assigned_to name="Markus Keller">markus_keller@ch.ibm.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
    
    <cc>noopur_gupta@in.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706887-Dral45dZzw7APlUsn8DaaTo2wAbl0nmL5WlGtpICoXs</token>

      

      

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2278502</commentid>
    <comment_count>0</comment_count>
    <who name="Thirumala Reddy Mutchukota">thirumala@google.com</who>
    <bug_when>2013-06-27 19:03:40 -0400</bug_when>
    <thetext>When I rerun a test by selecting &quot;Run&quot; from the JUnit test results view context menu the test launch is happening on the UI thread. When build before launch is enabled the project build is invoked on UI thread on Eclipse is frozen during the test launch process.

I am working on a patch to avoid it by delegating the rerun config launching to DebugUITools.launch() and will attach it to the bug soon.

A sample stack trace captured during the freeze is ...

java.io.UnixFileSystem.createDirectory(Native Method)
                java.io.File.mkdir(File.java:1239)
                java.io.File.mkdirs(File.java:1266)
                org.eclipse.core.internal.filesystem.local.LocalFile.mkdir(LocalFile.java:286)
                org.eclipse.core.internal.localstore.FileSystemResourceManager.write(FileSystemResourceManager.java:1132)
                org.eclipse.core.internal.resources.Folder.internalCreate(Folder.java:180)
                org.eclipse.core.internal.resources.Folder.create(Folder.java:107)
                org.eclipse.jdt.internal.core.builder.AbstractImageBuilder.createFolder(AbstractImageBuilder.java:470)
                org.eclipse.jdt.internal.core.builder.AbstractImageBuilder$1.visit(AbstractImageBuilder.java:254)
                org.eclipse.core.internal.resources.Resource$1.visitElement(Resource.java:85)
                org.eclipse.core.internal.watson.ElementTreeIterator.doIteration(ElementTreeIterator.java:82)
                org.eclipse.core.internal.watson.ElementTreeIterator.doIteration(ElementTreeIterator.java:86)
                org.eclipse.core.internal.watson.ElementTreeIterator.doIteration(ElementTreeIterator.java:86)
                org.eclipse.core.internal.watson.ElementTreeIterator.doIteration(ElementTreeIterator.java:86)
                org.eclipse.core.internal.watson.ElementTreeIterator.doIteration(ElementTreeIterator.java:86)
                org.eclipse.core.internal.watson.ElementTreeIterator.doIteration(ElementTreeIterator.java:86)
                org.eclipse.core.internal.watson.ElementTreeIterator.doIteration(ElementTreeIterator.java:86)
                org.eclipse.core.internal.watson.ElementTreeIterator.iterate(ElementTreeIterator.java:127)
                org.eclipse.core.internal.resources.Resource.accept(Resource.java:95)
                org.eclipse.core.internal.resources.Resource.accept(Resource.java:52)
                org.eclipse.jdt.internal.core.builder.AbstractImageBuilder.addAllSourceFiles(AbstractImageBuilder.java:219)
                org.eclipse.jdt.internal.core.builder.BatchImageBuilder.build(BatchImageBuilder.java:51)
                org.eclipse.jdt.internal.core.builder.JavaBuilder.buildAll(JavaBuilder.java:254)
                org.eclipse.jdt.internal.core.builder.JavaBuilder.build(JavaBuilder.java:184)
                org.eclipse.core.internal.events.BuildManager$2.run(BuildManager.java:728)
                org.eclipse.core.runtime.SafeRunner.run(SafeRunner.java:42)
                org.eclipse.core.internal.events.BuildManager.basicBuild(BuildManager.java:199)
                org.eclipse.core.internal.events.BuildManager.basicBuild(BuildManager.java:239)
                org.eclipse.core.internal.events.BuildManager$1.run(BuildManager.java:292)
                org.eclipse.core.runtime.SafeRunner.run(SafeRunner.java:42)
                org.eclipse.core.internal.events.BuildManager.basicBuild(BuildManager.java:295)
                org.eclipse.core.internal.events.BuildManager.basicBuild(BuildManager.java:256)
                org.eclipse.core.internal.events.BuildManager.build(BuildManager.java:394)
                org.eclipse.core.internal.resources.Project$1.run(Project.java:618)
                org.eclipse.core.internal.resources.Workspace.run(Workspace.java:2344)
                org.eclipse.core.internal.resources.Project.internalBuild(Project.java:597)
                org.eclipse.core.internal.resources.Project.build(Project.java:114)
                org.eclipse.debug.core.model.LaunchConfigurationDelegate$1.run(LaunchConfigurationDelegate.java:423)
                org.eclipse.core.internal.resources.Workspace.run(Workspace.java:2344)
                org.eclipse.core.internal.resources.Workspace.run(Workspace.java:2326)
                org.eclipse.debug.core.model.LaunchConfigurationDelegate.buildProjects(LaunchConfigurationDelegate.java:430)
                org.eclipse.debug.core.model.LaunchConfigurationDelegate.buildForLaunch(LaunchConfigurationDelegate.java:126)
                org.eclipse.debug.internal.core.LaunchConfiguration.launch(LaunchConfiguration.java:823)
                org.eclipse.debug.internal.core.LaunchConfiguration.launch(LaunchConfiguration.java:704)
                org.eclipse.jdt.internal.junit.model.TestRunSession.rerunTest(TestRunSession.java:485)
                org.eclipse.jdt.internal.junit.ui.TestRunnerViewPart.rerunTest(TestRunnerViewPart.java:2062)
                org.eclipse.jdt.internal.junit.ui.RerunAction.run(RerunAction.java:52)
                org.eclipse.jface.action.Action.runWithEvent(Action.java:498)
                org.eclipse.jface.action.ActionContributionItem.handleWidgetSelection(ActionContributionItem.java:584)
                org.eclipse.jface.action.ActionContributionItem.access$2(ActionContributionItem.java:501)
                org.eclipse.jface.action.ActionContributionItem$5.handleEvent(ActionContributionItem.java:411)
                org.eclipse.swt.widgets.EventTable.sendEvent(EventTable.java:84)
                org.eclipse.swt.widgets.Widget.sendEvent(Widget.java:1276)
                org.eclipse.swt.widgets.Display.runDeferredEvents(Display.java:3554)
                org.eclipse.swt.widgets.Display.readAndDispatch(Display.java:3179)</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2278535</commentid>
    <comment_count>1</comment_count>
      <attachid>232871</attachid>
    <who name="Thirumala Reddy Mutchukota">thirumala@google.com</who>
    <bug_when>2013-06-28 00:03:00 -0400</bug_when>
    <thetext>Created attachment 232871
Move the rerun test launch out of UI thread</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2279295</commentid>
    <comment_count>2</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-07-01 06:03:37 -0400</bug_when>
    <thetext>Markus, please have a look.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2279703</commentid>
    <comment_count>3</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-07-02 07:14:57 -0400</bug_when>
    <thetext>Thanks, looks good. Could you please add an explicit CoO sign-off comment here?
http://wiki.eclipse.org/Development_Resources/Contributing_via_Git#Contributing_via_Bugzilla</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2279895</commentid>
    <comment_count>4</comment_count>
    <who name="Thirumala Reddy Mutchukota">thirumala@google.com</who>
    <bug_when>2013-07-02 13:44:55 -0400</bug_when>
    <thetext>This contribution complies with the Certificate of Origin http://www.eclipse.org/legal/CoO.php</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2279899</commentid>
    <comment_count>5</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-07-02 13:52:49 -0400</bug_when>
    <thetext>Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=a81cebacbf0361dd2d01e385028159c4776d8b43

Removed unused NLS string and updated bundle versions with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=409462bc339e971281fd3d01a36a02a1295c348b</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2279900</commentid>
    <comment_count>6</comment_count>
    <who name="Thirumala Reddy Mutchukota">thirumala@google.com</who>
    <bug_when>2013-07-02 13:55:03 -0400</bug_when>
    <thetext>(In reply to comment #5)
&gt; Fixed with
&gt; http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/
&gt; ?id=a81cebacbf0361dd2d01e385028159c4776d8b43
&gt; 
&gt; Removed unused NLS string and updated bundle versions with
&gt; http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/
&gt; ?id=409462bc339e971281fd3d01a36a02a1295c348b

Thanks Markus.</thetext>
  </long_desc>
      
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>232871</attachid>
            <date>2013-06-28 00:03:00 -0400</date>
            <delta_ts>2013-06-28 00:03:00 -0400</delta_ts>
            <desc>Move the rerun test launch out of UI thread</desc>
            <filename>EclipseBug411841.patch</filename>
            <type>text/plain</type>
            <size>8650</size>
            <attacher name="Thirumala Reddy Mutchukota">thirumala@google.com</attacher>
            
              <token>1425706887-wWKQwFymhoBkiiSy4d3ZGskkcKRbhzaq8zoHtM8hUJU</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>411794</bug_id>
          
          <creation_ts>2013-06-27 12:12:00 -0400</creation_ts>
          <short_desc>[JUnit] Add a monospace font option for the Junit view</short_desc>
          <delta_ts>2013-08-08 09:26:03 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>VERIFIED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>enhancement</bug_severity>
          <target_milestone>4.4 M1</target_milestone>
          
          <blocked>414666</blocked>
          <everconfirmed>1</everconfirmed>
          <reporter name="Andrew Eisenberg">andrew.eisenberg@gmail.com</reporter>
          <assigned_to name="Andrew Eisenberg">andrew.eisenberg@gmail.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>kpiwko@redhat.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
    
    <cc>maxime.hamm@laposte.net</cc>
    
    <cc>noopur_gupta@in.ibm.com</cc>
    
    <cc>Olivier_Thomann@ca.ibm.com</cc>
          
          <votes>1</votes>

      
          <token>1425706887-LqShLodi7G3CwAAy50WgjNDvyffmFVdxOR8Xiv1JwLI</token>

      

      <flag name="review"
          id="58897"
          type_id="1"
          status="+"
          setter="noopur_gupta@in.ibm.com"
    />

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2278285</commentid>
    <comment_count>0</comment_count>
    <who name="Andrew Eisenberg">andrew.eisenberg@gmail.com</who>
    <bug_when>2013-06-27 12:12:00 -0400</bug_when>
    <thetext>Some unit testing frameworks rely on monospace ascii layout in their results. One example of this is the spock framework https://code.google.com/p/spock/ 

The JUnit results view should be configurable so that it can display a monospace font.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2278286</commentid>
    <comment_count>1</comment_count>
    <who name="Andrew Eisenberg">andrew.eisenberg@gmail.com</who>
    <bug_when>2013-06-27 12:12:35 -0400</bug_when>
    <thetext>I am willing to contribute a patch for this if this is a feature that you would consider including in Luna, or even Kepler SR1.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2278579</commentid>
    <comment_count>2</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-06-28 04:08:55 -0400</bug_when>
    <thetext>You would only need the font in the failure trace section, right?</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2278580</commentid>
    <comment_count>3</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-06-28 04:10:14 -0400</bug_when>
    <thetext>(In reply to comment #2)
&gt; You would only need the font in the failure trace section, right?

That would be bug 57570 then.

Markus, I&apos;d say we accept a patch, but of course not for SRx.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2278838</commentid>
    <comment_count>4</comment_count>
      <attachid>232895</attachid>
    <who name="Andrew Eisenberg">andrew.eisenberg@gmail.com</who>
    <bug_when>2013-06-28 13:32:49 -0400</bug_when>
    <thetext>Created attachment 232895
Implementation of this feature

This patch implements the feature described in this bug report.  No unit tests are included since this feature is not really easily amenable to testing.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2287316</commentid>
    <comment_count>5</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-07-23 09:18:57 -0400</bug_when>
    <thetext>*** Bug 57570 has been marked as a duplicate of this bug. ***</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2287333</commentid>
    <comment_count>6</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-07-23 09:49:29 -0400</bug_when>
    <thetext>The default font should not be changed, so I think the &apos;defaultsTo=...&apos; should be removed from the patch.

Andrew, could you please sign the CLA and write this line in a comment here?

&gt; This contribution complies with http://www.eclipse.org/legal/CoO.php

Noopur, please review the patch. If it looks good, follow the process at http://wiki.eclipse.org/Development_Resources/Handling_Git_Contributions#Bugzilla and commit to master.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2287417</commentid>
    <comment_count>7</comment_count>
    <who name="Andrew Eisenberg">andrew.eisenberg@gmail.com</who>
    <bug_when>2013-07-23 12:00:54 -0400</bug_when>
    <thetext>By making and signing (by using the git signed-off-by mechanism or any other signing mechanism which may be specified by the Eclipse Foundation from time to time) a contribution to an Eclipse project, I certify that:

    I have authored 100% of the contribution.
    I have the necessary rights to submit this contribution, including any necessary permissions from my employer.
    I am providing this contribution under the license(s) associated with the Eclipse Foundation project I am contributing to.
    I understand and agree that Eclipse projects and my contributions are public, and that a record of the contribution (including all personal information I submit with it, including my sign-off) is maintained indefinitely and may be redistributed consistent with the license(s) involved.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2287418</commentid>
    <comment_count>8</comment_count>
    <who name="Andrew Eisenberg">andrew.eisenberg@gmail.com</who>
    <bug_when>2013-07-23 12:01:42 -0400</bug_when>
    <thetext>CLA signed. Please let me know if there is anything else you need.  Thanks.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2287427</commentid>
    <comment_count>9</comment_count>
    <who name="Andrew Eisenberg">andrew.eisenberg@gmail.com</who>
    <bug_when>2013-07-23 12:16:35 -0400</bug_when>
    <thetext>(In reply to comment #8)
&gt; CLA signed. Please let me know if there is anything else you need.  Thanks.

Hmmm...not sure why there is still a &apos;-&apos; in the CLA box next to my name.  It looks like it is all signed for me.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2287452</commentid>
    <comment_count>10</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-07-23 12:45:14 -0400</bug_when>
    <thetext>&gt; Hmmm...not sure why there is still a &apos;-&apos; in the CLA box next to my name.  It
&gt; looks like it is all signed for me.

Probably a browser cache problem. I&apos;ll follow up in bug 401549.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2287462</commentid>
    <comment_count>11</comment_count>
    <who name="Andrew Eisenberg">andrew.eisenberg@gmail.com</who>
    <bug_when>2013-07-23 13:10:21 -0400</bug_when>
    <thetext>I see the check now.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2287724</commentid>
    <comment_count>12</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-07-24 05:10:13 -0400</bug_when>
    <thetext>The patch looks good.

Removed &apos;defaultsTo=...&apos;, added Andrew&apos;s name to the contributors&apos; list and updated the copyright date in the files.

Tested and released with:

http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=d0add1708b812c80384d88ef4eb52493b862187d</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2287944</commentid>
    <comment_count>13</comment_count>
    <who name="Andrew Eisenberg">andrew.eisenberg@gmail.com</who>
    <bug_when>2013-07-24 11:47:18 -0400</bug_when>
    <thetext>This feature will make lots of people happy.  Thanks for getting it in.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2287986</commentid>
    <comment_count>14</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-07-24 12:56:13 -0400</bug_when>
    <thetext>I was first reluctant to add yet another preference, but I didn&apos;t find a better solution, see bug 72847 comment 17.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2292742</commentid>
    <comment_count>15</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-08-08 09:26:03 -0400</bug_when>
    <thetext>Filed bug 414666 regarding the label of the font.</thetext>
  </long_desc>
      
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>232895</attachid>
            <date>2013-06-28 13:32:00 -0400</date>
            <delta_ts>2013-06-28 13:32:49 -0400</delta_ts>
            <desc>Implementation of this feature</desc>
            <filename>bug411794.patch</filename>
            <type>text/plain</type>
            <size>5215</size>
            <attacher name="Andrew Eisenberg">andrew.eisenberg@gmail.com</attacher>
            
              <token>1425706887-iD0ggTHFP1xri2VNDHP05SkKwfcDy8TygC0SEdOOLmg</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>411636</bug_id>
          
          <creation_ts>2013-06-25 14:51:00 -0400</creation_ts>
          <short_desc>Save is very slow (burns cycles in the Package and Project Explorer)</short_desc>
          <delta_ts>2013-08-22 05:01:30 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>VERIFIED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords>performance</keywords>
          <priority>P2</priority>
          <bug_severity>major</bug_severity>
          <target_milestone>4.3.1</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Matt Wallace">msw@mattwallace.org</reporter>
          <assigned_to name="Noopur Gupta">noopur_gupta@in.ibm.com</assigned_to>
          <cc>borodachyov.stanislav@gmail.com</cc>
    
    <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
    
    <cc>robert.munteanu@gmail.com</cc>
          
          <votes>0</votes>

      
          <token>1425706887-49SdghbHmYMMqd66f7KOlBSY9mIDV3qG9KQ7yeOJs5o</token>

      

      <flag name="review"
          id="58737"
          type_id="1"
          status="+"
          setter="daniel_megert@ch.ibm.com"
    />
    <flag name="review"
          id="58756"
          type_id="1"
          status="+"
          setter="markus_keller@ch.ibm.com"
    />

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2277053</commentid>
    <comment_count>0</comment_count>
      <attachid>232751</attachid>
    <who name="Matt Wallace">msw@mattwallace.org</who>
    <bug_when>2013-06-25 14:51:15 -0400</bug_when>
    <thetext>Created attachment 232751
Stack trace

I noticed that when I saved a Java file, the UI would be come unresponsive for about 5 seconds.  I did a stack trace (attached) and noticed that the main thread seemed to be hung up somewhere in the project explorer.  When I unchecked &quot;Link With Editor&quot; this delay went away.

I tried doing the same action on the exact same workspace in Indigo and did not notice the same delay.  My workspace is very large (100+ projects, maybe 50-100K files).

I&apos;m using:
Version: 4.3.0
Build id: I20130605-2000</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2277056</commentid>
    <comment_count>1</comment_count>
    <who name="Matt Wallace">msw@mattwallace.org</who>
    <bug_when>2013-06-25 14:54:37 -0400</bug_when>
    <thetext>After further testing it actually seems this is trigger not by having &quot;Link With Editor&quot; checked but rather by having my package explorer view expanded to show the file I&apos;m working on.  That is, this behavior happens when Link With Editor is on, but it also happens if Link With Editor is off, but the project tree is still expanded.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2277275</commentid>
    <comment_count>2</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-06-26 06:20:58 -0400</bug_when>
    <thetext>This is caused by the fix for bug 357450: we now refresh the whole project when a CU is saved.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2277334</commentid>
    <comment_count>3</comment_count>
      <attachid>232791</attachid>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-06-26 09:07:53 -0400</bug_when>
    <thetext>Created attachment 232791
Patch

As per bug 357450 comment 12, the parent refresh is required when parent is LibraryContainer.

So the condition given was:
if (result == IJavaElementDelta.F_CONTENT || result == IJavaElementDelta.F_CHILDREN) {...}

Due to this, whenever there is a children change, the parent is refreshed.
Hence, on CU save also, the project is refreshed here which is wrong.

Here the parent should be refreshed if there is a children change and the parent is LibraryContainer.

So, modifying the condition as below should be fine:
if (result == IJavaElementDelta.F_CONTENT || (result == IJavaElementDelta.F_CHILDREN &amp;&amp; parent instanceof LibraryContainer)) {...}

Attached a patch with the change.
Dani, please have a look.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2277645</commentid>
    <comment_count>4</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-06-27 02:16:29 -0400</bug_when>
    <thetext>*** Bug 411120 has been marked as a duplicate of this bug. ***</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2278692</commentid>
    <comment_count>5</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-06-28 09:09:12 -0400</bug_when>
    <thetext>The fix looks OK except for the duplicate instanceof check.

Markus, please also double-check.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2278694</commentid>
    <comment_count>6</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-06-28 09:12:03 -0400</bug_when>
    <thetext>Noopur, please also add an additional test.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2278758</commentid>
    <comment_count>7</comment_count>
      <attachid>232886</attachid>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-06-28 10:49:51 -0400</bug_when>
    <thetext>Created attachment 232886
Patch + Test

Created a boolean for duplicate instanceof check and added a new test case to check that project is not refreshed on change in a class within it.
Please review.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2296856</commentid>
    <comment_count>8</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-08-20 10:30:07 -0400</bug_when>
    <thetext>(In reply to comment #7)
This still refreshes the whole class folder even if just one file in it was changed. I think we could use more of the existing infrastructure (handleAffectedChildren at the end of processDelta) to update the resource in this case.

However, the patch is a good compromise for R4_3_maintenance that
- fixes the performance problems from comment 2 (bug 357450)
- only performs special refreshes if an element inside the library container got updated
- is not prone to further updating issues with the all the possible variants where a class folder could be placed in the file system

Released to R4_3_maintenance:
http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=d33e8a3bc1db30290261aeb8ff9a7d3bea4282a8

and master:
http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=d1f7ad24f801351fb3eb5219c4c9cd328fcb2649</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2297704</commentid>
    <comment_count>9</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-08-22 05:01:30 -0400</bug_when>
    <thetext>Verified in N20130821-2000 and M20130821-0800.</thetext>
  </long_desc>
      
          <attachment
              isobsolete="0"
              ispatch="0"
              isprivate="0"
          >
            <attachid>232751</attachid>
            <date>2013-06-25 14:51:00 -0400</date>
            <delta_ts>2013-06-25 14:51:15 -0400</delta_ts>
            <desc>Stack trace</desc>
            <filename>file_411636.txt</filename>
            <type>text/plain</type>
            <size>26819</size>
            <attacher name="Matt Wallace">msw@mattwallace.org</attacher>
            
              <token>1425706887-kPqr6G_F7boHHSJI2TuMUU7yqjdbeL8ER2-EYqyOG5M</token>

          </attachment>
          <attachment
              isobsolete="1"
              ispatch="1"
              isprivate="0"
          >
            <attachid>232791</attachid>
            <date>2013-06-26 09:07:00 -0400</date>
            <delta_ts>2013-06-28 10:49:51 -0400</delta_ts>
            <desc>Patch</desc>
            <filename>Bug-411636-Save-is-very-slow.patch</filename>
            <type>text/plain</type>
            <size>1092</size>
            <attacher name="Noopur Gupta">noopur_gupta@in.ibm.com</attacher>
            
              <token>1425706887-kFvkLWEsr718DSjOweRiC2g2PcMsWgM-scfeJcQsuXI</token>

          </attachment>
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>232886</attachid>
            <date>2013-06-28 10:49:00 -0400</date>
            <delta_ts>2013-06-28 10:49:51 -0400</delta_ts>
            <desc>Patch + Test</desc>
            <filename>Bug-411636-Save-is-very-slow.patch</filename>
            <type>text/plain</type>
            <size>3475</size>
            <attacher name="Noopur Gupta">noopur_gupta@in.ibm.com</attacher>
            
              <token>1425706887-xA7vXZZMIEYDLWN7iPcPwTupkOZYPmsU-_Orlut4kA8</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>411588</bug_id>
          
          <creation_ts>2013-06-25 07:28:00 -0400</creation_ts>
          <short_desc>&quot;Convert for loops to enhanced&quot; may mess up program logic when dealing with Iterable</short_desc>
          <delta_ts>2013-08-05 05:39:46 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>VERIFIED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>major</bug_severity>
          <target_milestone>4.4 M1</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Nicolas Something">pathogenyx@gmail.com</reporter>
          <assigned_to name="Noopur Gupta">noopur_gupta@in.ibm.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
    
    <cc>noopur_gupta@in.ibm.com</cc>
    
    <cc>srikanth_sankaran@in.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706887-hzqWCdWcq7zTXx37DhSY3Iif_Mm4iZPBLwUxt9wv4SA</token>

      

      <flag name="review"
          id="58766"
          type_id="1"
          status="+"
          setter="markus_keller@ch.ibm.com"
    />

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2276725</commentid>
    <comment_count>0</comment_count>
    <who name="Nicolas Something">pathogenyx@gmail.com</who>
    <bug_when>2013-06-25 07:28:22 -0400</bug_when>
    <thetext>With the save action &quot;Convert &apos;for&apos; loops to enhanced &apos;for&apos; loops&quot; enabled, 
the conversion to enhanced loop might introduce a logical error.

Lets suppose you have an object &quot;s&quot; with a class implementing java.lang.Iterable and this class has also another method named &quot;iterator&quot;, also with an &quot;Iterator&quot; return type, BUT with a __non empty signature__.

for (Iterator&lt;Object&gt; it = s.iterator(42) ; it.hasNext(); ) {
	Object obj = it.next();
	// ...
}

The save action will convert it to an enhanced loop assuming the use of &quot;s.iterator()&quot; instead of &quot;s.iterator(42)&quot; !

for (Object obj : s) { 
	// ...		 
}

(The bug exists also in 3.7.2 and probably in all releases until Kepler)</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2276726</commentid>
    <comment_count>1</comment_count>
      <attachid>232724</attachid>
    <who name="Nicolas Something">pathogenyx@gmail.com</who>
    <bug_when>2013-06-25 07:29:22 -0400</bug_when>
    <thetext>Created attachment 232724
Test case illustrating the bug</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2279247</commentid>
    <comment_count>2</comment_count>
    <who name="Srikanth Sankaran">srikanth_sankaran@in.ibm.com</who>
    <bug_when>2013-07-01 01:37:00 -0400</bug_when>
    <thetext>Forward to JDT/UI for comment.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2279262</commentid>
    <comment_count>3</comment_count>
      <attachid>232936</attachid>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-07-01 04:12:45 -0400</bug_when>
    <thetext>Created attachment 232936
Patch + Test

ConvertIterableLoopOperation.checkIteratorCondition() checks if the method name in initializer (method invocation) is &apos;iterator&apos;. 

If the method name is not &apos;iterator&apos;, a warning status is returned: &quot;Converting the loop may change the semantics of the code.&quot; for the quick assist and the action is not applied on save. 
So in the given example, if &apos;iterator(int filter)&apos; is renamed to &apos;foo(int filter)&apos;, we do not have any issue.

However, the given case is a bug.
We should also check if there are any arguments passed in the method invocation and return the warning status accordingly.
The save action should not be applicable here.

Attached a patch with the change and test case. 
Markus, please have a look.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2279818</commentid>
    <comment_count>4</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-07-02 10:59:06 -0400</bug_when>
    <thetext>Looks good, released as http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=a8d9f126228148d76f67078eaac3e3ee48e11b6e</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2291449</commentid>
    <comment_count>5</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-08-05 05:39:46 -0400</bug_when>
    <thetext>Verified using Build id: I20130804-2300 (Version 4.4.0).</thetext>
  </long_desc>
      
          <attachment
              isobsolete="0"
              ispatch="0"
              isprivate="0"
          >
            <attachid>232724</attachid>
            <date>2013-06-25 07:29:00 -0400</date>
            <delta_ts>2013-06-25 07:29:22 -0400</delta_ts>
            <desc>Test case illustrating the bug</desc>
            <filename>TestSaveActionConvertToEnhancedForLoop.java</filename>
            <type>text/x-java</type>
            <size>757</size>
            <attacher name="Nicolas Something">pathogenyx@gmail.com</attacher>
            
              <token>1425706887-LPlyBjQ9DTeBHtgkO-YgsCQn5nuizeiD-amWm-R2sp0</token>

          </attachment>
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>232936</attachid>
            <date>2013-07-01 04:12:00 -0400</date>
            <delta_ts>2013-07-01 04:12:45 -0400</delta_ts>
            <desc>Patch + Test</desc>
            <filename>Fixed-bug-411588-Convert-for-loops-to-enhanced.patch</filename>
            <type>text/plain</type>
            <size>6074</size>
            <attacher name="Noopur Gupta">noopur_gupta@in.ibm.com</attacher>
            
              <token>1425706887-1ZXejaPhe2g55rYOUh0BfEC3DKdM17v4E9eo6nRvf3I</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>411585</bug_id>
          
          <creation_ts>2013-06-25 07:02:00 -0400</creation_ts>
          <short_desc>[mark occurrence][search] Mark occurrences reports 0 based line numbers but the actual line numbers in the line number rulers starts with 1</short_desc>
          <delta_ts>2013-06-25 07:58:37 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>normal</bug_severity>
          <target_milestone>4.4 M1</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Johan Compagner">jcompagner@gmail.com</reporter>
          <assigned_to name="Dani Megert">daniel_megert@ch.ibm.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706887-tS0iaQtnoFdQXNzhicE3-hnJZm1Fpjwai2KKAWvTm0U</token>

      

      

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2276719</commentid>
    <comment_count>0</comment_count>
    <who name="Johan Compagner">jcompagner@gmail.com</who>
    <bug_when>2013-06-25 07:02:59 -0400</bug_when>
    <thetext>If i do ctrl-shift-u on a identifier i get a list of lines in the search view where those are found.
But the line numbers that are reported are 1 off. It does jump to the right line but it is funny to see that the search view reports &quot;203:&quot; and the actual code is according to the line of the ruler is on  204

It seems that the search view reports 0 based but the line number ruler starts with 1



Eclipse SDK

Version: 4.3.0
Build id: I20130605-2000</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2276734</commentid>
    <comment_count>1</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-06-25 07:58:37 -0400</bug_when>
    <thetext>Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=b5d624f1845fb6bff7f13342aa09670074aa22ed</thetext>
  </long_desc>
      
      

    </bug>
    <bug>
          <bug_id>410989</bug_id>
          
          <creation_ts>2013-06-18 04:13:00 -0400</creation_ts>
          <short_desc>[1.8][organize imports] Removes required import for TYPE_USE annotation</short_desc>
          <delta_ts>2014-02-24 21:05:18 -0500</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>VERIFIED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>enhancement</bug_severity>
          <target_milestone>BETA J8</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Noopur Gupta">noopur_gupta@in.ibm.com</reporter>
          <assigned_to name="Noopur Gupta">noopur_gupta@in.ibm.com</assigned_to>
          <cc>manju656@gmail.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
    
    <cc>noopur_gupta@in.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706887-6m4VC0fuzV9cZ7LM02wM5YWZDiFzBTE0ZJ1eOIgk1dA</token>

      

      <flag name="review"
          id="58677"
          type_id="1"
          status="+"
          setter="markus_keller@ch.ibm.com"
    />

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2273744</commentid>
    <comment_count>0</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-06-18 04:13:31 -0400</bug_when>
    <thetext>- Create a package com.p1 and add the following annotation type in it:

package com.p1;

import java.lang.annotation.Documented;
import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

@Target(ElementType.TYPE_USE)
@Retention(RetentionPolicy.RUNTIME)
@Documented
public @interface TypeUse {
}

- Create another package com.p2 and add the following class in it:

package com.p2;

import java.util.ArrayList;

import com.p1.TypeUse;

public class C1 {
	
	ArrayList&lt;@TypeUse String&gt; list;
}

- Perform: Source &gt; Organize Imports (Ctrl+Shift+O) on the class.

import com.p1.TypeUse; is removed and we get compilation error on @TypeUse in the class.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2275510</commentid>
    <comment_count>1</comment_count>
      <attachid>232641</attachid>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-06-21 09:18:14 -0400</bug_when>
    <thetext>Created attachment 232641
Patch + Tests

Updated ImportReferencesCollector&apos;s visit(...) methods for SimpleType and ArrayType to visit the annotations also by adding: doVisitChildren(node.annotations());

Added tests for all AnnotatableType nodes:
PrimitiveType, SimpleType, QualifiedType, PackageQualifiedType, WildcardType, ArrayType.

Markus, please review.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2365516</commentid>
    <comment_count>2</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2014-02-19 10:08:17 -0500</bug_when>
    <thetext>Pushed to BETA_JAVA8 with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=3537588fb11588198eccbfa28281053e65d5cce5 (took the commit from mmathew/BETA_JAVA8, which only added tests; the rest was already done in BETA_JAVA8)</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2367940</commentid>
    <comment_count>3</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2014-02-24 21:05:18 -0500</bug_when>
    <thetext>Verified using Kepler SR2 + Java 8 RC1 + Eclipse Java Development Tools Patch for Java 8 Support (BETA) 1.0.0.v20140223-2022</thetext>
  </long_desc>
      
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>232641</attachid>
            <date>2013-06-21 09:18:00 -0400</date>
            <delta_ts>2013-06-21 09:18:14 -0400</delta_ts>
            <desc>Patch + Tests</desc>
            <filename>Bug-410989-18-organize-imports.patch</filename>
            <type>text/plain</type>
            <size>25144</size>
            <attacher name="Noopur Gupta">noopur_gupta@in.ibm.com</attacher>
            
              <token>1425706887-DoYGrsVwi9msZmkxP97x97b3Z1kT5tAv6oDYNGow1MA</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>410570</bug_id>
          
          <creation_ts>2013-06-12 05:12:00 -0400</creation_ts>
          <short_desc>ignore eclipse.platform.releng.aggregator from chkpii</short_desc>
          <delta_ts>2013-08-02 07:40:07 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>VERIFIED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords>test</keywords>
          <priority>P3</priority>
          <bug_severity>normal</bug_severity>
          <target_milestone>4.3.1</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Dani Megert">daniel_megert@ch.ibm.com</reporter>
          <assigned_to name="Dani Megert">daniel_megert@ch.ibm.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706887-W00LIFl8JWNvKyW28M7DEd4esb1j93BbH5H4gnk_lMM</token>

      

      <flag name="review"
          id="58752"
          type_id="1"
          status="+"
          setter="markus_keller@ch.ibm.com"
    />

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2271697</commentid>
    <comment_count>0</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-06-12 05:12:35 -0400</bug_when>
    <thetext>4.3 RC4.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2271698</commentid>
    <comment_count>1</comment_count>
      <attachid>232273</attachid>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-06-12 05:13:46 -0400</bug_when>
    <thetext>Created attachment 232273
Fix</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2274765</commentid>
    <comment_count>2</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-06-20 03:48:45 -0400</bug_when>
    <thetext>Fixed in &apos;master&apos; with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=b3dbf432e08989481681d7518ee591ffdc26fcef</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2289854</commentid>
    <comment_count>3</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-07-30 14:10:01 -0400</bug_when>
    <thetext>Fixed in R4_3_maintenance with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=8a062652c70042ba7882c47a2ce0c3affe2584dc</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2290972</commentid>
    <comment_count>4</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-08-02 07:40:07 -0400</bug_when>
    <thetext>Verified in &apos;R4_3_maintenance&apos;.

The bundle version also needed to be adjusted.
Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=25426ba1d7e32e71845b678edfe790d305244d4e</thetext>
  </long_desc>
      
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>232273</attachid>
            <date>2013-06-12 05:13:00 -0400</date>
            <delta_ts>2013-06-12 05:13:46 -0400</delta_ts>
            <desc>Fix</desc>
            <filename>eclipse.jdt.ui.patch</filename>
            <type>text/plain</type>
            <size>576</size>
            <attacher name="Dani Megert">daniel_megert@ch.ibm.com</attacher>
            
              <token>1425706888-T531c-3SCgN4iI8pzoUUzPhv1UWry0S1tbhlnaCRJPU</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>410371</bug_id>
          
          <creation_ts>2013-06-10 13:41:00 -0400</creation_ts>
          <short_desc>[generalize type] Generalize Type adds import that changes semantics of existing simple names</short_desc>
          <delta_ts>2013-12-05 14:27:11 -0500</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>normal</bug_severity>
          <target_milestone>4.4 M4</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Markus Keller">markus_keller@ch.ibm.com</reporter>
          <assigned_to name="Markus Keller">markus_keller@ch.ibm.com</assigned_to>
          <cc>markus_keller@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706888-Z_Y2TRUmJ6IoVMOXh97HgJgj4XSRzju7v8uuzIm--F8</token>

      

      

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2270690</commentid>
    <comment_count>0</comment_count>
      <attachid>232190</attachid>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-06-10 13:41:18 -0400</bug_when>
    <thetext>Created attachment 232190
Fix

4.3 RC4

In BETA_JAVA8 in org.eclipse.jdt.core.dom.ASTConverter, I tried to generalize a type reference &quot;org.eclipse.jdt.internal.compiler.ast.LambdaExpression&quot; to &quot;org.eclipse.jdt.internal.compiler.ast.Expression&quot;.

The refactoring added an import for &quot;Expression&quot;, although a homonym from the enclosing package org.eclipse.jdt.core.dom was already in use.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2338321</commentid>
    <comment_count>1</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-12-05 14:27:11 -0500</bug_when>
    <thetext>Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=db27665eba539edfb102480f405aada3fd1a35b8</thetext>
  </long_desc>
      
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>232190</attachid>
            <date>2013-06-10 13:41:00 -0400</date>
            <delta_ts>2013-06-10 13:41:18 -0400</delta_ts>
            <desc>Fix</desc>
            <filename>eclipse.jdt.ui.patch</filename>
            <type>text/plain</type>
            <size>2539</size>
            <attacher name="Markus Keller">markus_keller@ch.ibm.com</attacher>
            
              <token>1425706888-K5I-_33rjw6vC_eLGHbKhQvLiAUwkNq-0Q8P9Ov5iV8</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>410173</bug_id>
          
          <creation_ts>2013-06-07 08:09:00 -0400</creation_ts>
          <short_desc>[1.8][quick assist] &apos;Assign parameter to new field&apos; on parameters of static and default interface methods</short_desc>
          <delta_ts>2013-06-26 02:16:03 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>normal</bug_severity>
          <target_milestone>BETA J8</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Noopur Gupta">noopur_gupta@in.ibm.com</reporter>
          <assigned_to name="Noopur Gupta">noopur_gupta@in.ibm.com</assigned_to>
          <cc>manju656@gmail.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706888-c7BsVSbgE6uU5-I6_4Ro61wkp5shw6jgBNIf2sjOUEI</token>

      

      <flag name="review"
          id="58714"
          type_id="1"
          status="+"
          setter="manju656@gmail.com"
    />

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2269788</commentid>
    <comment_count>0</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-06-07 08:09:35 -0400</bug_when>
    <thetext>public interface I1 {
	default void foo(int i) { // quick assist on &apos;i&apos; [1]
		System.out.println(i);
	}
	
	static void bar(int i) {  // quick assist on &apos;i&apos; [2]
		System.out.println(i);
	}
}

Quick assist &apos;Assign parameter to new field&apos; on &apos;i&apos; as shown above, creates the following:

[1]
private int i;
default void foo(int i) {
	this.i = i;
	System.out.println(i);
}

[2]
private static int i;
static void bar(int i) {
	I1.i = i;
	System.out.println(i);
}

The modifier &apos;private&apos; on newly created fields is incorrect.
Also, fields in an interface are &apos;final&apos; and cannot be assigned again in the method. 
This leads to compilation errors.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2276738</commentid>
    <comment_count>1</comment_count>
      <attachid>232726</attachid>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-06-25 08:07:55 -0400</bug_when>
    <thetext>Created attachment 232726
Patch + Tests

The field in an interface has to be initialized with some value, here that value depends on the caller of the method and is unknown.
Also, the field would be final so it cannot be used for assignment in the method.

Hence, disabled this quick assist for interface types.

Manju, please review.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2276916</commentid>
    <comment_count>2</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-06-25 11:07:44 -0400</bug_when>
    <thetext>The fix done in QuickAssistProcessor looks fine.

The new test class &apos;AssistQuickFixTest18&apos; is missing the copyright info as well as the Java 8 header info.

@since 3.9 BETA_JAVA8 tag missing in the Javadoc of the new methods added in JavaProjectHelper.

The Java 8 test setup looks fine, but it would be good if Markus can have a look at the test setup as this will be the test environment we will be using for Java 8 work .

I am giving a review+ for the patch under the trust that the copyright and @since tag information will be added before releasing the patch :)</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2277203</commentid>
    <comment_count>3</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-06-26 02:16:03 -0400</bug_when>
    <thetext>(In reply to comment #2)
Thanks for the review Manju. Added copyright and Java8 header for &apos;AssistQuickFixTest18&apos;. Also, added @since for new methods in JavaProjectHelper.

Pushed with:
http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?h=BETA_JAVA8&amp;id=68906597e0b2e7bab42767bb4d21b85794e3634c</thetext>
  </long_desc>
      
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>232726</attachid>
            <date>2013-06-25 08:07:00 -0400</date>
            <delta_ts>2013-06-25 08:07:55 -0400</delta_ts>
            <desc>Patch + Tests</desc>
            <filename>bug-410173-18-quick-assist-Assign-parameter-to-field.patch</filename>
            <type>text/plain</type>
            <size>12024</size>
            <attacher name="Noopur Gupta">noopur_gupta@in.ibm.com</attacher>
            
              <token>1425706888-dstU7lrAHIJP_SjEAm_VFC62PEMT924LIS4p2RZojCY</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>410170</bug_id>
          
          <creation_ts>2013-06-07 07:53:00 -0400</creation_ts>
          <short_desc>[1.8][quick fix] Remove invalid modifier on static and default interface methods</short_desc>
          <delta_ts>2014-04-13 22:11:29 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>enhancement</bug_severity>
          <target_milestone>4.4 M7</target_milestone>
          <dependson>400977</dependson>
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Noopur Gupta">noopur_gupta@in.ibm.com</reporter>
          <assigned_to name="Manju Mathew">manju656@gmail.com</assigned_to>
          <cc>manju656@gmail.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
    
    <cc>noopur_gupta@in.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706888-ZJhZ9_m0tR4omqHXgikWQeKh1f4WCCiZ5G--L3Ef20A</token>

      

      <flag name="review"
          id="58706"
          type_id="1"
          status="+"
          setter="noopur_gupta@in.ibm.com"
    />

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2269779</commentid>
    <comment_count>0</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-06-07 07:53:13 -0400</bug_when>
    <thetext>interface I {
	private static void foo() { // Error [1]
	}
	
	private default void bar() { // Error [2]
	}	
}

[1] 
&apos;Remove invalid modifier&apos; quick fix removes &apos;static&apos; modifier also along with &apos;private&apos;. 

[2] 
No quick fix is available.

The quick fix should be updated to handle static and default interface methods at ModifierCorrectionSubProcessor.addRemoveInvalidModifiersProposal(..).</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2271017</commentid>
    <comment_count>1</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-06-11 06:21:02 -0400</bug_when>
    <thetext>We also need to handle the case when there are illegal visibility modifier combination in Interface method.
e.g. public abstract static void m1(){}
     public abstract default void m2(){}
     public default static void  m3(){}
All the above have illegal modifier combinations.

For this a new problem id has to generated in core that can be similar to IllegalVisibilityModifierCombinationForInterfaceMethod. This will be handled in bug 400977 in JDT Core.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2276086</commentid>
    <comment_count>2</comment_count>
      <attachid>232685</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-06-24 03:50:05 -0400</bug_when>
    <thetext>Created attachment 232685
Patch with testcases.

I have used the patch provided by Manoj from bug 400977 to complete this task. Provided valid quick fixes for invalid access modifier if used for static and default interface methods.
No quick fix is provided for invalid modifier combination (IProblem#IllegalModifierCombinationForInterfaceMethod), the error marker informs user of the problem.
Added testcases to cover the scenario.
@Noopur: Kindly review and give an initial feedback.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2303515</commentid>
    <comment_count>3</comment_count>
      <attachid>235219</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-09-06 02:00:06 -0400</bug_when>
    <thetext>Created attachment 235219
Updated Patch with tests

Created fresh patch from the newly created remote branch after eliminating duplicate changes.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2386668</commentid>
    <comment_count>4</comment_count>
      <attachid>241759</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2014-04-09 02:03:54 -0400</bug_when>
    <thetext>Created attachment 241759
Correct patch + tests

Previous patch did not contain all the changes.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2387345</commentid>
    <comment_count>5</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2014-04-10 05:51:08 -0400</bug_when>
    <thetext>Review comments:

- Is there an example for modifying the case for &quot;IllegalModifierForInterfaceMethod&quot; with Java 8 condition in ModifierCorrectionSubProcessor? I could not see a corresponding test case also.

- It would be good to place the case for &quot;IllegalModifierForInterfaceMethod18&quot; near other cases for interfaces, like after &quot;IllegalModifierForInterfaceMethod&quot;, in both the files.

- Can we handle &quot;IllegalStrictfpForAbstractInterfaceMethod&quot; also? For example:
    strictfp void fun1();
    strictfp abstract void fun2();</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2387886</commentid>
    <comment_count>6</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2014-04-11 03:05:08 -0400</bug_when>
    <thetext>(In reply to Noopur Gupta from comment #5)
&gt; Review comments:

(In reply to Noopur Gupta from comment #5)
&gt; Review comments:
&gt; 
&gt; - Is there an example for modifying the case for
&gt; &quot;IllegalModifierForInterfaceMethod&quot; with Java 8 condition in
&gt; ModifierCorrectionSubProcessor? I could not see a corresponding test case
&gt; also.
&gt; 
This change was unnecessary, reverted it.

&gt; - It would be good to place the case for
&gt; &quot;IllegalModifierForInterfaceMethod18&quot; near other cases for interfaces, like
&gt; after &quot;IllegalModifierForInterfaceMethod&quot;, in both the files.
&gt; 
done.
&gt; - Can we handle &quot;IllegalStrictfpForAbstractInterfaceMethod&quot; also? For
&gt; example:
&gt;     strictfp void fun1();
&gt;     strictfp abstract void fun2();

Isn&apos;t the error message clear enough?
&quot;strictfp is not permitted for abstract interface method fun2&quot;. For this same reason currently there is no quick fix provided for IProblem#IllegalModifierCombinationForInterfaceMethod.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2388026</commentid>
    <comment_count>7</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2014-04-11 08:09:33 -0400</bug_when>
    <thetext>(In reply to Manju Mathew from comment #6) 
&gt; &gt; - Can we handle &quot;IllegalStrictfpForAbstractInterfaceMethod&quot; also? For
&gt; &gt; example:
&gt; &gt;     strictfp void fun1();
&gt; &gt;     strictfp abstract void fun2();
&gt; 
&gt; Isn&apos;t the error message clear enough?
&gt; &quot;strictfp is not permitted for abstract interface method fun2&quot;. For this
&gt; same reason currently there is no quick fix provided for
&gt; IProblem#IllegalModifierCombinationForInterfaceMethod.

I was suggesting to add the quick fix that will remove &apos;strictfp&apos; as suggested by the error message that it is not permitted here. But we can leave it for now and add it later, if required.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2388501</commentid>
    <comment_count>8</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2014-04-13 22:11:29 -0400</bug_when>
    <thetext>Thanks Noopur. Released the fix as : http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=93033f2a57fd8b34d836f67639f3daed6b4e0f75</thetext>
  </long_desc>
      
          <attachment
              isobsolete="1"
              ispatch="1"
              isprivate="0"
          >
            <attachid>232685</attachid>
            <date>2013-06-24 03:50:00 -0400</date>
            <delta_ts>2013-09-06 02:00:06 -0400</delta_ts>
            <desc>Patch with testcases.</desc>
            <filename>Fix-for-Bug-410170-18-remove-invalid-modifier-on-static.patch</filename>
            <type>text/plain</type>
            <size>17387</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706888-hIQlECYfHnibvvZ2CzVhebN1BVW049A_6lf_hs2E-7Y</token>

          </attachment>
          <attachment
              isobsolete="1"
              ispatch="1"
              isprivate="0"
          >
            <attachid>235219</attachid>
            <date>2013-09-06 02:00:00 -0400</date>
            <delta_ts>2014-04-09 02:03:54 -0400</delta_ts>
            <desc>Updated Patch with tests</desc>
            <filename>Fix-for-Bug-410170-18-remove-invalid-modifier-on-static.patch</filename>
            <type>text/plain</type>
            <size>1247</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706888-GK7lMeBTV0Ok0ZiUhZgVhQ6GJxdgCBTpuVMstnVNwYs</token>

          </attachment>
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>241759</attachid>
            <date>2014-04-09 02:03:00 -0400</date>
            <delta_ts>2014-04-09 02:03:54 -0400</delta_ts>
            <desc>Correct patch + tests</desc>
            <filename>Fix-for-Bug-410170-18-remove-invalid-modifier-on-static.patch</filename>
            <type>text/plain</type>
            <size>5649</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706888-rKdDe5teUiiW1EII44rX36s2p20Ufto33hgwgTRH20c</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>410077</bug_id>
          
          <creation_ts>2013-06-06 10:13:00 -0400</creation_ts>
          <short_desc>[hovering] Javadoc extracted from generated html is rendered with bullets</short_desc>
          <delta_ts>2013-08-05 05:57:48 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>VERIFIED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>normal</bug_severity>
          <target_milestone>4.3.1</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Markus Keller">markus_keller@ch.ibm.com</reporter>
          <assigned_to name="Markus Keller">markus_keller@ch.ibm.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>manju656@gmail.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
    
    <cc>noopur_gupta@in.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706888-UOTVDynFAtUXMH8a6U0w3MHztRJifuZhDloodm1gXn4</token>

      

      <flag name="review"
          id="58749"
          type_id="1"
          status="+"
          setter="noopur_gupta@in.ibm.com"
    />
    <flag name="review"
          id="58908"
          type_id="1"
          status="+"
          setter="daniel_megert@ch.ibm.com"
    />

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2269250</commentid>
    <comment_count>0</comment_count>
      <attachid>232043</attachid>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-06-06 10:13:35 -0400</bug_when>
    <thetext>Created attachment 232043
Fix

4.3.0.I20130605-2000, spawned from bug 409765

Some Javadoc extracted from generated html is rendered with bullets that don&apos;t make sense. The problem is the new Javadoc tool/stylesheet that is used since JDK 7. It generates &lt;ul&gt; tags that are set to &quot;list-style:none;&quot; via CSS.

I think the best fix is to include these CSS tweaks in our CSS.

The bullets are visible at the beginning of extracted methods, constructors, and fields, and at the end of class/interface Javadocs.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2277411</commentid>
    <comment_count>1</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-06-26 11:01:57 -0400</bug_when>
    <thetext>Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=f10b01ba397b72bca83ce6e8832888997db0fa92</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2278122</commentid>
    <comment_count>2</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-06-27 07:12:12 -0400</bug_when>
    <thetext>Noopur, can you please review for 4.3.1 and test with a few more JDK7 Javadocs? 

Make sure you remove the source attachment from the rt.jar, so that you really get the Javadoc from generated HTML files. When looking at extracted docs in Javadoc view and hover, also compare with what you see in the browser (bug 409765).</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2278701</commentid>
    <comment_count>3</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-06-28 09:17:19 -0400</bug_when>
    <thetext>Fix looks good. Verified that with the fix, complete description is shown in the javadocs and there are no more additional bullets or incorrect formatting.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2278831</commentid>
    <comment_count>4</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-06-28 13:12:53 -0400</bug_when>
    <thetext>Reopening until the fix has been released to R4_3_maintenance.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2287793</commentid>
    <comment_count>5</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-07-24 08:17:07 -0400</bug_when>
    <thetext>Fixed in 4.3.1 with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=7428ce1386aac016bd3f1c0ec50b2828b32d04f0</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2291458</commentid>
    <comment_count>6</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-08-05 05:57:48 -0400</bug_when>
    <thetext>Verified in 4.4 using Build id: I20130804-2300 and verified in 4.3.1 using Build id: M20130731-0800</thetext>
  </long_desc>
      
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>232043</attachid>
            <date>2013-06-06 10:13:00 -0400</date>
            <delta_ts>2013-06-06 10:13:35 -0400</delta_ts>
            <desc>Fix</desc>
            <filename>eclipse.jdt.ui.patch</filename>
            <type>text/plain</type>
            <size>1097</size>
            <attacher name="Markus Keller">markus_keller@ch.ibm.com</attacher>
            
              <token>1425706888-3uR5bXHOEIuC5dX7xh0ofjZ-77F-nDCnSTvtoQ3KvVE</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>410056</bug_id>
          
          <creation_ts>2013-06-06 07:21:00 -0400</creation_ts>
          <short_desc>[1.8][move method] Moving default method brings up Textual Move wizard</short_desc>
          <delta_ts>2014-05-19 05:56:39 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>VERIFIED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>enhancement</bug_severity>
          <target_milestone>4.4 RC1</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Noopur Gupta">noopur_gupta@in.ibm.com</reporter>
          <assigned_to name="Manju Mathew">manju656@gmail.com</assigned_to>
          <cc>manju656@gmail.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
    
    <cc>noopur_gupta@in.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706888-AWtpPATGrFSIRqhQVaxLdX1gJOCwrRJeL9xfwjJFG1I</token>

      

      <flag name="review"
          id="62161"
          type_id="1"
          status="+"
          setter="noopur_gupta@in.ibm.com"
    />

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2269147</commentid>
    <comment_count>0</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-06-06 07:21:45 -0400</bug_when>
    <thetext>public interface I {
        default void foo(XYZ xyz) {	
	}
}

class XYZ {}

Refactor &gt; Move on method &quot;foo(XYZ)&quot;.
It brings up the &quot;Textual Move&quot; wizard.

Moving a default method is like moving an instance method, so Move Instance Method refactoring should be adjusted to handle it. 
Default methods can be with/without a valid target type and we will have to retain or remove &apos;default&apos; depending on the target type.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2269181</commentid>
    <comment_count>1</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-06-06 08:20:46 -0400</bug_when>
    <thetext>And whenever the refactoring removes the &apos;default&apos; modifier, it also has to add &apos;public&apos; (since the default method was implicitly public).</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2361298</commentid>
    <comment_count>2</comment_count>
      <attachid>239807</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2014-02-10 21:53:37 -0500</bug_when>
    <thetext>Created attachment 239807
Patch + Tests

MoveInstanceMethodProcessor is modified to handled default interface methods.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2361299</commentid>
    <comment_count>3</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2014-02-10 21:55:20 -0500</bug_when>
    <thetext>Though the change was minor, i did not push it to BETA_JAVA8 as the files modified were previously changed for other bugs and those are yet to be pushed into BETA_JAVA8.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2365259</commentid>
    <comment_count>4</comment_count>
      <attachid>240098</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2014-02-18 23:51:07 -0500</bug_when>
    <thetext>Created attachment 240098
Additional patch

Updated the condition written in RefactoringAvailabilityTester in the previous patch.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2389026</commentid>
    <comment_count>5</comment_count>
      <attachid>241994</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2014-04-15 01:37:20 -0400</bug_when>
    <thetext>Created attachment 241994
Patch+Tests

Consolidated the patch and updated against master.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2389902</commentid>
    <comment_count>6</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2014-04-16 13:32:31 -0400</bug_when>
    <thetext>Review comments:

- Will the condition updated in MoveInstanceMethodProcessor#checkMethodDeclaration ever be executed?
This method will not be called for static or abstract interface methods, and no error has to be shown for default methods. If so, this condition can be removed along with the message.

- It should also handle moving to an interface which is the type of a field.

- Also, moving a method from class to interface should be possible and accordingly the &apos;default&apos; modifier will be added and visibility will have to be adjusted. (probably as a separate bug?)

- Moving to an interface should only be allowed if that *target* interface is &gt;= 1.8. Currently it allows moving to any interface. And it should not be based on &apos;default&apos; modifier.

- Since the target can also be an interface now and not only a class, the messages may need to be updated by replacing &apos;class&apos; with &apos;type&apos;.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2390053</commentid>
    <comment_count>7</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2014-04-16 23:21:10 -0400</bug_when>
    <thetext>(In reply to Noopur Gupta from comment #6)
&gt; Review comments:
&gt; 
&gt; - Will the condition updated in
&gt; MoveInstanceMethodProcessor#checkMethodDeclaration ever be executed?
&gt; This method will not be called for static or abstract interface methods, and
&gt; no error has to be shown for default methods. If so, this condition can be
&gt; removed along with the message.
The condition is required and the method will be invoked for static and abstract interface methods. Note that only the first and second conditions are written in if and else..if, the remaining conditions are written using independent if&apos;s and hence the new condition will be evaluated when the method is static/abstract/default.

&gt; - It should also handle moving to an interface which is the type of a field.
Did you mean if the target is interface? If so, that is handled in MoveInstanceMethodProcessor#createMethodCopy. test18_2 tests moving a default method to another interface.

&gt; - Also, moving a method from class to interface should be possible and
&gt; accordingly the &apos;default&apos; modifier will be added and visibility will have to
&gt; be adjusted. (probably as a separate bug?)
Created bug 432971 to handle this case.

&gt; - Moving to an interface should only be allowed if that *target* interface
&gt; is &gt;= 1.8. Currently it allows moving to any interface. And it should not be
&gt; based on &apos;default&apos; modifier.
Right, added the version check and removed the default method check.

&gt; - Since the target can also be an interface now and not only a class, the
&gt; messages may need to be updated by replacing &apos;class&apos; with &apos;type&apos;.
If we replace the message with &apos;type&apos;, it will not be the exact message when dealing with less than Java 8 projects. Another option is to have 2 different message depending on the project Java version compatibility. Again it will be confusing when project A is in Java 1.8 which depends on project B that is Java 1.6 compatible and user try to move a method from Project A to Project B. 
@Markus: What do you suggest?</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2390532</commentid>
    <comment_count>8</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2014-04-18 04:55:38 -0400</bug_when>
    <thetext>(In reply to Manju Mathew from comment #7)
&gt; (In reply to Noopur Gupta from comment #6)
&gt; &gt; Review comments:
&gt; &gt; 
&gt; &gt; - Will the condition updated in
&gt; &gt; MoveInstanceMethodProcessor#checkMethodDeclaration ever be executed?
&gt; &gt; This method will not be called for static or abstract interface methods, and
&gt; &gt; no error has to be shown for default methods. If so, this condition can be
&gt; &gt; removed along with the message.
&gt; The condition is required and the method will be invoked for static and
&gt; abstract interface methods. Note that only the first and second conditions
&gt; are written in if and else..if, the remaining conditions are written using
&gt; independent if&apos;s and hence the new condition will be evaluated when the
&gt; method is static/abstract/default.

I get &quot;Move static members&quot; dialog on moving a static interface method and &quot;Textual move&quot; dialog on moving abstract interface method. MoveInstanceMethodProcessor#checkMethodDeclaration is invoked only for default interface methods.

&gt; &gt; - It should also handle moving to an interface which is the type of a field.
&gt; Did you mean if the target is interface? If so, that is handled in
&gt; MoveInstanceMethodProcessor#createMethodCopy. test18_2 tests moving a
&gt; default method to another interface.

No, in Move refactoring, we can also move to the type of a field (other than type of an argument). Example - it should be possible to move #f1 to &apos;J&apos; in the following case (change &apos;I&apos;, &apos;J&apos; to classes to see that):
interface I {
	J j= new J() {};
	default void f1() {
		System.out.println(j.toString());
	}
}

interface J {	
}</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2395174</commentid>
    <comment_count>9</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2014-04-30 02:24:22 -0400</bug_when>
    <thetext>(In reply to Noopur Gupta from comment #8)
&gt; I get &quot;Move static members&quot; dialog on moving a static interface method and
&gt; &quot;Textual move&quot; dialog on moving abstract interface method.
&gt; MoveInstanceMethodProcessor#checkMethodDeclaration is invoked only for
&gt; default interface methods.
MoveInstanceMethodTests#failHelper1 internally invokes MoveInstanceMethodProcessor#checkMethodDeclaration for all the testFail cases and if the condition is removed then MoveInstanceMethodTests#testFail0 will fail.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2395710</commentid>
    <comment_count>10</comment_count>
      <attachid>242584</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2014-04-30 21:14:20 -0400</bug_when>
    <thetext>Created attachment 242584
Patch+Tests

With this patch move default interface method will allow declared fields as the possible target.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2396055</commentid>
    <comment_count>11</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2014-05-02 02:48:13 -0400</bug_when>
    <thetext>(In reply to Manju Mathew from comment #10)
&gt; Created attachment 242584 [details] [diff]
&gt; Patch+Tests
&gt; 
&gt; With this patch move default interface method will allow declared fields as
&gt; the possible target.
Looks good.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2401968</commentid>
    <comment_count>12</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2014-05-14 19:11:48 -0400</bug_when>
    <thetext>In MoveInstanceMethodProcessor.createMethodCopy(..):
- replaced Modifier.ModifierKeyword.PUBLIC_KEYWORD.toFlagValue() by Modifier.PUBLIC
- added modifier adjustments for moving method from class to 1.8 interface

In computeTargetCategories, excluded annotation types from potential targets.

Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=0bdb6019092ac1ae9e6528adf53cc81a87497585</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2403561</commentid>
    <comment_count>13</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2014-05-19 05:56:39 -0400</bug_when>
    <thetext>Verified as working in build id: I20140515-1230.</thetext>
  </long_desc>
      
          <attachment
              isobsolete="1"
              ispatch="1"
              isprivate="0"
          >
            <attachid>239807</attachid>
            <date>2014-02-10 21:53:00 -0500</date>
            <delta_ts>2014-04-15 01:37:20 -0400</delta_ts>
            <desc>Patch + Tests</desc>
            <filename>Fixed-Bug-410056-18move-method-Moving-default-method.patch</filename>
            <type>text/plain</type>
            <size>14936</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706888-gT3WMkFrEeDC2QWbfxKhckztDRL5qDNyYXarS5o98Sk</token>

          </attachment>
          <attachment
              isobsolete="1"
              ispatch="1"
              isprivate="0"
          >
            <attachid>240098</attachid>
            <date>2014-02-18 23:51:00 -0500</date>
            <delta_ts>2014-04-15 01:37:20 -0400</delta_ts>
            <desc>Additional patch</desc>
            <filename>Fixed-Bug-410056-18move-method-Moving-default-method_part2.patch</filename>
            <type>text/plain</type>
            <size>1159</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706888-KXasUfytB1Ihj_XK0MZ6w5qxEbtEnZRsjrkXMn4OSLg</token>

          </attachment>
          <attachment
              isobsolete="1"
              ispatch="1"
              isprivate="0"
          >
            <attachid>241994</attachid>
            <date>2014-04-15 01:37:00 -0400</date>
            <delta_ts>2014-04-30 21:14:20 -0400</delta_ts>
            <desc>Patch+Tests</desc>
            <filename>Fixed-Bug-410056-18move-method-Moving-default-method.patch</filename>
            <type>text/plain</type>
            <size>12042</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706888-yPL4FzkCr_L4SzqtsWiv2br-NwoP8h5MhW2hlyx_gik</token>

          </attachment>
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>242584</attachid>
            <date>2014-04-30 21:14:00 -0400</date>
            <delta_ts>2014-04-30 21:14:20 -0400</delta_ts>
            <desc>Patch+Tests</desc>
            <filename>Fixed-Bug-410056-18move-method-Moving-default-methodv4.patch</filename>
            <type>text/plain</type>
            <size>17183</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706888-rSSgVp-9qcmx4A0_Xy78tiajPAHcEf_kICW12ChKdl4</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>409906</bug_id>
          
          <creation_ts>2013-06-05 02:43:00 -0400</creation_ts>
          <short_desc>[1.8][move static members] Error in Preview while moving static method to interface</short_desc>
          <delta_ts>2014-02-26 04:18:28 -0500</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>VERIFIED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>enhancement</bug_severity>
          <target_milestone>BETA J8</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Noopur Gupta">noopur_gupta@in.ibm.com</reporter>
          <assigned_to name="Noopur Gupta">noopur_gupta@in.ibm.com</assigned_to>
          <cc>manju656@gmail.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706888-Vkjb4daXPLs2IpKJ_yLBhA6OVKk-FcAu76ypFtHFefA</token>

      

      <flag name="review"
          id="58389"
          type_id="1"
          status="+"
          setter="markus_keller@ch.ibm.com"
    />

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2268119</commentid>
    <comment_count>0</comment_count>
      <attachid>231968</attachid>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-06-05 02:43:44 -0400</bug_when>
    <thetext>Created attachment 231968
Screenshot

Consider the following example:

public interface I {

}

class X {
	static int get() { // Move &apos;get&apos;
		return 0;
	}
}

Refactor &gt; Move on get(). We get Move Static Members wizard. 
Select Destination type for get() as the interface I.
Click Preview -&gt; Error is shown as in the attached screenshot.
Click Continue and then OK. Refactoring is completed without any compilation error.

The error in the Preview should not be shown.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2268227</commentid>
    <comment_count>1</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-06-05 06:01:25 -0400</bug_when>
    <thetext>(In reply to comment #0)
&gt; Created attachment 231968 [details]
&gt; Screenshot
&gt; 
&gt; Consider the following example:
&gt; 
&gt; public interface I {
&gt; 
&gt; }
&gt; 
&gt; class X {
&gt; 	static int get() { // Move &apos;get&apos;
&gt; 		return 0;
&gt; 	}
&gt; }
&gt; 
&gt; Refactor &gt; Move on get(). We get Move Static Members wizard. 
&gt; Select Destination type for get() as the interface I.
&gt; Click Preview -&gt; Error is shown as in the attached screenshot.
&gt; Click Continue and then OK. Refactoring is completed without any compilation
&gt; error.
&gt; 
&gt; The error in the Preview should not be shown.

The example should be: 

public interface I {

}
class X {
	public static int get() { // Move &apos;get&apos;
		return 0;
	}
}

Only &apos;public&apos; static methods should be allowed to move to an interface.

In the example of comment #1, we should modify the error message to include &apos;public static&apos; methods also.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2268504</commentid>
    <comment_count>2</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-06-05 09:51:01 -0400</bug_when>
    <thetext>We should allow moving static methods to an interface, but only if source level is &gt;= 1.8.

If the member to be moved to an interface is not yet public, we should have a warning (not an error) that the visibility will be increased to public.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2269218</commentid>
    <comment_count>3</comment_count>
      <attachid>232039</attachid>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-06-06 09:06:07 -0400</bug_when>
    <thetext>Created attachment 232039
Patch

Updated MoveStaticMembersProcessor#canMoveToInterface(IMember) to accept &apos;public static&apos; methods if source level is &gt;= 1.8.
Also, updated the message to include &apos;public static&apos; methods and added a warning if visibility is being increased to public.

Currently &quot;Move&quot; refactoring on static and default methods in an interface shows the &quot;Textual Move&quot; dialog. The method is moved to the selected destination and its references are not updated.

This is fixed for static methods in the attached patch, by updating RefactoringAvailabilityTester#isMoveStaticAvailable(IMember) to accept static methods from interfaces. Also, handled addition of &apos;public&apos; to implicitly public methods while moving to a class. 

However, the Move Static Members refactoring does not remove redundant modifiers while moving to an interface.

For moving default methods from an interface, see bug 410056.

Markus, please have a look.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2275085</commentid>
    <comment_count>4</comment_count>
      <attachid>232606</attachid>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-06-20 12:41:11 -0400</bug_when>
    <thetext>Created attachment 232606
Patch + Tests

(In reply to comment #3)
&gt; added a warning if visibility is being increased to public.
Updating visibility and adding the warning is already taken care in MemberVisibilityAdjustor.

Added source level check for 1.8 at RefactoringAvailabilityTester#isMoveStaticAvailable(IMember) and included tests.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2303584</commentid>
    <comment_count>5</comment_count>
      <attachid>235232</attachid>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-09-06 05:13:45 -0400</bug_when>
    <thetext>Created attachment 235232
Patch + Tests

Updated patch with a bug fix and removed code that is already released.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2366304</commentid>
    <comment_count>6</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2014-02-20 15:26:52 -0500</bug_when>
    <thetext>The added warning message in MoveStaticMembersProcessor for

    if (!Flags.isPublic(fMembersToMove[i].getFlags())) ...

didn&apos;t make sense. Changed the message to &quot;Moved member will be public in the destination interface&quot;.

The is18OrHigher(..) check must be done on the destination project, not on the source. And the correct check is a bit more complicated, since it also has to block interface-to-interface moves of a method if the destination is pre-18.

Renamed the test methods in MoveMembersTests18 to test18_1 etc. to avoid conflicts when the next one tries to add another test to MoveMembersTests.

Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=23d13dacca9861ae060410926043fea86d2e5795 and parent commit.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2366305</commentid>
    <comment_count>7</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2014-02-20 15:26:59 -0500</bug_when>
    <thetext>.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2366511</commentid>
    <comment_count>8</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2014-02-21 02:36:26 -0500</bug_when>
    <thetext>Verified in Java 8 RC1 using Kepler SR2(RC4) +  Eclipse Java Development Tools
Patch for Java 8 Support (BETA)   1.0.0.v20140220-2054

One doubt, if the destination already has a method abstract/default/static which is explicitly public, then shouldn&apos;t the moved method follow the existing signature?
public interface I {
    public void abstractM();
}

class X {
	static int get() { // Move &apos;get&apos;
		return 0;
	}
}</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2368609</commentid>
    <comment_count>9</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2014-02-26 04:18:28 -0500</bug_when>
    <thetext>(In reply to Manju Mathew from comment #8)
See bug 71627 comment #8 : We should not add redundant &apos;public&apos;.</thetext>
  </long_desc>
      
          <attachment
              isobsolete="0"
              ispatch="0"
              isprivate="0"
          >
            <attachid>231968</attachid>
            <date>2013-06-05 02:43:00 -0400</date>
            <delta_ts>2013-06-05 02:43:44 -0400</delta_ts>
            <desc>Screenshot</desc>
            <filename>1.PNG</filename>
            <type>image/png</type>
            <size>29034</size>
            <attacher name="Noopur Gupta">noopur_gupta@in.ibm.com</attacher>
            
              <token>1425706888-hJNHGzDAuozah85rc97Zmy9CjDxZNJyxr2Y10inWs2I</token>

          </attachment>
          <attachment
              isobsolete="1"
              ispatch="1"
              isprivate="0"
          >
            <attachid>232039</attachid>
            <date>2013-06-06 09:06:00 -0400</date>
            <delta_ts>2013-06-20 12:41:11 -0400</delta_ts>
            <desc>Patch</desc>
            <filename>Bug-409906-18-move-static-members.patch</filename>
            <type>text/plain</type>
            <size>9822</size>
            <attacher name="Noopur Gupta">noopur_gupta@in.ibm.com</attacher>
            
              <token>1425706888-o_jzMoypQQXpTKpvWrYUZ5_aQPOOhUqtJ2TZCm5zp6k</token>

          </attachment>
          <attachment
              isobsolete="1"
              ispatch="1"
              isprivate="0"
          >
            <attachid>232606</attachid>
            <date>2013-06-20 12:41:00 -0400</date>
            <delta_ts>2013-09-06 05:13:45 -0400</delta_ts>
            <desc>Patch + Tests</desc>
            <filename>18-move-static-members.patch</filename>
            <type>text/plain</type>
            <size>25435</size>
            <attacher name="Noopur Gupta">noopur_gupta@in.ibm.com</attacher>
            
              <token>1425706888-unx4okij9wdkvC-ZeEutbUyY-djfaRzSbtsgAlO4L9E</token>

          </attachment>
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>235232</attachid>
            <date>2013-09-06 05:13:00 -0400</date>
            <delta_ts>2013-09-06 05:13:45 -0400</delta_ts>
            <desc>Patch + Tests</desc>
            <filename>move-static-members.patch</filename>
            <type>text/plain</type>
            <size>19371</size>
            <attacher name="Noopur Gupta">noopur_gupta@in.ibm.com</attacher>
            
              <token>1425706888-IW7n_rbpnvZHDcN9VLG06GkSwIjWl0RMjAe4y9aJLOU</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>409723</bug_id>
          
          <creation_ts>2013-06-03 09:03:00 -0400</creation_ts>
          <short_desc>[1.8][introduce indirection] Unable to introduce indirection on methods in an interface</short_desc>
          <delta_ts>2014-04-24 09:18:04 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>enhancement</bug_severity>
          <target_milestone>4.4 M7</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Noopur Gupta">noopur_gupta@in.ibm.com</reporter>
          <assigned_to name="Noopur Gupta">noopur_gupta@in.ibm.com</assigned_to>
          <cc>manju656@gmail.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
    
    <cc>noopur_gupta@in.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706888-9Y57VWS98BWZ_iN9y3WL3qBRA65EKNOfRPBvy4-Y_tA</token>

      

      <flag name="review"
          id="58524"
          type_id="1"
          status="+"
          setter="markus_keller@ch.ibm.com"
    />

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2266950</commentid>
    <comment_count>0</comment_count>
      <attachid>231871</attachid>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-06-03 09:03:53 -0400</bug_when>
    <thetext>Created attachment 231871
Screenshot

Refactor &gt; Introduce Indirection on default and static methods in an interface gives the error &quot;Cannot place new method on an interface.&quot; as shown in the attached screenshot.

Expected result for the default method is shown below: 

public interface I {

	public static void foo(I i) {
		i.foo();
	}

	default void foo() {

	}
}</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2271633</commentid>
    <comment_count>1</comment_count>
      <attachid>232267</attachid>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-06-12 02:10:17 -0400</bug_when>
    <thetext>Created attachment 232267
Patch

Removed the check for target interface in IntroduceIndirectionRefactoring.setIntermediaryTypeName(String).

Renamed &quot;class&quot; to &quot;type&quot; in fields/methods/comments/messages.

IntroduceIndirectionRefactoring.checkFinalConditions(..)had the comment: &quot;intermediary class is already non binary/non-enum/non-interface.&quot;
Changed it to &quot;intermediary type is already non binary/non-enum&quot;.
But I could not see any change that would be required in the code following this comment, specific to the intermediary type being an interface.

Also, updated the FilteredTypesSelectionDialog&apos;s elementKinds as IJavaSearchConstants.CLASS_AND_INTERFACE to show interfaces also in the &apos;Choose 
Type&apos; dialog.

IntroduceIndirectionRefactoring.copyExceptions(..) has changes part of bug 403924 (Replace usages of MethodDeclaration#thrownExceptions()). But it loses TYPE_USE annotations currently (bug 409586).

Also, the refactoring does not remove redundant modifiers while adding the new method to an interface.

Markus, please have a look.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2274870</commentid>
    <comment_count>2</comment_count>
      <attachid>232589</attachid>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-06-20 07:13:21 -0400</bug_when>
    <thetext>Created attachment 232589
Patch + Tests

(In reply to comment #1)
 
&gt; Removed the check for target interface in
&gt; IntroduceIndirectionRefactoring.setIntermediaryTypeName(String).
...
&gt; Also, updated the FilteredTypesSelectionDialog&apos;s elementKinds as
&gt; IJavaSearchConstants.CLASS_AND_INTERFACE to show interfaces also in the
&gt; &apos;Choose Type&apos; dialog.

Added checks for the above to change the behavior only if source level is &gt;= 1.8.

Also, added tests in the patch.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2389218</commentid>
    <comment_count>3</comment_count>
      <attachid>242006</attachid>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2014-04-15 09:10:39 -0400</bug_when>
    <thetext>Created attachment 242006
Fix + Tests

Updated the patch based on master branch.

The behavior is similar to introduce indirection refactoring with an abstract class.

Changes related to the fix are very small as mentioned in the above comments.
Most of the changes in the patch are due to replacing &quot;class&quot; with &quot;type&quot; everywhere.

Manju, please review.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2389906</commentid>
    <comment_count>4</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2014-04-16 13:38:01 -0400</bug_when>
    <thetext>Should we have separate messages from refactoring.properties for &apos;class&apos; and &apos;type&apos; variants based on the level being &lt; or &gt;= 1.8?</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2390089</commentid>
    <comment_count>5</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2014-04-17 03:49:04 -0400</bug_when>
    <thetext>(In reply to Noopur Gupta from comment #3)
&gt; Created attachment 242006 [details] [diff]
&gt; Fix + Tests

1. While creating the new static method in interface, why are the redundant public modifier not removed?
2. Regarding the modified message, we have the same concern in bug 410056. Markus what is your opinion?
3. Consider the below code snippet, I8 is an interface in Java 1.8 project and A7 is in a Java 1.7 project:
package p2;

import p1.I8;

public class A7 {
	void foo(I8 i) {
		i.defaultM2(); // Invoke &apos;Introduce Indirection&apos;
	}
}

If the target is chosen as I8, then error message is displayed &quot;Cannot place a new method in interface&quot;. 
Since I8 is in a Java 1.8 project, can&apos;t we create a static method in I8?

4.Similarly when &apos;Introduce Indirection&apos; is invoked from a Java 1.8 project and if the target is in Java 1.7 project, then currently the we create static method in Java 1.7 interface which results in compiler errors.

5. While testing found that trying to access a static interface method from a 1.7 project gives compiler error. Discussed with Jay and he has raised the concern in bug 390889 comment 49. Separate bug will be raised by Jay if this issue is not already being discussed in another bug.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2390566</commentid>
    <comment_count>6</comment_count>
      <attachid>242120</attachid>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2014-04-18 07:50:23 -0400</bug_when>
    <thetext>Created attachment 242120
Fix + Tests

(In reply to Manju Mathew from comment #5)
&gt; 1. While creating the new static method in interface, why are the redundant
&gt; public modifier not removed?
As mentioned in comment #1 (and bug 409906 comment #3), removing redundant modifiers was not handled as I expected bug 71627 to handle that for all refactorings. However, fixed it for Introduce indirection in the attached patch.

&gt; 3 and 4.
After discussion following bug 390889 comment 49, it looks like we should allow adding the new static method in a target interface only when both the source and target projects are &gt;= 1.8. Updated patch accordingly.

Manju, please have a look.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2392508</commentid>
    <comment_count>7</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2014-04-24 09:18:04 -0400</bug_when>
    <thetext>Looks good, thanks. Released with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=e01fd4fbc98253da7f6289cae92721071c39a317</thetext>
  </long_desc>
      
          <attachment
              isobsolete="0"
              ispatch="0"
              isprivate="0"
          >
            <attachid>231871</attachid>
            <date>2013-06-03 09:03:00 -0400</date>
            <delta_ts>2013-06-03 09:03:53 -0400</delta_ts>
            <desc>Screenshot</desc>
            <filename>1.PNG</filename>
            <type>image/png</type>
            <size>26468</size>
            <attacher name="Noopur Gupta">noopur_gupta@in.ibm.com</attacher>
            
              <token>1425706888-rNLGe8Le8SvQdF7ECOI7brRfpgMYutSgnpEKx-UVEMQ</token>

          </attachment>
          <attachment
              isobsolete="1"
              ispatch="1"
              isprivate="0"
          >
            <attachid>232267</attachid>
            <date>2013-06-12 02:10:00 -0400</date>
            <delta_ts>2013-06-20 07:13:21 -0400</delta_ts>
            <desc>Patch</desc>
            <filename>Bug-409723-18-introduce-indirection.patch</filename>
            <type>text/plain</type>
            <size>34446</size>
            <attacher name="Noopur Gupta">noopur_gupta@in.ibm.com</attacher>
            
              <token>1425706888-1JN4It6ak3okTWQZW01bvtZWkywxvVC8REyk5f9afcU</token>

          </attachment>
          <attachment
              isobsolete="1"
              ispatch="1"
              isprivate="0"
          >
            <attachid>232589</attachid>
            <date>2013-06-20 07:13:00 -0400</date>
            <delta_ts>2014-04-15 09:10:39 -0400</delta_ts>
            <desc>Patch + Tests</desc>
            <filename>18-introduce-indirection.patch</filename>
            <type>text/plain</type>
            <size>54778</size>
            <attacher name="Noopur Gupta">noopur_gupta@in.ibm.com</attacher>
            
              <token>1425706888-gRNsXraAWWEqTIAxUQh7CpeLDs0_dGTdxlI49D9QnjQ</token>

          </attachment>
          <attachment
              isobsolete="1"
              ispatch="1"
              isprivate="0"
          >
            <attachid>242006</attachid>
            <date>2014-04-15 09:10:00 -0400</date>
            <delta_ts>2014-04-18 07:50:23 -0400</delta_ts>
            <desc>Fix + Tests</desc>
            <filename>Introduce indirection.patch</filename>
            <type>text/plain</type>
            <size>43284</size>
            <attacher name="Noopur Gupta">noopur_gupta@in.ibm.com</attacher>
            
              <token>1425706888-jouvbfZ2mCt9dytWhDrN09sQdsKf3TbGb_SaHNm6DCA</token>

          </attachment>
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>242120</attachid>
            <date>2014-04-18 07:50:00 -0400</date>
            <delta_ts>2014-04-18 07:50:23 -0400</delta_ts>
            <desc>Fix + Tests</desc>
            <filename>introduce indirection.patch</filename>
            <type>text/plain</type>
            <size>44373</size>
            <attacher name="Noopur Gupta">noopur_gupta@in.ibm.com</attacher>
            
              <token>1425706888-2QnoFROZ8GAe_Y6xJsgaC-vZcMGJQWmP0txEJF9gU5s</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>409719</bug_id>
          
          <creation_ts>2013-06-03 08:41:00 -0400</creation_ts>
          <short_desc>[1.8][refactoring] Incorrect Method signature preview for default methods</short_desc>
          <delta_ts>2014-02-24 21:53:37 -0500</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>PC</rep_platform>
          <op_sys>Windows 7</op_sys>
          <bug_status>VERIFIED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>enhancement</bug_severity>
          <target_milestone>BETA J8</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Noopur Gupta">noopur_gupta@in.ibm.com</reporter>
          <assigned_to name="Noopur Gupta">noopur_gupta@in.ibm.com</assigned_to>
          <cc>manju656@gmail.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706888-1Ci7s27NIQuMpLDU9aOSpoQkQ9rG6r8krNw1eSrMCG0</token>

      

      <flag name="review"
          id="58338"
          type_id="1"
          status="+"
          setter="markus_keller@ch.ibm.com"
    />

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2266936</commentid>
    <comment_count>0</comment_count>
      <attachid>231869</attachid>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-06-03 08:41:51 -0400</bug_when>
    <thetext>Created attachment 231869
Screenshot

In Refactoring wizards like Change Method Signature and Introduce Parameter Object, the Method signature preview for default methods does not show the default modifier. Attached the screenshot.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2267033</commentid>
    <comment_count>1</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-06-03 10:25:09 -0400</bug_when>
    <thetext>Yup, that should be added.

Please fix all refactorings that use InputPageUtil#createSignaturePreview(Composite) to create such previews.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2268207</commentid>
    <comment_count>2</comment_count>
      <attachid>231978</attachid>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-06-05 05:26:42 -0400</bug_when>
    <thetext>Created attachment 231978
Patch

(In reply to comment #1)
&gt; Please fix all refactorings that use
&gt; InputPageUtil#createSignaturePreview(Composite) to create such previews.

The refactorings using InputPageUtil#createSignaturePreview(Composite) are:
1. Change Method Signature
2. Introduce Parameter Object
3. Introduce Parameter
4. Extract Method
5. Replace Invocations

Fixed 1, 2, 3 by updating the getNewMethodSignature(), getOldMethodSignature() methods of ChangeSignatureProcessor.

Extract method refactoring shows the preview of the new method which will be handled in bug 406786.

Replace Invocations refactoring is not yet complete (bug 44201) and also it creates the preview text with:
JavaElementLabels.getElementLabel(fRefactoring.getMethod(), LABEL_FLAGS);

Also, updated TypeContextChecker#appendMethodDeclaration(..).

Markus, please review.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2365473</commentid>
    <comment_count>3</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2014-02-19 09:14:34 -0500</bug_when>
    <thetext>Committed to BETA_JAVA8 with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=d9552c2abd0d8618f2c51ea9f0b1586dc00e9624</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2367942</commentid>
    <comment_count>4</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2014-02-24 21:53:37 -0500</bug_when>
    <thetext>Verified using Kepler SR2 + Java 8 RC1 + Eclipse Java Development Tools Patch for Java 8 Support (BETA) 1.0.0.v20140223-2022</thetext>
  </long_desc>
      
          <attachment
              isobsolete="0"
              ispatch="0"
              isprivate="0"
          >
            <attachid>231869</attachid>
            <date>2013-06-03 08:41:00 -0400</date>
            <delta_ts>2013-06-03 08:41:51 -0400</delta_ts>
            <desc>Screenshot</desc>
            <filename>1.png</filename>
            <type>image/png</type>
            <size>26778</size>
            <attacher name="Noopur Gupta">noopur_gupta@in.ibm.com</attacher>
            
              <token>1425706888-nK8Woy77ofjS71lDOueEOqkYyLKAawIPOhhKzW98A3E</token>

          </attachment>
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>231978</attachid>
            <date>2013-06-05 05:26:00 -0400</date>
            <delta_ts>2013-06-05 05:26:42 -0400</delta_ts>
            <desc>Patch</desc>
            <filename>Fixed-Bug-409719--18-Incorrect-Method-sign-preview.patch</filename>
            <type>text/plain</type>
            <size>4137</size>
            <attacher name="Noopur Gupta">noopur_gupta@in.ibm.com</attacher>
            
              <token>1425706888-WBqNQYQwJ1oQ4H0HwKbSB-RgFZrWJDOEaiNuATmZqY8</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>409717</bug_id>
          
          <creation_ts>2013-06-03 08:39:00 -0400</creation_ts>
          <short_desc>[hovering] Javadoc link to package doesn&apos;t work in attached package-info.java</short_desc>
          <delta_ts>2013-06-21 00:00:05 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>normal</bug_severity>
          <target_milestone>4.4 M1</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Markus Keller">markus_keller@ch.ibm.com</reporter>
          <assigned_to name="Manju Mathew">manju656@gmail.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706888-J8azY-sSHN49DPgRQI45lAWgPI54pEnfsJu36xJiREM</token>

      

      <flag name="review"
          id="58353"
          type_id="1"
          status="+"
          setter="markus_keller@ch.ibm.com"
    />

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2266931</commentid>
    <comment_count>0</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-06-03 08:39:06 -0400</bug_when>
    <thetext>The Javadoc in javax.lang.model&apos;s package-info.java (in attached source) contains: &quot;{@linkplain javax.annotation.processing annotation processing}&quot;

The parsing of this link fails in JavaElementLinks#parseURI(URI) because the
&quot;if (element instanceof IPackageFragment)&quot; branch only resolves types, but not packages. We should use the same code as in &quot;if (element instanceof IType)&quot; to resolve a link to package as well.

Also need to check whether the Javadoc tool supports links to members. If it does, then reuse that part of &quot;if (element instanceof IType)&quot; as well.

And last but not least, Javadocs of JavaElementLinks need to tell that refTypeName can also refer to a package.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2266932</commentid>
    <comment_count>1</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-06-03 08:39:57 -0400</bug_when>
    <thetext>Manju, please have a look for 4.4.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2266941</commentid>
    <comment_count>2</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-06-03 08:45:12 -0400</bug_when>
    <thetext>Make sure we continue to only support fully-qualified type name references in package-info.java, see bug 216451.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2268684</commentid>
    <comment_count>3</comment_count>
      <attachid>231996</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-06-05 11:20:22 -0400</bug_when>
    <thetext>Created attachment 231996
Patch.

Handled resolving of package links appearing in attached package-info.java file.

Verified that links to members in package-info.java are supported in Javadoc generated by the Javadoc tool. e.g. : {@linkplain javax.lang.model.element.AnnotationMirror#getAnnotationType() annotationMethod}. This is supported in the current implementation of JavaElementLinks.
Javadoc generated by Javadoc tool supports only fully qualified type name references in package-info.java, this behavior is maintained in our views as well.

Updated the Javadoc for &apos;refTypeName&apos; in JavaElementLinks#createURI(...)

Markus, kindly review.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2274997</commentid>
    <comment_count>4</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-06-20 10:34:41 -0400</bug_when>
    <thetext>Looks good, please release.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2275323</commentid>
    <comment_count>5</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-06-21 00:00:05 -0400</bug_when>
    <thetext>Thanks Markus. Released the fix as:
http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=95a429c87e11d9f532ec6d0ef68c3d442f81a499</thetext>
  </long_desc>
      
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>231996</attachid>
            <date>2013-06-05 11:20:00 -0400</date>
            <delta_ts>2013-06-05 11:20:22 -0400</delta_ts>
            <desc>Patch.</desc>
            <filename>Fix-for-bug-409717-Javadoc-link-to-package-doesnt-wo.patch</filename>
            <type>text/plain</type>
            <size>1386</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706888-NU1uqyNhUjOH6pLSC4a4MSJsdIKNL6EXzr56K_PagWw</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>409707</bug_id>
          
          <creation_ts>2013-06-03 05:48:00 -0400</creation_ts>
          <short_desc>PropertiesFileQuickAssistTest.testRemoveProperty3 and testRemoveProperty4 failed</short_desc>
          <delta_ts>2013-12-10 14:33:10 -0500</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords>test</keywords>
          <priority>P3</priority>
          <bug_severity>normal</bug_severity>
          <target_milestone>4.4 M4</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Dani Megert">daniel_megert@ch.ibm.com</reporter>
          <assigned_to name="Markus Keller">markus_keller@ch.ibm.com</assigned_to>
          <cc>deepakazad@gmail.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706888-dOR5ja6GghtD__mXhHpR7LU8ZivriKSu_nIhIecofbo</token>

      

      

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2266839</commentid>
    <comment_count>0</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-06-03 05:48:09 -0400</bug_when>
    <thetext>I20130531-2000.

PropertiesFileQuickAssistTest.testRemoveProperty3 and testRemoveProperty4 failed.

http://download.eclipse.org/eclipse/downloads/drops4/I20130531-2000/testresults/html/org.eclipse.jdt.ui.tests_macosx.cocoa.x86_5.0.html


nls file expected:&lt;... static String Test_[]2; } &gt; but was:&lt;... static String Test_[1; public static String Test_]2; } &gt;

junit.framework.ComparisonFailure: nls file expected:&lt;... static String Test_[]2;
}
&gt; but was:&lt;... static String Test_[1;
public static String Test_]2;
}
&gt;
at org.eclipse.jdt.ui.tests.quickfix.PropertiesFileQuickAssistTest.assertEqualLines(PropertiesFileQuickAssistTest.java:153)
at org.eclipse.jdt.ui.tests.quickfix.PropertiesFileQuickAssistTest.checkContentOfCu(PropertiesFileQuickAssistTest.java:124)
at org.eclipse.jdt.ui.tests.quickfix.PropertiesFileQuickAssistTest.testRemoveProperty3(PropertiesFileQuickAssistTest.java:641)
at junit.extensions.TestDecorator.basicRun(TestDecorator.java:23)
at junit.extensions.TestSetup$1.protect(TestSetup.java:23)
at junit.extensions.TestSetup.run(TestSetup.java:27)
at junit.extensions.TestDecorator.basicRun(TestDecorator.java:23)
at junit.extensions.TestSetup$1.protect(TestSetup.java:23)
at junit.extensions.TestSetup.run(TestSetup.java:27)
at junit.extensions.TestDecorator.basicRun(TestDecorator.java:23)
at junit.extensions.TestSetup$1.protect(TestSetup.java:23)
at junit.extensions.TestSetup.run(TestSetup.java:27)
at org.eclipse.test.EclipseTestRunner.run(EclipseTestRunner.java:655)
at org.eclipse.test.EclipseTestRunner.run(EclipseTestRunner.java:310)
at org.eclipse.test.UITestApplication$2.run(UITestApplication.java:197)
at org.eclipse.swt.widgets.RunnableLock.run(RunnableLock.java:35)
at org.eclipse.swt.widgets.Synchronizer.runAsyncMessages(Synchronizer.java:135)
at org.eclipse.swt.widgets.Display.runAsyncMessages(Display.java:3976)
at org.eclipse.swt.widgets.Display.readAndDispatch(Display.java:3653)
at org.eclipse.e4.ui.internal.workbench.swt.PartRenderingEngine$9.run(PartRenderingEngine.java:1113)
at org.eclipse.core.databinding.observable.Realm.runWithDefault(Realm.java:332)
at org.eclipse.e4.ui.internal.workbench.swt.PartRenderingEngine.run(PartRenderingEngine.java:997)
at org.eclipse.e4.ui.internal.workbench.E4Workbench.createAndRunUI(E4Workbench.java:138)
at org.eclipse.ui.internal.Workbench$5.run(Workbench.java:610)
at org.eclipse.core.databinding.observable.Realm.runWithDefault(Realm.java:332)
at org.eclipse.ui.internal.Workbench.createAndRunWorkbench(Workbench.java:567)
at org.eclipse.ui.PlatformUI.createAndRunWorkbench(PlatformUI.java:150)
at org.eclipse.ui.internal.ide.application.IDEApplication.start(IDEApplication.java:124)
at org.eclipse.test.UITestApplication.runApplication(UITestApplication.java:140)
at org.eclipse.test.UITestApplication.run(UITestApplication.java:62)
at org.eclipse.test.UITestApplication.start(UITestApplication.java:212)
at org.eclipse.equinox.internal.app.EclipseAppHandle.run(EclipseAppHandle.java:196)
at org.eclipse.core.runtime.internal.adaptor.EclipseAppLauncher.runApplication(EclipseAppLauncher.java:110)
at org.eclipse.core.runtime.internal.adaptor.EclipseAppLauncher.start(EclipseAppLauncher.java:79)
at org.eclipse.core.runtime.adaptor.EclipseStarter.run(EclipseStarter.java:354)
at org.eclipse.core.runtime.adaptor.EclipseStarter.run(EclipseStarter.java:181)
at org.eclipse.equinox.launcher.Main.invokeFramework(Main.java:636)
at org.eclipse.equinox.launcher.Main.basicRun(Main.java:591)
at org.eclipse.equinox.launcher.Main.run(Main.java:1450)
at org.eclipse.equinox.launcher.Main.main(Main.java:1426)
at org.eclipse.core.launcher.Main.main(Main.java:34)


nls file expected:&lt;... static String Test_[]5; public static...&gt; but was:&lt;... static String Test_[3; public static String Test_4; public static String Test_]5; public static...&gt;

junit.framework.ComparisonFailure: nls file expected:&lt;... static String Test_[]5;
public static...&gt; but was:&lt;... static String Test_[3;
public static String Test_4;
public static String Test_]5;
public static...&gt;
at org.eclipse.jdt.ui.tests.quickfix.PropertiesFileQuickAssistTest.assertEqualLines(PropertiesFileQuickAssistTest.java:153)
at org.eclipse.jdt.ui.tests.quickfix.PropertiesFileQuickAssistTest.checkContentOfCu(PropertiesFileQuickAssistTest.java:124)
at org.eclipse.jdt.ui.tests.quickfix.PropertiesFileQuickAssistTest.testRemoveProperty4(PropertiesFileQuickAssistTest.java:709)
at junit.extensions.TestDecorator.basicRun(TestDecorator.java:23)
at junit.extensions.TestSetup$1.protect(TestSetup.java:23)
at junit.extensions.TestSetup.run(TestSetup.java:27)
at junit.extensions.TestDecorator.basicRun(TestDecorator.java:23)
at junit.extensions.TestSetup$1.protect(TestSetup.java:23)
at junit.extensions.TestSetup.run(TestSetup.java:27)
at junit.extensions.TestDecorator.basicRun(TestDecorator.java:23)
at junit.extensions.TestSetup$1.protect(TestSetup.java:23)
at junit.extensions.TestSetup.run(TestSetup.java:27)
at org.eclipse.test.EclipseTestRunner.run(EclipseTestRunner.java:655)
at org.eclipse.test.EclipseTestRunner.run(EclipseTestRunner.java:310)
at org.eclipse.test.UITestApplication$2.run(UITestApplication.java:197)
at org.eclipse.swt.widgets.RunnableLock.run(RunnableLock.java:35)
at org.eclipse.swt.widgets.Synchronizer.runAsyncMessages(Synchronizer.java:135)
at org.eclipse.swt.widgets.Display.runAsyncMessages(Display.java:3976)
at org.eclipse.swt.widgets.Display.readAndDispatch(Display.java:3653)
at org.eclipse.e4.ui.internal.workbench.swt.PartRenderingEngine$9.run(PartRenderingEngine.java:1113)
at org.eclipse.core.databinding.observable.Realm.runWithDefault(Realm.java:332)
at org.eclipse.e4.ui.internal.workbench.swt.PartRenderingEngine.run(PartRenderingEngine.java:997)
at org.eclipse.e4.ui.internal.workbench.E4Workbench.createAndRunUI(E4Workbench.java:138)
at org.eclipse.ui.internal.Workbench$5.run(Workbench.java:610)
at org.eclipse.core.databinding.observable.Realm.runWithDefault(Realm.java:332)
at org.eclipse.ui.internal.Workbench.createAndRunWorkbench(Workbench.java:567)
at org.eclipse.ui.PlatformUI.createAndRunWorkbench(PlatformUI.java:150)
at org.eclipse.ui.internal.ide.application.IDEApplication.start(IDEApplication.java:124)
at org.eclipse.test.UITestApplication.runApplication(UITestApplication.java:140)
at org.eclipse.test.UITestApplication.run(UITestApplication.java:62)
at org.eclipse.test.UITestApplication.start(UITestApplication.java:212)
at org.eclipse.equinox.internal.app.EclipseAppHandle.run(EclipseAppHandle.java:196)
at org.eclipse.core.runtime.internal.adaptor.EclipseAppLauncher.runApplication(EclipseAppLauncher.java:110)
at org.eclipse.core.runtime.internal.adaptor.EclipseAppLauncher.start(EclipseAppLauncher.java:79)
at org.eclipse.core.runtime.adaptor.EclipseStarter.run(EclipseStarter.java:354)
at org.eclipse.core.runtime.adaptor.EclipseStarter.run(EclipseStarter.java:181)
at org.eclipse.equinox.launcher.Main.invokeFramework(Main.java:636)
at org.eclipse.equinox.launcher.Main.basicRun(Main.java:591)
at org.eclipse.equinox.launcher.Main.run(Main.java:1450)
at org.eclipse.equinox.launcher.Main.main(Main.java:1426)
at org.eclipse.core.launcher.Main.main(Main.java:34)</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2267030</commentid>
    <comment_count>1</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-06-03 10:20:23 -0400</bug_when>
    <thetext>http://download.eclipse.org/eclipse/downloads/drops4/I20130531-2000/testresults/macosx.cocoa.x86_5.0/org.eclipse.jdt.ui.tests.AutomatedSuite.txt says the reason is that one of the files is out of sync with the local file system.

I can&apos;t explain why that could happen -- the tests only manipulate files through IFile and ICompilationUnit.

Closing this bug for now, since it didn&apos;t happen again in subsequent builds. May reopen if it turns out happen more often.


!ENTRY org.eclipse.jdt.ui 4 10001 2013-06-01 05:01:20.318
!MESSAGE Internal Error
!STACK 1
org.eclipse.core.runtime.CoreException: The file is not synchronized with the local file system.
	at org.eclipse.core.internal.filebuffers.ResourceTextFileBuffer.commitFileBufferContent(ResourceTextFileBuffer.java:338)
	at org.eclipse.core.internal.filebuffers.ResourceFileBuffer.commit(ResourceFileBuffer.java:325)
	at org.eclipse.ltk.core.refactoring.TextFileChange.commit(TextFileChange.java:233)
	at org.eclipse.ltk.core.refactoring.TextChange.perform(TextChange.java:240)
	at org.eclipse.ltk.core.refactoring.CompositeChange.perform(CompositeChange.java:278)
	at org.eclipse.jdt.ui.text.java.correction.ChangeCorrectionProposal.performChange(ChangeCorrectionProposal.java:185)
	at org.eclipse.jdt.ui.text.java.correction.ChangeCorrectionProposal.apply(ChangeCorrectionProposal.java:113)
	at org.eclipse.jdt.ui.tests.quickfix.PropertiesFileQuickAssistTest.testRemoveProperty3(PropertiesFileQuickAssistTest.java:626)
...</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2283208</commentid>
    <comment_count>2</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-07-11 05:13:21 -0400</bug_when>
    <thetext>PropertiesFileQuickAssistTest.testRemoveProperty2 failed again in N20130710-2000 - this time on Windows 7. This time, only a deletion failure was logged.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2283212</commentid>
    <comment_count>3</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-07-11 05:15:38 -0400</bug_when>
    <thetext>(In reply to comment #2)
&gt; PropertiesFileQuickAssistTest.testRemoveProperty2 failed again in
&gt; N20130710-2000 - this time on Windows 7. This time, only a deletion failure
&gt; was logged.

Other components also show unexpected failures, so, this was probably just a bad day for the build machine.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2339899</commentid>
    <comment_count>4</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-12-10 08:52:56 -0500</bug_when>
    <thetext>PropertiesFileQuickAssistTest.testRemoveProperty4 failed again on Windows 7:

http://download.eclipse.org/eclipse/downloads/drops4/I20131209-2000/testresults/html/org.eclipse.jdt.ui.tests_win32.win32.x86_7.0.html

This time, no other tests failed unexpectedly.


Wrong number of proposals, is: 0, expected: 1

junit.framework.AssertionFailedError: Wrong number of proposals, is: 0, expected: 1

at org.eclipse.jdt.ui.tests.quickfix.QuickFixTest.assertNumberOfProposals(QuickFixTest.java:436)
at org.eclipse.jdt.ui.tests.quickfix.PropertiesFileQuickAssistTest.testRemoveProperty4(PropertiesFileQuickAssistTest.java:687)
at junit.extensions.TestDecorator.basicRun(TestDecorator.java:23)
at junit.extensions.TestSetup$1.protect(TestSetup.java:23)
at junit.extensions.TestSetup.run(TestSetup.java:27)
at junit.extensions.TestDecorator.basicRun(TestDecorator.java:23)
at junit.extensions.TestSetup$1.protect(TestSetup.java:23)
at junit.extensions.TestSetup.run(TestSetup.java:27)
at junit.extensions.TestDecorator.basicRun(TestDecorator.java:23)
at junit.extensions.TestSetup$1.protect(TestSetup.java:23)
at junit.extensions.TestSetup.run(TestSetup.java:27)
at org.eclipse.test.EclipseTestRunner.run(EclipseTestRunner.java:657)
at org.eclipse.test.EclipseTestRunner.run(EclipseTestRunner.java:310)
at org.eclipse.test.UITestApplication$2.run(UITestApplication.java:197)
at org.eclipse.swt.widgets.RunnableLock.run(RunnableLock.java:35)
at org.eclipse.swt.widgets.Synchronizer.runAsyncMessages(Synchronizer.java:136)
at org.eclipse.swt.widgets.Display.runAsyncMessages(Display.java:4145)
at org.eclipse.swt.widgets.Display.readAndDispatch(Display.java:3762)
at org.eclipse.e4.ui.internal.workbench.swt.PartRenderingEngine$9.run(PartRenderingEngine.java:1122)
at org.eclipse.core.databinding.observable.Realm.runWithDefault(Realm.java:332)
at org.eclipse.e4.ui.internal.workbench.swt.PartRenderingEngine.run(PartRenderingEngine.java:1006)
at org.eclipse.e4.ui.internal.workbench.E4Workbench.createAndRunUI(E4Workbench.java:146)
at org.eclipse.ui.internal.Workbench$5.run(Workbench.java:611)
at org.eclipse.core.databinding.observable.Realm.runWithDefault(Realm.java:332)
at org.eclipse.ui.internal.Workbench.createAndRunWorkbench(Workbench.java:565)
at org.eclipse.ui.PlatformUI.createAndRunWorkbench(PlatformUI.java:150)
at org.eclipse.ui.internal.ide.application.IDEApplication.start(IDEApplication.java:125)
at org.eclipse.test.UITestApplication.runApplication(UITestApplication.java:140)
at org.eclipse.test.UITestApplication.run(UITestApplication.java:62)
at org.eclipse.test.UITestApplication.start(UITestApplication.java:212)
at org.eclipse.equinox.internal.app.EclipseAppHandle.run(EclipseAppHandle.java:196)
at org.eclipse.core.runtime.internal.adaptor.EclipseAppLauncher.runApplication(EclipseAppLauncher.java:109)
at org.eclipse.core.runtime.internal.adaptor.EclipseAppLauncher.start(EclipseAppLauncher.java:80)
at org.eclipse.core.runtime.adaptor.EclipseStarter.run(EclipseStarter.java:372)
at org.eclipse.core.runtime.adaptor.EclipseStarter.run(EclipseStarter.java:226)
at org.eclipse.equinox.launcher.Main.invokeFramework(Main.java:636)
at org.eclipse.equinox.launcher.Main.basicRun(Main.java:591)
at org.eclipse.equinox.launcher.Main.run(Main.java:1450)
at org.eclipse.equinox.launcher.Main.main(Main.java:1426)
at org.eclipse.core.launcher.Main.main(Main.java:34)</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2340126</commentid>
    <comment_count>5</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-12-10 14:33:10 -0500</bug_when>
    <thetext>The problem in testRemoveProperty4() is a race condition with PropertiesFileEditor#fAccessorTypes, which was added in bug 361535.

To reproduce, just add a breakpoint in PropertiesFileEditor.java:132

PropertiesFileEditor#getAccessorType() cannot assume the job is always done. It has to join fJob to be sure.

Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=e0bbf7568d196788ff118465b93f6463dcc2026b</thetext>
  </long_desc>
      
      

    </bug>
    <bug>
          <bug_id>409705</bug_id>
          
          <creation_ts>2013-06-03 05:23:00 -0400</creation_ts>
          <short_desc>IntroduceIndirectionTests.test31 fails with an error while deleting resources</short_desc>
          <delta_ts>2013-06-05 06:19:42 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>PC</rep_platform>
          <op_sys>Windows 7</op_sys>
          <bug_status>VERIFIED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords>test</keywords>
          <priority>P3</priority>
          <bug_severity>normal</bug_severity>
          <target_milestone>4.3 RC4</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Dani Megert">daniel_megert@ch.ibm.com</reporter>
          <assigned_to name="Markus Keller">markus_keller@ch.ibm.com</assigned_to>
          <cc>markus_keller@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706888-fz3fnjKapjmdM4CW3o0jb-rZixW-6hPn59KShKKx1E4</token>

      

      

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2266829</commentid>
    <comment_count>0</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-06-03 05:23:16 -0400</bug_when>
    <thetext>IntroduceIndirectionTests.test31 fails with an error while deleting resources.

http://download.eclipse.org/eclipse/downloads/drops4/I20130602-2000/testresults/html/org.eclipse.jdt.ui.tests.refactoring_win32.win32.x86_7.0.html


Problems encountered while deleting resources.

Java Model Exception: Core Exception [code 273] Problems encountered while deleting resources.
at org.eclipse.jdt.internal.core.MultiOperation.processElements(MultiOperation.java:175)
at org.eclipse.jdt.internal.core.MultiOperation.executeOperation(MultiOperation.java:90)
at org.eclipse.jdt.internal.core.JavaModelOperation.run(JavaModelOperation.java:728)
at org.eclipse.core.internal.resources.Workspace.run(Workspace.java:2345)
at org.eclipse.jdt.internal.core.JavaModelOperation.runOperation(JavaModelOperation.java:793)
at org.eclipse.jdt.internal.core.JavaModel.delete(JavaModel.java:135)
at org.eclipse.jdt.internal.core.CompilationUnit.delete(CompilationUnit.java:471)
at org.eclipse.jdt.ui.tests.refactoring.IntroduceIndirectionTests.helper(IntroduceIndirectionTests.java:122)
at org.eclipse.jdt.ui.tests.refactoring.IntroduceIndirectionTests.helperPass(IntroduceIndirectionTests.java:127)
at org.eclipse.jdt.ui.tests.refactoring.IntroduceIndirectionTests.test31(IntroduceIndirectionTests.java:306)
at junit.extensions.TestDecorator.basicRun(TestDecorator.java:23)
at junit.extensions.TestSetup$1.protect(TestSetup.java:23)
at junit.extensions.TestSetup.run(TestSetup.java:27)
at junit.extensions.TestDecorator.basicRun(TestDecorator.java:23)
at junit.extensions.TestSetup$1.protect(TestSetup.java:23)
at junit.extensions.TestSetup.run(TestSetup.java:27)
at org.eclipse.test.EclipseTestRunner.run(EclipseTestRunner.java:655)
at org.eclipse.test.EclipseTestRunner.run(EclipseTestRunner.java:310)
at org.eclipse.test.UITestApplication$2.run(UITestApplication.java:197)
at org.eclipse.swt.widgets.RunnableLock.run(RunnableLock.java:35)
at org.eclipse.swt.widgets.Synchronizer.runAsyncMessages(Synchronizer.java:135)
at org.eclipse.swt.widgets.Display.runAsyncMessages(Display.java:4145)
at org.eclipse.swt.widgets.Display.readAndDispatch(Display.java:3762)
at org.eclipse.e4.ui.internal.workbench.swt.PartRenderingEngine$9.run(PartRenderingEngine.java:1113)
at org.eclipse.core.databinding.observable.Realm.runWithDefault(Realm.java:332)
at org.eclipse.e4.ui.internal.workbench.swt.PartRenderingEngine.run(PartRenderingEngine.java:997)
at org.eclipse.e4.ui.internal.workbench.E4Workbench.createAndRunUI(E4Workbench.java:138)
at org.eclipse.ui.internal.Workbench$5.run(Workbench.java:610)
at org.eclipse.core.databinding.observable.Realm.runWithDefault(Realm.java:332)
at org.eclipse.ui.internal.Workbench.createAndRunWorkbench(Workbench.java:567)
at org.eclipse.ui.PlatformUI.createAndRunWorkbench(PlatformUI.java:150)
at org.eclipse.ui.internal.ide.application.IDEApplication.start(IDEApplication.java:124)
at org.eclipse.test.UITestApplication.runApplication(UITestApplication.java:140)
at org.eclipse.test.UITestApplication.run(UITestApplication.java:62)
at org.eclipse.test.UITestApplication.start(UITestApplication.java:212)
at org.eclipse.equinox.internal.app.EclipseAppHandle.run(EclipseAppHandle.java:196)
at org.eclipse.core.runtime.internal.adaptor.EclipseAppLauncher.runApplication(EclipseAppLauncher.java:110)
at org.eclipse.core.runtime.internal.adaptor.EclipseAppLauncher.start(EclipseAppLauncher.java:79)
at org.eclipse.core.runtime.adaptor.EclipseStarter.run(EclipseStarter.java:354)
at org.eclipse.core.runtime.adaptor.EclipseStarter.run(EclipseStarter.java:181)
at org.eclipse.equinox.launcher.Main.invokeFramework(Main.java:636)
at org.eclipse.equinox.launcher.Main.basicRun(Main.java:591)
at org.eclipse.equinox.launcher.Main.run(Main.java:1450)
at org.eclipse.equinox.launcher.Main.main(Main.java:1426)
at org.eclipse.core.launcher.Main.main(Main.java:34)
Caused by: org.eclipse.core.internal.resources.ResourceException: Problems encountered while deleting resources.
at org.eclipse.core.internal.resources.Resource.delete(Resource.java:816)
at org.eclipse.jdt.internal.core.JavaModelOperation.deleteResource(JavaModelOperation.java:331)
at org.eclipse.jdt.internal.core.DeleteResourceElementsOperation.processElement(DeleteResourceElementsOperation.java:107)
at org.eclipse.jdt.internal.core.MultiOperation.processElements(MultiOperation.java:163)
Caused by: org.eclipse.core.internal.resources.ResourceException: Problems encountered while deleting resources.
at org.eclipse.core.internal.resources.Resource.delete(Resource.java:816)
at org.eclipse.jdt.internal.core.JavaModelOperation.deleteResource(JavaModelOperation.java:331)
at org.eclipse.jdt.internal.core.DeleteResourceElementsOperation.processElement(DeleteResourceElementsOperation.java:107)
at org.eclipse.jdt.internal.core.MultiOperation.processElements(MultiOperation.java:163)
at org.eclipse.jdt.internal.core.MultiOperation.executeOperation(MultiOperation.java:90)
at org.eclipse.jdt.internal.core.JavaModelOperation.run(JavaModelOperation.java:728)
at org.eclipse.core.internal.resources.Workspace.run(Workspace.java:2345)
at org.eclipse.jdt.internal.core.JavaModelOperation.runOperation(JavaModelOperation.java:793)
at org.eclipse.jdt.internal.core.JavaModel.delete(JavaModel.java:135)
at org.eclipse.jdt.internal.core.CompilationUnit.delete(CompilationUnit.java:471)
at org.eclipse.jdt.ui.tests.refactoring.IntroduceIndirectionTests.helper(IntroduceIndirectionTests.java:122)
at org.eclipse.jdt.ui.tests.refactoring.IntroduceIndirectionTests.helperPass(IntroduceIndirectionTests.java:127)
at org.eclipse.jdt.ui.tests.refactoring.IntroduceIndirectionTests.test31(IntroduceIndirectionTests.java:306)
at junit.extensions.TestDecorator.basicRun(TestDecorator.java:23)
at junit.extensions.TestSetup$1.protect(TestSetup.java:23)
at junit.extensions.TestSetup.run(TestSetup.java:27)
at junit.extensions.TestDecorator.basicRun(TestDecorator.java:23)
at junit.extensions.TestSetup$1.protect(TestSetup.java:23)
at junit.extensions.TestSetup.run(TestSetup.java:27)
at org.eclipse.test.EclipseTestRunner.run(EclipseTestRunner.java:655)
at org.eclipse.test.EclipseTestRunner.run(EclipseTestRunner.java:310)
at org.eclipse.test.UITestApplication$2.run(UITestApplication.java:197)
at org.eclipse.swt.widgets.RunnableLock.run(RunnableLock.java:35)
at org.eclipse.swt.widgets.Synchronizer.runAsyncMessages(Synchronizer.java:135)
at org.eclipse.swt.widgets.Display.runAsyncMessages(Display.java:4145)
at org.eclipse.swt.widgets.Display.readAndDispatch(Display.java:3762)
at org.eclipse.e4.ui.internal.workbench.swt.PartRenderingEngine$9.run(PartRenderingEngine.java:1113)
at org.eclipse.core.databinding.observable.Realm.runWithDefault(Realm.java:332)
at org.eclipse.e4.ui.internal.workbench.swt.PartRenderingEngine.run(PartRenderingEngine.java:997)
at org.eclipse.e4.ui.internal.workbench.E4Workbench.createAndRunUI(E4Workbench.java:138)
at org.eclipse.ui.internal.Workbench$5.run(Workbench.java:610)
at org.eclipse.core.databinding.observable.Realm.runWithDefault(Realm.java:332)
at org.eclipse.ui.internal.Workbench.createAndRunWorkbench(Workbench.java:567)
at org.eclipse.ui.PlatformUI.createAndRunWorkbench(PlatformUI.java:150)
at org.eclipse.ui.internal.ide.application.IDEApplication.start(IDEApplication.java:124)
at org.eclipse.test.UITestApplication.runApplication(UITestApplication.java:140)
at org.eclipse.test.UITestApplication.run(UITestApplication.java:62)
at org.eclipse.test.UITestApplication.start(UITestApplication.java:212)
at org.eclipse.equinox.internal.app.EclipseAppHandle.run(EclipseAppHandle.java:196)
at org.eclipse.core.runtime.internal.adaptor.EclipseAppLauncher.runApplication(EclipseAppLauncher.java:110)
at org.eclipse.core.runtime.internal.adaptor.EclipseAppLauncher.start(EclipseAppLauncher.java:79)
at org.eclipse.core.runtime.adaptor.EclipseStarter.run(EclipseStarter.java:354)
at org.eclipse.core.runtime.adaptor.EclipseStarter.run(EclipseStarter.java:181)
at org.eclipse.equinox.launcher.Main.invokeFramework(Main.java:636)
at org.eclipse.equinox.launcher.Main.basicRun(Main.java:591)
at org.eclipse.equinox.launcher.Main.run(Main.java:1450)
at org.eclipse.equinox.launcher.Main.main(Main.java:1426)
at org.eclipse.core.launcher.Main.main(Main.java:34)
Contains: Could not delete &apos;C:\hb\workspace\ep4-unit-win32\workarea\I20130602-2000\eclipse-testing\test-eclipse\eclipse\refactoring_folder\TestProject1370245576152\src\p\Test.java&apos;.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2267019</commentid>
    <comment_count>1</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-06-03 10:04:41 -0400</bug_when>
    <thetext>Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=0ac85d526d67ab00390c45fd46510e10c157ba19</thetext>
  </long_desc>
      
      

    </bug>
    <bug>
          <bug_id>409704</bug_id>
          
          <creation_ts>2013-06-03 05:21:00 -0400</creation_ts>
          <short_desc>MoveInnerToTopLevelTests.test25 throws error during tearDown</short_desc>
          <delta_ts>2013-06-05 06:19:46 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>PC</rep_platform>
          <op_sys>Windows 7</op_sys>
          <bug_status>VERIFIED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords>test</keywords>
          <priority>P3</priority>
          <bug_severity>normal</bug_severity>
          <target_milestone>4.3 RC4</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Dani Megert">daniel_megert@ch.ibm.com</reporter>
          <assigned_to name="Markus Keller">markus_keller@ch.ibm.com</assigned_to>
          <cc>markus_keller@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706888-EzQReYznfCJ0gjg8rCpsVurenBWz5dwJp29eYKEA7R4</token>

      

      

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2266827</commentid>
    <comment_count>0</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-06-03 05:21:39 -0400</bug_when>
    <thetext>MoveInnerToTopLevelTests.test25 throws error during tearDown because it can&apos;t delete some resource.

test26 then probably fails due to this.


http://download.eclipse.org/eclipse/downloads/drops4/I20130602-2000/testresults/html/org.eclipse.jdt.ui.tests.refactoring_win32.win32.x86_7.0.html


Problems encountered while deleting resources.

Java Model Exception: Core Exception [code 566] Problems encountered while deleting resources.
at org.eclipse.jdt.internal.core.MultiOperation.processElements(MultiOperation.java:175)
at org.eclipse.jdt.internal.core.MultiOperation.executeOperation(MultiOperation.java:90)
at org.eclipse.jdt.internal.core.JavaModelOperation.run(JavaModelOperation.java:728)
at org.eclipse.core.internal.resources.Workspace.run(Workspace.java:2345)
at org.eclipse.jdt.internal.core.JavaModelOperation.runOperation(JavaModelOperation.java:793)
at org.eclipse.jdt.internal.core.JavaModel.delete(JavaModel.java:135)
at org.eclipse.jdt.internal.core.PackageFragment.delete(PackageFragment.java:158)
at org.eclipse.jdt.ui.tests.refactoring.RefactoringTest.tearDown(RefactoringTest.java:141)
at org.eclipse.jdt.ui.tests.refactoring.MoveInnerToTopLevelTests.tearDown(MoveInnerToTopLevelTests.java:85)
at junit.extensions.TestDecorator.basicRun(TestDecorator.java:23)
at junit.extensions.TestSetup$1.protect(TestSetup.java:23)
at junit.extensions.TestSetup.run(TestSetup.java:27)
at junit.extensions.TestDecorator.basicRun(TestDecorator.java:23)
at junit.extensions.TestSetup$1.protect(TestSetup.java:23)
at junit.extensions.TestSetup.run(TestSetup.java:27)
at org.eclipse.test.EclipseTestRunner.run(EclipseTestRunner.java:655)
at org.eclipse.test.EclipseTestRunner.run(EclipseTestRunner.java:310)
at org.eclipse.test.UITestApplication$2.run(UITestApplication.java:197)
at org.eclipse.swt.widgets.RunnableLock.run(RunnableLock.java:35)
at org.eclipse.swt.widgets.Synchronizer.runAsyncMessages(Synchronizer.java:135)
at org.eclipse.swt.widgets.Display.runAsyncMessages(Display.java:4145)
at org.eclipse.swt.widgets.Display.readAndDispatch(Display.java:3762)
at org.eclipse.e4.ui.internal.workbench.swt.PartRenderingEngine$9.run(PartRenderingEngine.java:1113)
at org.eclipse.core.databinding.observable.Realm.runWithDefault(Realm.java:332)
at org.eclipse.e4.ui.internal.workbench.swt.PartRenderingEngine.run(PartRenderingEngine.java:997)
at org.eclipse.e4.ui.internal.workbench.E4Workbench.createAndRunUI(E4Workbench.java:138)
at org.eclipse.ui.internal.Workbench$5.run(Workbench.java:610)
at org.eclipse.core.databinding.observable.Realm.runWithDefault(Realm.java:332)
at org.eclipse.ui.internal.Workbench.createAndRunWorkbench(Workbench.java:567)
at org.eclipse.ui.PlatformUI.createAndRunWorkbench(PlatformUI.java:150)
at org.eclipse.ui.internal.ide.application.IDEApplication.start(IDEApplication.java:124)
at org.eclipse.test.UITestApplication.runApplication(UITestApplication.java:140)
at org.eclipse.test.UITestApplication.run(UITestApplication.java:62)
at org.eclipse.test.UITestApplication.start(UITestApplication.java:212)
at org.eclipse.equinox.internal.app.EclipseAppHandle.run(EclipseAppHandle.java:196)
at org.eclipse.core.runtime.internal.adaptor.EclipseAppLauncher.runApplication(EclipseAppLauncher.java:110)
at org.eclipse.core.runtime.internal.adaptor.EclipseAppLauncher.start(EclipseAppLauncher.java:79)
at org.eclipse.core.runtime.adaptor.EclipseStarter.run(EclipseStarter.java:354)
at org.eclipse.core.runtime.adaptor.EclipseStarter.run(EclipseStarter.java:181)
at org.eclipse.equinox.launcher.Main.invokeFramework(Main.java:636)
at org.eclipse.equinox.launcher.Main.basicRun(Main.java:591)
at org.eclipse.equinox.launcher.Main.run(Main.java:1450)
at org.eclipse.equinox.launcher.Main.main(Main.java:1426)
at org.eclipse.core.launcher.Main.main(Main.java:34)
Caused by: org.eclipse.core.internal.resources.ResourceException: Problems encountered while deleting resources.
at org.eclipse.core.internal.resources.Workspace.delete(Workspace.java:1441)
at org.eclipse.jdt.internal.core.JavaModelOperation.deleteResources(JavaModelOperation.java:345)
at org.eclipse.jdt.internal.core.DeleteResourceElementsOperation.deletePackageFragment(DeleteResourceElementsOperation.java:53)
at org.eclipse.jdt.internal.core.DeleteResourceElementsOperation.processElement(DeleteResourceElementsOperation.java:110)
at org.eclipse.jdt.internal.core.MultiOperation.processElements(MultiOperation.java:163)
Caused by: org.eclipse.core.internal.resources.ResourceException: Problems encountered while deleting resources.
at org.eclipse.core.internal.resources.Workspace.delete(Workspace.java:1441)
at org.eclipse.jdt.internal.core.JavaModelOperation.deleteResources(JavaModelOperation.java:345)
at org.eclipse.jdt.internal.core.DeleteResourceElementsOperation.deletePackageFragment(DeleteResourceElementsOperation.java:53)
at org.eclipse.jdt.internal.core.DeleteResourceElementsOperation.processElement(DeleteResourceElementsOperation.java:110)
at org.eclipse.jdt.internal.core.MultiOperation.processElements(MultiOperation.java:163)
at org.eclipse.jdt.internal.core.MultiOperation.executeOperation(MultiOperation.java:90)
at org.eclipse.jdt.internal.core.JavaModelOperation.run(JavaModelOperation.java:728)
at org.eclipse.core.internal.resources.Workspace.run(Workspace.java:2345)
at org.eclipse.jdt.internal.core.JavaModelOperation.runOperation(JavaModelOperation.java:793)
at org.eclipse.jdt.internal.core.JavaModel.delete(JavaModel.java:135)
at org.eclipse.jdt.internal.core.PackageFragment.delete(PackageFragment.java:158)
at org.eclipse.jdt.ui.tests.refactoring.RefactoringTest.tearDown(RefactoringTest.java:141)
at org.eclipse.jdt.ui.tests.refactoring.MoveInnerToTopLevelTests.tearDown(MoveInnerToTopLevelTests.java:85)
at junit.extensions.TestDecorator.basicRun(TestDecorator.java:23)
at junit.extensions.TestSetup$1.protect(TestSetup.java:23)
at junit.extensions.TestSetup.run(TestSetup.java:27)
at junit.extensions.TestDecorator.basicRun(TestDecorator.java:23)
at junit.extensions.TestSetup$1.protect(TestSetup.java:23)
at junit.extensions.TestSetup.run(TestSetup.java:27)
at org.eclipse.test.EclipseTestRunner.run(EclipseTestRunner.java:655)
at org.eclipse.test.EclipseTestRunner.run(EclipseTestRunner.java:310)
at org.eclipse.test.UITestApplication$2.run(UITestApplication.java:197)
at org.eclipse.swt.widgets.RunnableLock.run(RunnableLock.java:35)
at org.eclipse.swt.widgets.Synchronizer.runAsyncMessages(Synchronizer.java:135)
at org.eclipse.swt.widgets.Display.runAsyncMessages(Display.java:4145)
at org.eclipse.swt.widgets.Display.readAndDispatch(Display.java:3762)
at org.eclipse.e4.ui.internal.workbench.swt.PartRenderingEngine$9.run(PartRenderingEngine.java:1113)
at org.eclipse.core.databinding.observable.Realm.runWithDefault(Realm.java:332)
at org.eclipse.e4.ui.internal.workbench.swt.PartRenderingEngine.run(PartRenderingEngine.java:997)
at org.eclipse.e4.ui.internal.workbench.E4Workbench.createAndRunUI(E4Workbench.java:138)
at org.eclipse.ui.internal.Workbench$5.run(Workbench.java:610)
at org.eclipse.core.databinding.observable.Realm.runWithDefault(Realm.java:332)
at org.eclipse.ui.internal.Workbench.createAndRunWorkbench(Workbench.java:567)
at org.eclipse.ui.PlatformUI.createAndRunWorkbench(PlatformUI.java:150)
at org.eclipse.ui.internal.ide.application.IDEApplication.start(IDEApplication.java:124)
at org.eclipse.test.UITestApplication.runApplication(UITestApplication.java:140)
at org.eclipse.test.UITestApplication.run(UITestApplication.java:62)
at org.eclipse.test.UITestApplication.start(UITestApplication.java:212)
at org.eclipse.equinox.internal.app.EclipseAppHandle.run(EclipseAppHandle.java:196)
at org.eclipse.core.runtime.internal.adaptor.EclipseAppLauncher.runApplication(EclipseAppLauncher.java:110)
at org.eclipse.core.runtime.internal.adaptor.EclipseAppLauncher.start(EclipseAppLauncher.java:79)
at org.eclipse.core.runtime.adaptor.EclipseStarter.run(EclipseStarter.java:354)
at org.eclipse.core.runtime.adaptor.EclipseStarter.run(EclipseStarter.java:181)
at org.eclipse.equinox.launcher.Main.invokeFramework(Main.java:636)
at org.eclipse.equinox.launcher.Main.basicRun(Main.java:591)
at org.eclipse.equinox.launcher.Main.run(Main.java:1450)
at org.eclipse.equinox.launcher.Main.main(Main.java:1426)
at org.eclipse.core.launcher.Main.main(Main.java:34)
Contains: Could not delete &apos;/TestProject1370245265306/src/A.java&apos;.
Contains: Could not delete &apos;C:\hb\workspace\ep4-unit-win32\workarea\I20130602-2000\eclipse-testing\test-eclipse\eclipse\refactoring_folder\TestProject1370245265306\src\A.java&apos;.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2267012</commentid>
    <comment_count>1</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-06-03 09:59:29 -0400</bug_when>
    <thetext>Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=8029c94ba8f0cb368deb09e3b2f19467d14ad8ed</thetext>
  </long_desc>
      
      

    </bug>
    <bug>
          <bug_id>409596</bug_id>
          
          <creation_ts>2013-05-31 10:16:00 -0400</creation_ts>
          <short_desc>[1.8][refactoring] UI refactorings affected by lack of TYPE_USE annotations in ITypeBindings</short_desc>
          <delta_ts>2014-02-21 02:12:33 -0500</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>VERIFIED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P2</priority>
          <bug_severity>normal</bug_severity>
          <target_milestone>BETA J8</target_milestone>
          <dependson>409586</dependson>
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Manju Mathew">manju656@gmail.com</reporter>
          <assigned_to name="JDT-UI-Inbox">jdt-ui-inbox@eclipse.org</assigned_to>
          <cc>markus_keller@ch.ibm.com</cc>
    
    <cc>noopur_gupta@in.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706888-L1tuMa2d7U06jAxhpBXKzCAd150KaE0GcXp69d28bXQ</token>

      

      

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2266248</commentid>
    <comment_count>0</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-05-31 10:16:56 -0400</bug_when>
    <thetext>Below are the UI refactorings affected by bug 409586.
1 =&gt; Move Method refactoring
Step 1:  Consider the method:
public void foo(java.io.@NonNull FileNotFoundException arg, AnnotatedType type)
			throws java.io.@NonNull EOFException {
}
Step 2: Invoke Refactoring&gt; Move on foo. Resultant method is shown below:

public void foo(FileNotFoundException arg)
			throws java.io.@NonNull EOFException {
}
Note that the method argument after move is just a SimpleType and not a PackageQualifiedType. This is because in MoveInstanceMethodProcessor#createMethodArguments(...)#getArgumentNode(...), we create a SimpleType from the TypeBinding. Here we need a mechanism to identify PackageQualifiedType/SimpleType from the given TypeBinding.


2 =&gt; Change Method Signature refactoring
Step 1:  Consider the method:
public void foo(java.io.@NonNull FileNotFoundException arg, AnnotatedType type)
			throws java.io.@NonNull EOFException {
}
Step 2: Invoke Refactoring&gt; Change Method Signature on foo. In the first page of the &apos;Change Method Signature&apos; wizard, the &apos;Method signature preview:&apos; shows the method arguments and the throws clause as SimpleType and not PackageQualifiedType as shown below:
public void foo(FileNotFoundException arg, AnnotatedType type) throws EOFException

We will update this bug as and when new issues with TYPE_USE annotation in the context of ITypeBinding is encountered in UI.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2266262</commentid>
    <comment_count>1</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-05-31 10:28:17 -0400</bug_when>
    <thetext>&gt; Here we need a mechanism to
&gt; identify PackageQualifiedType/SimpleType from the given TypeBinding.

An alternative (similar to the &quot;shallow encoding&quot; from bug 409586 comment 1) could be to pass the original org.eclipse.jdt.core.dom.Type around and insert the annotations into the Type returned by ImportRewrite#addImport(ITypeBinding, AST). But in general, this becomes complicated due to the &quot;extra dimensions&quot; syntax, and because the ITypeBinding can also be resolved from an Expression node, where a declaring Type node may not be available at all.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2267449</commentid>
    <comment_count>2</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-06-04 02:56:39 -0400</bug_when>
    <thetext>&apos;Introduce Indirection&apos; is another UI refactoring where PackageQualifiedType is not honored:

       public void foo( java.io.@NonNull FileNotFoundException arg)
			throws java.io.@NonNull EOFException {
		try {
			System.out.println(&quot;test&quot;);
		} catch ( java.io.@NonNull IOError e) {
		}
	}

Invoke &apos;Introduce Indirection&apos; on &apos;foo&apos;.
After the refactoring, the new method signature does not preserve the package qualified type and TYPE_USE annotation associated to the original method.
IntroduceIndirectionRefactoring# createIntermediaryMethod()</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2268100</commentid>
    <comment_count>3</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-06-05 01:22:43 -0400</bug_when>
    <thetext>(In reply to comment #0)

&gt; 2 =&gt; Change Method Signature refactoring
&gt; Step 1:  Consider the method:
&gt; public void foo(java.io.@NonNull FileNotFoundException arg, AnnotatedType
&gt; type)
&gt; 			throws java.io.@NonNull EOFException {
&gt; }
Method signature preview is computed from Java Model and not from AST, hence the above issue can be addressed in bug 405843, which deals with support type annotations in Java Model.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2365256</commentid>
    <comment_count>4</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2014-02-18 23:38:13 -0500</bug_when>
    <thetext>The issues reported in this bug are resolved when bug 409586 was fixed. Hence closing this bug.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2366507</commentid>
    <comment_count>5</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2014-02-21 02:12:33 -0500</bug_when>
    <thetext>Verified for Eclipse + Java 8 RC1 using Kepler SR2(RC4) +   
Eclipse Java Development Tools Patch for Java 8 Support (BETA)	
1.0.0.v20140220-2054.

The type use annotations are being preserved in the examples given in the bug report.

Regarding comment #3, we still do not see the type annotations in method signature preview.</thetext>
  </long_desc>
      
      

    </bug>
    <bug>
          <bug_id>409520</bug_id>
          
          <creation_ts>2013-05-30 12:58:00 -0400</creation_ts>
          <short_desc>[1.8][quick fix] &quot;Add unimplemented methods&quot; should not create stubs for default methods</short_desc>
          <delta_ts>2013-08-08 09:57:40 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>VERIFIED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>normal</bug_severity>
          <target_milestone>4.3.1</target_milestone>
          <dependson>403924</dependson>
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Markus Keller">markus_keller@ch.ibm.com</reporter>
          <assigned_to name="Manju Mathew">manju656@gmail.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>manju656@gmail.com</cc>
    
    <cc>noopur_gupta@in.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706889-v_SlqQ7_xl2MWSL_syCqNOLEfEU9xTBpx57w_Eii7YY</token>

      

      <flag name="review"
          id="58909"
          type_id="1"
          status="+"
          setter="daniel_megert@ch.ibm.com"
    />

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2265695</commentid>
    <comment_count>0</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-05-30 12:58:01 -0400</bug_when>
    <thetext>BETA_JAVA8 and master

The &quot;Add unimplemented methods&quot; quick fix should not create stubs for default methods.

public class MyString implements CharSequence {
}

=&gt; When compiling against a 1.8 JRE, the quick fix also adds stubs for chars() and codePoints(), which are new default methods in CharSequence.

&quot;Source &gt; Override/Implement Methods&quot; already looks good (only selects abstract methods).</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2265696</commentid>
    <comment_count>1</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-05-30 12:58:58 -0400</bug_when>
    <thetext>Tentatively targeting 4.3.1.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2271701</commentid>
    <comment_count>2</comment_count>
      <attachid>232274</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-06-12 05:26:04 -0400</bug_when>
    <thetext>Created attachment 232274
Patch with testcases.

With this patch only abstract method stubs will be created during the &quot;Add unimplemented methods&quot; quick fix. Added 2 testcases for this scenario.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2271705</commentid>
    <comment_count>3</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-06-12 05:31:31 -0400</bug_when>
    <thetext>Marking it as dependent on bug 403924 as StubUtility2 has 2 instances where it uses #thrownExceptions.

@Noopur, can you review the patch and give an initial feedback?</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2271732</commentid>
    <comment_count>4</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-06-12 06:44:53 -0400</bug_when>
    <thetext>*** Bug 406277 has been marked as a duplicate of this bug. ***</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2272249</commentid>
    <comment_count>5</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-06-13 02:09:04 -0400</bug_when>
    <thetext>(In reply to comment #3) 
&gt; @Noopur, can you review the patch and give an initial feedback?

The patch looks good. It covers both default and static methods of interface, by allowing only abstract methods to be added for implementation.

In the tests, JavaProjectHelper#addRTJar18 should call set18CompilerOptions(IJavaProject) instead of #set17CompilerOptions.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2287849</commentid>
    <comment_count>6</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-07-24 09:52:59 -0400</bug_when>
    <thetext>Fixed in &apos;master&apos; with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=100ddaa5694f03a7e942ff937ac9ff1e157c43b3 (without the 1.8 tests).

Fixed in &apos;R4_3_maintenance&apos; with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=98840432b7dc09315cd0db1bfa67b184698b24a3 (without the 1.8 tests).

Fixed in &apos;BETA_JAVA8&apos; with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=74903cbca471e4ba0e503ada3a029c76046b5fcf (with tests).</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2291462</commentid>
    <comment_count>7</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-08-05 06:08:50 -0400</bug_when>
    <thetext>Verified in 4.4 using Build id: I20130804-2300 and verified for 4.3.1 using
Build id: M20130731-0800.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2292759</commentid>
    <comment_count>8</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-08-08 09:57:40 -0400</bug_when>
    <thetext>Marking as verified as indicated in comment 7.</thetext>
  </long_desc>
      
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>232274</attachid>
            <date>2013-06-12 05:26:00 -0400</date>
            <delta_ts>2013-06-12 05:26:04 -0400</delta_ts>
            <desc>Patch with testcases.</desc>
            <filename>eclipse.jdt.ui.patch</filename>
            <type>text/plain</type>
            <size>14450</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706889-8n9YVyrxiKXxkYCtEVAIqJH3I0Qhej3P3B7or-JEokU</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>409275</bug_id>
          
          <creation_ts>2013-05-28 08:28:00 -0400</creation_ts>
          <short_desc>[1.8] Change &apos;default&apos; access modifier in dialogs related to methods</short_desc>
          <delta_ts>2013-06-04 07:02:50 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>PC</rep_platform>
          <op_sys>Windows 7</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>enhancement</bug_severity>
          <target_milestone>BETA J8</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Noopur Gupta">noopur_gupta@in.ibm.com</reporter>
          <assigned_to name="Noopur Gupta">noopur_gupta@in.ibm.com</assigned_to>
          <cc>manju656@gmail.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706889-uNCU8pbu5iCCmyoVWU3VwljzBjDDooTH4swvWTdTf4Y</token>

      

      <flag name="review"
          id="58166"
          type_id="1"
          status="+"
          setter="manju656@gmail.com"
    />

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2264181</commentid>
    <comment_count>0</comment_count>
      <attachid>231612</attachid>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-05-28 08:28:08 -0400</bug_when>
    <thetext>Created attachment 231612
Screenshot - &apos;default&apos; in Extract Method dialog

As per JSR 335 Part H and bug 401223:
&quot;To avoid confusion with the default modifier, the access level given implicitly to unmodified declarations in classes is now referred to as package access rather than default access;&quot;

The access modifier &apos;default&apos; used in different dialogs related to methods (like Extract Method, Change Method Signature), could now be changed to &apos;package-access&apos; or something else to avoid confusion with the modifier &apos;default&apos; used to declare a default method.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2264234</commentid>
    <comment_count>1</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-05-28 09:26:00 -0400</bug_when>
    <thetext>Good catch. Please make a pass over the whole JDT UI and replace &apos;default&apos; access with &apos;package&apos; access everywhere in the UI. E.g. in the dialogs, the access modifier should be called &apos;package&apos; (not &apos;package-access&apos;).

Don&apos;t touch identifiers in our code at this time. In new code, we will use &apos;package&apos; in identifiers, but it&apos;s not worth the hassle if we rename APIs or even internal helper methods. Also make sure you don&apos;t touch unrelated occurrences of the term &apos;default&apos;, e.g. in &apos;(default package)&apos;.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2265079</commentid>
    <comment_count>2</comment_count>
      <attachid>231715</attachid>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-05-29 13:06:48 -0400</bug_when>
    <thetext>Created attachment 231715
Patch

Replaced &apos;default&apos; with &apos;package&apos; everywhere in the UI, taking care of the points mentioned in comment #1.

Markus, please review.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2265100</commentid>
    <comment_count>3</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-05-29 13:35:31 -0400</bug_when>
    <thetext>Please have a look at the mnemonics again. You e.g. changed

    SelfEncapsulateFieldInputPage_default=defa&amp;ult

to packag&amp;e, but the &quot;&amp;e&quot; is not free.

The case in NewTypeWizardPage is quite tricky. Hint: You can trade the &quot;&amp;u&quot; for a &quot;&amp;c&quot; from &quot;&amp;Constructors from superclass&quot;.


I found more occurrences that need to be updated, e.g. 
56: NLSAccessorConfigurationDialog_default= (default) 
636: MembersOrderPreferencePage_default_label=Default 

Please do File Search for regex &quot;d&amp;?e&amp;?f&amp;?a&amp;?u&amp;?l&amp;?t&quot; in *.properties files again and check occurrences in code, unless the label clearly rules out a match (hint: Ctrl+Click in the *.properties file should take you to the referencing code).

After this is done, please let Manju review the new patch and then release it to BETA_JAVA8.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2266130</commentid>
    <comment_count>4</comment_count>
      <attachid>231798</attachid>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-05-31 06:36:08 -0400</bug_when>
    <thetext>Created attachment 231798
Patch

(In reply to comment #3)
&gt; Please have a look at the mnemonics again. You e.g. changed
&gt;     SelfEncapsulateFieldInputPage_default=defa&amp;ult
&gt; to packag&amp;e, but the &quot;&amp;e&quot; is not free.
Used &quot;&amp;a&quot;, which was available.

&gt; The case in NewTypeWizardPage is quite tricky. Hint: You can trade the &quot;&amp;u&quot;
&gt; for a &quot;&amp;c&quot; from &quot;&amp;Constructors from superclass&quot;.
Thanks for the hint.
 
&gt; 56: NLSAccessorConfigurationDialog_default= (default) 
This is not updated as it represents the &apos;(default)&apos; label next to the package field in dialog. 
Same with, 91: NewTypeWizardPage_default=(default)

&gt; 636: MembersOrderPreferencePage_default_label=Default 
Done. 
Also updated, 502: JavadocProblemsConfigurationBlock_default=Default
These were missed as I did a case sensitive search earlier.

Attached the patch with changes. Manju, Please review.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2267077</commentid>
    <comment_count>5</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-06-03 11:03:02 -0400</bug_when>
    <thetext>The patch has updated all the relevant occurrence of &apos;default&apos; with &apos;package&apos;. One point found is in the new type creation wizard, if user enable &apos;Enclosing type&apos;, then below mnemonics are being shared:
1. pa&amp;ckage / stati&amp;c =&gt; c
2. pro&amp;tected / abs&amp;tract =&gt; t
3. pri&amp;vate / public static &amp;void main =&gt; v

We need to do one more cycle of round robin and find the right mnemonics for each of them.

Otherwise the patch looks good to go.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2267572</commentid>
    <comment_count>6</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-06-04 06:51:05 -0400</bug_when>
    <thetext>(In reply to comment #5)
Thanks Manju. 

As discussed, the above mnemonics are shared only when we enable &apos;Enclosing type&apos; and also there is no other letter that could be used here. 
And since it is still possible to use the same mnemonic to access the shared fields, we will keep it as it is.

Released the patch with:
http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?h=BETA_JAVA8&amp;id=ba1353abd4c1954150f73ef66764d2e3badfed42</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2267574</commentid>
    <comment_count>7</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-06-04 06:59:27 -0400</bug_when>
    <thetext>.</thetext>
  </long_desc>
      
          <attachment
              isobsolete="0"
              ispatch="0"
              isprivate="0"
          >
            <attachid>231612</attachid>
            <date>2013-05-28 08:28:00 -0400</date>
            <delta_ts>2013-05-28 08:28:08 -0400</delta_ts>
            <desc>Screenshot - &apos;default&apos; in Extract Method dialog</desc>
            <filename>Image.PNG</filename>
            <type>image/png</type>
            <size>54471</size>
            <attacher name="Noopur Gupta">noopur_gupta@in.ibm.com</attacher>
            
              <token>1425706889-na5FSHsFiww865fG3gREaZukiQeTbuCEe7SQUC2DbDU</token>

          </attachment>
          <attachment
              isobsolete="1"
              ispatch="1"
              isprivate="0"
          >
            <attachid>231715</attachid>
            <date>2013-05-29 13:06:00 -0400</date>
            <delta_ts>2013-05-31 06:36:08 -0400</delta_ts>
            <desc>Patch</desc>
            <filename>Bug-409275--18-Change-default-access-modifier-.patch</filename>
            <type>text/plain</type>
            <size>15359</size>
            <attacher name="Noopur Gupta">noopur_gupta@in.ibm.com</attacher>
            
              <token>1425706889-BHnm-8vQlcXtTZNOOPrHHR1iMSJo4haEZdOw0IPIy1I</token>

          </attachment>
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>231798</attachid>
            <date>2013-05-31 06:36:00 -0400</date>
            <delta_ts>2013-05-31 06:36:08 -0400</delta_ts>
            <desc>Patch</desc>
            <filename>Fixed-Bug-409275-18-Change-default-access-modifier.patch</filename>
            <type>text/plain</type>
            <size>17042</size>
            <attacher name="Noopur Gupta">noopur_gupta@in.ibm.com</attacher>
            
              <token>1425706889-srO-_IMkLf30881Vv1j_2i_WBg-OeaFEKUYxPwL68k4</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>408979</bug_id>
          
          <creation_ts>2013-05-24 09:04:00 -0400</creation_ts>
          <short_desc>[1.8][quick fix] NPE and incorrect result from &quot;Add return statement&quot; quick fix on lambda expression</short_desc>
          <delta_ts>2014-03-13 16:08:20 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>PC</rep_platform>
          <op_sys>Windows 7</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>normal</bug_severity>
          <target_milestone>BETA J8</target_milestone>
          
          <blocked>405305</blocked>
          <everconfirmed>1</everconfirmed>
          <reporter name="Noopur Gupta">noopur_gupta@in.ibm.com</reporter>
          <assigned_to name="Manju Mathew">manju656@gmail.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>manju656@gmail.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706889-7XXrq1LogHtJxWzkuXl9Mc03Yh0tnEyXI1jyMmVEx8I</token>

      

      

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2262421</commentid>
    <comment_count>0</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-05-24 09:04:36 -0400</bug_when>
    <thetext>Consider the following example and apply the quick fix &quot;Add return statement&quot; on the lines with comments:

@FunctionalInterface
interface I {
	int foo(int x);	
}

public class A {
	void fun1() {
		I i= (int x) -&gt; { // [1] NPE on applying quick fix
			x++;
		};		
	}
	
	void fun2() {
		I i= (int x) -&gt; { // [2] Incorrect result from quick fix
			x++;
		};
		
		fun1();
	}
}

[1] =&gt;
java.lang.NullPointerException
	at org.eclipse.jdt.internal.corext.dom.ASTNodes.asString(ASTNodes.java:132)
	at org.eclipse.jdt.internal.ui.text.correction.proposals.MissingReturnTypeCorrectionProposal.evaluateReturnExpressions(MissingReturnTypeCorrectionProposal.java:154)
	at org.eclipse.jdt.internal.ui.text.correction.proposals.MissingReturnTypeCorrectionProposal.getRewrite(MissingReturnTypeCorrectionProposal.java:113)
	at org.eclipse.jdt.ui.text.java.correction.ASTRewriteCorrectionProposal.addEdits(ASTRewriteCorrectionProposal.java:113)
	at org.eclipse.jdt.ui.text.java.correction.CUCorrectionProposal.createTextChange(CUCorrectionProposal.java:234)
...


[2] =&gt; Adds return statement to method fun2() instead of the lambda expression. Results in:
	void fun2() {
		I i= (int x) -&gt; { 
			x++;
		};
		
		return fun1(); // Incorrect result
	}</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2309141</commentid>
    <comment_count>1</comment_count>
      <attachid>235652</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-09-20 04:39:43 -0400</bug_when>
    <thetext>Created attachment 235652
Patch with testcases.

This patch is created from the remote branch ngupta/BETA_JAVA8.
With this patch only one proposal is given for the missing return type in lambda expression i.e. to &quot;Add return statement&quot;. The other proposal &quot;Change return type to void&quot; is not shown as in most of the cases the quick fix is not complete(either the functional interface is defined in a different file or it does not find all references of the method and change the return type there also) and the resulting compilation unit still has compiler errors.
The test cases are also attached.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2333252</commentid>
    <comment_count>2</comment_count>
      <attachid>237635</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-11-21 23:37:52 -0500</bug_when>
    <thetext>Created attachment 237635
Additional Changes

The changes for Bug 403927: [1.8] Switch ASTs to JLS8, added visit methods for LambdaExpression which resulted in local variables declared in the Lambda Expression being ignored during the ScopeAnalyzerVisit operation. In the above patch the #visit(LambdaExpession) is overridden in ScopeAnalyzerVisit.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2374127</commentid>
    <comment_count>3</comment_count>
      <attachid>240739</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2014-03-11 00:57:51 -0400</bug_when>
    <thetext>Created attachment 240739
Fix+Test for the additional issues found

Fixed 2 more issues found in the same bug category
1.
 @FunctionalInterface
interface I {
     int foo(int x);    
}
public class A {    
    I i2= (int x) -&gt; {
        x++;
    };
}
&apos;x&apos; was never proposed as a possible return candidate as FieldDeclaration was never visited in detail.
Soln: Enabled to visit FieldDeclaration in HierarchicalASTVisitor and modified ScopeAnalyzer to consider FielDeclaration while computing local variable declaration.
2.
@FunctionalInterface
interface D&lt;S, T&gt; {
	Object m(Class c);
}

class E {
	D&lt;BigInteger, BigInteger&gt; d = (x) -&gt; {
	};
}
&apos;d&apos; was proposed as a possible return candidate which resulted in compiler error as &apos;d&apos; is yet to be defined.
Soln: While computing the proposal for lambda return, bindings are checked to avoid the above scenario.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2375740</commentid>
    <comment_count>4</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2014-03-13 16:08:20 -0400</bug_when>
    <thetext>(In reply to Manju Mathew from comment #3)
&gt; Soln: Enabled to visit FieldDeclaration in HierarchicalASTVisitor

This is definitely a no-go, see the spec of HierarchicalASTVisitor. You can&apos;t change a general utility class just for one specific usage.

I guess you wanted to add this to ScopeAnalyzerVisitor:

		@Override
		public boolean visit(FieldDeclaration node) {
			return !fBreak &amp;&amp; isInside(node);
		}
		
		@Override
		public boolean visit(LambdaExpression node) {
			return !fBreak &amp;&amp; isInside(node);
		}

(In reply to Manju Mathew from comment #1)
&gt; Created attachment 235652 [details] [diff]
&gt; Patch with testcases.

The change in ASTResolving#getPossibleReferenceBinding() at
&quot;case ASTNode.RETURN_STATEMENT:&quot; didn&apos;t get executed by the tests. But the idea makes sense, so I left it in. But I used ASTResolving.findEnclosingLambdaExpression(..) instead of the unsafe ASTResolving.findAncestor(..), and added a disclaimer to the latter.

Didn&apos;t have time for a thorough review of MissingReturnType*CorrectionProposal, but the changes and tests looked reasonable.

Released all 3 patches together as http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=ac35462a94ac60b8320ccf4979113602e3153c36</thetext>
  </long_desc>
      
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>235652</attachid>
            <date>2013-09-20 04:39:00 -0400</date>
            <delta_ts>2013-09-20 04:39:43 -0400</delta_ts>
            <desc>Patch with testcases.</desc>
            <filename>Fix-for-bug-408979-18quick-fix-NPE-and-incorrect-res.patch</filename>
            <type>text/plain</type>
            <size>24239</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706889-oTkBxrJ8si1g0HgQoB8VCJVAqP_DypX57FdGDwJ6H-A</token>

          </attachment>
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>237635</attachid>
            <date>2013-11-21 23:37:00 -0500</date>
            <delta_ts>2013-11-21 23:37:52 -0500</delta_ts>
            <desc>Additional Changes</desc>
            <filename>Fixed-Bug-408979-18quick-fix-NPE-and-incorrect-resul.v2.patch</filename>
            <type>text/plain</type>
            <size>1399</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706889-P6f9yFzUbSEkbym_b1al2OAnX3ewPuBuaIP_SOUeX-Y</token>

          </attachment>
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>240739</attachid>
            <date>2014-03-11 00:57:00 -0400</date>
            <delta_ts>2014-03-11 00:57:51 -0400</delta_ts>
            <desc>Fix+Test for the additional issues found</desc>
            <filename>Fixed-Bug-408979-18quick-fix-NPE-and-incorrect-result.patch</filename>
            <type>text/plain</type>
            <size>11657</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706889-n9ng-9SieuUHqj4tHJUhcUNvUXBSafIf5GEnJTHIWqs</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>408966</bug_id>
          
          <creation_ts>2013-05-24 08:01:00 -0400</creation_ts>
          <short_desc>[1.8][inline] Invalid inline constant and inline temp refactorings using lambda expressions</short_desc>
          <delta_ts>2014-06-15 08:08:22 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>enhancement</bug_severity>
          <target_milestone>4.4 M7</target_milestone>
          <dependson>422766</dependson>
    
    <dependson>422566</dependson>
          <blocked>405305</blocked>
    
    <blocked>423439</blocked>
    
    <blocked>424745</blocked>
          <everconfirmed>1</everconfirmed>
          <reporter name="Noopur Gupta">noopur_gupta@in.ibm.com</reporter>
          <assigned_to name="Noopur Gupta">noopur_gupta@in.ibm.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
    
    <cc>noopur_gupta@in.ibm.com</cc>
    
    <cc>souheil.sultan@laposte.net</cc>
          
          <votes>0</votes>

      
          <token>1425706889-PTiU-o38pYIfX0htuI-snT4gASSpYto6kh2iSh4Kxjw</token>

      

      <flag name="review"
          id="60257"
          type_id="1"
          status="+"
          setter="markus_keller@ch.ibm.com"
    />

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2262359</commentid>
    <comment_count>0</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-05-24 08:01:26 -0400</bug_when>
    <thetext>Consider the following example and perform Refactor &gt; Inline as per the comments:

@FunctionalInterface
interface I1 {
	int foo(int x);	
}

public class X {
	public static final I1 a= (int x) -&gt; x;
	
	void fun1() {
		int n = a.foo(0); // [1] Inline &quot;a&quot; =&gt; AFE	
		
		I1 i= (int x) -&gt; { return x; }; // [2] Inline &quot;i&quot;
		I1 i1= x -&gt; i.foo(x); // =&gt; Invalid inlining of &quot;i&quot;
		fun2(i); // =&gt; Valid inlining of &quot;i&quot;
	}
	
	void fun2(I1 i) {}
}

[1] =&gt; 
java.lang.reflect.InvocationTargetException
...
Caused by: org.eclipse.core.runtime.AssertionFailedException: assertion failed: 
	at org.eclipse.core.runtime.Assert.isTrue(Assert.java:110)
	at org.eclipse.core.runtime.Assert.isTrue(Assert.java:96)
	at org.eclipse.jdt.internal.corext.dom.fragments.ASTFragmentFactory$FragmentFactory.setFragment(ASTFragmentFactory.java:194)
	at org.eclipse.jdt.internal.corext.dom.fragments.ASTFragmentFactory$FragmentForFullSubtreeFactory.visit(ASTFragmentFactory.java:133)
	at org.eclipse.jdt.internal.corext.dom.HierarchicalASTVisitor.visit(HierarchicalASTVisitor.java:547)
	at org.eclipse.jdt.internal.corext.dom.HierarchicalASTVisitor.visit(HierarchicalASTVisitor.java:566)
	at org.eclipse.jdt.core.dom.SimpleName.accept0(SimpleName.java:149)
	at org.eclipse.jdt.core.dom.ASTNode.accept(ASTNode.java:2670)
	at org.eclipse.jdt.core.dom.ASTNode.acceptChild(ASTNode.java:2718)
	at org.eclipse.jdt.core.dom.LambdaExpression.accept0(LambdaExpression.java:215)
	at org.eclipse.jdt.core.dom.ASTNode.accept(ASTNode.java:2670)
	at org.eclipse.jdt.internal.corext.dom.fragments.ASTFragmentFactory$FragmentFactory.createFragment(ASTFragmentFactory.java:186)
	at org.eclipse.jdt.internal.corext.dom.fragments.ASTFragmentFactory$FragmentForFullSubtreeFactory.createFragmentFor(ASTFragmentFactory.java:115)
	at org.eclipse.jdt.internal.corext.dom.fragments.ASTFragmentFactory.createFragmentForFullSubtree(ASTFragmentFactory.java:56)
	at org.eclipse.jdt.internal.corext.refactoring.code.InlineConstantRefactoring.checkInitializer(InlineConstantRefactoring.java:789)
	at org.eclipse.jdt.internal.corext.refactoring.code.InlineConstantRefactoring.checkInitialConditions(InlineConstantRefactoring.java:736)
	at org.eclipse.ltk.core.refactoring.CheckConditionsOperation.run(CheckConditionsOperation.java:83)
...


[2] =&gt; Results in:
I1 i1= x -&gt; (int x) -&gt; { return x; }.foo(x); // =&gt; Invalid inlining of &quot;i&quot;
fun2((int x) -&gt; { return x; }); // =&gt; Valid inlining of &quot;i&quot;</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2332287</commentid>
    <comment_count>1</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-11-20 08:43:42 -0500</bug_when>
    <thetext>When we have a lambda reference being used as the expression in a method invocation, we cannot inline the lambda as shown in cases [1] and [2]&apos;s invalid inlining in comment #0.

In cases like [1], the inline refactoring can be disabled.
In cases like [2], where some occurrences are valid and some are not, we cannot remove the lambda declaration as invalid occurrences cannot be inlined. Should we inline only the valid locations and keep the lambda declaration also for other occurrences or should the inline refactoring be disabled here?</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2332558</commentid>
    <comment_count>2</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-11-20 14:46:30 -0500</bug_when>
    <thetext>&gt; Should we inline only the valid locations and keep the lambda
&gt; declaration also for other occurrences [..]?

Let&apos;s do the same as Inline Method (bug 83041):
- show a (non-fatal) error message for each invalid location and then don&apos;t inline
- keep the declaration if these was an invalid location</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2334691</commentid>
    <comment_count>3</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-11-26 14:38:15 -0500</bug_when>
    <thetext>The categorization of places where a lambda or a method reference can be inlined and where not looks like a generally useful property of an ASTNode location.

The general question is: Can the StructuralPropertyDescriptor for the target location hold a poly expression? This will probably also be useful for other refactorings, so please make this functionality reusable (e.g. in ASTNodes).

For cases where inlining is possible (i.e., the target accepts a poly expression), we also need to think about inadvertent semantic shifts because the type inference could resolve to different types at the new location. Maybe we need something similar to MethodInvocation#isResolvedTypeInferredFromExpectedType() from JDT Core?

See also the call hierarchy of Invocations#isResolvedTypeInferredFromExpectedType(Expression). I expect the fix for this bug to be applicable in similar situations, so this is probably an opportunity to share even more code.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2335507</commentid>
    <comment_count>4</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-11-28 08:56:35 -0500</bug_when>
    <thetext>-------------------------------------------------------------
package test.inline.lambda.constant;

@FunctionalInterface
interface FI {
	int foo(int x);
}

@FunctionalInterface
interface F {
	FI foo();
}

class C1 {
	public static final FI fi = x -&gt; x++;	// inline all references of &apos;fi&apos; and delete it.
	
	static {
		FI fi1 = fi;	// [1]
		
		FI fi2;
		fi2 = fi;		// [2]		
	}
	
	private FI fun1() {
		return fi;		// [3]
	}
	
	FI[] fis = new FI[] {fi, fi}; // [4]
	
	
	int x1 = fun2(fi);	// [5a]
	
	C1 c1 = new C1(fi);	// [5b]
	
	private int fun2(FI fi) {return 0;}
	public C1(FI fi) {}

	FI fi3 = fun3();

	private FI fun3() {
		F f = () -&gt; fi;	// [6]
		return f.foo();
	}

	private void fun4() {
		boolean flag = true;
		FI fi4 = flag ? fi : fi; // [7]
	}
	
	
	private Object fun5() {
		Object o = fi; // [8a]
		
		Object fi2;
		fi2 = fi; // [8b]
		
		Object[] fis = new Object[] {fi, fi}; // [8c]
		
		System.out.println(fi);  // [8d]

		Object fi4 = true ? fi : fi; // [8e]
		
		int x2 = fi.foo(10); // [8f]
				
		return fi;	// [8g]
	}
        
        // etc.
}
-------------------------------------------------------------

The above example shows some cases where a lambda constant can be inlined.

In cases [1] to [7], it can be inlined directly.
In cases [8*], lambda will need a type cast to the functional interface type while inlining.

Examples are based on http://cr.openjdk.java.net/~briangoetz/lambda/lambda-state-final.html, section 5: Contexts for target typing.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2335522</commentid>
    <comment_count>5</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-11-28 09:14:33 -0500</bug_when>
    <thetext>(In reply to Markus Keller from comment #3)
&gt; The categorization of places where a lambda or a method reference can be
&gt; inlined and where not looks like a generally useful property of an ASTNode
&gt; location.
&gt; 
&gt; The general question is: Can the StructuralPropertyDescriptor for the target
&gt; location hold a poly expression? This will probably also be useful for other
&gt; refactorings, so please make this functionality reusable (e.g. in ASTNodes).

Does it mean that we need to know if the StructuralPropertyDescriptor of the target location defines a target type, as poly expressions cannot be typed in the absence of a target type?
http://cr.openjdk.java.net/~briangoetz/lambda/lambda-state-final.html, section 5: Contexts for target typing : lists the contexts that have target types. Would that be helpful?

If the target location&apos;s StructuralPropertyDescriptor accepts a poly expression ( i.e. defines a target type) then we need to know what is the defined target type.

And, if the defined target type matches the type of the lambda expr being inlined, it can be inlined directly.
Otherwise, we could cast the lambda expr to its functional interface type, as the target was already having the functional interface reference at that location before inling.

&gt; For cases where inlining is possible (i.e., the target accepts a poly
&gt; expression), we also need to think about inadvertent semantic shifts because
&gt; the type inference could resolve to different types at the new location.
&gt; Maybe we need something similar to
&gt; MethodInvocation#isResolvedTypeInferredFromExpectedType() from JDT Core?

Can you give an example?

&gt; See also the call hierarchy of
&gt; Invocations#isResolvedTypeInferredFromExpectedType(Expression). I expect the
&gt; fix for this bug to be applicable in similar situations, so this is probably
&gt; an opportunity to share even more code.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2335563</commentid>
    <comment_count>6</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-11-28 10:10:09 -0500</bug_when>
    <thetext>&gt; http://cr.openjdk.java.net/~briangoetz/lambda/lambda-state-final.html,
&gt; section 5: Contexts for target typing : lists the contexts that have target
&gt; types. Would that be helpful?

Yes, that section is helpful to understand the problem, but the implementation should be based on the spec: http://cr.openjdk.java.net/~dlsmith/jsr335-0.7.0.html#E

&gt; &gt; For cases where inlining is possible (i.e., the target accepts a poly
&gt; &gt; expression), we also need to think about inadvertent semantic shifts because
&gt; &gt; the type inference could resolve to different types at the new location.
&gt; &gt; Maybe we need something similar to
&gt; &gt; MethodInvocation#isResolvedTypeInferredFromExpectedType() from JDT Core?
&gt; 
&gt; Can you give an example?

@FunctionalInterface
interface FI {
    int foo(int x);
}
@FunctionalInterface
interface FL {
    long foo(long x);
}

class C2 {
    public static final FI fi = x -&gt; x++; // inline &apos;fi&apos;
    public static final FL fl = x -&gt; x++;

    {
        bar(fi); // can&apos;t inline fi without explicit cast to FI
        bar(fl); // can&apos;t inline fl without explicit cast to FL
    }
    void bar(FI fi) { }
    void bar(FL fl) { }
}</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2345276</commentid>
    <comment_count>7</comment_count>
      <attachid>238615</attachid>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-12-31 01:56:31 -0500</bug_when>
    <thetext>Created attachment 238615
Fix

Attaching a patch for the fix based on the common code given in bug 423439 comment #6.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2345278</commentid>
    <comment_count>8</comment_count>
      <attachid>238616</attachid>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-12-31 02:34:19 -0500</bug_when>
    <thetext>Created attachment 238616
Tests

Attaching the patch for the following commit from mmathew/BETA_JAVA8 branch:

http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?h=mmathew/BETA_JAVA8&amp;id=262e59c07ad895ff0657dd9c9a42c9b541c1a5ac</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2393657</commentid>
    <comment_count>9</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2014-04-27 18:44:41 -0400</bug_when>
    <thetext>There are a few more cases, where we need to insert a cast:

@FunctionalInterface
interface I1 {
    int foo(int x); 
    int CONST= 12;
}

public class FI {
    void fun1() {
        I1 i= (int x) -&gt; { return x; }; // [3] Inline &quot;i&quot;
        int c = i.CONST;
        IntFunction&lt;Integer&gt; f= i::foo;
        synchronized (i) { }
    }
}

I think we can avoid adding more cases to ASTNodes#getExplicitCast(..) if we just add a cast when getTargetType(reference) returns null. These are exactly the those cases where the target type is not defined and hence needs to be supplied by a cast.

Fixed InlineConstantTests18#test1003()/test3()/test4() to make them interesting again after bug 423439 comment 14: FX#foo() now also returns int.

Committed fix &amp; tests with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=7a1839ac4f876d3ebafe5fef49d315db2ab6f6f9</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2417110</commentid>
    <comment_count>10</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2014-06-15 08:08:22 -0400</bug_when>
    <thetext>*** Bug 437442 has been marked as a duplicate of this bug. ***</thetext>
  </long_desc>
      
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>238615</attachid>
            <date>2013-12-31 01:56:00 -0500</date>
            <delta_ts>2013-12-31 01:56:31 -0500</delta_ts>
            <desc>Fix</desc>
            <filename>Fixed-bug-408966-1.8-Inline-refactoring.patch</filename>
            <type>text/plain</type>
            <size>1525</size>
            <attacher name="Noopur Gupta">noopur_gupta@in.ibm.com</attacher>
            
              <token>1425706889-el55mSeMf_aAuObqWtc6xWip-Wy8bP_qGMK34thxFR0</token>

          </attachment>
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>238616</attachid>
            <date>2013-12-31 02:34:00 -0500</date>
            <delta_ts>2013-12-31 02:34:19 -0500</delta_ts>
            <desc>Tests</desc>
            <filename>Fixed-bug-408966-1.8-inline-constant-temp-tests.patch</filename>
            <type>text/plain</type>
            <size>43713</size>
            <attacher name="Noopur Gupta">noopur_gupta@in.ibm.com</attacher>
            
              <token>1425706889-zLC6u3e47HwQ_cksHwPyvsglXnpIw-YQHhaEnyjRA6g</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>408937</bug_id>
          
          <creation_ts>2013-05-24 04:29:00 -0400</creation_ts>
          <short_desc>[1.8][rename] Unable to rename variables in lambda expression field</short_desc>
          <delta_ts>2014-04-01 02:32:51 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>PC</rep_platform>
          <op_sys>Windows 7</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>enhancement</bug_severity>
          <target_milestone>4.4 M7</target_milestone>
          <dependson>408230</dependson>
          <blocked>405305</blocked>
          <everconfirmed>1</everconfirmed>
          <reporter name="Noopur Gupta">noopur_gupta@in.ibm.com</reporter>
          <assigned_to name="Manju Mathew">manju656@gmail.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>manju656@gmail.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706889-RhrglcUWb_PJe-UBKWS2-O88HODAzKjZZLXezjRlc4c</token>

      

      <flag name="review"
          id="59308"
          type_id="1"
          status="?"
          setter="manju656@gmail.com"
          requestee="markus_keller@ch.ibm.com"
    />

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2262241</commentid>
    <comment_count>0</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-05-24 04:29:29 -0400</bug_when>
    <thetext>Consider the following example and try to rename the variables mentioned in comments using &quot;Alt+Shift+R&quot;:

@FunctionalInterface
interface I {
	int foo (int x);
}

public class C1 {
	I i= (int x) -&gt; { // Unable to Rename &quot;x&quot;
		int p= 10; // Unable to Rename &quot;p&quot;
		I ii= (int a) -&gt; a+100; // Unable to Rename &quot;ii&quot;, &quot;a&quot;
		return ii.foo(x) + p;
	};

	void foo() {
		I i= (int x) -&gt; x; // works here
	}	
}

We get the error, &quot;Only local variables declared in methods and initializers can be renamed&quot;. 

However, it should be possible to rename variables in any type of lambda expr also.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2303662</commentid>
    <comment_count>1</comment_count>
      <attachid>235236</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-09-06 08:11:19 -0400</bug_when>
    <thetext>Created attachment 235236
Patch with testcases.

Renaming of variables within lambda is taken care off. Testcases are also included.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2308647</commentid>
    <comment_count>2</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-09-19 02:32:49 -0400</bug_when>
    <thetext>Due to bug 408230 the below case(inferred parameter type) fails during rename operation.
I i1= (x) -&gt; {
		x++; // Select &apos;x&apos; and invoke rename
		return x;
	     };</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2363244</commentid>
    <comment_count>3</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2014-02-14 01:35:57 -0500</bug_when>
    <thetext>Released the fix to BETA_JAVA8 as:
http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?h=BETA_JAVA8&amp;id=1fa7558ed5b5098be920ba39ae0d8f2d68e3f004

(In reply to Manju Mathew from comment #2)
&gt; Due to bug 408230 the below case(inferred parameter type) fails during
&gt; rename operation.
&gt; I i1= (x) -&gt; {
&gt; 		x++; // Select &apos;x&apos; and invoke rename
&gt; 		return x;
&gt; 	     };
Added an additional test for the above case and released to BETA_JAVA8 as: 
http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?h=BETA_JAVA8&amp;id=ecba45b579d03f4e3032f64b0dc29bd0b019f356</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2382812</commentid>
    <comment_count>4</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2014-04-01 02:32:51 -0400</bug_when>
    <thetext>Fixed, changes are available in master.</thetext>
  </long_desc>
      
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>235236</attachid>
            <date>2013-09-06 08:11:00 -0400</date>
            <delta_ts>2013-09-06 08:11:19 -0400</delta_ts>
            <desc>Patch with testcases.</desc>
            <filename>Fix-for-bug-408937-18rename-Unable-to-rename-variabl.patch</filename>
            <type>text/plain</type>
            <size>20818</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706889-_TrclH6OnDjDlvnymRzae9hgiihUrjQUPKFaiBKAy_A</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>408555</bug_id>
          
          <creation_ts>2013-05-21 06:13:00 -0400</creation_ts>
          <short_desc>DeleteTest.testDeleteInternalJAR fails sporadically</short_desc>
          <delta_ts>2013-05-31 04:18:03 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>PC</rep_platform>
          <op_sys>Windows 7</op_sys>
          <bug_status>VERIFIED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords>test</keywords>
          <priority>P3</priority>
          <bug_severity>normal</bug_severity>
          <target_milestone>4.3 RC3</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Dani Megert">daniel_megert@ch.ibm.com</reporter>
          <assigned_to name="Markus Keller">markus_keller@ch.ibm.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706889-y8DzCezqKNuSRnDzFRoVkGNAMF3y-fcguEEFhJAY5Og</token>

      

      

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2260011</commentid>
    <comment_count>0</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-05-21 06:13:40 -0400</bug_when>
    <thetext>http://download.eclipse.org/eclipse/downloads/drops4/I20130518-1500/testresults/html/org.eclipse.jdt.ui.tests.refactoring_win32.win32.x86_7.0.html</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2264843</commentid>
    <comment_count>1</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-05-29 05:37:20 -0400</bug_when>
    <thetext>Failed again. We should either make it more stable or disable it for now.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2264975</commentid>
    <comment_count>2</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-05-29 10:15:58 -0400</bug_when>
    <thetext>These tests actually need performDummySearch, since they test the Delete refactoring.

Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=4fc272a117b65b419fab3e20439e992f8167053f and added some explanation to JavaProjectHelper.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2266069</commentid>
    <comment_count>3</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-05-31 04:18:03 -0400</bug_when>
    <thetext>Verified in I20130530-1430.</thetext>
  </long_desc>
      
      

    </bug>
    <bug>
          <bug_id>408334</bug_id>
          
          <creation_ts>2013-05-17 07:53:00 -0400</creation_ts>
          <short_desc>[extract interface] AFE on selecting next change in refactoring Preview</short_desc>
          <delta_ts>2013-12-05 14:21:13 -0500</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>normal</bug_severity>
          <target_milestone>4.4 M4</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Noopur Gupta">noopur_gupta@in.ibm.com</reporter>
          <assigned_to name="Markus Keller">markus_keller@ch.ibm.com</assigned_to>
          
          
          <votes>0</votes>

      
          <token>1425706889-EdMmelBzD0STqSclzW1VZALde0z6_M9R5cOcaH_m-4Q</token>

      

      

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2258673</commentid>
    <comment_count>0</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-05-17 07:53:04 -0400</bug_when>
    <thetext>public class Test {

}

Right click and select &apos;Refactor &gt; Extract Interface&apos; for the above class.
Give some name for interface and click &quot;Preview&quot;.
Use down arrow button i.e. &quot;Select Next Change&quot;.   

It expands the 1st change node and &quot;Add super interface&quot; is selected.
No input in the details page.
Error is logged in the Error Log view:

org.eclipse.core.runtime.AssertionFailedException: assertion failed: 
	at org.eclipse.core.runtime.Assert.isTrue(Assert.java:110)
	at org.eclipse.core.runtime.Assert.isTrue(Assert.java:96)
	at org.eclipse.ltk.core.refactoring.TextChange.getCurrentContent(TextChange.java:334)
	at org.eclipse.ltk.internal.ui.refactoring.TextEditChangePreviewViewer.setInput(TextEditChangePreviewViewer.java:192)
...</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2258683</commentid>
    <comment_count>1</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-05-17 08:13:57 -0400</bug_when>
    <thetext>Not a regression. 
Also reproducible in:
Version: 3.8.1
Build id: M20120914-1540</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2258858</commentid>
    <comment_count>2</comment_count>
      <attachid>231162</attachid>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-05-17 11:19:15 -0400</bug_when>
    <thetext>Created attachment 231162
Fix

This is not trivial to fix, because ExtractInterfaceProcessor#rewriteTypeOccurrences(..) abuses the CompilationUnitRewrite infrastructure.

The method calls &quot;rewrite.rewriteAST(..)&quot;, applies the TextEdits on a private document and then creates multiple levels of working copies and additional ASTs. The operations on the ASTRewrite in ExtractInterfaceProcessor#createTypeSignature(..) assign a CategorizedTextEditGroup to the rewrite event, and every execution of rewriteAST(..) adds more TextEdits to the CategorizedTextEditGroup, although only the last ones are relevant for the final CompilationUnitChange.

I think the right fix for this bug and the equivalent http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=f9e9d48ede0432e8537dc71496c5ca2ce432ff7c is to always clear all TextEdits before running the last rewriteAST(..) whose results end up in the CompilationUnitChange.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2338320</commentid>
    <comment_count>3</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-12-05 14:21:13 -0500</bug_when>
    <thetext>Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=c100afc6ed5f1c88c6024bb1bf5789552f013be5</thetext>
  </long_desc>
      
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>231162</attachid>
            <date>2013-05-17 11:19:00 -0400</date>
            <delta_ts>2013-05-17 11:19:15 -0400</delta_ts>
            <desc>Fix</desc>
            <filename>eclipse.jdt.ui.patch</filename>
            <type>text/plain</type>
            <size>2409</size>
            <attacher name="Markus Keller">markus_keller@ch.ibm.com</attacher>
            
              <token>1425706889-W7dCW9WzvMwz59VK7LnR8gn15zoSbLvCy-DC_0_mAk4</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>408330</bug_id>
          
          <creation_ts>2013-05-17 07:22:00 -0400</creation_ts>
          <short_desc>Java Model Exception from Javadoc view if element is deleted</short_desc>
          <delta_ts>2013-05-22 03:08:50 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>VERIFIED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>normal</bug_severity>
          <target_milestone>4.3 RC2</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Noopur Gupta">noopur_gupta@in.ibm.com</reporter>
          <assigned_to name="Manju Mathew">manju656@gmail.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>manju656@gmail.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706889-0QLrtjOsSC32nrqLKV7QN975xYl9SYY7fhDIjvcZvqY</token>

      

      <flag name="review"
          id="57433"
          type_id="1"
          status="+"
          setter="daniel_megert@ch.ibm.com"
    />
    <flag name="review"
          id="57508"
          type_id="1"
          status="+"
          setter="markus_keller@ch.ibm.com"
    />

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2258657</commentid>
    <comment_count>0</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-05-17 07:22:46 -0400</bug_when>
    <thetext>Select foo() in the following example and open the Javadoc view:

public class Test {
	private void foo() {}
}

Now, delete the method: 
private void foo() {}

An error is logged in the Error Log view on deletion:

Java Model Exception: Java Model Status [foo() [in Test [in [Working copy] Test.java [in test.bugs.var [in src [in com.bugs.test]]]]] does not exist]
	at org.eclipse.jdt.internal.core.JavaElement.newNotPresentException(JavaElement.java:498)
	at org.eclipse.jdt.internal.core.JavaElement.openWhenClosed(JavaElement.java:532)
...
at org.eclipse.jdt.internal.ui.text.javadoc.JavadocContentAccess2.getHTMLContentFromSource(JavadocContentAccess2.java:600)
	at org.eclipse.jdt.internal.ui.text.javadoc.JavadocContentAccess2.getHTMLContent(JavadocContentAccess2.java:495)
	at org.eclipse.jdt.internal.ui.infoviews.JavadocView.getJavadocHtml(JavadocView.java:1097)
	at org.eclipse.jdt.internal.ui.infoviews.JavadocView.computeInput(JavadocView.java:908)</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2258674</commentid>
    <comment_count>1</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-05-17 07:58:00 -0400</bug_when>
    <thetext>This is a regression from bug 403074.
When the current view input is invalid, the requirement was to preserve the last shown input. In this case the last input is invalid/does not exist.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2258679</commentid>
    <comment_count>2</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-05-17 08:05:07 -0400</bug_when>
    <thetext>We should fix this for RC2.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2258682</commentid>
    <comment_count>3</comment_count>
      <attachid>231148</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-05-17 08:13:06 -0400</bug_when>
    <thetext>Created attachment 231148
Patch.

To avoid the exception, the check to make sure that the element exists is moved up.
Dani, please review.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2260034</commentid>
    <comment_count>4</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-05-21 07:10:46 -0400</bug_when>
    <thetext>+1 for RC2.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2260246</commentid>
    <comment_count>5</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-05-21 11:02:50 -0400</bug_when>
    <thetext>Thanks Manju, released with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=a0f013e697405dc12a34ea39752fa3fbaed64ba0</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2260667</commentid>
    <comment_count>6</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-05-22 03:08:50 -0400</bug_when>
    <thetext>Verified in I20130521-2000.</thetext>
  </long_desc>
      
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>231148</attachid>
            <date>2013-05-17 08:13:00 -0400</date>
            <delta_ts>2013-05-21 07:12:39 -0400</delta_ts>
            <desc>Patch.</desc>
            <filename>eclipse.jdt.ui.patch</filename>
            <type>text/plain</type>
            <size>1272</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706889-z-yKxw0vdjYHENyxOTCBmCB4yeSidB8tEXIrPxBqfC4</token>
<flag name="review"
          id="57525"
          type_id="6"
          status="+"
          setter="daniel_megert@ch.ibm.com"
    />
          </attachment>
      

    </bug>
    <bug>
          <bug_id>408114</bug_id>
          
          <creation_ts>2013-05-15 07:59:00 -0400</creation_ts>
          <short_desc>[1.8][extract local] Unable to extract local variable within lambda expression&apos;s body</short_desc>
          <delta_ts>2014-09-30 04:19:45 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>normal</bug_severity>
          <target_milestone>4.5 M3</target_milestone>
          
          <blocked>405305</blocked>
          <everconfirmed>1</everconfirmed>
          <reporter name="Noopur Gupta">noopur_gupta@in.ibm.com</reporter>
          <assigned_to name="Noopur Gupta">noopur_gupta@in.ibm.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
    
    <cc>noopur_gupta@in.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706889-tAQZ2dXb4ONiuYn7gwMLFfUXO8udu_09uyLrnfocTTo</token>

      

      <flag name="review"
          id="63565"
          type_id="1"
          status="+"
          setter="markus_keller@ch.ibm.com"
    />

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2257316</commentid>
    <comment_count>0</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-05-15 07:59:16 -0400</bug_when>
    <thetext>Since a lambda expression is like a method, it should be possible to extract local variables within its body.

Consider the following example and try to extract a local variable from the lines with comments, we get different error messages:

@FunctionalInterface
interface FI {
	int foo(int a);
}

public class TestExtractLocalVariable {
	FI fi1= (a) -&gt; a + 10;	// Error
	
	FI fi2= (int a) -&gt; {	
		int b= a + 10; // Error
		return b;
	};
	
	void bar(FI fi) {
	     FI fi1= (a) -&gt; a + 10; // Error, not extracted within lambda body
		
	     FI fi2= (a) -&gt; {	
		    int b= a + 10; // Works here
		    return b;
	     };		
	}	
}</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2457294</commentid>
    <comment_count>1</comment_count>
      <attachid>247437</attachid>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2014-09-29 06:14:09 -0400</bug_when>
    <thetext>Created attachment 247437
Patch

Attached fix and tests to extract local variable in lambda expression&apos;s body.
Markus, please have a look.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2457595</commentid>
    <comment_count>2</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2014-09-29 15:15:30 -0400</bug_when>
    <thetext>Looks good, thanks.

Nits:

* The separate message constant is not really necessary, since the addition of &quot;lambda expression&quot; is not wrong for earlier versions of Java. I&apos;d favor less code and less messages over a sightly more concise message for a soon-to-be-EOL&apos;d language version.

* Better use Bindings.isVoidType(..) instead of ast.resolveWellKnownType(&quot;void&quot;).isEqualTo(..)

* The double casts here are not too nice:
    SimpleName varName= ((VariableDeclarationFragment) ((VariableDeclarationStatement) replacement).fragments().get(0)).getName();

Better extract &quot;createTempDeclaration(initializer)&quot;, remove the comment, and use the new local variable that already has the right type.

The other cast can be avoided by extracting this local variable:

    List&lt;VariableDeclarationFragment&gt; fragments= tempDeclaration.fragments();

This works because the jdt.ui project has the &quot;Ignore unavoidable generic type problems due to raw APIs&quot; warning enabled.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2457603</commentid>
    <comment_count>3</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2014-09-29 15:19:57 -0400</bug_when>
    <thetext>(In reply to Markus Keller from comment #2)
&gt; This works because the jdt.ui project has the &quot;Ignore unavoidable generic
&gt; type problems due to raw APIs&quot; warning enabled.

I meant: ... the ... *option* enabled.

That option can fix &quot;type safety&quot; problems, but it cannot insert casts, since that would make the compiler deviate from the JLS.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2457791</commentid>
    <comment_count>4</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2014-09-30 04:19:45 -0400</bug_when>
    <thetext>Thanks Markus. Updated the patch as per review comments and released as:
http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=4f588b97a34c99264ee85309e6786c822be612ed</thetext>
  </long_desc>
      
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>247437</attachid>
            <date>2014-09-29 06:14:00 -0400</date>
            <delta_ts>2014-09-29 06:14:09 -0400</delta_ts>
            <desc>Patch</desc>
            <filename>Fixed-bug-408114-extract-local.patch</filename>
            <type>text/plain</type>
            <size>26125</size>
            <attacher name="Noopur Gupta">noopur_gupta@in.ibm.com</attacher>
            
              <token>1425706889-oKnrq9CxBBuxp2fACMTLby0EjyWK8qD7nRQkXkBdoBY</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>408072</bug_id>
          
          <creation_ts>2013-05-14 21:31:00 -0400</creation_ts>
          <short_desc>[nls tooling] Interface is flagged as missing NLS key</short_desc>
          <delta_ts>2013-06-20 09:21:09 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>normal</bug_severity>
          <target_milestone>4.4 M1</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Michael Rennie">Michael_Rennie@ca.ibm.com</reporter>
          <assigned_to name="Dani Megert">daniel_megert@ch.ibm.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706889-eRdmTHFpO7s79qK1WK90F9gxRA1QAZgp-wCIjbTJn1o</token>

      

      

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2257117</commentid>
    <comment_count>0</comment_count>
    <who name="Michael Rennie">Michael_Rennie@ca.ibm.com</who>
    <bug_when>2013-05-14 21:31:21 -0400</bug_when>
    <thetext>Version: 4.3.0
Build id: I20130513-2000

While scanning org.eclipse.jface I got the following during the search:

Undefined keys in: MenuManager.java - org.eclipse.jface.action (2 matches)

One of the matches is: ExternalActionManager.ICallback callback = ExternalActionManager.getInstance().getCallback();

with ExternalActionManager.ICallback highlighted. There are 17 of these flagged for all of jface.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2257959</commentid>
    <comment_count>1</comment_count>
      <attachid>231072</attachid>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-05-16 07:57:13 -0400</bug_when>
    <thetext>Created attachment 231072
Fix</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2274933</commentid>
    <comment_count>2</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-06-20 09:21:09 -0400</bug_when>
    <thetext>Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=9a7c42ae635d04d9f3e7d88e63fc12c52e64edab</thetext>
  </long_desc>
      
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>231072</attachid>
            <date>2013-05-16 07:57:00 -0400</date>
            <delta_ts>2013-05-16 07:57:13 -0400</delta_ts>
            <desc>Fix</desc>
            <filename>eclipse.jdt.ui.patch</filename>
            <type>text/plain</type>
            <size>1339</size>
            <attacher name="Dani Megert">daniel_megert@ch.ibm.com</attacher>
            
              <token>1425706889-DHnYHL2Mh7TQLX9aN-NyF2vlOMjZYXmsPQGurF3KZxI</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>408060</bug_id>
          
          <creation_ts>2013-05-14 15:55:00 -0400</creation_ts>
          <short_desc>Bug in NLSSearchQuery</short_desc>
          <delta_ts>2013-08-27 08:32:35 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>normal</bug_severity>
          <target_milestone>4.4 M1</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Michael Rennie">Michael_Rennie@ca.ibm.com</reporter>
          <assigned_to name="Michael Rennie">Michael_Rennie@ca.ibm.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706889-LvzCm4u_bSqYndzOlzyeOiHWYENUF4PdCqzSXkcjROM</token>

      

      

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2257019</commentid>
    <comment_count>0</comment_count>
      <attachid>230978</attachid>
    <who name="Michael Rennie">Michael_Rennie@ca.ibm.com</who>
    <bug_when>2013-05-14 15:55:49 -0400</bug_when>
    <thetext>Created attachment 230978
proposed fix

While looking at how the search works for bug 408059 I found that the search query checks twice to see if the wrapper class exists, when it should probably be testing if the properties file exists in the second check.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2257965</commentid>
    <comment_count>1</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-05-16 08:06:41 -0400</bug_when>
    <thetext>Good catch!</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2274910</commentid>
    <comment_count>2</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-06-20 08:54:26 -0400</bug_when>
    <thetext>Pushed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=3969b419201db89064520e2f18c8fcd7fe24d44e</thetext>
  </long_desc>
      
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>230978</attachid>
            <date>2013-05-14 15:55:00 -0400</date>
            <delta_ts>2013-05-16 08:07:38 -0400</delta_ts>
            <desc>proposed fix</desc>
            <filename>eclipse.jdt.ui.nls.search.patch</filename>
            <type>text/plain</type>
            <size>1573</size>
            <attacher name="Michael Rennie">Michael_Rennie@ca.ibm.com</attacher>
            
              <token>1425706889-IiWhcM5qlNBQ4GG3Guw0fCVszm5OFJuM_bdVdbT5aRE</token>
<flag name="review"
          id="57396"
          type_id="6"
          status="+"
          setter="daniel_megert@ch.ibm.com"
    />
          </attachment>
      

    </bug>
    <bug>
          <bug_id>408009</bug_id>
          
          <creation_ts>2013-05-14 08:48:00 -0400</creation_ts>
          <short_desc>[1.8][extract method] Unable to extract lambda expression to method</short_desc>
          <delta_ts>2014-02-23 18:21:42 -0500</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>VERIFIED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>enhancement</bug_severity>
          <target_milestone>BETA J8</target_milestone>
          <dependson>407985</dependson>
          <blocked>405305</blocked>
          <everconfirmed>1</everconfirmed>
          <reporter name="Noopur Gupta">noopur_gupta@in.ibm.com</reporter>
          <assigned_to name="Noopur Gupta">noopur_gupta@in.ibm.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>manju656@gmail.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
    
    <cc>noopur_gupta@in.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706889-rDat342p_AMulv02z-n_iPHsCllYyutb3y6E_wsM7_w</token>

      

      

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2256651</commentid>
    <comment_count>0</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-05-14 08:48:55 -0400</bug_when>
    <thetext>Consider the example below:

@FunctionalInterface
public interface I1 {
	int foo(int a);
}

class X {	
	void foo() {	
		I1 i1= (int a) -&gt; {return 10;}; // Extract lambda expr
		
		I1 i2= (a) -&gt; {return 10;}; // Extract lambda expr
		bar(a -&gt; 10); // Extract lambda expr
	}
	
	void bar(I1 i) {
	}

	// expected method after extraction
	I1 m() {
		return (int a) -&gt; {return 10;};
	}
}

Try to extract only the lambda expr from the lines with comments to a method using Alt+Shift+M. 

We get different error messages in above cases and it is not possible to extract the lambda expr to a method as shown in the expected method above.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2257318</commentid>
    <comment_count>1</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-05-15 08:00:41 -0400</bug_when>
    <thetext>The same is applicable to Extract Local Variable refactoring.
It is not possible to extract the lambda expr to a local variable using Alt+Shift+L. 
Example - Same as comment #0.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2301363</commentid>
    <comment_count>2</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-08-30 12:26:04 -0400</bug_when>
    <thetext>(In reply to comment #1)
&gt; The same is applicable to Extract Local Variable refactoring.
&gt; It is not possible to extract the lambda expr to a local variable using
&gt; Alt+Shift+L. 
&gt; Example - Same as comment #0.

Created bug 416264 for Extract Local Variable refactoring.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2304914</commentid>
    <comment_count>3</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-09-10 10:15:59 -0400</bug_when>
    <thetext>This will be fixed along with the patch for bug 407985.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2366197</commentid>
    <comment_count>4</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2014-02-20 12:20:59 -0500</bug_when>
    <thetext>(In reply to Noopur Gupta from comment #3)
&gt; This will be fixed along with the patch for bug 407985.

Fixed with bug 407985.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2367342</commentid>
    <comment_count>5</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2014-02-23 18:21:42 -0500</bug_when>
    <thetext>Verified the functionality in bug 407985 using Kepler SR2 + Java 8 RC1 +   Eclipse Java Development Tools Patch for Java 8 Support (BETA) 1.0.0.v20140220-2054</thetext>
  </long_desc>
      
      

    </bug>
    <bug>
          <bug_id>407985</bug_id>
          
          <creation_ts>2013-05-14 05:16:00 -0400</creation_ts>
          <short_desc>[1.8][extract method] Extract Method refactoring from Lambda Expressions</short_desc>
          <delta_ts>2014-02-23 18:20:02 -0500</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>VERIFIED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>enhancement</bug_severity>
          <target_milestone>BETA J8</target_milestone>
          <dependson>406786</dependson>
    
    <dependson>413592</dependson>
    
    <dependson>416560</dependson>
    
    <dependson>417017</dependson>
          <blocked>405305</blocked>
    
    <blocked>408009</blocked>
          <everconfirmed>1</everconfirmed>
          <reporter name="Noopur Gupta">noopur_gupta@in.ibm.com</reporter>
          <assigned_to name="Noopur Gupta">noopur_gupta@in.ibm.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>manju656@gmail.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
    
    <cc>michal.piotrkowski@pragmatists.pl</cc>
    
    <cc>noopur_gupta@in.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706889-n-z8c2d4_sGiXkR64-t-F_AL59O2nfUfegx-TKmvGnk</token>

      

      <flag name="review"
          id="59341"
          type_id="1"
          status="+"
          setter="markus_keller@ch.ibm.com"
    />

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2256540</commentid>
    <comment_count>0</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-05-14 05:16:19 -0400</bug_when>
    <thetext>Consider the following having lambda expressions: Class X and Interface I2.
We get exception or incorrect refactoring by performing &quot;Extract Method&quot; refactoring on the lines with comments.

It should be possible to extract methods from a lambda expression, which would be created in its enclosing type.

@FunctionalInterface
public interface I1 {
	int foo(int a);
}

// Error: Extracted to m1() and placed in enclosing type. 
// But replaced with &quot;m1();&quot; instead of &quot;int b= m1();&quot;
class X {
	I1 i1= (int a) -&gt; {
		int b= 10; // Error
		return a + b;
	};
	
	class Y {
		I1 i1= (int a) -&gt; {
			int b= 10; // Error
			return a + b;
		};
	}
	
	void foo() {
		I1 i1= (int a) -&gt; {
			int b= 10; // Error
			return a + b;
		};
	}
	
	void bar() {
		Runnable r= new Runnable() {
			I1 i1= (int a) -&gt; {
				int b= 10; // Error
				return a + b;
			};
			
			@Override
			public void run() {
				I1 i1= (int a) -&gt; {
					int b= 10; // Error
					return a + b;
				};				
			}
		};
	}
}

// see bug 406786 for Extract Method from lambda expr in interfaces
interface I2 {	
	I1 i1= (int a) -&gt; {
		int b= 10; // Exception on extracting to method
		return a + b;
	};	
}</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2256591</commentid>
    <comment_count>1</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-05-14 07:15:52 -0400</bug_when>
    <thetext>Another case is when we have an inferred type parameter in lambda expression and we use it in an expression, being extracted to a method. 
We get &quot;Unknown VariableDeclaration&quot; exception.

Example:

class Y {
	I1 i = (a) -&gt; { 
		int b= a; //  Exception(Unknown VariableDeclaration)
		return b;
	};
}</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2297753</commentid>
    <comment_count>2</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-08-22 06:30:08 -0400</bug_when>
    <thetext>(In reply to comment #0)
&gt; // see bug 406786 for Extract Method from lambda expr in interfaces
&gt; interface I2 {	
&gt; 	I1 i1= (int a) -&gt; {
&gt; 		/*[*/ int b= 10; /*]*/ // Exception on extracting to method
&gt; 		return a + b;
&gt; 	};	
&gt; }

After bug 406786 is fixed, there will not be any exception in the above example.
The code will be extracted to a static method in I2 and now the issue will be as in the other examples of comment #0:
&gt; // But replaced with &quot;m1();&quot; instead of &quot;int b= m1();&quot;</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2300442</commentid>
    <comment_count>3</comment_count>
      <attachid>234907</attachid>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-08-29 05:22:49 -0400</bug_when>
    <thetext>Created attachment 234907
Patch for exception in comment #1

(In reply to comment #1)
&gt; Another case is when we have an inferred type parameter in lambda expression
&gt; and we use it in an expression, being extracted to a method. 
&gt; We get &quot;Unknown VariableDeclaration&quot; exception.
&gt; 
&gt; Example:
&gt; 
&gt; class Y {
&gt; 	I1 i = (a) -&gt; { 
&gt; 		/*[*/ int b= a; /*]*/ //  Exception(Unknown VariableDeclaration)
&gt; 		return b;
&gt; 	};
&gt; }

The attached patch fixes the issue mentioned above i.e. now there will not be any exception in the above example. The code will be extracted to a method in Y and now the issue will be as in the other examples of comment #0:
&gt; // replaced with &quot;m1(a);&quot; instead of &quot;int b= m1(a);&quot;

Markus, please have a look.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2301228</commentid>
    <comment_count>4</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-08-30 07:45:50 -0400</bug_when>
    <thetext>Some more cases:

1. 
@FunctionalInterface
public interface I {
	int foo(int a);
}

class C_Test {

	// [1] Error - return type of new method is void, should be int
	I i= a -&gt; {
		/*[*/ return a++; /*]*/ 
	};
	
	String foo() {
		// [2] Error - return type of new method is String, should be int
		I i= a -&gt; {
			/*[*/ return a++; /*]*/ 	
		};
	
		return &quot;&quot;;
	}	
}

This is because the valid enclosing body declarations for method extraction are method declaration, field declaration and initializer only.
Hence, on extracting a return statement in a lambda expr, the return type of the corresponding enclosing body decl is checked, which is null in case [1] (for field) and String in case [2] (for method).

If the return stmt being extracted is within a lambda expr, return type of lambda expr should be considered instead of the enclosing body decl&apos;s return type.

2.
@FunctionalInterface
public interface J {
	void foo();
}

class X1 {
	J j1= () -&gt; {
		/*[*/ return; /*]*/ 
	};
}

Results in =&gt;

class X1 {
	J j1= () -&gt; {
		extracted();
		return; // Bug - &apos;return;&apos; not removed.
	};

	private void extracted() {
		/*[*/ return; /*]*/
	}
}</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2305294</commentid>
    <comment_count>5</comment_count>
      <attachid>235376</attachid>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-09-11 04:45:46 -0400</bug_when>
    <thetext>Created attachment 235376
Patch + Tests

- The patch is created from ngupta/BETA_JAVA8 branch for:
http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?h=ngupta/BETA_JAVA8&amp;id=7da82302f552442f5453a887781bf468047f8d44
It depends on the patch for bug 406786 and patch given for comment #1.

- Added the following important methods:
* ExtractMethodAnalyzer#endVisit(FieldDeclaration) to prevent CCE when only a variable declaration fragment is extracted from field declaration.
* ExtractMethodAnalyzer#visit(LambdaExpression) to allow extraction only at valid locations in lambda expr and handle bug 408009. 
* ASTNodeFactory#newReturnType(LambdaExpression, AST, ImportRewrite, ImportRewriteContext) to get the Type node for return type of lambda expr.
* ASTResolving#findEnclosingLambdaExpression(ASTNode node)

- Paste the given example in package explorer and edit the file (example: change /*a*/ to /*b*/).
Select lambda expr &quot;(int n1, int n2) -&gt; n1 * n2&quot; and extract it to a method.
The extracted method takes unnecessary param &quot;int n1&quot; and will have compilation error which is due to bug 416560.
-------------------------------
package misc.test;

interface FI {
	int foo(int s1, int s2);
}

class Test {
	FI fi= /*a*/ (int n1, int n2) -&gt; n1 * n2;
}
------------------------------- 

- TODO: Update tests with formatted default methods, once bug 413592 is fixed.

Markus, please have a look.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2305483</commentid>
    <comment_count>6</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-09-11 11:52:42 -0400</bug_when>
    <thetext>Another test case to be added after bug 417017 is fixed, which currently produces wrong parameter type for the extracted method:

@FunctionalInterface
interface FI {
	int foo1(int a);
}

class FI_1 {
	void fun(int a) {
		FI i1 = x1-&gt; x1;
		FI i2 = xxx-&gt; {
			i1.foo1(a);
			/*]*/return xxx;/*[*/
		};
	}
}</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2312983</commentid>
    <comment_count>7</comment_count>
      <attachid>236009</attachid>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-10-01 09:28:24 -0400</bug_when>
    <thetext>Created attachment 236009
Patch with updated tests

(In reply to Noopur Gupta from comment #5)
&gt; - TODO: Update tests with formatted default methods, once bug 413592 is
&gt; fixed.
Updated the tests with formatted default methods, added the test case from comment #6, updated fReturnTypeBinding for lambda expr.

- The patch is created from ngupta/BETA_JAVA8 branch for:
http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?h=ngupta/BETA_JAVA8&amp;id=fb4597d2163679af8202c37f5efc73a96ffa7db7
It depends on the patch given in comment #5.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2357762</commentid>
    <comment_count>8</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2014-02-03 03:38:59 -0500</bug_when>
    <thetext>(In reply to Noopur Gupta from comment #5)
&gt; - Paste the given example in package explorer and edit the file (example:
&gt; change /*a*/ to /*b*/).
&gt; Select lambda expr &quot;(int n1, int n2) -&gt; n1 * n2&quot; and extract it to a method.
&gt; The extracted method takes unnecessary param &quot;int n1&quot; and will have
&gt; compilation error which is due to bug 416560.

Verified that the above issue is not reproducible after bug 416560 is fixed.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2366175</commentid>
    <comment_count>9</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2014-02-20 11:59:29 -0500</bug_when>
    <thetext>Released to BETA_JAVA8 with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=f09aabc28fa041d926f45d21e601d4fac0e59812 and parent commit.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2367341</commentid>
    <comment_count>10</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2014-02-23 18:20:02 -0500</bug_when>
    <thetext>Verified using Kepler SR2 + Java 8 RC1 +   Eclipse Java Development Tools Patch for Java 8 Support (BETA) 1.0.0.v20140220-2054</thetext>
  </long_desc>
      
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>234907</attachid>
            <date>2013-08-29 05:22:00 -0400</date>
            <delta_ts>2013-08-29 05:22:49 -0400</delta_ts>
            <desc>Patch for exception in comment #1</desc>
            <filename>bug407985comment1.patch</filename>
            <type>text/plain</type>
            <size>5272</size>
            <attacher name="Noopur Gupta">noopur_gupta@in.ibm.com</attacher>
            
              <token>1425706889-A6lacsDCVOXvLiwF4UMtKklcixENoWGTj4OVVMhkJr8</token>

          </attachment>
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>235376</attachid>
            <date>2013-09-11 04:45:00 -0400</date>
            <delta_ts>2013-09-11 04:45:46 -0400</delta_ts>
            <desc>Patch + Tests</desc>
            <filename>Fixed-bug-407985-18-Extract-Method-Lambda.patch</filename>
            <type>text/plain</type>
            <size>56852</size>
            <attacher name="Noopur Gupta">noopur_gupta@in.ibm.com</attacher>
            
              <token>1425706889-sy0F0TkjAG6JDHjkzstaplia20VhW2RILaxia9e82D8</token>

          </attachment>
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>236009</attachid>
            <date>2013-10-01 09:28:00 -0400</date>
            <delta_ts>2013-10-01 09:28:24 -0400</delta_ts>
            <desc>Patch with updated tests</desc>
            <filename>Fixed-bug-407985-18-Extract-Method-lambda-Updated.patch</filename>
            <type>text/plain</type>
            <size>5155</size>
            <attacher name="Noopur Gupta">noopur_gupta@in.ibm.com</attacher>
            
              <token>1425706889-oifxI8eatzQOJJuGw_vNXN0pSGGtDvDp4KTtlbEcsPY</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>407382</bug_id>
          
          <creation_ts>2013-05-07 06:15:00 -0400</creation_ts>
          <short_desc>[type wizards] NPE on content assist for a new workspace</short_desc>
          <delta_ts>2013-05-13 04:23:08 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>VERIFIED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>normal</bug_severity>
          <target_milestone>4.3 RC1</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Noopur Gupta">noopur_gupta@in.ibm.com</reporter>
          <assigned_to name="Dani Megert">daniel_megert@ch.ibm.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706889-8ZNMB7PVOvkOQXuMi6mslP1sjKOsrknFkSAkagGZtzI</token>

      

      <flag name="review"
          id="57104"
          type_id="1"
          status="+"
          setter="markus_keller@ch.ibm.com"
    />

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2253235</commentid>
    <comment_count>0</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-05-07 06:15:43 -0400</bug_when>
    <thetext>1. Open a new workspace.
2. Go to File -&gt; New -&gt; Class. (Open any New type wizard).
3. Check &quot;Enclosing type&quot;.
4. Press Ctrl+Space in the text field of Enclosing type.
We get an exception in Error Log view.

org.eclipse.e4.core.di.InjectionException: java.lang.NullPointerException
	at org.eclipse.e4.core.internal.di.MethodRequestor.execute(MethodRequestor.java:63)
....
Caused by: java.lang.NullPointerException
	at org.eclipse.jdt.internal.ui.refactoring.contentassist.CUPositionCompletionProcessor.computeCompletionProposals(CUPositionCompletionProcessor.java:159)</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2253316</commentid>
    <comment_count>1</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-05-07 08:40:10 -0400</bug_when>
    <thetext>No regression.

The underlying issue is bug 43825. Since we won&apos;t work on that bug, we should simply protect against the NPE.

This is easy enough to qualify for RC1.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2253331</commentid>
    <comment_count>2</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-05-07 08:55:57 -0400</bug_when>
    <thetext>+1 for RC1.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2253893</commentid>
    <comment_count>3</comment_count>
      <attachid>230636</attachid>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-05-08 05:23:12 -0400</bug_when>
    <thetext>Created attachment 230636
Fix</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2254115</commentid>
    <comment_count>4</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-05-08 10:33:47 -0400</bug_when>
    <thetext>Released patch: http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=eaba6982dc2b001ff0b88f52be3aebd19350e66c</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2255816</commentid>
    <comment_count>5</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-05-13 04:23:08 -0400</bug_when>
    <thetext>Verified in I20130512-2000.</thetext>
  </long_desc>
      
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>230636</attachid>
            <date>2013-05-08 05:23:00 -0400</date>
            <delta_ts>2013-05-08 05:23:12 -0400</delta_ts>
            <desc>Fix</desc>
            <filename>eclipse.jdt.ui.patch</filename>
            <type>text/plain</type>
            <size>1478</size>
            <attacher name="Dani Megert">daniel_megert@ch.ibm.com</attacher>
            
              <token>1425706890-685rC3kJ0gELcnXhYj1QtTSRUy0nHJD0SJWI783ybmk</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>407056</bug_id>
          
          <creation_ts>2013-05-02 05:53:00 -0400</creation_ts>
          <short_desc>[1.8] Support PackageQualifiedType AST node</short_desc>
          <delta_ts>2014-02-07 19:25:02 -0500</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>normal</bug_severity>
          <target_milestone>BETA J8</target_milestone>
          <dependson>403924</dependson>
    
    <dependson>404489</dependson>
    
    <dependson>406469</dependson>
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Markus Keller">markus_keller@ch.ibm.com</reporter>
          <assigned_to name="Manju Mathew">manju656@gmail.com</assigned_to>
          <cc>markus_keller@ch.ibm.com</cc>
    
    <cc>noopur_gupta@in.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706890-GzHrAdwlXuZbqFr5pAKR9V37KvquGHZuNq9wmvt23f8</token>

      

      <flag name="review"
          id="59823"
          type_id="1"
          status="+"
          setter="markus_keller@ch.ibm.com"
    />

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2251403</commentid>
    <comment_count>0</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-05-02 05:53:34 -0400</bug_when>
    <thetext>Support the new PackageQualifiedType AST node from bug 404489 in JDT UI.

The node occurs when a type-use annotation is added to a package-qualified type. Before, such types were represented as SimpleType(QualifiedName).

See the explanations in the Javadoc of QualifiedType in BETA_JAVA8.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2251405</commentid>
    <comment_count>1</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-05-02 06:00:50 -0400</bug_when>
    <thetext>Note that ASTRewrite has not yet been implemented for this node (bug 406469). But we can still start with identifying problem areas and working on solutions.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2261480</commentid>
    <comment_count>2</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-05-23 08:41:25 -0400</bug_when>
    <thetext>The issue to be tackled with this bug is to fix all the places where we currently assume the SimpleType(QualifiedName) structure. I.e. ASTVisitors and any other code that:
- assumes it knows it gets a SimpleType(QualifiedName), but now gets a PackageQualifiedType
- assumes that the parent of a QualifiedName or a SimpleName must be one of the old a subtypes of Type, but now it can also be a PackageQualifiedType</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2268104</commentid>
    <comment_count>3</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-06-05 01:38:00 -0400</bug_when>
    <thetext>Updated the potential locations where PackageQualifiedType can occur in JDT UI except in #thrownExceptionTypes. Need to perform one more round of checking once the bug 403924 which deals with updating MethodDeclaration#thrownExceptions() with MethodDeclaration#thrownExceptionTypes() is resolved. #thrownExceptionTypes() can return a List with SimpleType and PackageQualifiedType. Hence i&apos;m holding the patch for the time being.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2277625</commentid>
    <comment_count>4</comment_count>
      <attachid>232819</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-06-27 00:55:59 -0400</bug_when>
    <thetext>Created attachment 232819
WIP Patch

This is a WIP patch. Uploading this in case Noopur you have time to look into it once bug 403923 is completed.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2277626</commentid>
    <comment_count>5</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-06-27 00:57:01 -0400</bug_when>
    <thetext>I meant bug 403924 in my previous comment.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2324226</commentid>
    <comment_count>6</comment_count>
      <attachid>236994</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-10-29 02:29:40 -0400</bug_when>
    <thetext>Created attachment 236994
Patch created against BETA_JAVA8 ws

I have created the patch after updating most of the potential locations where PackageQualifiedType can occur in JDT UI. Below are the files where SimpleType(QualifiedName/SimpleName) usage appears but I have ignored them as I felt PackageQualifiedType could not occur in those scenario. Listing the files ignored for verification.
=&gt; ASTNodeFactory.java (2 matches): 
	-&gt; 286: if (type instanceof SimpleType) { 
	-&gt; 354: if (type instanceof SimpleType) { 
In the above locations, type is created via ImportRewrite.addImport(..) and that never returns a PQT. Hence ignored the occurrence of PQT in the above cases.

=&gt; MoveInnerToTopRefactoring.java (3 matches) -&gt; Here the QualifiedName of a SimpleType is used to handle the import statement, hence ignoring the occurrence of PQT at this place.

=&gt; Java50Fix.java#isRawTypeReference(ASTNode) -&gt; This method handles only a SimpleType. What is the usecase, is it possibe that the type can be a PackageQualifiedType at this point?</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2346296</commentid>
    <comment_count>7</comment_count>
      <attachid>238708</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2014-01-06 22:28:50 -0500</bug_when>
    <thetext>Created attachment 238708
Updated Patch

Patch updated. Created against BETA_JAVA8 branch as per bug 424920.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2350310</commentid>
    <comment_count>8</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2014-01-15 19:47:37 -0500</bug_when>
    <thetext>(In reply to Manju Mathew from comment #6)
&gt; =&gt; ASTNodeFactory.java (2 matches): 
&gt; 	-&gt; 286: if (type instanceof SimpleType) { 
&gt; 	-&gt; 354: if (type instanceof SimpleType) { 
&gt; In the above locations, type is created via ImportRewrite.addImport(..) and
&gt; that never returns a PQT. Hence ignored the occurrence of PQT in the above
&gt; cases.

The above assumption would be wrong after bug 417937 is fixed. ImportRewrite.addImport(..) can return a NQT.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2360488</commentid>
    <comment_count>9</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2014-02-07 19:25:02 -0500</bug_when>
    <thetext>Released Manju&apos;s patch with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=815164b3b52c2daf5d745ad9399c77ceb9c881fa and my additions with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=f9694bfb4ba224ca3ff558a3eef89f9433b055e5

(In reply to Manju Mathew from comment #8)
&gt; The above assumption would be wrong after bug 417937 is fixed.
&gt; ImportRewrite.addImport(..) can return a NQT.

That&apos;s correct in general, but we know this can&apos;t happen for an annotation type, because the grammar doesn&apos;t allow type annotations on such a type name reference.
The newAnnotation(..) methods have been moved into ImportRewrite, where it&apos;s safe to keep this assumption.</thetext>
  </long_desc>
      
          <attachment
              isobsolete="1"
              ispatch="1"
              isprivate="0"
          >
            <attachid>232819</attachid>
            <date>2013-06-27 00:55:00 -0400</date>
            <delta_ts>2013-10-29 02:29:40 -0400</delta_ts>
            <desc>WIP Patch</desc>
            <filename>eclipse.jdt.ui.4thJune.patch</filename>
            <type>text/plain</type>
            <size>50889</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706890-1kFI-1Y2ZNMFK9VcUzdKOBZxj-n3OJ8h1NicFMHNsRE</token>

          </attachment>
          <attachment
              isobsolete="1"
              ispatch="1"
              isprivate="0"
          >
            <attachid>236994</attachid>
            <date>2013-10-29 02:29:00 -0400</date>
            <delta_ts>2014-01-06 22:28:50 -0500</delta_ts>
            <desc>Patch created against BETA_JAVA8 ws</desc>
            <filename>eclipse.jdt.ui.v2.patch</filename>
            <type>text/plain</type>
            <size>25663</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706890-XuFWLJ_ZFIKwIK_nXjT9sG2fj7hPsXytVXIRm2-9UQU</token>

          </attachment>
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>238708</attachid>
            <date>2014-01-06 22:28:00 -0500</date>
            <delta_ts>2014-01-06 22:28:50 -0500</delta_ts>
            <desc>Updated Patch</desc>
            <filename>eclipse.jdt.ui.v3.patch</filename>
            <type>text/plain</type>
            <size>27639</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706890-ydnTqc93AYYrXYJov7_Xu3HpecLtY-fEqU1dc8ck6So</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>406976</bug_id>
          
          <creation_ts>2013-05-01 06:59:00 -0400</creation_ts>
          <short_desc>[JUnit] Improve icons for ignored and assumption failed test</short_desc>
          <delta_ts>2013-05-02 02:40:16 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>VERIFIED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>minor</bug_severity>
          <target_milestone>4.3 M7</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Dani Megert">daniel_megert@ch.ibm.com</reporter>
          <assigned_to name="Markus Keller">markus_keller@ch.ibm.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706890-ukaT3Nhz0JGu8rpCyiOxNSCEY6hDZK7xk5l31ao5IYY</token>

      

      

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2250973</commentid>
    <comment_count>0</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-05-01 06:59:26 -0400</bug_when>
    <thetext>I20130430-2000.

The icons for ignored and assumption failed test should use the &apos;/org.eclipse.jdt.ui/icons/full/ovr16/ignore_optional_problems_ovr.gif&apos; decorator instead of crossing out the &quot;normal&quot; icon.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2251210</commentid>
    <comment_count>1</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-05-01 15:22:57 -0400</bug_when>
    <thetext>Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=cf3b1e0557cf1dfa6e51ae0572b8b24d58a6d378</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2251341</commentid>
    <comment_count>2</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-05-02 02:40:16 -0400</bug_when>
    <thetext>Verified in I20130501-2000. Nice!</thetext>
  </long_desc>
      
      

    </bug>
    <bug>
          <bug_id>406786</bug_id>
          
          <creation_ts>2013-04-29 07:44:00 -0400</creation_ts>
          <short_desc>[1.8][extract method] Extract Method refactoring in interfaces not handled</short_desc>
          <delta_ts>2014-02-23 19:35:14 -0500</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>VERIFIED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>enhancement</bug_severity>
          <target_milestone>BETA J8</target_milestone>
          <dependson>413592</dependson>
          <blocked>405305</blocked>
    
    <blocked>407985</blocked>
          <everconfirmed>1</everconfirmed>
          <reporter name="Noopur Gupta">noopur_gupta@in.ibm.com</reporter>
          <assigned_to name="Noopur Gupta">noopur_gupta@in.ibm.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>manju656@gmail.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
    
    <cc>noopur_gupta@in.ibm.com</cc>
    
    <cc>timo.kinnunen@gmail.com</cc>
          
          <votes>0</votes>

      
          <token>1425706890-PAnwm-s8lJ8FQfMdMoJ1xfgSqvdRkytXTLtmqnBun5s</token>

      

      <flag name="review"
          id="59107"
          type_id="1"
          status="+"
          setter="markus_keller@ch.ibm.com"
    />

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2249727</commentid>
    <comment_count>0</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-04-29 07:44:40 -0400</bug_when>
    <thetext>Consider the following interfaces: I2 (having lambda expression) and I3 (having default and static methods). 
Perform &quot;Extract Method&quot; refactoring on the lines with comments. We get exception and no refactoring is performed.
It should be possible to extract methods in interfaces which would be created as default or static methods in those interfaces.

@FunctionalInterface
public interface I1 {
	int foo(int a);
}

interface I2 {
	I1 i1= (a) -&gt; {
		int b= 10; // Exception on extracting to method
		return a + b;
	};
}

interface I3 {
	default int foo () {
		int a= 10; // Exception on extracting to method
		return a;
	}
	
	static int bar() {
		int a= 10; // Exception on extracting to method
		return a;
	}
}</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2276995</commentid>
    <comment_count>1</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-06-25 13:28:22 -0400</bug_when>
    <thetext>*** Bug 411608 has been marked as a duplicate of this bug. ***</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2283225</commentid>
    <comment_count>2</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-07-11 06:40:51 -0400</bug_when>
    <thetext>If the method is being extracted from a default method, then the extracted method will be default; otherwise it will be static.
 
Some open points regarding the expected behavior:
 
1. Access Modifier radio buttons:
If Destination type while opening the wizard is an interface, should &apos;public&apos; be selected by default with all radio buttons disabled, or should we hide the access modifier composite itself?
And, when user changes the Destination type from an interface to non-interface and vice-versa, the composite would need to be updated accordingly.
 
2. When the expr being extracted from a default method, is also present in a static method and &quot;Replace additional occurrences...&quot; is checked, we get compilation error after refactoring since the new default method cannot be accessed from the static method. 
The same issue already happens in a class also.
 
3. Currently if we try to extract a method from a field initialization expr in an interface for source level &lt; 1.8, we get NPE.
We can add a check and show error message &quot;Cannot extract to an interface.&quot; in this case.
  
Markus, please share your thoughts.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2283266</commentid>
    <comment_count>3</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-07-11 08:24:06 -0400</bug_when>
    <thetext>&gt; 1. Access Modifier radio buttons:

We should keep the access modifier composite, but disable the modifiers that are not allowed for the selected destination. If the destination is an interface, then the extracted method should have the same keyword modifiers as the source method (i.e. if the original doesn&apos;t have a &apos;public&apos; keyword, then the extracted method also shouldn&apos;t have it, although &apos;public&apos; was selected in the UI).

&gt; 2. When the expr being extracted from a default method, ...

Yeah, that&apos;s bug 393098. The &quot;default method&quot; variant can also be handled there.

&gt; 3. Currently if we try to extract a method from a field initialization expr
&gt; in an interface for source level &lt; 1.8, we get NPE.
&gt; We can add a check and show error message &quot;Cannot extract to an interface.&quot;
&gt; in this case.

Yes, please do that.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2297765</commentid>
    <comment_count>4</comment_count>
      <attachid>234655</attachid>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-08-22 07:01:01 -0400</bug_when>
    <thetext>Created attachment 234655
Patch + Tests

Patch contains the following major changes:

- ExtractMethodInputPage.java:
* If destination is an interface, all access modifiers in the wizard should be disabled and &apos;public&apos; should be selected.
The access modifier setting for next invocation of the wizard should not be changed by the earlier forced &apos;public&apos; for interface.
---------------------------------
- ExtractMethodRefactoring.java
* createChange(..) : Updated since the first type in destinations list need not be the direct parent type of code being extracted. Example:
class C {
    @interface A {
    	int i= /*[*/0;/*]*/	
    }
}
* initializeDestinations() : Updated so that combo displays only valid destination types.
* createNewMethodDeclaration() : 
  - If the user extracts an expression from a method into the directly enclosing interface, the extracted method has &apos;public&apos; iff the enclosing method also was public.
  - New method will be &apos;static&apos; if any of its ancestor nodes up to the destination type (excluding the destination) is static. In case of interface as destination, if method is not &apos;static&apos; then it will be &apos;default&apos;.
---------------------------------
- ExtractMethodAnalyzer.java:
* isValidDestination(ASTNode) : To check for interfaces &lt; 1.8 and annotation types.
* checkInitialConditions(ImportRewrite) : check if any valid destination type exists for extraction, otherwise return with error.
* checkInput(RefactoringStatus, String, ASTNode) : Existing impl ignored the methods from direct super-interfaces hierarchies of destination type, added check for that. And added null check for super-class in interface.
---------------------------------
- Checks.java:
* checkMethodInType(ITypeBinding, String, ITypeBinding[]) : Updated as constructor warning is already added and it is not an &apos;error&apos; to have a method with same name as constructor.
* checkMethodInHierarchy(ITypeBinding, String, ITypeBinding, ITypeBinding[]) : Added a different explicit warning message for constructors.
---------------------------------
- ASTResolving.java:
* Updated javadocs of #findParentType(..) methods.
---------------------------------
- TODO:
* Update test cases with formatted default methods (instead of the unformatted ones currently), once bug 413592 is fixed.
---------------------------------
- This patch also contains changes from bug 403924 in ExtractMethodRefactoring.java.

Markus, please have a look.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2312947</commentid>
    <comment_count>5</comment_count>
      <attachid>236008</attachid>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-10-01 08:25:10 -0400</bug_when>
    <thetext>Created attachment 236008
Patch + Tests

(In reply to Noopur Gupta from comment #4)
&gt; - TODO:
&gt; * Update test cases with formatted default methods (instead of the
&gt; unformatted ones currently), once bug 413592 is fixed.

Updated the tests with formatted default methods.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2349976</commentid>
    <comment_count>6</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2014-01-15 09:08:40 -0500</bug_when>
    <thetext>*** Bug 425759 has been marked as a duplicate of this bug. ***</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2350345</commentid>
    <comment_count>7</comment_count>
      <attachid>239048</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2014-01-15 22:11:21 -0500</bug_when>
    <thetext>Created attachment 239048
Patch + Tests


(In reply to Markus Keller from comment #3)
&gt; &gt; 2. When the expr being extracted from a default method, ...
&gt; 
&gt; Yeah, that&apos;s bug 393098. The &quot;default method&quot; variant can also be handled
&gt; there.
This patch handles the case when code is extracted from default method and the duplicate code is present in static method also. The fix was given in bug 393098, i have merged the changes from master and added a testcase. The patch is checked in to mmathew/BETA_JAVA8 branch.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2366176</commentid>
    <comment_count>8</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2014-02-20 11:59:33 -0500</bug_when>
    <thetext>Released all necessary commits to BETA_JAVA8, see http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=c656ba52079370b803406e5b65ffe3b2c3f6e8f6 and 4 parent commits.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2367348</commentid>
    <comment_count>9</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2014-02-23 19:35:14 -0500</bug_when>
    <thetext>Verified using Kepler SR2 + Java 8 RC1 +   Eclipse Java Development Tools Patch for Java 8 Support (BETA) 1.0.0.v20140220-2054</thetext>
  </long_desc>
      
          <attachment
              isobsolete="1"
              ispatch="1"
              isprivate="0"
          >
            <attachid>234655</attachid>
            <date>2013-08-22 07:01:00 -0400</date>
            <delta_ts>2013-10-01 08:25:10 -0400</delta_ts>
            <desc>Patch + Tests</desc>
            <filename>Bug-406786-ExtractMethod-refactoring.patch</filename>
            <type>text/plain</type>
            <size>66937</size>
            <attacher name="Noopur Gupta">noopur_gupta@in.ibm.com</attacher>
            
              <token>1425706890-xQobLteVoS3l6CcaOl7aQ4mk81UrtES6HP-bOPe1gm8</token>

          </attachment>
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>236008</attachid>
            <date>2013-10-01 08:25:00 -0400</date>
            <delta_ts>2013-10-01 08:25:10 -0400</delta_ts>
            <desc>Patch + Tests</desc>
            <filename>Fixed-bug-406786-18-extract-method-in-interface.patch</filename>
            <type>text/plain</type>
            <size>68029</size>
            <attacher name="Noopur Gupta">noopur_gupta@in.ibm.com</attacher>
            
              <token>1425706890-_0g4E2oKQSoQ3hBO7PVwuwF641FQYxo95UM03v8Hv3k</token>

          </attachment>
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>239048</attachid>
            <date>2014-01-15 22:11:00 -0500</date>
            <delta_ts>2014-01-15 22:11:21 -0500</delta_ts>
            <desc>Patch + Tests</desc>
            <filename>Fixed-Bug-406786-18extract-method-Extract-Method-ref.patch</filename>
            <type>text/plain</type>
            <size>3515</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706890-1lc4LVUyxtbQ82Ov3VJQhpr_h0Nt_YwFm3hbwTiDfk8</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>406274</bug_id>
          
          <creation_ts>2013-04-23 01:54:00 -0400</creation_ts>
          <short_desc>[1.8][extract interface] Invoking &apos;Extract Interface&apos; on an interface with default method results in losing the default method implementation.</short_desc>
          <delta_ts>2014-04-03 18:41:43 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>enhancement</bug_severity>
          <target_milestone>4.4 M7</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Manju Mathew">manju656@gmail.com</reporter>
          <assigned_to name="Manju Mathew">manju656@gmail.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
    
    <cc>noopur_gupta@in.ibm.com</cc>
    
    <cc>pbenedict@apache.org</cc>
          
          <votes>0</votes>

      
          <token>1425706890-uhPBU01TCoZ9s8liZ4zEIiNMs2_jWJKZ4HfrCz3o6bs</token>

      

      <flag name="review"
          id="58929"
          type_id="1"
          status="+"
          setter="markus_keller@ch.ibm.com"
    />
    <flag name="review"
          id="58936"
          type_id="1"
          status="+"
          setter="noopur_gupta@in.ibm.com"
    />

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2247108</commentid>
    <comment_count>0</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-04-23 01:54:37 -0400</bug_when>
    <thetext>Consider the below interface
package p1;

public interface I1 {	
	 default int defaultMethod(){
		 return 10;
	 }	
}

Invoke &apos;Refactor-&gt; Extract Interface...&apos; on I1. Select #defaultMethod to be part of the new interface. Click &apos;OK&apos; button. In the newly created interface the method is created as abstract and in the original interface the method is removed. So basically the method implementation is lost after refactoring.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2271752</commentid>
    <comment_count>1</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-06-12 07:40:43 -0400</bug_when>
    <thetext>In the current implementation of &apos;Extract Interface&apos;, the criteria for a method to be extract-able is:
case IJavaElement.METHOD:
     return JdtFlags.isPublic(member) &amp;&amp; !JdtFlags.isStatic(member) &amp;&amp; !((IMethod) member).isConstructor();

Can we allow default methods be part of extract-able interface methods?

While checking the current implementation, I came across this method JdtFlags#isAbstract(member). I passed a static method and it returned &apos;true&apos;. Looked in to this method, if the member is a method and if the declaring type is an interface then it says the method is abstract. This is wrong with Java8. I did not find an existing bug in 1.8 which is taking care of it. If not, then shall i update that method  as part of this bug fix?</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2272754</commentid>
    <comment_count>2</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-06-14 07:11:21 -0400</bug_when>
    <thetext>&gt; Can we allow default methods be part of extract-able interface methods?

Yes.

&gt; JdtFlags#isAbstract(member). I passed a static method and it returned &apos;true&apos;.

Yes, that needs to be fixed. Make sure that the fix is also correct if the member has source level &lt; 1.8. Remember that it needs to work for source methods (where IMethod#getFlags() only returns explicit flags) and for binary methods (where it returns implicit flags as well).

Please make a pass over all methods in JdtFlags and adjust them for JSR 308. This can be done as part of this bug. Then open a new bug to check all references to the methods you changed (maybe some other clients need adjustments now).</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2274259</commentid>
    <comment_count>3</comment_count>
      <attachid>232526</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-06-19 04:25:31 -0400</bug_when>
    <thetext>Created attachment 232526
Patch with testcases.

With this patch, &apos;Extract Interface&apos; refactoring allows to extract default methods also from interfaces. The default method body is preserved in the extracted interface. If &apos;Extract Interface&apos; is invoked from a class, then the method will be extracted as abstract just as it was earlier.

Added few testcases for the above scenario.

Since I did not use JDTFlags for this patch, the updated JDTFlags will be uploaded as a separate patch.

@Noopur can you take a look at the patch?</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2274272</commentid>
    <comment_count>4</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-06-19 04:53:26 -0400</bug_when>
    <thetext>I overlooked one condition:
public interface I {
	public static final int count = 10;
	public default void defaultMethod() {		
		System.out.println(count);			
	}
}
When &apos;Extract Interface&apos; is invoked on &apos;I&apos; and if user selects only the default method, then after refactoring we end up with compiler error as the field &apos;count &apos; is not accessible. Should this field be made part of the newly extracted interface during refactoring to avoid compiler error?
Since it is bad to leave user with a compiler error after refactoring, i suggest we should take care of including the field also during refactoring.
 
Even worse case:
public interface I1 {
	public static final int count = 10;
}
public interface I2 extends I1 {
	public default void defaultMethod() {		
		System.out.println(count);			
	}
}</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2289129</commentid>
    <comment_count>5</comment_count>
      <attachid>233884</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-07-29 08:06:36 -0400</bug_when>
    <thetext>Created attachment 233884
Proposed patch+testcases after updating JDTFlags

(In reply to comment #2)
&gt; &gt; JdtFlags#isAbstract(member). I passed a static method and it returned &apos;true&apos;.
&gt; 
&gt; Yes, that needs to be fixed. Make sure that the fix is also correct if the
&gt; member has source level &lt; 1.8. Remember that it needs to work for source
&gt; methods (where IMethod#getFlags() only returns explicit flags) and for
&gt; binary methods (where it returns implicit flags as well).
&gt; 
&gt; Please make a pass over all methods in JdtFlags and adjust them for JSR 308.
&gt; This can be done as part of this bug. Then open a new bug to check all
&gt; references to the methods you changed (maybe some other clients need
&gt; adjustments now).
As mentioned in the above comment JDTFlags is modified. Added two new methods to identify whether a method is default. Attaching the testcases.
Markus, kindly review the patch for the changes in JDTFlags.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2289696</commentid>
    <comment_count>6</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-07-30 09:51:49 -0400</bug_when>
    <thetext>Noopur, can you please review comment 5?</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2290011</commentid>
    <comment_count>7</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-07-31 00:45:26 -0400</bug_when>
    <thetext>(In reply to comment #4)
&gt; I overlooked one condition:
&gt; public interface I {
&gt; 	public static final int count = 10;
&gt; 	public default void defaultMethod() {		
&gt; 		System.out.println(count);			
&gt; 	}
&gt; }
&gt; When &apos;Extract Interface&apos; is invoked on &apos;I&apos; and if user selects only the
&gt; default method, then after refactoring we end up with compiler error as the
&gt; field &apos;count &apos; is not accessible. Should this field be made part of the
&gt; newly extracted interface during refactoring to avoid compiler error?
&gt; Since it is bad to leave user with a compiler error after refactoring, i
&gt; suggest we should take care of including the field also during refactoring.
&gt;  
&gt; Even worse case:
&gt; public interface I1 {
&gt; 	public static final int count = 10;
&gt; }
&gt; public interface I2 extends I1 {
&gt; 	public default void defaultMethod() {		
&gt; 		System.out.println(count);			
&gt; 	}
&gt; }

Had a discussion with Markus regarding the above point. It is decided that Extract Interface should create an abstract method in the interface and leave the default method in the selected interface. In a later version, we can then add a UI that looks similar to Pull Up, where the user can select which implementations to move and which methods to declare abstract in the interface.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2290078</commentid>
    <comment_count>8</comment_count>
      <attachid>233968</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-07-31 05:27:49 -0400</bug_when>
    <thetext>Created attachment 233968
Patch with testcases for Extract Interface involving default methods

As discussed, here is the patch for the Extract Interface when default methods are involved. As per this patch, the default implementation remain in the current interface and the method is marked as abstract in the new interface. Thus the actual implementation is not lost.

Markus, please review.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2290143</commentid>
    <comment_count>9</comment_count>
      <attachid>233977</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-07-31 08:23:19 -0400</bug_when>
    <thetext>Created attachment 233977
Test data for the JDTFlags tests

Attaching the test data zip for the patch in comment 5.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2294179</commentid>
    <comment_count>10</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-08-13 08:45:21 -0400</bug_when>
    <thetext>(In reply to comment #6)
&gt; Noopur, can you please review comment 5?

- The condition added for 1.8 in JdtFlags#isStatic(IMember member) will cause the method to return &apos;false&apos; in &gt;= 1.8 for an enum nested in an interface.
interface I {
	enum E {}
}

- For the case where an enum is nested in a class, the existing impl returns false, which is a bug. We should handle it here.
class C {
	enum E {}
}

- Tests can be added for the cases of &apos;enum constants&apos;, &apos;nested enum in an interface&apos; and &apos;nested enum in a class&apos; for #isStatic(..).

- Tests can be added for methods taking IMethodBinding as parameter i.e. isDefaultMethod(IMethodBinding), isAbstract(IMethodBinding), isStatic(IMethodBinding).

- The existing impl of JdtFlags#isAbstract(IMethodBinding member) has unnecessary check for &apos;isInterfaceOrAnnotationMember(member)&apos; which can be removed.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2296782</commentid>
    <comment_count>11</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-08-20 09:07:40 -0400</bug_when>
    <thetext>Thanks Noopur! Incorporated all your review comments.
Removed #isStrictfp() as the method was not correctly implemented and also it is not used anywhere.
Modified #isFinal() to include the condition stated in JLS 7: &quot;An enum type is implicitly final unless it contains at least one enum constant that has a class body.&quot;
Released the fix as: http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?h=BETA_JAVA8&amp;id=9b6dd388609e3db2651daf863440f6280055d31c</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2296920</commentid>
    <comment_count>12</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-08-20 12:17:37 -0400</bug_when>
    <thetext>Added isStatic(BodyDeclaration) in JdtFlags.java and updated the test cases accordingly:
http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?h=BETA_JAVA8&amp;id=9f7bf1712cbc2d04a595b924f1ddb319a292361b</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2297017</commentid>
    <comment_count>13</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-08-20 14:55:12 -0400</bug_when>
    <thetext>(In reply to comment #12)

#isDefaultMethod(IMethodBinding):
- parameter name should be &apos;method&apos;
- member.getModifiers() should be extracted into a local variable
- should return false for foo() in &quot;class C { void foo(){} }&quot;

#isDefaultMethod(IMember):
- why it the parameter not IMethod?

#isEnumTypeFinal(IMember):
- shouldn&apos;t the &quot;&amp;&amp;&quot; in the first condition be an &quot;||&quot;? Easier to understand after applying quick fixes to switch the infix around and pull the negation up:

    if (!(member.getElementType() == IJavaElement.TYPE &amp;&amp; isEnum(member)))
        return false;</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2297041</commentid>
    <comment_count>14</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-08-20 15:43:07 -0400</bug_when>
    <thetext>Comment 13 was for comment 11. This is for comment 12:

#isStatic(BodyDeclaration):

- if (bodyDeclaration.getNodeType() != ASTNode.METHOD_DECLARATION &amp;&amp;
          isInterfaceOrAnnotationMember(bodyDeclaration))
      return true;

  =&gt; Looks wrong: What if bodyDeclaration is an AnnotationTypeMemberDeclaration?

- if (bodyDeclaration instanceof EnumDeclaration ...

  =&gt; Looks incomplete: What if parent is an EnumDeclaration? Better use &quot;instanceof AbstractTypeDeclaration&quot; etc.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2297177</commentid>
    <comment_count>15</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-08-21 05:28:51 -0400</bug_when>
    <thetext>(In reply to comment #13)
Thanks Markus. Incorporated the review comments. Released the fix as: http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?h=BETA_JAVA8&amp;id=8347634ab8f8c99021cfbd82ba6b5b149d7df22b</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2297196</commentid>
    <comment_count>16</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-08-21 06:38:40 -0400</bug_when>
    <thetext>(In reply to comment #14)
Thanks Markus. Updated JdtFlags#isStatic(BodyDeclaration) and associated methods.
Also, added tests for the same.
http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?h=BETA_JAVA8&amp;id=5806dfa2c156de6f156f69d1feb051ca43f3f2e1</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2383447</commentid>
    <comment_count>17</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2014-04-02 07:29:14 -0400</bug_when>
    <thetext>(In reply to Manju Mathew from comment #8)
&gt; Created attachment 233968 [details] [diff]
&gt; Patch with testcases for Extract Interface involving default methods
&gt; 
&gt; As discussed, here is the patch for the Extract Interface when default
&gt; methods are involved. As per this patch, the default implementation remain
&gt; in the current interface and the method is marked as abstract in the new
&gt; interface. Thus the actual implementation is not lost.

The fix looks fine. Some comments:
- update copyright year n remove early draft declaration in all files.
- caller of ExtractInterfaceProcessor#removeDefaultMethods already throws JavaModelException, so you don&apos;t need to catch it.
- return statement in #removeDefaultMethods can be written as:
return methods.toArray(new IMethod[methods.size()]);
- you can also combine #removeDefaultMethods in #getExtractedMethods with a comment for default methods.
- ExtractInterfaceTests18 can extend ExtractInterfaceTests like other 1.8 refactoring test classes.
- In ExtractInterfaceTests18, test methods can be re-ordered to keep #testExtractInterfaceFromInterface1 and #testExtractInterfaceFromInterface2 one after the other.
- The test resources folder can be renamed as &quot;ExtractInterface18&quot; instead of &quot;Refactoring18&quot; to keep it next to &quot;ExtractInterface&quot; folder.
- Check if tests for testExtractInterfaceFromAbstractClass and testExtractInterfaceFromClass are required as these should already be present in &quot;ExtractInterface&quot; tests. Otherwise, move them to ExtractInterfaceTests  and &quot;ExtractInterface&quot; folder as these are not 1.8 specific.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2383860</commentid>
    <comment_count>18</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2014-04-02 21:12:31 -0400</bug_when>
    <thetext>(In reply to Noopur Gupta from comment #17)

&gt; The fix looks fine. Some comments:
&gt; - Check if tests for testExtractInterfaceFromAbstractClass and
&gt; testExtractInterfaceFromClass are required as these should already be
&gt; present in &quot;ExtractInterface&quot; tests. Otherwise, move them to
&gt; ExtractInterfaceTests  and &quot;ExtractInterface&quot; folder as these are not 1.8
&gt; specific.
Thanks Noopur. Since Java 8 allows static methods in interface testExtractInterfaceFromAbstractClass and testExtractInterfaceFromClass are guard tests to ensure that static methods are not extracted to  interface during Extract Interface refactoring in Java 8.
Updated with review comments and released the fix with: http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=42f8ee398a55c72dbc68d19c23a33f4f5b1672d9</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2384239</commentid>
    <comment_count>19</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2014-04-03 10:55:40 -0400</bug_when>
    <thetext>.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2384325</commentid>
    <comment_count>20</comment_count>
    <who name="Paul Benedict">pbenedict@apache.org</who>
    <bug_when>2014-04-03 12:33:18 -0400</bug_when>
    <thetext>Question: if a person is extracting an interface from an interface, technically a super interface is being made, right? I would imagine default methods shouldn&apos;t be assumed to be wanted in all cases. Wouldn&apos;t it make more sense if this was a checkbox option during the refactoring?</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2384464</commentid>
    <comment_count>21</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2014-04-03 18:41:43 -0400</bug_when>
    <thetext>(In reply to Paul Benedict from comment #20)
&gt; Question: if a person is extracting an interface from an interface,
&gt; technically a super interface is being made, right?
Right.

&gt; I would imagine default
&gt; methods shouldn&apos;t be assumed to be wanted in all cases. Wouldn&apos;t it make
&gt; more sense if this was a checkbox option during the refactoring?
When this refactoring is invoked, user is prompted with a dialog where all the abstract and default members are listed, user can choose what needs to be part of the super interface.</thetext>
  </long_desc>
      
          <attachment
              isobsolete="1"
              ispatch="1"
              isprivate="0"
          >
            <attachid>232526</attachid>
            <date>2013-06-19 04:25:00 -0400</date>
            <delta_ts>2013-07-29 08:06:36 -0400</delta_ts>
            <desc>Patch with testcases.</desc>
            <filename>eclipse.jdt.ui.patch</filename>
            <type>text/plain</type>
            <size>18944</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706890-ivzvmcD4CcRJdIBXZvY1HxI6TBND4_n0iSaudRiwUgo</token>

          </attachment>
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>233884</attachid>
            <date>2013-07-29 08:06:00 -0400</date>
            <delta_ts>2013-07-29 08:06:36 -0400</delta_ts>
            <desc>Proposed patch+testcases after updating JDTFlags</desc>
            <filename>eclipse.jdt.ui.patch</filename>
            <type>text/plain</type>
            <size>14648</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706890-PSS9XA55InqVMe2mVx5JSnHJ_g81aVACYDiYuFIIm9Q</token>

          </attachment>
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>233968</attachid>
            <date>2013-07-31 05:27:00 -0400</date>
            <delta_ts>2013-07-31 05:27:49 -0400</delta_ts>
            <desc>Patch with testcases for Extract Interface involving default methods</desc>
            <filename>eclipse.jdt.ui.extractinterface.patch</filename>
            <type>text/plain</type>
            <size>22488</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706890-WnzrixnHKhn54HAPSAeAqs9C9bjyZqXEZaihLQyq-RA</token>

          </attachment>
          <attachment
              isobsolete="0"
              ispatch="0"
              isprivate="0"
          >
            <attachid>233977</attachid>
            <date>2013-07-31 08:23:00 -0400</date>
            <delta_ts>2013-08-01 05:42:35 -0400</delta_ts>
            <desc>Test data for the JDTFlags tests</desc>
            <filename>JDTFlagsTest18.zip</filename>
            <type>application/octet-stream</type>
            <size>571</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706890-afb_06oJvM_ZlF6FVHZjm5s-c0nzPI5M72QOD7S7ZOc</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>405719</bug_id>
          
          <creation_ts>2013-04-15 08:34:00 -0400</creation_ts>
          <short_desc>Remove no longer used bundles from &apos;eclipse.jdt&apos; repository</short_desc>
          <delta_ts>2013-04-17 08:20:07 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>enhancement</bug_severity>
          <target_milestone>4.3 M7</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Dani Megert">daniel_megert@ch.ibm.com</reporter>
          <assigned_to name="Dani Megert">daniel_megert@ch.ibm.com</assigned_to>
          <cc>markus_keller@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706890-qOScps0ob-5PdQj0CpO3Ngy0exgNOMLeWHGyD7XstEQ</token>

      

      

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2243650</commentid>
    <comment_count>0</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-04-15 08:34:27 -0400</bug_when>
    <thetext>3.8.

Remove no longer used bundles from &apos;eclipse.jdt&apos; repository:
org.eclipse.jdt.macosx-feature
org.eclipse.jdt.macosx.source-feature
org.eclipse.jdt.macosx.source
org.eclipse.jdt.macosx
org.eclipse.jdt.source-feature
org.eclipse.jdt.source

NOTE: Must also update root pom.xml if necessary.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2244741</commentid>
    <comment_count>1</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-04-17 08:20:07 -0400</bug_when>
    <thetext>Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.git/commit/?id=http://git.eclipse.org/c/jdt/eclipse.jdt.git/commit/?id=5107631f41786ffb8793cd4b3bf859a71dafafab</thetext>
  </long_desc>
      
      

    </bug>
    <bug>
          <bug_id>405704</bug_id>
          
          <creation_ts>2013-04-15 06:16:00 -0400</creation_ts>
          <short_desc>[1.8][render] Adornment for default methods and annotation type elements with default</short_desc>
          <delta_ts>2013-08-20 15:35:14 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>enhancement</bug_severity>
          <target_milestone>BETA J8</target_milestone>
          <dependson>405517</dependson>
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Markus Keller">markus_keller@ch.ibm.com</reporter>
          <assigned_to name="Manju Mathew">manju656@gmail.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706890-v8NAEgUSttl_toV_1WgYWMTtCKFvawh-zVbueAhesJg</token>

      

      <flag name="review"
          id="56653"
          type_id="1"
          status="+"
          setter="markus_keller@ch.ibm.com"
    />

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2243579</commentid>
    <comment_count>0</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-04-15 06:16:27 -0400</bug_when>
    <thetext>Add an icon adornment for default methods and annotation type elements with a default value.

The overlay for both will be a blue &quot;D&quot; with colors borrowed from
native_co.gif / final_co.gif.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2244685</commentid>
    <comment_count>1</comment_count>
      <attachid>229797</attachid>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-04-17 06:26:09 -0400</bug_when>
    <thetext>Created attachment 229797
default_co.gif</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2245298</commentid>
    <comment_count>2</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-04-18 05:47:56 -0400</bug_when>
    <thetext>Manju, please have a look.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2246054</commentid>
    <comment_count>3</comment_count>
      <attachid>229909</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-04-19 08:55:59 -0400</bug_when>
    <thetext>Created attachment 229909
Patch.

Default icon adornment added for default methods and annotation type elements with a default value. Tested the icon visibility in Outline View, Call Hierarchy View, Type Hierarchy View and Package explorer view.

Markus, kindly review.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2246099</commentid>
    <comment_count>4</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-04-19 09:54:03 -0400</bug_when>
    <thetext>We don&apos;t need two constants in JavaPluginImages. These are not API.

HierarchyLabelProvider:
- bad formatting/parentheses
- why do we need this change?

JavaElementImageProvider:
- since we know these flags are only for IMethods, we should not process them for all IMembers

BindingLabelProvider:
- same as above: only process for methods
- I don&apos;t think Modifier.isDefault(..) will work, see analysis in bug 405517 comment 0. Please test this and mention here how to test it.
- implement AnnotationDefault flag</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2246666</commentid>
    <comment_count>5</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-04-22 06:37:06 -0400</bug_when>
    <thetext>Below are some of the issues/clarifications that came up while working on this bug:
1. Default &amp; static methods of the interface are not shown in the concrete class&apos;s method completion proposal.
2. Extract Interface from an Interface with default methods, in the newly created interface, the default methods are converted to abstract methods. The default implementation is lost.
3. Have an interface with a default method, static method and an abstract method. The concrete class which implements this interface will be asked to add the unimplemented methods. On using this quick fix, along with the abstract method, the default and static methods are also implemented. Is this the right behavior? Shouldn&apos;t we give an option to user not to re-implement the default method? The static method overriding ends up in a compiler error.
4. During content assist, shouldn&apos;t the default methods and the type annotation with default values be adorned with the proper image? This can be taken care in the current fix if required.

Markus, let me know if i need to create separate bug for any of the above points.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2246679</commentid>
    <comment_count>6</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-04-22 07:11:52 -0400</bug_when>
    <thetext>(In reply to comment #5)
These all sound like valid [1.8] bugs. Please open a new bug for each item.

For content assist, parts of the problem could also be in JDT Core. The first task for that bug will be to determine where exactly the problem is (not just implement a solution in JDT UI or Text).</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2246731</commentid>
    <comment_count>7</comment_count>
      <attachid>229959</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-04-22 09:40:07 -0400</bug_when>
    <thetext>Created attachment 229959
Updated Patch.

(In reply to comment #4)
&gt; We don&apos;t need two constants in JavaPluginImages. These are not API.
Renamed the image descriptor to &quot;DESC_OVR_ANNOTATION_DEFAULT_METHOD&quot; which will be shared by default methods and type annotaion with default values.

&gt; HierarchyLabelProvider:
&gt; - bad formatting/parentheses
&gt; - why do we need this change?
Wrong code change, removed it.

&gt; JavaElementImageProvider:
&gt; - since we know these flags are only for IMethods, we should not process
&gt; them for all IMembers
Done
 
&gt; BindingLabelProvider:
&gt; - same as above: only process for methods
Done

&gt; - I don&apos;t think Modifier.isDefault(..) will work, see analysis in bug 405517
&gt; comment 0. 
Done.

&gt; Please test this and mention here how to test it.
To test copy paste the below code to package explorer.
package p1;

public interface I1 {	
	 default int m1(){
		 return 10;
	 }	
}

package p1;

public class Clazz implements I1{}

Invoke Source-&gt; Override/Implement Methods... on Clazz

&gt; - implement AnnotationDefault flag
Done
To test, remove the checks in GenerateMethodAbstractAction#checkAndRun(IType) and then invoke Source &gt; Generate toString() on the below Type Annotation.
package p1;
public @interface ClassPreamble {
   String author();
   String date();
   int currentRevision() default 1;
   String lastModified() default &quot;N/A&quot;;
   String lastModifiedBy() default &quot;N/A&quot;;
   String[] reviewers();
}

(In reply to comment #6)
&gt; (In reply to comment #5)
&gt; These all sound like valid [1.8] bugs. Please open a new bug for each item.
I will create new bugs for them.

&gt; For content assist, parts of the problem could also be in JDT Core. The
&gt; first task for that bug will be to determine where exactly the problem is
&gt; (not just implement a solution in JDT UI or Text).
The proposal itself not being populated is partly the core issue. The image not displayed for default method and annotation with default value is fixed in the UI component CompletionProposalLabelProvider#decorateImageDescriptor and is included as part of the current patch.

Markus, kindly review.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2247105</commentid>
    <comment_count>8</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-04-23 01:33:24 -0400</bug_when>
    <thetext>(In reply to comment #6)
&gt; (In reply to comment #5)
&gt; These all sound like valid [1.8] bugs. Please open a new bug for each item.
&gt; 
&gt; For content assist, parts of the problem could also be in JDT Core. The
&gt; first task for that bug will be to determine where exactly the problem is
&gt; (not just implement a solution in JDT UI or Text).
bug 402812 in JDT Core deals with this issue. Once this bug is fixed we can check if we require additional effort in UI.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2247918</commentid>
    <comment_count>9</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-04-24 10:30:25 -0400</bug_when>
    <thetext>The changes in TypeNameMatchLabelProvider also look unnecessary. The rest looks good, please commit.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2249568</commentid>
    <comment_count>10</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-04-29 02:12:39 -0400</bug_when>
    <thetext>Thanks Markus. Removed the changes in TypeNameMatchLabelProvider and released the patch as:
http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?h=BETA_JAVA8&amp;id=449a3453b969f43104f75fec7c5c1f039a339dc7</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2297038</commentid>
    <comment_count>11</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-08-20 15:35:14 -0400</bug_when>
    <thetext>The blue color of the D can make it hard to distinguish abstract and default methods, e.g. in an Override/Implement Methods dialog for a class that implements Map.

Changed to brown: http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=38330b7ef90447fa12ba22332c94c02d0ef62306</thetext>
  </long_desc>
      
          <attachment
              isobsolete="0"
              ispatch="0"
              isprivate="0"
          >
            <attachid>229797</attachid>
            <date>2013-04-17 06:26:00 -0400</date>
            <delta_ts>2013-04-17 06:26:09 -0400</delta_ts>
            <desc>default_co.gif</desc>
            <filename>default_co.gif</filename>
            <type>image/gif</type>
            <size>102</size>
            <attacher name="Markus Keller">markus_keller@ch.ibm.com</attacher>
            
              <token>1425706890-pVyj3az2Hz5kxE_MbsAadCetyUP-cxQ-tM3RKHVyJFk</token>

          </attachment>
          <attachment
              isobsolete="1"
              ispatch="1"
              isprivate="0"
          >
            <attachid>229909</attachid>
            <date>2013-04-19 08:55:00 -0400</date>
            <delta_ts>2013-04-22 09:40:07 -0400</delta_ts>
            <desc>Patch.</desc>
            <filename>eclipse.jdt.ui.patch</filename>
            <type>text/plain</type>
            <size>10113</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706890-DUcSDkcJfYy7_Zcwow5pbaZDH_5-fq9xLvzgWGr3Y0E</token>

          </attachment>
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>229959</attachid>
            <date>2013-04-22 09:40:00 -0400</date>
            <delta_ts>2013-04-22 09:40:07 -0400</delta_ts>
            <desc>Updated Patch.</desc>
            <filename>eclipse.jdt.ui.patch</filename>
            <type>text/plain</type>
            <size>12075</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706890-9yelxqVVLmsRu63aYR5RKYbdbZiWctdTCZrKxgMsTJE</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>405305</bug_id>
          
          <creation_ts>2013-04-09 13:48:00 -0400</creation_ts>
          <short_desc>[1.8] UI work for LambdaExpression</short_desc>
          <delta_ts>2014-04-22 06:48:40 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>normal</bug_severity>
          <target_milestone>4.4 M7</target_milestone>
          <dependson>408940</dependson>
    
    <dependson>416340</dependson>
    
    <dependson>406786</dependson>
    
    <dependson>407985</dependson>
    
    <dependson>408009</dependson>
    
    <dependson>408114</dependson>
    
    <dependson>408937</dependson>
    
    <dependson>408966</dependson>
    
    <dependson>408979</dependson>
    
    <dependson>409086</dependson>
    
    <dependson>409253</dependson>
    
    <dependson>416264</dependson>
    
    <dependson>416992</dependson>
    
    <dependson>416998</dependson>
          <blocked>380190</blocked>
          <everconfirmed>1</everconfirmed>
          <reporter name="Markus Keller">markus_keller@ch.ibm.com</reporter>
          <assigned_to name="Noopur Gupta">noopur_gupta@in.ibm.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706890-C02eDLumfVhvS7qbHD8LSvow7KtPooa0g5ghl0LesNY</token>

      

      

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2241664</commentid>
    <comment_count>0</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-04-09 13:48:28 -0400</bug_when>
    <thetext>Investigate what we have to do for LambdaExpressions in the UI.

Possible pain points:

- code that traverses the parent chain to find the enclosing scope (e.g. to find visibility of variables, possible target position for Extract Local Variable or Extract Method)

- type of lambda expression is inferred from context (e.g. extracting a lambda expression into a local variable may need special handling to get the right type; compare to MethodInvocation.isResolvedTypeInferredFromExpectedType())

- problems with lambda parameters without a declared type

- ...</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2391212</commentid>
    <comment_count>1</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2014-04-22 06:48:40 -0400</bug_when>
    <thetext>Closing this as the status will be updated individually in the remaining bugs.</thetext>
  </long_desc>
      
      

    </bug>
    <bug>
          <bug_id>405086</bug_id>
          
          <creation_ts>2013-04-06 15:49:00 -0400</creation_ts>
          <short_desc>[quick fix] don&apos;t propose null annotations when those are disabled</short_desc>
          <delta_ts>2013-04-24 10:54:49 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>normal</bug_severity>
          <target_milestone>4.3 M7</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Stephan Herrmann">stephan.herrmann@berlin.de</reporter>
          <assigned_to name="Stephan Herrmann">stephan.herrmann@berlin.de</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706890-gwTOoFngwSeKaKPaYXHhf6M_vv3a0anuIHPm2K40H4o</token>

      

      

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2240564</commentid>
    <comment_count>0</comment_count>
    <who name="Stephan Herrmann">stephan.herrmann@berlin.de</who>
    <bug_when>2013-04-06 15:49:43 -0400</bug_when>
    <thetext>Looking at QuickFixProcessor.process() two kinds of problems could actually
trigger insertion of null annotations while annotation-based null analysis
is disabled:

 IProblem.NonNullLocalVariableComparisonYieldsFalse

 IProblem.RedundantNullCheckOnNonNullLocalVariable

Checks should be inserted to prevent bogus proposals.

Even if null annotations are enabled, some proposals offered on this route
don&apos;t make much sense, I&apos;m afraid.


I&apos;ll investigate.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2240572</commentid>
    <comment_count>1</comment_count>
      <attachid>229402</attachid>
    <who name="Stephan Herrmann">stephan.herrmann@berlin.de</who>
    <bug_when>2013-04-06 19:04:21 -0400</bug_when>
    <thetext>Created attachment 229402
proposed fix

Proposed solution in two small steps:

- check enablement of annotation-based null analysis (the original issue)

- migrate from the two mentions IProblems to their newer counter-parts
  since bug 365859, which already ensure that a null annotation was the
  reason behind the problem

Included tests &amp; another tiny logic bug.

Note, that this patch was created on top of the patch in bug 400668.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2247938</commentid>
    <comment_count>2</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-04-24 10:54:49 -0400</bug_when>
    <thetext>Thanks for the patch.

Committed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=17c7783177bc359beb03a7575237fd347cc3ba49 together with other fixes.</thetext>
  </long_desc>
      
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>229402</attachid>
            <date>2013-04-06 19:04:00 -0400</date>
            <delta_ts>2013-04-06 19:04:21 -0400</delta_ts>
            <desc>proposed fix</desc>
            <filename>Bug-405086.patch</filename>
            <type>text/plain</type>
            <size>10130</size>
            <attacher name="Stephan Herrmann">stephan.herrmann@berlin.de</attacher>
            
              <token>1425706890-C5eHEkdeKsTKFw3SaQnMEdOYeKQHpB-ayG8PUhndlSw</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>403927</bug_id>
          
          <creation_ts>2013-03-20 13:46:00 -0400</creation_ts>
          <short_desc>[1.8] Switch ASTs to JLS8</short_desc>
          <delta_ts>2013-12-02 01:27:56 -0500</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>normal</bug_severity>
          <target_milestone>BETA J8</target_milestone>
          <dependson>409586</dependson>
    
    <dependson>413569</dependson>
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Markus Keller">markus_keller@ch.ibm.com</reporter>
          <assigned_to name="Markus Keller">markus_keller@ch.ibm.com</assigned_to>
          <cc>aclement@gopivotal.com</cc>
    
    <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>deepakazad@gmail.com</cc>
    
    <cc>jarthana@in.ibm.com</cc>
    
    <cc>manju656@gmail.com</cc>
    
    <cc>manpalat@in.ibm.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
    
    <cc>nikolaymetchev@gmail.com</cc>
    
    <cc>noopur_gupta@in.ibm.com</cc>
    
    <cc>srikanth_sankaran@in.ibm.com</cc>
    
    <cc>timo.kinnunen@gmail.com</cc>
          
          <votes>0</votes>

      
          <token>1425706890-eUl5yFcOtEi5vB4MVztqqwxHfJckfFZkQyLGpLleLcY</token>

      

      

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2234413</commentid>
    <comment_count>0</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-03-20 13:46:30 -0400</bug_when>
    <thetext></thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2264253</commentid>
    <comment_count>1</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-05-28 09:43:07 -0400</bug_when>
    <thetext>*** Bug 409086 has been marked as a duplicate of this bug. ***</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2304075</commentid>
    <comment_count>2</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-09-08 11:46:48 -0400</bug_when>
    <thetext>I pushed a preliminary version as http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?h=mkeller/BETA_JAVA8&amp;id=ddc9a1de9aaf508b44b7eb3ad9c6bf23d9e97457

Note that this will be broken once bug 413569 is released, that&apos;s why I didn&apos;t push it to BETA_JAVA8 yet.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2321849</commentid>
    <comment_count>3</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-10-22 14:42:46 -0400</bug_when>
    <thetext>I&apos;ve pushed an update of the basic infrastructure to mkeller/BETA_JAVA8:
http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=1879086c44e8179e125d1c613b6aeb74a0b9acae

Tomorrow, I&apos;ll continue with cherry-picking and reviewing commits from ngupta/BETA_JAVA8, most notably bug 403924 that should fix many of the test failures.

Once the branch is in a consumable shape, I&apos;ll push it to the main BETA_JAVA8 branch.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2323765</commentid>
    <comment_count>4</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-10-27 20:56:49 -0400</bug_when>
    <thetext>Picked bug 403923 and added more fixes for ArrayType structure changes:
http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=6fc1828cf96f851f50cf86a34854d6b3ad91a2b9

Pushed this commit to the main BETA_JAVA8 branch as well.

The last commit that still used the JLS4 AST was http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=09d493bb3e41114936f7d7348794820e78a073a1</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2336360</commentid>
    <comment_count>5</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-12-02 01:27:56 -0500</bug_when>
    <thetext>*** Bug 422902 has been marked as a duplicate of this bug. ***</thetext>
  </long_desc>
      
      

    </bug>
    <bug>
          <bug_id>403924</bug_id>
          
          <creation_ts>2013-03-20 13:29:00 -0400</creation_ts>
          <short_desc>[1.8] Replace usages of MethodDeclaration#thrownExceptions() in the AST</short_desc>
          <delta_ts>2013-10-24 16:05:36 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>normal</bug_severity>
          <target_milestone>BETA J8</target_milestone>
          
          <blocked>407056</blocked>
    
    <blocked>409520</blocked>
          <everconfirmed>1</everconfirmed>
          <reporter name="Markus Keller">markus_keller@ch.ibm.com</reporter>
          <assigned_to name="Noopur Gupta">noopur_gupta@in.ibm.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>manju656@gmail.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706890-qj5QacG3wZLh00UQDE_DIUVWjEKPKgEqk_d5PFIrqiQ</token>

      

      <flag name="review"
          id="56339"
          type_id="1"
          status="+"
          setter="markus_keller@ch.ibm.com"
    />

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2234399</commentid>
    <comment_count>0</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-03-20 13:29:35 -0400</bug_when>
    <thetext>Replace usages of MethodDeclaration#thrownExceptions() in the AST.

For jsr308, MethodDeclaration&apos;s thrownExceptions property has been replaced with thrownExceptionTypes. Make a pass over all JDT UI code that uses the old property in any way (direct access or via property descriptor) and update usages.

File separate bugs if things get too complicated somewhere or if you think we should add new features for handling these constructs.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2239077</commentid>
    <comment_count>1</comment_count>
      <attachid>229281</attachid>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-04-03 07:04:57 -0400</bug_when>
    <thetext>Created attachment 229281
Patch

The attached patch updates the usages of old &apos;thrownExceptions&apos; property of MethodDeclaration in JDT UI code, except the usage in ExceptionOccurrencesFinder.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2310213</commentid>
    <comment_count>2</comment_count>
      <attachid>235754</attachid>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-09-24 08:42:06 -0400</bug_when>
    <thetext>Created attachment 235754
Updated Patch

Updated the patch with JUnit fixes for thrownExceptionTypes.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2322904</commentid>
    <comment_count>3</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-10-24 16:05:36 -0400</bug_when>
    <thetext>In a few places, you replaced
 ASTNodeFactory.newName(fAST, fImportRewriter.addImport(exceptionType, context))
with
 ASTNodeFactory.newType(fAST, fImportRewriter.addImport(exceptionType, context))

The original code was a kludge from times before ImportRewrite could take an AST. I used the better replacement
 fImportRewriter.addImport(exceptionType, fAST, context)

Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=c11b26a1362f47a11287b295af6e00b350648613


http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=4cfd5392c2e3139a9903acc170a1fb06f3bc06c8 doesn&apos;t look completely correct. The revert of ChangeMethodSignatureProposal is good, although this could break again when ImportRewrite considers annotations.

JavadocTagsSubProcessor/LocalCorrectionsSubProcessor only worked for un-annotated types. A Javadoc @throws tag cannot contain annotations.

Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=83079ba6f0bba9525f7776d99c306db57c54d2c0</thetext>
  </long_desc>
      
          <attachment
              isobsolete="1"
              ispatch="1"
              isprivate="0"
          >
            <attachid>229281</attachid>
            <date>2013-04-03 07:04:00 -0400</date>
            <delta_ts>2013-09-24 08:42:06 -0400</delta_ts>
            <desc>Patch</desc>
            <filename>Bug-403924-18-Replace-usages-of-thrownExceptions.patch</filename>
            <type>text/plain</type>
            <size>63756</size>
            <attacher name="Noopur Gupta">noopur_gupta@in.ibm.com</attacher>
            
              <token>1425706890-z1KaKTD6JkVxwIjCxb5dxbrjkB6Ar1K1Opv2pUWhE6w</token>

          </attachment>
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>235754</attachid>
            <date>2013-09-24 08:42:00 -0400</date>
            <delta_ts>2013-09-24 08:42:06 -0400</delta_ts>
            <desc>Updated Patch</desc>
            <filename>Fixed-bug-403924-18-Replace-usages-of-MethodDeclarat.patch</filename>
            <type>text/plain</type>
            <size>60413</size>
            <attacher name="Noopur Gupta">noopur_gupta@in.ibm.com</attacher>
            
              <token>1425706890-Z2fpxi4eM9MWdzhZd_o7L1kAo28eSA5--JZgUOHqjPM</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>403923</bug_id>
          
          <creation_ts>2013-03-20 13:26:00 -0400</creation_ts>
          <short_desc>[1.8] Handle annotations on extra dimensions in the AST</short_desc>
          <delta_ts>2013-10-27 20:50:31 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>normal</bug_severity>
          <target_milestone>BETA J8</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Markus Keller">markus_keller@ch.ibm.com</reporter>
          <assigned_to name="Noopur Gupta">noopur_gupta@in.ibm.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706890-mn9dAyw5Ewxa0WyO6afQxN-w8-UaVu-r62c3GPi2iGM</token>

      

      <flag name="review"
          id="56237"
          type_id="1"
          status="+"
          setter="markus_keller@ch.ibm.com"
    />

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2234395</commentid>
    <comment_count>0</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-03-20 13:26:04 -0400</bug_when>
    <thetext>Handle annotations on extra dimensions in the AST.

For jsr308, a new extraDimensions2 property has been added to MethodDeclaration and to the two concrete VariableDeclaration types. Make a pass over all JDT UI code that uses the old property in any way (direct access or via property descriptor) and update usages.

File separate bugs if things get too complicated somewhere or if you think we should add new features for handling these constructs.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2236048</commentid>
    <comment_count>1</comment_count>
      <attachid>228980</attachid>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-03-25 04:27:20 -0400</bug_when>
    <thetext>Created attachment 228980
Initial Patch

The attached patch updates the usages of old &apos;extraDimensions&apos; property in JDT UI code.

In order to avoid code duplication, I have created the method &apos;copyExtraDimensions(final VariableDeclaration oldVarDeclaration, final VariableDeclaration newVarDeclaration)&apos; in HierarchyProcessor.java as public to be used in:
1. PromoteTempToFieldRefactoring.java
2. SelfEncapsulateFieldRefactoring.java
Please let me know if it should be a protected method like others and if there is a utility class where I can create this method for use in the above mentioned java classes.

Also, the newly added code in the following java classes can be extracted to utility methods:
1. TypeChangeCorrectionProposal.java
2. ChangeMethodSignatureProposal.java

Please let me know the suitable utility classes so that I can update it.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2323763</commentid>
    <comment_count>2</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-10-27 20:50:31 -0400</bug_when>
    <thetext>(In reply to Noopur Gupta from comment #1)
Released as http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=51bb48b17cab7e2d4ece79e1fc1dcf6ca38e219b

Taken care via bug 403927:

&gt; In order to avoid code duplication, I have created the method
&gt; &apos;copyExtraDimensions(final VariableDeclaration oldVarDeclaration, final
&gt; VariableDeclaration newVarDeclaration)&apos; in HierarchyProcessor.java as public
&gt; to be used in:
&gt; 1. PromoteTempToFieldRefactoring.java
&gt; 2. SelfEncapsulateFieldRefactoring.java
&gt; Please let me know if it should be a protected method like others and if
&gt; there is a utility class where I can create this method for use in the above
&gt; mentioned java classes.

The method is OK for HierarchyProcessor, since other code in those processors makes equally questionable calls to ASTNode#copySubtree(..). But wherever we can, we should use ASTRewrite#createCopyTarget(..), since that method also preserves formatting and comments.

I&apos;ve added DimensionRewrite#copyDimensions(ASTRewrite, List&lt;Dimension&gt;) for the other usages.

&gt; Also, the newly added code in the following java classes can be extracted to
&gt; utility methods:
&gt; 1. TypeChangeCorrectionProposal.java
&gt; 2. ChangeMethodSignatureProposal.java
&gt; 
&gt; Please let me know the suitable utility classes so that I can update it.

For lack of a better place, I&apos;ve also put it into DimensionRewrite for now. Next time, please already extract the method when you&apos;re realizing you&apos;re doing the same thing twice.</thetext>
  </long_desc>
      
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>228980</attachid>
            <date>2013-03-25 04:27:00 -0400</date>
            <delta_ts>2013-03-25 04:27:20 -0400</delta_ts>
            <desc>Initial Patch</desc>
            <filename>Bug-403923-1.8-Handle-annotations-on-extra-dimensions.patch</filename>
            <type>text/plain</type>
            <size>30594</size>
            <attacher name="Noopur Gupta">noopur_gupta@in.ibm.com</attacher>
            
              <token>1425706890-MZyaS2KEFt4gznBgM5IVeO2pqT3gi-hGtrhqCg9qrCU</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>403749</bug_id>
          
          <creation_ts>2013-03-19 06:43:00 -0400</creation_ts>
          <short_desc>[1.8][clean up][quick assist] migrate anonymous class creations to lambda expressions</short_desc>
          <delta_ts>2013-12-06 10:17:40 -0500</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>enhancement</bug_severity>
          <target_milestone>BETA J8</target_milestone>
          <dependson>412726</dependson>
          <blocked>421479</blocked>
          <everconfirmed>1</everconfirmed>
          <reporter name="Markus Keller">markus_keller@ch.ibm.com</reporter>
          <assigned_to name="Deepak Azad">deepakazad@gmail.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>deepakazad@gmail.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
    
    <cc>noopur_gupta@in.ibm.com</cc>
    
    <cc>srikanth_sankaran@in.ibm.com</cc>
    
    <cc>stephan.herrmann@berlin.de</cc>
          
          <votes>0</votes>

      
          <token>1425706890-VDYXW7DnB8oWKU0RKWYK98FetE2WtkJ3CSQsfw4wWMc</token>

      

      <flag name="review"
          id="58964"
          type_id="1"
          status="+"
          setter="markus_keller@ch.ibm.com"
    />

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2233504</commentid>
    <comment_count>0</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-03-19 06:43:32 -0400</bug_when>
    <thetext>Create a clean up / multi fix / quick assist that migrates anonymous class creations to lambda expressions.

The result must be semantically equivalent to the original code. The migration can only work if the type is a &quot;Functional Interface&quot;, and if the anonymous class body only contains a single method.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2283152</commentid>
    <comment_count>1</comment_count>
    <who name="Deepak Azad">deepakazad@gmail.com</who>
    <bug_when>2013-07-11 01:09:09 -0400</bug_when>
    <thetext>Markus, I pushed branch the following branch with an initial implementation of the quick assist - http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/log/?h=dazad/BETA_JAVA8

We need an API from JDT Core to check if an anonymous class creation corresponds to a Functional interface. For now I implemented a very simple check in our code.

Note: the branch has SHARED_AST_LEVEL= AST.JLS8 otherwise the quick assist will not work.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2283156</commentid>
    <comment_count>2</comment_count>
    <who name="Deepak Azad">deepakazad@gmail.com</who>
    <bug_when>2013-07-11 01:17:28 -0400</bug_when>
    <thetext>(In reply to comment #1)
&gt; We need an API from JDT Core to check if an anonymous class creation
&gt; corresponds to a Functional interface. For now I implemented a very simple
&gt; check in our code.

Opened Bug 412726</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2287638</commentid>
    <comment_count>3</comment_count>
    <who name="Deepak Azad">deepakazad@gmail.com</who>
    <bug_when>2013-07-23 19:13:36 -0400</bug_when>
    <thetext>Clean up implementation - first draft
http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?h=dazad/BETA_JAVA8&amp;id=00ea70edad7c0cafb22fe394db2115b0a0aa2e66

For now, the preference for the new clean up is on &apos;Code Style&apos; page. But I am wondering if there should be a new tab specifically for Java 8 features, Markus?</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2289336</commentid>
    <comment_count>4</comment_count>
    <who name="Deepak Azad">deepakazad@gmail.com</who>
    <bug_when>2013-07-29 14:42:43 -0400</bug_when>
    <thetext>http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?h=dazad/BETA_JAVA8&amp;id=deee37e65cea10dafad06e45fe1979afcbc7b7af

Incorporated the new API from Bug 412726.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2290439</commentid>
    <comment_count>5</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-07-31 19:43:27 -0400</bug_when>
    <thetext>Thanks Deepak, looks like we&apos;re on a good track here.

I didn&apos;t do a thorough review yet, but I just noticed one UI glitch in the Clean Up edit dialog: The &quot;Use lambda where possible&quot; option does not update the enabled clean ups counter, and hence it can&apos;t be run as the sole clean up.

Please also start thinking about the inverse operation. For the &quot;Enhanced for loop&quot;, it turned out that users also need to go back to the verbose form. Initially, to convert 1.5 code to 1.4, but also on a case-by-case basis if more control over the iteration is necessary.

I think we should at least offer a quick assist to convert a lambda to an anonymous class, but maybe we also want this as a clean up?</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2290442</commentid>
    <comment_count>6</comment_count>
    <who name="Deepak Azad">deepakazad@gmail.com</who>
    <bug_when>2013-07-31 20:07:38 -0400</bug_when>
    <thetext>(In reply to comment #5)
&gt; I think we should at least offer a quick assist to convert a lambda to an
&gt; anonymous class, but maybe we also want this as a clean up?
Fair point. I will add the reverse quick assist. If it would be useful, we can also add the clean up since it is not that much more work.

I will also take a look at the UI glitch.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2290443</commentid>
    <comment_count>7</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-07-31 20:15:24 -0400</bug_when>
    <thetext>If the method body just contains a single return statement, then the lambda should use the short form with just an expression body, e.g.:

        Callable&lt;String&gt; c = new Callable&lt;String&gt;() {
            @Override
            public String call() {
                return &quot;OK&quot;;
            }
        };

=&gt;

        Callable&lt;String&gt; c = () -&gt; &quot;OK&quot;;</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2291301</commentid>
    <comment_count>8</comment_count>
    <who name="Deepak Azad">deepakazad@gmail.com</who>
    <bug_when>2013-08-03 17:37:36 -0400</bug_when>
    <thetext>- I created the reverse quick assist. But I was not sure that we need the reverse clean up as well, hence I just implemented the quick assist as a multi-fix so that if we need the cleanup it will be a trivial task. 

http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?h=dazad/BETA_JAVA8&amp;id=5fe26f2d0a91a33b0f75c6538337ab3494489948

- Fixed the UI glitch from comment 5
- Fixed the use case from comment 7

To ensure that everything works without throwing an exception I had to fix a few usages of MethodDeclaration#thrownExceptions(). For this I have followed the following code pattern...
int apiLevel= ast.apiLevel();
List&lt;ASTNode&gt; thrownExceptions= apiLevel &lt; AST.JLS8 ? decl.thrownExceptions() : decl.thrownExceptionTypes();

- There are a few TODOs in LambdaExpressionsFix which relate to minor (style) points.

Awaiting review...</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2309986</commentid>
    <comment_count>9</comment_count>
    <who name="Deepak Azad">deepakazad@gmail.com</who>
    <bug_when>2013-09-23 15:02:52 -0400</bug_when>
    <thetext>*** Bug 417795 has been marked as a duplicate of this bug. ***</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2309988</commentid>
    <comment_count>10</comment_count>
    <who name="Deepak Azad">deepakazad@gmail.com</who>
    <bug_when>2013-09-23 15:03:41 -0400</bug_when>
    <thetext>*** Bug 417796 has been marked as a duplicate of this bug. ***</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2310554</commentid>
    <comment_count>11</comment_count>
    <who name="Srikanth Sankaran">srikanth_sankaran@in.ibm.com</who>
    <bug_when>2013-09-25 01:37:57 -0400</bug_when>
    <thetext>We are hoping this will be in reasonable shape for us to include it in
a demo in ECE Oct 30th. Any help needed from JDT/Core, let us know, we
will pull out all stops to make it happen. Thank you.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2310560</commentid>
    <comment_count>12</comment_count>
    <who name="Deepak Azad">deepakazad@gmail.com</who>
    <bug_when>2013-09-25 02:19:08 -0400</bug_when>
    <thetext>(In reply to Srikanth Sankaran from comment #11)
&gt; We are hoping this will be in reasonable shape for us to include it in
&gt; a demo in ECE Oct 30th. Any help needed from JDT/Core, let us know, we
&gt; will pull out all stops to make it happen. Thank you.

This can be demoed. The code is in dazad/BETA_JAVA8 branch (and not in the common BETA_JAVA8 branch), but that should not be a blocker for it to be demoed.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2322588</commentid>
    <comment_count>13</comment_count>
    <who name="Srikanth Sankaran">srikanth_sankaran@in.ibm.com</who>
    <bug_when>2013-10-24 08:53:12 -0400</bug_when>
    <thetext>(In reply to Deepak Azad from comment #12)
&gt; (In reply to Srikanth Sankaran from comment #11)
&gt; &gt; We are hoping this will be in reasonable shape for us to include it in
&gt; &gt; a demo in ECE Oct 30th. Any help needed from JDT/Core, let us know, we
&gt; &gt; will pull out all stops to make it happen. Thank you.
&gt; 
&gt; This can be demoed. The code is in dazad/BETA_JAVA8 branch (and not in the
&gt; common BETA_JAVA8 branch), but that should not be a blocker for it to be
&gt; demoed.

4.3.1 + bundles from http://dist.springsource.com/snapshot/TOOLS/java8/e43
as the IDE, I launched on a clean workspace, clone the UI repo, imported the
projects and switched to your branch. Launched an inner instance on a
clean workspace, created a 1.8 project and pasted the code below.

I get the offer of assist to transform anonymous class to lambda and it
works fine for the case below.

Thanks. However any attempt to even ever so lightly modify the file results
in numerous exceptions being thrown about use of unsupported operations in
JLS8 (multiple errors have occurred, operation supported only in JLS2,3, 4.

So while this feature looks ready, other foundational pieces don&apos;t. We are
evaluating our options.

// ---
import java.util.EventListener;

interface IResourceChangeEvent {
	int CHEESE_MOVE = 0;
	Object getDelta();
}

interface IResourceChangeListener extends EventListener {
	// ...
	public void handleResourceChange(IResourceChangeEvent event);
	// ...
}

interface IWorkspace {
	// ...
	public void addResourceChangeListener(IResourceChangeListener listener, int eventMask);
	// ...
}
public class X {
	void foo(IWorkspace workspace) {
		workspace.addResourceChangeListener(new IResourceChangeListener() {
			@Override
			public void handleResourceChange(IResourceChangeEvent event) {
				handleCheeseMove(event.getDelta());
				
			}
		}, IResourceChangeEvent.CHEESE_MOVE);
	}
	private void handleCheeseMove(Object delta) {
		// ...
	}
}
// --</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2322742</commentid>
    <comment_count>14</comment_count>
    <who name="Stephan Herrmann">stephan.herrmann@berlin.de</who>
    <bug_when>2013-10-24 11:37:54 -0400</bug_when>
    <thetext>From playing with this for the demo:

- the quickfix doesn&apos;t seem to respect the formatter settings,
  notably: I get no linebreaks within the lambda, although it
  exceeds the Maximum line width by many (&gt; 50) characters
  Is this expected?
  Deselecting the lambda and hitting Ctrl-Shift-F produces a
  somewhat useful layout (we probably don&apos;t yet have formatter
  settings for really smart formatting of lambdas, right?).

- are there any interesting variations where the quickfix behaves
  differently, apart from just not being available if, e.g.,
  not having a functional interface type?</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2323784</commentid>
    <comment_count>15</comment_count>
    <who name="Srikanth Sankaran">srikanth_sankaran@in.ibm.com</who>
    <bug_when>2013-10-28 00:09:19 -0400</bug_when>
    <thetext>Deepak, now that https://bugs.eclipse.org/bugs/show_bug.cgi?id=403927 is resolved,
can you pull the changes and get your branch up to date so we can test it and
use it for a demo on 30th Oct if possible ? 

Please also see unanswered questions in comment#14

Thanks in advance.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2323787</commentid>
    <comment_count>16</comment_count>
    <who name="Srikanth Sankaran">srikanth_sankaran@in.ibm.com</who>
    <bug_when>2013-10-28 00:41:19 -0400</bug_when>
    <thetext>Markus, since it appears Deepak may be done with this work and it is
waiting for review from your side, if you can give it a look through and
if is ready to be promoted to branch head, go ahead and release it that
would help.

TIA.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2323875</commentid>
    <comment_count>17</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-10-28 06:52:05 -0400</bug_when>
    <thetext>I&apos;ve already merged dazad/BETA_JAVA8 into BETA_JAVA8 in my workspace and I&apos;ll push it to BETA_JAVA8 after I&apos;m done with my review.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2324119</commentid>
    <comment_count>18</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-10-28 16:35:18 -0400</bug_when>
    <thetext>I&apos;m not yet done with the full review, but a fairly-well-working preview is now in branch mkeller/BETA_JAVA8:
http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?h=mkeller/BETA_JAVA8&amp;id=455ffd012f312dd5147ffb01ee159912d5c26317

This can be used to prepare a demo, but don&apos;t base other work on it, since I&apos;ll massage the commits a bit before it goes into BETA_JAVA8.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2324242</commentid>
    <comment_count>19</comment_count>
    <who name="Deepak Azad">deepakazad@gmail.com</who>
    <bug_when>2013-10-29 03:41:11 -0400</bug_when>
    <thetext>(In reply to Stephan Herrmann from comment #14)
&gt; From playing with this for the demo:
&gt; 
&gt; - the quickfix doesn&apos;t seem to respect the formatter settings,
&gt;   notably: I get no linebreaks within the lambda, although it
&gt;   exceeds the Maximum line width by many (&gt; 50) characters
&gt;   Is this expected?
&gt;   Deselecting the lambda and hitting Ctrl-Shift-F produces a
&gt;   somewhat useful layout (we probably don&apos;t yet have formatter
&gt;   settings for really smart formatting of lambdas, right?).
Umm.. I think the formatter usually handles this by default. We don&apos;t really do anything special in UI to format the code, ASTRewrite is supposed to take care of things.
 
&gt; - are there any interesting variations where the quickfix behaves
&gt;   differently, apart from just not being available if, e.g.,
&gt;   not having a functional interface type?
Not really, the only non-trivial case where the quick assist is not offered was when the anonymous class had fields or say implemented methods from the Object class. 

There could be other minor variations which are currently TODOs in code
// TODO: minor: no parentheses for single inferred-type parameter?
// TODO: minor: do we want to create VaribaleDeclarationFragments or inferred-type parameter - never?

But I doubt if any of these are too interesting to be worth mentioning in a demo.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2324270</commentid>
    <comment_count>20</comment_count>
    <who name="Srikanth Sankaran">srikanth_sankaran@in.ibm.com</who>
    <bug_when>2013-10-29 04:47:57 -0400</bug_when>
    <thetext>(In reply to Markus Keller from comment #18)
&gt; I&apos;m not yet done with the full review, but a fairly-well-working preview is
&gt; now in branch mkeller/BETA_JAVA8:
&gt; http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?h=mkeller/
&gt; BETA_JAVA8&amp;id=455ffd012f312dd5147ffb01ee159912d5c26317
&gt; 
&gt; This can be used to prepare a demo, but don&apos;t base other work on it, since
&gt; I&apos;ll massage the commits a bit before it goes into BETA_JAVA8.

This works pretty well, I tested it a bit by editing a file with the sample
code from comment#13 and by adding default methods, static methods, redeclaring
java.lang.Object&apos;s methods, converting interface to abstract class, adding
a second abstract method etc. I get the quick assist offer where I should and
don&apos;t where I shouldn&apos;t.

This is great news, Thanks Markus &amp; Deepak.

Is there any chance this will be to get promoted to BETA_JAVA8 after review
with follow up bugs raised for open items found during code review which can be
addressed in due course ? 

It would be nice to give a demo right from BETA_JAVA8 without having to 
launch an inner IDE, so the audience know this is real &amp; live - but only if 
it makes sense from your team&apos;s pov.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2337581</commentid>
    <comment_count>21</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-12-04 09:10:19 -0500</bug_when>
    <thetext>Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=21b51b36c3333f310d1cb3db44748ee5ee28f721

LambdaExpressionsFix has a few TODOs that can be handles in bug 421479.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2338450</commentid>
    <comment_count>22</comment_count>
    <who name="Srikanth Sankaran">srikanth_sankaran@in.ibm.com</who>
    <bug_when>2013-12-05 19:56:17 -0500</bug_when>
    <thetext>See that this transformation has the potential to break programs:

e.g:

interface I {
	int foo(String s);
}

interface J {
	Integer foo(String s);
}

public class X {
	static void goo(I i) {
		System.out.println(&quot;goo(I)&quot;);
	}
	static void goo(J j) {
		System.out.println(&quot;goo(J)&quot;);
	}
	
	public static void main(String[] args) {
		goo(new I() {

			@Override
			public int foo(String s) {
				return 0;
			}});
	}
}

The transformed code won&apos;t compile any more. There could be scenarios
where the call would compile, but bind to a different method altogether.

If you need some help from Core to figure out whether the overload semantics
would alter the resolution, please file an ER with a proposed API. Thanks.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2338452</commentid>
    <comment_count>23</comment_count>
    <who name="Srikanth Sankaran">srikanth_sankaran@in.ibm.com</who>
    <bug_when>2013-12-05 19:59:59 -0500</bug_when>
    <thetext>(In reply to Srikanth Sankaran from comment #22)
&gt; See that this transformation has the potential to break programs:

[...]

&gt; If you need some help from Core to figure out whether the overload semantics
&gt; would alter the resolution, please file an ER with a proposed API. Thanks.

In the interim, if you wish, you can stick in a cast to the functional type.
A casted poly expression ceases to be a poly expression and cannot be influenced
by the context or influence the context.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2338678</commentid>
    <comment_count>24</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-12-06 10:17:40 -0500</bug_when>
    <thetext>(In reply to Srikanth Sankaran from comment #22 and comment #23)
Noopur is working on this in 408966.

Filed bug 423439 to fix the cleanup/quickassist, since bug 421479 is about something else.</thetext>
  </long_desc>
      
      

    </bug>
    <bug>
          <bug_id>401878</bug_id>
          
          <creation_ts>2013-02-27 06:13:00 -0500</creation_ts>
          <short_desc>Replace provisional icon for Link With Selection not in sync</short_desc>
          <delta_ts>2013-04-22 02:59:33 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>VERIFIED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>enhancement</bug_severity>
          <target_milestone>4.3 M7</target_milestone>
          
          <blocked>393143</blocked>
          <everconfirmed>1</everconfirmed>
          <reporter name="Dani Megert">daniel_megert@ch.ibm.com</reporter>
          <assigned_to name="Dani Megert">daniel_megert@ch.ibm.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706890-SAjAznAMn1lj_EI6nVAKstntU9Mdrkn5gOV8n-mz5fg</token>

      

      

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2222525</commentid>
    <comment_count>0</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-02-27 06:13:44 -0500</bug_when>
    <thetext>In the fix for bug 393143 we added a handmade icon for the Link With Selection icon that indicates out of sync.

We need to replace this with an official icon from our designers.

/org.eclipse.jdt.ui/icons/full/elcl16/sync_broken.gif</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2222585</commentid>
    <comment_count>1</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-02-27 08:39:58 -0500</bug_when>
    <thetext>Icon request ID: 8904</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2246570</commentid>
    <comment_count>2</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-04-22 02:59:14 -0400</bug_when>
    <thetext>The designer did not come up with a better icon than we suggested initially.

Decided to use our proposed icon as the final solution.</thetext>
  </long_desc>
      
      

    </bug>
    <bug>
          <bug_id>401666</bug_id>
          
          <creation_ts>2013-02-25 05:44:00 -0500</creation_ts>
          <short_desc>[1.8] UI for new Lambda code formatter options</short_desc>
          <delta_ts>2013-03-22 04:20:23 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>enhancement</bug_severity>
          <target_milestone>BETA J8</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Markus Keller">markus_keller@ch.ibm.com</reporter>
          <assigned_to name="Manju Mathew">manju656@gmail.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>jesper@selskabet.org</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
    
    <cc>srikanth_sankaran@in.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706891-ig35XjoOt8zweLSMnu_K239muq1JCRXei1mrEpI1fD0</token>

      

      <flag name="review"
          id="56202"
          type_id="1"
          status="+"
          setter="markus_keller@ch.ibm.com"
    />

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2221422</commentid>
    <comment_count>0</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-02-25 05:44:13 -0500</bug_when>
    <thetext>We need UI for the Java 8 code formatter options from bug 400830.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2221435</commentid>
    <comment_count>1</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-02-25 05:51:49 -0500</bug_when>
    <thetext>Manju, please have a look.

Note that this is work for the BETA_JAVA8 branch of the jdt.core and jdt.ui repos. I suggest you create a separate workspace for BETA_JAVA8 work, with separate git repos.
See http://wiki.eclipse.org/JDT_Core/Java8#IMPORTANT_NOTE about header comments.

For the implementation, use a similar existing code formatter option as a template. Open a call hierarchy on the DefaultCodeFormatterConstants constant for the template, and duplicate/adjust everything for the new option.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2228520</commentid>
    <comment_count>2</comment_count>
    <who name="Srikanth Sankaran">srikanth_sankaran@in.ibm.com</who>
    <bug_when>2013-03-09 15:42:35 -0500</bug_when>
    <thetext>We are breaking down the work in bug 400830 into 3 chunks: formatting of
(a) lambda expressions, (b) reference expressions (JDT lingo for method
and constructor references) and (c) 308 related.

(a) has been reviewed and released (https://bugs.eclipse.org/bugs/show_bug.cgi?id=402173). You may want to start on that part. I&apos;ll CC you to other formatter
bugs as they are resolved so you can stay abreast of the developments.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2233432</commentid>
    <comment_count>3</comment_count>
      <attachid>228617</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-03-19 05:12:21 -0400</bug_when>
    <thetext>Created attachment 228617
UI for lambda code formatting.

Two options are provided in the code formatter UI template for lambda.
1. Braces tab 
2. White Space tab =&gt; Declarations =&gt; Lambda
Note : If &quot;white space before opening brace&quot; is checked for a block statement, then the value of &quot;white space after arrow operator&quot; for lambda will not have any effect. To see it working first un-check &quot;white space before opening brace&quot; for block statement and then try again.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2234456</commentid>
    <comment_count>4</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-03-20 15:14:19 -0400</bug_when>
    <thetext>(In reply to comment #3)
Looks pretty good, but I&apos;d request two changes:

1) In BracesTabPage.PREVIEW, the two statements in the lambda body don&apos;t seem to add any information. Please remove one of the statements.

2) In WhiteSpaceOptions, note that options can also be sorted by Syntax element. If you open a call hierarchy on LAMBDA_EXPR_PREVIEW and LABEL_PREVIEW, you see the difference.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2234466</commentid>
    <comment_count>5</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-03-20 15:32:09 -0400</bug_when>
    <thetext>The label on the Braces page also needs to be changed to &quot;Lambda b&amp;ody:&quot;.

The mnemonic &amp;L conflicts with the &quot;New &amp;Lines&quot; tab. The riddle can be solved like this:
- &amp;Class... =&gt; inter&amp;face
- Enum c&amp;onstant body =&gt; Enum &amp;constant body
- =&gt; &amp;o is free for Lambda b&amp;ody</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2234660</commentid>
    <comment_count>6</comment_count>
      <attachid>228808</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-03-21 01:40:57 -0400</bug_when>
    <thetext>Created attachment 228808
UI for lambda. Patch updated with review comments.

Thanks Markus for the review. Here is the updated patch with the below changes.

1. Modified the preview body in BracesTabPage.
2. Handled sort by syntax element for arrow operator in WhiteSpaceTabPage. Added &quot;Arrow operator&quot; option as a child of &quot;Before operator&quot; and &quot;After operator&quot;.
3. Updated the mnemonics. Class or inter&amp;face declaration: , Enum &amp;constant body: and Lambda b&amp;ody:</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2235099</commentid>
    <comment_count>7</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-03-21 13:28:25 -0400</bug_when>
    <thetext>&gt; 1. Modified the preview body in BracesTabPage.
Thanks! That&apos;s a great solution to avoid the option dependency you mentioned in comment 3.

Added an empty line after the beta-blurb in FormatterMessages.properties and fixed the NLS warning in WhiteSpaceOptions.java.

Released as http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=e22f118178ef366019ebbb07d469d6a8a346515f</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2235319</commentid>
    <comment_count>8</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-03-21 23:46:00 -0400</bug_when>
    <thetext>Markus, shouldn&apos;t we keep this bug open until all the Java 8 code formatter requirements are taken care off?</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2235342</commentid>
    <comment_count>9</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-03-22 04:20:23 -0400</bug_when>
    <thetext>(In reply to comment #8)
&gt; Markus, shouldn&apos;t we keep this bug open until all the Java 8 code formatter
&gt; requirements are taken care off?

I&apos;ve adjusted the summary. We can deal with additional options in a separate bug.</thetext>
  </long_desc>
      
          <attachment
              isobsolete="1"
              ispatch="1"
              isprivate="0"
          >
            <attachid>228617</attachid>
            <date>2013-03-19 05:12:00 -0400</date>
            <delta_ts>2013-03-21 01:40:57 -0400</delta_ts>
            <desc>UI for lambda code formatting.</desc>
            <filename>eclipse.jdt.ui.lambda.patch</filename>
            <type>text/plain</type>
            <size>10017</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706891-7A_EKgOSUnUxriFi_678wL3qPueIEK94cbuIs4WUcWQ</token>

          </attachment>
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>228808</attachid>
            <date>2013-03-21 01:40:00 -0400</date>
            <delta_ts>2013-03-21 01:40:57 -0400</delta_ts>
            <desc>UI for lambda. Patch updated with review comments.</desc>
            <filename>eclipse.jdt.ui.lambda.20130321.patch</filename>
            <type>text/plain</type>
            <size>12908</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706891-sNcJwaBwQgF5qDBjajKoB6hGlw4_L5CAMeaju1rZZdw</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>401418</bug_id>
          
          <creation_ts>2013-02-21 07:29:00 -0500</creation_ts>
          <short_desc>[clean up] Add test case for bug 346230</short_desc>
          <delta_ts>2013-02-22 12:16:44 -0500</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>PC</rep_platform>
          <op_sys>Windows 7</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>normal</bug_severity>
          <target_milestone>4.3 M6</target_milestone>
          <dependson>346230</dependson>
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Dani Megert">daniel_megert@ch.ibm.com</reporter>
          <assigned_to name="Noopur Gupta">noopur_gupta@in.ibm.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706891-ZycFepdmbWV6KAJDCcZzyQJhtXallWnDCt-HwXGISzw</token>

      

      <flag name="review"
          id="55762"
          type_id="1"
          status="+"
          setter="daniel_megert@ch.ibm.com"
    />

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2219909</commentid>
    <comment_count>0</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-02-21 07:29:49 -0500</bug_when>
    <thetext>4.3 M5.

Add test case for bug 346230.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2219916</commentid>
    <comment_count>1</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-02-21 07:33:37 -0500</bug_when>
    <thetext>See org.eclipse.jdt.ui.tests.quickfix.CleanUpTestCase</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2220632</commentid>
    <comment_count>2</comment_count>
      <attachid>227437</attachid>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-02-22 03:09:37 -0500</bug_when>
    <thetext>Created attachment 227437
Patch-test case for bug 346230

Added testCodeStyleBug346230() in CleanUpTest.java.
Verified that it fails without the fix in bug 346230 and passes after the fix.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2220920</commentid>
    <comment_count>3</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-02-22 12:16:03 -0500</bug_when>
    <thetext>I assume it&apos;s just an oversight that the project is not deleted at the end of the test. I&apos;ve fixed that and committed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=79eb9ff8a108fc909abf657dde3c542e0c517a2c</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2220921</commentid>
    <comment_count>4</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-02-22 12:16:11 -0500</bug_when>
    <thetext>.</thetext>
  </long_desc>
      
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>227437</attachid>
            <date>2013-02-22 03:09:00 -0500</date>
            <delta_ts>2013-02-22 12:16:44 -0500</delta_ts>
            <desc>Patch-test case for bug 346230</desc>
            <filename>Bug-401418-clean-up-Add-test-case-for-bug-346230.patch</filename>
            <type>text/plain</type>
            <size>4884</size>
            <attacher name="Noopur Gupta">noopur_gupta@in.ibm.com</attacher>
            
              <token>1425706891-w3-Jsft1AmIoTnpb6KWla4WGpuFAzuvPzh2fBfYf9Ao</token>
<flag name="review"
          id="55772"
          type_id="6"
          status="+"
          setter="daniel_megert@ch.ibm.com"
    />
          </attachment>
      

    </bug>
    <bug>
          <bug_id>401120</bug_id>
          
          <creation_ts>2013-02-18 14:33:00 -0500</creation_ts>
          <short_desc>[CBI] (test) CBI build fails not finding org.junit4</short_desc>
          <delta_ts>2013-02-27 05:51:22 -0500</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>VERIFIED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>blocker</bug_severity>
          <target_milestone>4.3 M6</target_milestone>
          <dependson>387802</dependson>
          
          <everconfirmed>1</everconfirmed>
          <reporter name="David Williams">david_williams@us.ibm.com</reporter>
          <assigned_to name="Dani Megert">daniel_megert@ch.ibm.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706891-TOs1UdJU47wBBPNB9mdufpg0T8zMcO4jpT9fQY52kCA</token>

      

      

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2218268</commentid>
    <comment_count>0</comment_count>
    <who name="David Williams">david_williams@us.ibm.com</who>
    <bug_when>2013-02-18 14:33:51 -0500</bug_when>
    <thetext>In a local build I just happened to try this afternoon, I&apos;m seeing following error. My guess is something was removed from a &quot;project pom&quot;, but not from the &quot;repo pom&quot;? I know this as been changing ... not sure why this error shows up just now. (This will prevent next production build to fail, if still exists ... apologies if I&apos;m must catching you in the middle of making changes not fully committed/pushed yet). 

Here&apos;s full error message:

[ERROR] The build could not read 1 project -&gt; [Help 1]
org.apache.maven.project.ProjectBuildingException: Some problems were encountered while processing the POMs:
[ERROR] Child module /data/shared/eclipse/builds/4I/master/gitCache/eclipse.platform.releng.aggregator/eclipse.jdt.ui/org.junit4 of /data/shared/eclipse/builds/4I/master/gitCache/eclipse.platform.releng.aggregator/eclipse.jdt.ui/pom.xml does not exist @

        at org.apache.maven.project.DefaultProjectBuilder.build(DefaultProjectBuilder.java:363)
        at org.apache.maven.DefaultMaven.collectProjects(DefaultMaven.java:636)
        at org.apache.maven.DefaultMaven.getProjectsForMavenReactor(DefaultMaven.java:585)
        at org.apache.maven.DefaultMaven.doExecute(DefaultMaven.java:234)
        at org.apache.maven.DefaultMaven.execute(DefaultMaven.java:156)
        at org.apache.maven.cli.MavenCli.execute(MavenCli.java:537)
        at org.apache.maven.cli.MavenCli.doMain(MavenCli.java:196)
        at org.apache.maven.cli.MavenCli.main(MavenCli.java:141)
        at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
        at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
        at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
        at java.lang.reflect.Method.invoke(Method.java:601)
        at org.codehaus.plexus.classworlds.launcher.Launcher.launchEnhanced(Launcher.java:290)
        at org.codehaus.plexus.classworlds.launcher.Launcher.launch(Launcher.java:230)
        at org.codehaus.plexus.classworlds.launcher.Launcher.mainWithExitCode(Launcher.java:409)
        at org.codehaus.plexus.classworlds.launcher.Launcher.main(Launcher.java:352)
[ERROR]
[ERROR]   The project eclipse.jdt.ui:eclipse.jdt.ui:3.8.0-SNAPSHOT (/data/shared/eclipse/builds/4I/master/gitCache/eclipse.platform.releng.aggregator/eclipse.jdt.ui/pom.xml) has 1 error
[ERROR]     Child module /data/shared/eclipse/builds/4I/master/gitCache/eclipse.platform.releng.aggregator/eclipse.jdt.ui/org.junit4 of /data/shared/eclipse/builds/4I/master/gitCache/eclipse.platform.releng.aggregator/eclipse.jdt.ui/pom.xml does not exist</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2218444</commentid>
    <comment_count>1</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-02-19 04:23:29 -0500</bug_when>
    <thetext>org.junit4 has been removed. Looks like some build script still reference it though. Nothing JDT can fix.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2218452</commentid>
    <comment_count>2</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-02-19 04:36:36 -0500</bug_when>
    <thetext>(In reply to comment #1)
&gt; org.junit4 has been removed. Looks like some build script still reference it
&gt; though. Nothing JDT can fix.

Sorry, too fast. I&apos;ll take a look.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2218476</commentid>
    <comment_count>3</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-02-19 05:08:24 -0500</bug_when>
    <thetext>Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=7cc3f719fa1f6e9cb992e46834ac4c2a112f7db6</thetext>
  </long_desc>
      
      

    </bug>
    <bug>
          <bug_id>400668</bug_id>
          
          <creation_ts>2013-02-13 05:49:00 -0500</creation_ts>
          <short_desc>[quick fix] The fix change parameter type to @Nonnull generated a null change</short_desc>
          <delta_ts>2013-04-24 10:55:21 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>PC</rep_platform>
          <op_sys>Linux</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>normal</bug_severity>
          <target_milestone>4.3 M7</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Frits Jalvingh">jal@etc.to</reporter>
          <assigned_to name="Stephan Herrmann">stephan.herrmann@berlin.de</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>jarthana@in.ibm.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
    
    <cc>stephan.herrmann@berlin.de</cc>
          
          <votes>0</votes>

      
          <token>1425706891-ZmwSaYhmHGQtuNl9xdAegq6XZFp2bYDiEGq1ZPGUjh8</token>

      

      

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2216024</commentid>
    <comment_count>0</comment_count>
    <who name="Frits Jalvingh">jal@etc.to</who>
    <bug_when>2013-02-13 05:49:34 -0500</bug_when>
    <thetext>In a project with nullity annotations present I have a lot of warnings like:

Null type safety: the expression of type AppSession needs unchecked conversion to conform to &apos;@Nonnull AppSession&apos;.

On the warning message, click &quot;quick fix&quot; and select &quot;Change parameter type to @Nonnull&quot;, select a single file, then press finish. Eclipse comes with a popup stating &quot;an exception occured while applying the quick fix&quot;, and the message in the title of this bug report.

Selecting multiple files to fix dies without any kind of message, and no files are changed.

The log shows (dont&apos;t be scared, huge stack trace):
!ENTRY org.eclipse.jdt.ui 4 10001 2013-02-13 11:41:55.559
!MESSAGE Internal Error
!STACK 1
Java Model Exception: Core Exception [code 0] The fix &apos;Add Annotations&apos; generated a null change.
	at org.eclipse.jdt.internal.core.BatchOperation.executeOperation(BatchOperation.java:50)
	at org.eclipse.jdt.internal.core.JavaModelOperation.run(JavaModelOperation.java:728)
	at org.eclipse.core.internal.resources.Workspace.run(Workspace.java:2345)
	at org.eclipse.jdt.core.JavaCore.run(JavaCore.java:5332)
	at org.eclipse.jdt.internal.ui.actions.WorkbenchRunnableAdapter.run(WorkbenchRunnableAdapter.java:106)
	at org.eclipse.jdt.internal.ui.text.correction.proposals.FixCorrectionProposal$1.run(FixCorrectionProposal.java:218)
	at org.eclipse.jdt.internal.ui.refactoring.RefactoringExecutionHelper.perform(RefactoringExecutionHelper.java:191)
	at org.eclipse.jdt.internal.ui.refactoring.RefactoringExecutionHelper.perform(RefactoringExecutionHelper.java:151)
	at org.eclipse.jdt.internal.ui.text.correction.proposals.FixCorrectionProposal.resolve(FixCorrectionProposal.java:225)
	at org.eclipse.jdt.internal.ui.text.correction.CorrectionMarkerResolutionGenerator$CorrectionMarkerResolution.run(CorrectionMarkerResolutionGenerator.java:145)
	at org.eclipse.ui.internal.views.markers.QuickFixPage$11.run(QuickFixPage.java:565)
	at org.eclipse.jface.operation.ModalContext.runInCurrentThread(ModalContext.java:464)
	at org.eclipse.jface.operation.ModalContext.run(ModalContext.java:372)
	at org.eclipse.jface.wizard.WizardDialog.run(WizardDialog.java:1028)
	at org.eclipse.ui.internal.views.markers.QuickFixPage.performFinish(QuickFixPage.java:554)
	at org.eclipse.ui.internal.views.markers.QuickFixWizard$1.run(QuickFixWizard.java:97)
	at org.eclipse.jface.operation.ModalContext.runInCurrentThread(ModalContext.java:464)
	at org.eclipse.jface.operation.ModalContext.run(ModalContext.java:372)
	at org.eclipse.jface.wizard.WizardDialog.run(WizardDialog.java:1028)
	at org.eclipse.ui.internal.views.markers.QuickFixWizard.performFinish(QuickFixWizard.java:106)
	at org.eclipse.jface.wizard.WizardDialog.finishPressed(WizardDialog.java:827)
	at org.eclipse.jface.wizard.WizardDialog.buttonPressed(WizardDialog.java:432)
	at org.eclipse.jface.dialogs.Dialog$2.widgetSelected(Dialog.java:628)
	at org.eclipse.swt.widgets.TypedListener.handleEvent(TypedListener.java:248)
	at org.eclipse.swt.widgets.EventTable.sendEvent(EventTable.java:84)
	at org.eclipse.swt.widgets.Widget.sendEvent(Widget.java:1392)
	at org.eclipse.swt.widgets.Display.runDeferredEvents(Display.java:3705)
	at org.eclipse.swt.widgets.Display.readAndDispatch(Display.java:3326)
	at org.eclipse.jface.window.Window.runEventLoop(Window.java:825)
	at org.eclipse.jface.window.Window.open(Window.java:801)
	at org.eclipse.ui.internal.views.markers.QuickFixHandler.execute(QuickFixHandler.java:165)
	at org.eclipse.ui.internal.handlers.HandlerProxy.execute(HandlerProxy.java:290)
	at org.eclipse.ui.internal.handlers.E4HandlerProxy.execute(E4HandlerProxy.java:76)
	at sun.reflect.GeneratedMethodAccessor31.invoke(Unknown Source)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:601)
	at org.eclipse.e4.core.internal.di.MethodRequestor.execute(MethodRequestor.java:56)
	at org.eclipse.e4.core.internal.di.InjectorImpl.invokeUsingClass(InjectorImpl.java:231)
	at org.eclipse.e4.core.internal.di.InjectorImpl.invoke(InjectorImpl.java:212)
	at org.eclipse.e4.core.contexts.ContextInjectionFactory.invoke(ContextInjectionFactory.java:131)
	at org.eclipse.e4.core.commands.internal.HandlerServiceImpl.executeHandler(HandlerServiceImpl.java:171)
	at org.eclipse.e4.ui.bindings.keys.KeyBindingDispatcher.executeCommand(KeyBindingDispatcher.java:277)
	at org.eclipse.e4.ui.bindings.keys.KeyBindingDispatcher.press(KeyBindingDispatcher.java:496)
	at org.eclipse.e4.ui.bindings.keys.KeyBindingDispatcher.processKeyEvent(KeyBindingDispatcher.java:547)
	at org.eclipse.e4.ui.bindings.keys.KeyBindingDispatcher.filterKeySequenceBindings(KeyBindingDispatcher.java:368)
	at org.eclipse.e4.ui.bindings.keys.KeyBindingDispatcher.access$0(KeyBindingDispatcher.java:314)
	at org.eclipse.e4.ui.bindings.keys.KeyBindingDispatcher$KeyDownFilter.handleEvent(KeyBindingDispatcher.java:83)
	at org.eclipse.swt.widgets.EventTable.sendEvent(EventTable.java:84)
	at org.eclipse.swt.widgets.Display.filterEvent(Display.java:1552)
	at org.eclipse.swt.widgets.Widget.sendEvent(Widget.java:1391)
	at org.eclipse.swt.widgets.Widget.sendEvent(Widget.java:1416)
	at org.eclipse.swt.widgets.Widget.sendEvent(Widget.java:1401)
	at org.eclipse.swt.widgets.Widget.sendKeyEvent(Widget.java:1428)
	at org.eclipse.swt.widgets.Widget.gtk_key_press_event(Widget.java:829)
	at org.eclipse.swt.widgets.Control.gtk_key_press_event(Control.java:3180)
	at org.eclipse.swt.widgets.Composite.gtk_key_press_event(Composite.java:758)
	at org.eclipse.swt.widgets.Widget.windowProc(Widget.java:2092)
	at org.eclipse.swt.widgets.Control.windowProc(Control.java:5334)
	at org.eclipse.swt.widgets.Tree.windowProc(Tree.java:3566)
	at org.eclipse.swt.widgets.Display.windowProc(Display.java:4532)
	at org.eclipse.swt.internal.gtk.OS._gtk_main_do_event(Native Method)
	at org.eclipse.swt.internal.gtk.OS.gtk_main_do_event(OS.java:8549)
	at org.eclipse.swt.widgets.Display.eventProc(Display.java:1241)
	at org.eclipse.swt.internal.gtk.OS._g_main_context_iteration(Native Method)
	at org.eclipse.swt.internal.gtk.OS.g_main_context_iteration(OS.java:2281)
	at org.eclipse.swt.widgets.Display.readAndDispatch(Display.java:3324)
	at org.eclipse.e4.ui.internal.workbench.swt.PartRenderingEngine$9.run(PartRenderingEngine.java:1057)
	at org.eclipse.core.databinding.observable.Realm.runWithDefault(Realm.java:332)
	at org.eclipse.e4.ui.internal.workbench.swt.PartRenderingEngine.run(PartRenderingEngine.java:941)
	at org.eclipse.e4.ui.internal.workbench.E4Workbench.createAndRunUI(E4Workbench.java:79)
	at org.eclipse.ui.internal.Workbench$5.run(Workbench.java:588)
	at org.eclipse.core.databinding.observable.Realm.runWithDefault(Realm.java:332)
	at org.eclipse.ui.internal.Workbench.createAndRunWorkbench(Workbench.java:543)
	at org.eclipse.ui.PlatformUI.createAndRunWorkbench(PlatformUI.java:149)
	at org.eclipse.ui.internal.ide.application.IDEApplication.start(IDEApplication.java:124)
	at org.eclipse.equinox.internal.app.EclipseAppHandle.run(EclipseAppHandle.java:196)
	at org.eclipse.core.runtime.internal.adaptor.EclipseAppLauncher.runApplication(EclipseAppLauncher.java:110)
	at org.eclipse.core.runtime.internal.adaptor.EclipseAppLauncher.start(EclipseAppLauncher.java:79)
	at org.eclipse.core.runtime.adaptor.EclipseStarter.run(EclipseStarter.java:354)
	at org.eclipse.core.runtime.adaptor.EclipseStarter.run(EclipseStarter.java:181)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:601)
	at org.eclipse.equinox.launcher.Main.invokeFramework(Main.java:636)
	at org.eclipse.equinox.launcher.Main.basicRun(Main.java:591)
	at org.eclipse.equinox.launcher.Main.run(Main.java:1450)
	at org.eclipse.equinox.launcher.Main.main(Main.java:1426)
Caused by: org.eclipse.core.runtime.CoreException: The fix &apos;Add Annotations&apos; generated a null change.
	at org.eclipse.jdt.internal.corext.fix.CompilationUnitRewriteOperationsFix.createChange(CompilationUnitRewriteOperationsFix.java:106)
	at org.eclipse.jdt.internal.corext.fix.CleanUpRefactoring.calculateChange(CleanUpRefactoring.java:810)
	at org.eclipse.jdt.internal.corext.fix.CleanUpRefactoring$CleanUpASTRequestor.calculateSolutions(CleanUpRefactoring.java:305)
	at org.eclipse.jdt.internal.corext.fix.CleanUpRefactoring$CleanUpASTRequestor.acceptAST(CleanUpRefactoring.java:283)
	at org.eclipse.jdt.core.dom.CompilationUnitResolver.resolve(CompilationUnitResolver.java:892)
	at org.eclipse.jdt.core.dom.CompilationUnitResolver.resolve(CompilationUnitResolver.java:581)
	at org.eclipse.jdt.core.dom.ASTParser.createASTs(ASTParser.java:894)
	at org.eclipse.jdt.internal.corext.dom.ASTBatchParser.createASTs(ASTBatchParser.java:100)
	at org.eclipse.jdt.internal.corext.fix.CleanUpRefactoring$CleanUpFixpointIterator.next(CleanUpRefactoring.java:406)
	at org.eclipse.jdt.internal.corext.fix.CleanUpRefactoring.cleanUpProject(CleanUpRefactoring.java:718)
	at org.eclipse.jdt.internal.corext.fix.CleanUpRefactoring.checkFinalConditions(CleanUpRefactoring.java:674)
	at org.eclipse.ltk.core.refactoring.Refactoring.checkAllConditions(Refactoring.java:162)
	at org.eclipse.jdt.internal.ui.refactoring.RefactoringExecutionHelper$Operation.run(RefactoringExecutionHelper.java:80)
	at org.eclipse.jdt.internal.core.BatchOperation.executeOperation(BatchOperation.java:39)
	at org.eclipse.jdt.internal.core.JavaModelOperation.run(JavaModelOperation.java:728)
	at org.eclipse.core.internal.resources.Workspace.run(Workspace.java:2345)
	at org.eclipse.jdt.core.JavaCore.run(JavaCore.java:5332)
	at org.eclipse.jdt.internal.ui.actions.WorkbenchRunnableAdapter.run(WorkbenchRunnableAdapter.java:106)
	at org.eclipse.jdt.internal.ui.text.correction.proposals.FixCorrectionProposal$1.run(FixCorrectionProposal.java:218)
	at org.eclipse.jdt.internal.ui.refactoring.RefactoringExecutionHelper.perform(RefactoringExecutionHelper.java:191)
	at org.eclipse.jdt.internal.ui.refactoring.RefactoringExecutionHelper.perform(RefactoringExecutionHelper.java:151)
	at org.eclipse.jdt.internal.ui.text.correction.proposals.FixCorrectionProposal.resolve(FixCorrectionProposal.java:225)
	at org.eclipse.jdt.internal.ui.text.correction.CorrectionMarkerResolutionGenerator$CorrectionMarkerResolution.run(CorrectionMarkerResolutionGenerator.java:145)
	at org.eclipse.ui.internal.views.markers.QuickFixPage$11.run(QuickFixPage.java:565)
	at org.eclipse.jface.operation.ModalContext.runInCurrentThread(ModalContext.java:464)
	at org.eclipse.jface.operation.ModalContext.run(ModalContext.java:372)
	at org.eclipse.jface.wizard.WizardDialog.run(WizardDialog.java:1028)
	at org.eclipse.ui.internal.views.markers.QuickFixPage.performFinish(QuickFixPage.java:554)
	at org.eclipse.ui.internal.views.markers.QuickFixWizard$1.run(QuickFixWizard.java:97)
	at org.eclipse.jface.operation.ModalContext.runInCurrentThread(ModalContext.java:464)
	at org.eclipse.jface.operation.ModalContext.run(ModalContext.java:372)
	at org.eclipse.jface.wizard.WizardDialog.run(WizardDialog.java:1028)
	at org.eclipse.ui.internal.views.markers.QuickFixWizard.performFinish(QuickFixWizard.java:106)
	at org.eclipse.jface.wizard.WizardDialog.finishPressed(WizardDialog.java:827)
	at org.eclipse.jface.wizard.WizardDialog.buttonPressed(WizardDialog.java:432)
	at org.eclipse.jface.dialogs.Dialog$2.widgetSelected(Dialog.java:628)
	at org.eclipse.swt.widgets.TypedListener.handleEvent(TypedListener.java:248)
	at org.eclipse.swt.widgets.EventTable.sendEvent(EventTable.java:84)
	at org.eclipse.swt.widgets.Widget.sendEvent(Widget.java:1392)
	at org.eclipse.swt.widgets.Display.runDeferredEvents(Display.java:3705)
	at org.eclipse.swt.widgets.Display.readAndDispatch(Display.java:3326)
	at org.eclipse.jface.window.Window.runEventLoop(Window.java:825)
	at org.eclipse.jface.window.Window.open(Window.java:801)
	at org.eclipse.ui.internal.views.markers.QuickFixHandler.execute(QuickFixHandler.java:165)
	at org.eclipse.ui.internal.handlers.HandlerProxy.execute(HandlerProxy.java:290)
	at org.eclipse.ui.internal.handlers.E4HandlerProxy.execute(E4HandlerProxy.java:76)
	at sun.reflect.GeneratedMethodAccessor31.invoke(Unknown Source)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:601)
	at org.eclipse.e4.core.internal.di.MethodRequestor.execute(MethodRequestor.java:56)
	at org.eclipse.e4.core.internal.di.InjectorImpl.invokeUsingClass(InjectorImpl.java:231)
	at org.eclipse.e4.core.internal.di.InjectorImpl.invoke(InjectorImpl.java:212)
	at org.eclipse.e4.core.contexts.ContextInjectionFactory.invoke(ContextInjectionFactory.java:131)
	at org.eclipse.e4.core.commands.internal.HandlerServiceImpl.executeHandler(HandlerServiceImpl.java:171)
	at org.eclipse.e4.ui.bindings.keys.KeyBindingDispatcher.executeCommand(KeyBindingDispatcher.java:277)
	at org.eclipse.e4.ui.bindings.keys.KeyBindingDispatcher.press(KeyBindingDispatcher.java:496)
	at org.eclipse.e4.ui.bindings.keys.KeyBindingDispatcher.processKeyEvent(KeyBindingDispatcher.java:547)
	at org.eclipse.e4.ui.bindings.keys.KeyBindingDispatcher.filterKeySequenceBindings(KeyBindingDispatcher.java:368)
	at org.eclipse.e4.ui.bindings.keys.KeyBindingDispatcher.access$0(KeyBindingDispatcher.java:314)
	at org.eclipse.e4.ui.bindings.keys.KeyBindingDispatcher$KeyDownFilter.handleEvent(KeyBindingDispatcher.java:83)
	at org.eclipse.swt.widgets.EventTable.sendEvent(EventTable.java:84)
	at org.eclipse.swt.widgets.Display.filterEvent(Display.java:1552)
	at org.eclipse.swt.widgets.Widget.sendEvent(Widget.java:1391)
	at org.eclipse.swt.widgets.Widget.sendEvent(Widget.java:1416)
	at org.eclipse.swt.widgets.Widget.sendEvent(Widget.java:1401)
	at org.eclipse.swt.widgets.Widget.sendKeyEvent(Widget.java:1428)
	at org.eclipse.swt.widgets.Widget.gtk_key_press_event(Widget.java:829)
	at org.eclipse.swt.widgets.Control.gtk_key_press_event(Control.java:3180)
	at org.eclipse.swt.widgets.Composite.gtk_key_press_event(Composite.java:758)
	at org.eclipse.swt.widgets.Widget.windowProc(Widget.java:2092)
	at org.eclipse.swt.widgets.Control.windowProc(Control.java:5334)
	at org.eclipse.swt.widgets.Tree.windowProc(Tree.java:3566)
	at org.eclipse.swt.widgets.Display.windowProc(Display.java:4532)
	at org.eclipse.swt.internal.gtk.OS._gtk_main_do_event(Native Method)
	at org.eclipse.swt.internal.gtk.OS.gtk_main_do_event(OS.java:8549)
	at org.eclipse.swt.widgets.Display.eventProc(Display.java:1241)
	at org.eclipse.swt.internal.gtk.OS._g_main_context_iteration(Native Method)
	at org.eclipse.swt.internal.gtk.OS.g_main_context_iteration(OS.java:2281)
	at org.eclipse.swt.widgets.Display.readAndDispatch(Display.java:3324)
	at org.eclipse.e4.ui.internal.workbench.swt.PartRenderingEngine$9.run(PartRenderingEngine.java:1057)
	at org.eclipse.core.databinding.observable.Realm.runWithDefault(Realm.java:332)
	at org.eclipse.e4.ui.internal.workbench.swt.PartRenderingEngine.run(PartRenderingEngine.java:941)
	at org.eclipse.e4.ui.internal.workbench.E4Workbench.createAndRunUI(E4Workbench.java:79)
	at org.eclipse.ui.internal.Workbench$5.run(Workbench.java:588)
	at org.eclipse.core.databinding.observable.Realm.runWithDefault(Realm.java:332)
	at org.eclipse.ui.internal.Workbench.createAndRunWorkbench(Workbench.java:543)
	at org.eclipse.ui.PlatformUI.createAndRunWorkbench(PlatformUI.java:149)
	at org.eclipse.ui.internal.ide.application.IDEApplication.start(IDEApplication.java:124)
	at org.eclipse.equinox.internal.app.EclipseAppHandle.run(EclipseAppHandle.java:196)
	at org.eclipse.core.runtime.internal.adaptor.EclipseAppLauncher.runApplication(EclipseAppLauncher.java:110)
	at org.eclipse.core.runtime.internal.adaptor.EclipseAppLauncher.start(EclipseAppLauncher.java:79)
	at org.eclipse.core.runtime.adaptor.EclipseStarter.run(EclipseStarter.java:354)
	at org.eclipse.core.runtime.adaptor.EclipseStarter.run(EclipseStarter.java:181)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:601)
	at org.eclipse.equinox.launcher.Main.invokeFramework(Main.java:636)
	at org.eclipse.equinox.launcher.Main.basicRun(Main.java:591)
	at org.eclipse.equinox.launcher.Main.run(Main.java:1450)
	at org.eclipse.equinox.launcher.Main.main(Main.java:1426)
!SUBENTRY 1 org.eclipse.jdt.ui 4 0 2013-02-13 11:41:55.561
!MESSAGE The fix &apos;Add Annotations&apos; generated a null change.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2216026</commentid>
    <comment_count>1</comment_count>
    <who name="Frits Jalvingh">jal@etc.to</who>
    <bug_when>2013-02-13 05:50:20 -0500</bug_when>
    <thetext>Ah, this is in Eclipse 4.3 milestone 5.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2216045</commentid>
    <comment_count>2</comment_count>
    <who name="Frits Jalvingh">jal@etc.to</who>
    <bug_when>2013-02-13 06:16:37 -0500</bug_when>
    <thetext>The same bug is also present in Eclipse 3.8.1, except it does not show a message box on failure. In addition, in there at least it completes partially: it dies after having made a peculiar change to /another/ file (DomUtil.java) (not the one where I selected to fix the field in):


-	static public final Object getClassValue(@Nonnull final Object inst, @Nonnull final String name) throws Exception {
+	static public final Object getClassValue(final @Nonnull Object inst, @Nonnull final String name) throws Exception {

it moved the @Nonnull annotation to another location in the source (I usually move all annotations to the start of any parameter; I find them hideous and distracting from the real parameter).

The method that I want to fix starts as:

	protected void decodeJpaColumn(DefaultPropertyMetaModel&lt; ? &gt; pmm, final Annotation an) {
		try {
			/*
			 * Handle the &quot;length&quot; annotation. As usual, someone with a brain the size of a pea f.cked up the standard. The
			 * default value for the length is 255, which is of course a totally reasonable size. This makes it impossible to
			 * see if someone has actually provided a value. This means that in absence of the length the field is fscking
			 * suddenly 255 characters big. To prevent this utter disaster from f&apos;ing up the data we only accept this for
			 * STRING fields.
			 */
			Integer iv = (Integer) DomUtil.getClassValue(an, &quot;length&quot;);
			pmm.setLength(iv.intValue());
			if(pmm.getLength() == 255) { // Idiot value?
				if(pmm.getActualType() != String.class)
					pmm.setLength(-1);
			}

and it&apos;s the &quot;an&quot; field that has the warning that I apply the quick fix on.

The DomUtil.java file is left in the editor as &quot;changed and unsaved&quot;.

The 4.3m5 version does not do this, so I have no idea if it&apos;s relevant.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2216188</commentid>
    <comment_count>3</comment_count>
    <who name="Stephan Herrmann">stephan.herrmann@berlin.de</who>
    <bug_when>2013-02-13 10:17:13 -0500</bug_when>
    <thetext>Thanks for providing an example.
I&apos;ll take a look.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2240527</commentid>
    <comment_count>4</comment_count>
    <who name="Stephan Herrmann">stephan.herrmann@berlin.de</who>
    <bug_when>2013-04-06 10:12:28 -0400</bug_when>
    <thetext>I can reproduce and see these problems in the implementation:

(1) we couldn&apos;t quite decide whether to add @NonNull to the declaration of 
&quot;an&quot; in decodeJpaColumn() (that&apos;s what the quickfix label suggests) or 
to change the declaration of &quot;inst&quot; in getClassValue() to @Nullable
(that&apos;s what the implementation ends up trying).
Needs to be fixed in the logic around
NullAnnotationsRewriteOperations.createAddAnnotationOperation(..)

(2) The difference wrt ordering of &quot;final @NonNull&quot; vs. &quot;@NonNull final&quot;
I could not reproduce. The same problem can be reproduced regardless.

(3) Some of the methods NullAnnotationsRewriteOperations.*.rewriteAST()
perform additional analysis (which I considered too expensive for the phase
of collecting proposals). At these points a proposal may return early,
because at a closer look the proposal should not be offered (e.g., we don&apos;t
want to add @Nullable at remote locations (esp. in clean-up mode) IFF the
opposite annotation explicitly  exists (as opposed to, e.g., a parameter
being @NonNull due to @NonNullByDefault).

Apparently the framework cannot handle this use case, we get
- CoreException(&quot;The fix &apos;Add Annotations&apos; generated a null change.&quot;)
- and due to the missing change later we get the reported NPE</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2240533</commentid>
    <comment_count>5</comment_count>
    <who name="Stephan Herrmann">stephan.herrmann@berlin.de</who>
    <bug_when>2013-04-06 10:39:39 -0400</bug_when>
    <thetext>(In reply to comment #4)
&gt; (1) we couldn&apos;t quite decide whether to add @NonNull to the declaration of 
&gt; &quot;an&quot; in decodeJpaColumn() (that&apos;s what the quickfix label suggests) or 
&gt; to change the declaration of &quot;inst&quot; in getClassValue() to @Nullable
&gt; (that&apos;s what the implementation ends up trying).
&gt; Needs to be fixed in the logic around
&gt; NullAnnotationsRewriteOperations.createAddAnnotationOperation(..)

I&apos;ll provide a fix for this soon.
 
&gt; (2) The difference wrt ordering of &quot;final @NonNull&quot; vs. &quot;@NonNull final&quot;
&gt; I could not reproduce. The same problem can be reproduced regardless.

This is a no-op.
 
&gt; (3) Some of the methods NullAnnotationsRewriteOperations.*.rewriteAST()
&gt; perform additional analysis (which I considered too expensive for the phase
&gt; of collecting proposals). At these points a proposal may return early,
&gt; because at a closer look the proposal should not be offered (e.g., we don&apos;t
&gt; want to add @Nullable at remote locations (esp. in clean-up mode) IFF the
&gt; opposite annotation explicitly  exists (as opposed to, e.g., a parameter
&gt; being @NonNull due to @NonNullByDefault).

For post-Kepler follow-up I&apos;ve filed bug 405076.

For now I still need to figure out
(a) if the quick fix processor can perform _all_ the analysis before creating
    a proposal, or
(b) if the proposal can more gracefully signal its cancellation, by, e.g.,
    creating an empty change rather than no change, etc..</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2240562</commentid>
    <comment_count>6</comment_count>
      <attachid>229400</attachid>
    <who name="Stephan Herrmann">stephan.herrmann@berlin.de</who>
    <bug_when>2013-04-06 15:08:48 -0400</bug_when>
    <thetext>Created attachment 229400
proposed fix

(In reply to comment #4)
&gt; (1) we couldn&apos;t quite decide whether to add @NonNull to the declaration of 
&gt; &quot;an&quot; in decodeJpaColumn() (that&apos;s what the quickfix label suggests) or 
&gt; to change the declaration of &quot;inst&quot; in getClassValue() to @Nullable
&gt; (that&apos;s what the implementation ends up trying).
&gt; Needs to be fixed in the logic around
&gt; NullAnnotationsRewriteOperations.createAddAnnotationOperation(..)

Here&apos;s my proposed patch for that immediate problem.

Logic changes:
- better interpret the situation to distinguish when to modify the
  current method vs. a target method (in a message send)
- collect proposals in two rounds to propose both directions of adjustment

For clarity I&apos;ve replaced a bunch of flags with 
  enum ChangeKind { LOCAL, OVERRIDDEN, TARGET }
for steering into the desired kind of proposal


Label changes:
- added &quot;Change parameter of &apos;&apos;{0}(..)&apos;&apos; to &apos;&apos;@{1}&apos;&apos;&quot; for clarity
- shortened a few labels so they fit in the proposal popup


Test changes:
- new tests for this particular issue
- check the display string in more tests 
  (which revealed another tiny issue that&apos;s also fixed in the patch)


Strangely I get a test failure in the (I believe) unrelated
org.eclipse.jdt.junit.tests.TestRunListenerTest.testTreeJUnit4TestAdapter()
Indentations don&apos;t match expectation, I&apos;m probably using a mismatching
org.eclipse.jdt.junit.something (from M6).
Other than that JDT/UI tests are green.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2247941</commentid>
    <comment_count>7</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-04-24 10:55:21 -0400</bug_when>
    <thetext>Thanks for the patch.

Committed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=17c7783177bc359beb03a7575237fd347cc3ba49 together with other fixes.</thetext>
  </long_desc>
      
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>229400</attachid>
            <date>2013-04-06 15:08:00 -0400</date>
            <delta_ts>2013-04-06 15:08:48 -0400</delta_ts>
            <desc>proposed fix</desc>
            <filename>Bug-400668.patch</filename>
            <type>text/plain</type>
            <size>31268</size>
            <attacher name="Stephan Herrmann">stephan.herrmann@berlin.de</attacher>
            
              <token>1425706891-BvTj1arR4t_lFu_ugmTSAPhCJeJXU3YpPtIOhk5iy_o</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>400615</bug_id>
          
          <creation_ts>2013-02-12 13:51:00 -0500</creation_ts>
          <short_desc>Update JDT branding plugin qualifiers</short_desc>
          <delta_ts>2013-02-13 03:24:32 -0500</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>PC</rep_platform>
          <op_sys>Linux</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>normal</bug_severity>
          <target_milestone>4.3 M6</target_milestone>
          <dependson>400517</dependson>
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Paul Webster">pwebster@ca.ibm.com</reporter>
          <assigned_to name="Markus Keller">markus_keller@ch.ibm.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706891-ZF9PQUy7wSQ3UA8XLP4cHf0LsepKneOXkMni2K59cM8</token>

      

      

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2215675</commentid>
    <comment_count>0</comment_count>
      <attachid>226944</attachid>
    <who name="Paul Webster">pwebster@ca.ibm.com</who>
    <bug_when>2013-02-12 13:51:14 -0500</bug_when>
    <thetext>Created attachment 226944
JDT branding plugin

Make the branding plugin qualifiers consistent with the buildId

PW</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2215687</commentid>
    <comment_count>1</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-02-12 14:01:25 -0500</bug_when>
    <thetext>Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.git/commit/?id=938cf0e3b9dd0afcdc4cbf48137e5cd84cb90b97</thetext>
  </long_desc>
      
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>226944</attachid>
            <date>2013-02-12 13:51:00 -0500</date>
            <delta_ts>2013-02-12 13:51:14 -0500</delta_ts>
            <desc>JDT branding plugin</desc>
            <filename>branding-e.jdt.patch</filename>
            <type>text/plain</type>
            <size>462</size>
            <attacher name="Paul Webster">pwebster@ca.ibm.com</attacher>
            
              <token>1425706891-ccWiHl_IOgkypm2D_8HRahZzyo4uAK6dghSfsYayt5w</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>399265</bug_id>
          
          <creation_ts>2013-01-28 09:12:00 -0500</creation_ts>
          <short_desc>Update to JUnit 4.11</short_desc>
          <delta_ts>2013-03-28 06:49:09 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>VERIFIED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>normal</bug_severity>
          <target_milestone>4.3 M6</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Markus Keller">markus_keller@ch.ibm.com</reporter>
          <assigned_to name="Markus Keller">markus_keller@ch.ibm.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>david_williams@us.ibm.com</cc>
    
    <cc>jarthana@in.ibm.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706891-7RIy8-DnU7ne3NNAp9SEwf1aVUJx-uc7BiEeTkPLuzU</token>

      

      

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2208542</commentid>
    <comment_count>0</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-01-28 09:12:03 -0500</bug_when>
    <thetext>Update to latest available JUnit (4.11 at this time).

JUnit is now here:
https://github.com/KentBeck/junit/wiki/Download-and-Install

Also needs hamcrest-core-1.3.jar from here:
http://code.google.com/p/hamcrest/downloads/list</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2213147</commentid>
    <comment_count>1</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-02-06 13:13:54 -0500</bug_when>
    <thetext>Filed CQs and Orbit bugs:

JUnit 4.11:
https://dev.eclipse.org/ipzilla/show_bug.cgi?id=7064
https://bugs.eclipse.org/400133

hamcrest-core 1.3:
https://dev.eclipse.org/ipzilla/show_bug.cgi?id=7063
https://bugs.eclipse.org/400130</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2227381</commentid>
    <comment_count>2</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-03-07 08:44:07 -0500</bug_when>
    <thetext>Feature updated via bug 402573.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2237546</commentid>
    <comment_count>3</comment_count>
    <who name="Jay Arthanareeswaran">jarthana@in.ibm.com</who>
    <bug_when>2013-03-28 01:08:44 -0400</bug_when>
    <thetext>Markus, from M6 onwards we get several warnings about deprecated Assert and assert methods. What would be the best way forward for us to get rid of the warning without changing lot of code? Thanks!</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2237550</commentid>
    <comment_count>4</comment_count>
    <who name="Jay Arthanareeswaran">jarthana@in.ibm.com</who>
    <bug_when>2013-03-28 01:50:18 -0400</bug_when>
    <thetext>(In reply to comment #3)
&gt; Markus, from M6 onwards we get several warnings about deprecated Assert and
&gt; assert methods. What would be the best way forward for us to get rid of the
&gt; warning without changing lot of code? Thanks!

Actually, never mind. I was confused that I saw those warnings. But they were actually in R3_8*</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2237651</commentid>
    <comment_count>5</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-03-28 06:49:09 -0400</bug_when>
    <thetext>&gt; actually in R3_8*

That would mean there&apos;s something wrong in your setup. For R3_8_maintenance development, the target platform MUST be 3.8.2, which doesn&apos;t contain JUnit 4.11.

In the master branch of eclipse.jdt.core, many of these warnings have been fixed with bug 404169.</thetext>
  </long_desc>
      
      

    </bug>
    <bug>
          <bug_id>398995</bug_id>
          
          <creation_ts>2013-01-24 12:15:00 -0500</creation_ts>
          <short_desc>[quick fix] Extract field access to checked local variable</short_desc>
          <delta_ts>2013-02-13 07:50:25 -0500</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>enhancement</bug_severity>
          <target_milestone>4.3 M6</target_milestone>
          <dependson>331649</dependson>
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Stephan Herrmann">stephan.herrmann@berlin.de</reporter>
          <assigned_to name="Stephan Herrmann">stephan.herrmann@berlin.de</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706891-PkwtTYWfkWkd88CZK9UROmwNn9i50qGZpWkCtYq0y6s</token>

      

      <flag name="review"
          id="55327"
          type_id="1"
          status="+"
          setter="daniel_megert@ch.ibm.com"
    />

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2207170</commentid>
    <comment_count>0</comment_count>
    <who name="Stephan Herrmann">stephan.herrmann@berlin.de</who>
    <bug_when>2013-01-24 12:15:31 -0500</bug_when>
    <thetext>This was first proposed in Bug 331649 comment 32: 
When dereferencing a @Nullable field the safest solution is to assign the field to a local variable before null-checking and dereferencing.

The quick fix does exactly that.

My implementation was first attached to bug 337977 comment 18 but I think it deserves a bug on its own.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2207187</commentid>
    <comment_count>1</comment_count>
      <attachid>226058</attachid>
    <who name="Stephan Herrmann">stephan.herrmann@berlin.de</who>
    <bug_when>2013-01-24 12:41:36 -0500</bug_when>
    <thetext>Created attachment 226058
proposed implementation with tests

Here&apos;s my implementation, which is based on attachment 217460 (from bug 337977).
These bits were published as part of the beta feature, and have seen some field use already.

The patch includes a small fix for existing quick fixes, hope it&apos;s OK to include here:
- fix wrong label&lt;-&gt;operation association (see bug 337977 comment 36).



During cleanup I made the following improvements over attachment 217460:
1. make the quick fix applicable to more situations, not just field *dereference*,
  but also usage of a @Nullable/unknown field in a context where @NonNull is required
2. handle scoping of existing local variables
3. internal code refactoring

Item 3. is best explained by an example:

class X {
  @Nullable X other;
  String f;
  void Object foo() {
      String myF = this.other.f; // warning here: dereference @Nullable &apos;other&apos;
      System.out.println(myF);
  }
}

Previously, the quick fix would only wrap the current statement:
  void Object foo() {
      X other1 = this.other;
      if (other1 != null) {
        String myF = other1.f;
      } else {
         // TODO handle null value
      }
      System.out.println(myF);
  }
which obviously breaks the usage of myF further down.

My new implementation solves this like this: IFF the dangerous field dereference is inside the initialization of a local variable, all subsequent statements of the enclosing block are moved into the then part of the new if:
  void Object foo() {
      X other1 = this.other;
      if (other1 != null) {
        String myF = this.other.f;
      } else {
         // TODO handle null value
         System.out.println(myF);
      }
  }
If not changing the initialization of a local declaration, the change region is kept small by wrapping only the offensive statement.

The patch includes tests which also demonstrate the various situations handled by the quick fix.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2207275</commentid>
    <comment_count>2</comment_count>
    <who name="Stephan Herrmann">stephan.herrmann@berlin.de</who>
    <bug_when>2013-01-24 14:47:48 -0500</bug_when>
    <thetext>*** Bug 383540 has been marked as a duplicate of this bug. ***</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2216092</commentid>
    <comment_count>3</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-02-13 07:50:25 -0500</bug_when>
    <thetext>Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=9f5838bea1419b66d88c7e62d7617e995b5aa58e</thetext>
  </long_desc>
      
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>226058</attachid>
            <date>2013-01-24 12:41:00 -0500</date>
            <delta_ts>2013-01-24 12:41:36 -0500</delta_ts>
            <desc>proposed implementation with tests</desc>
            <filename>Bug-398995.patch</filename>
            <type>text/plain</type>
            <size>52279</size>
            <attacher name="Stephan Herrmann">stephan.herrmann@berlin.de</attacher>
            
              <token>1425706891-FLQAWBGxs324LPTWxA1mUJTAVSpUFerNGd-2pwYH9HA</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>398965</bug_id>
          
          <creation_ts>2013-01-24 07:52:00 -0500</creation_ts>
          <short_desc>[preferences] UI option for syntactic analysis for fields</short_desc>
          <delta_ts>2013-01-29 06:05:26 -0500</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>PC</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>enhancement</bug_severity>
          <target_milestone>4.3 M5</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Stephan Herrmann">stephan.herrmann@berlin.de</reporter>
          <assigned_to name="Stephan Herrmann">stephan.herrmann@berlin.de</assigned_to>
          <cc>amj87.iitr@gmail.com</cc>
    
    <cc>daniel_megert@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706891-ZO_srCOhNOCKRX-Vv-G9ytbLkoCH-NQEKbCE5wwzKcA</token>

      

      

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2207013</commentid>
    <comment_count>0</comment_count>
    <who name="Stephan Herrmann">stephan.herrmann@berlin.de</who>
    <bug_when>2013-01-24 07:52:48 -0500</bug_when>
    <thetext>Bug 383368 introduced a new preference constant JavaCore.COMPILER_PB_SYNTACTIC_NULL_ANALYSIS_FOR_FIELDS

Please provide a UI option for this.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2207014</commentid>
    <comment_count>1</comment_count>
      <attachid>226043</attachid>
    <who name="Stephan Herrmann">stephan.herrmann@berlin.de</who>
    <bug_when>2013-01-24 07:54:22 -0500</bug_when>
    <thetext>Created attachment 226043
proposed fix

This is what I used in the beta feature.
Feel free to use / modify.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2207561</commentid>
    <comment_count>2</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-01-25 05:27:54 -0500</bug_when>
    <thetext>Thanks for the patch!

Committed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=7bf809d912b4e04995fa69e7a9251cab067da6d1</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2209151</commentid>
    <comment_count>3</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-01-29 06:05:26 -0500</bug_when>
    <thetext>*** Bug 368390 has been marked as a duplicate of this bug. ***</thetext>
  </long_desc>
      
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>226043</attachid>
            <date>2013-01-24 07:54:00 -0500</date>
            <delta_ts>2013-01-24 07:54:22 -0500</delta_ts>
            <desc>proposed fix</desc>
            <filename>Bug-383368-UI-option.patch</filename>
            <type>text/plain</type>
            <size>4586</size>
            <attacher name="Stephan Herrmann">stephan.herrmann@berlin.de</attacher>
            
              <token>1425706891-EHJvtV5CmCoXse0YjKJfIop-GYimhYY7CtFsdhFYRqw</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>398211</bug_id>
          
          <creation_ts>2013-01-15 11:43:00 -0500</creation_ts>
          <short_desc>UI changes for bug 381443 (@NonNull parameter not annotated in overriding method)</short_desc>
          <delta_ts>2013-01-22 05:18:49 -0500</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>PC</rep_platform>
          <op_sys>Linux</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>normal</bug_severity>
          <target_milestone>4.3 M5</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Stephan Herrmann">stephan.herrmann@berlin.de</reporter>
          <assigned_to name="Noopur Gupta">noopur_gupta@in.ibm.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706891-02HMUZB4ZHIWOScWCBOPRJk-t1j2gtemgqnbMohCRSY</token>

      

      <flag name="review"
          id="55155"
          type_id="1"
          status="+"
          setter="markus_keller@ch.ibm.com"
    />

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2203166</commentid>
    <comment_count>0</comment_count>
    <who name="Stephan Herrmann">stephan.herrmann@berlin.de</who>
    <bug_when>2013-01-15 11:43:05 -0500</bug_when>
    <thetext>Once the final solution in bug 381443 is released two changes are needed in JDT/UI:

(1) Add a new preference option, late candidates where (bug 381443 comment 49):

@NonNull parameter not annotated in overriding method
@NonNull parameter form overridden method not annotated
Overridden @NonNull parameter not annotated

Option values are Error/Warning/Ignore

(2) Adjust currently failing test NullAnnotationsQuickFixTest.testChangeParameter3c()
I&apos;ll post a patch for that one in a second.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2203172</commentid>
    <comment_count>1</comment_count>
      <attachid>225651</attachid>
    <who name="Stephan Herrmann">stephan.herrmann@berlin.de</who>
    <bug_when>2013-01-15 11:50:28 -0500</bug_when>
    <thetext>Created attachment 225651
proposed test change

The proposed tiny change for the mentioned test.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2203174</commentid>
    <comment_count>2</comment_count>
    <who name="Stephan Herrmann">stephan.herrmann@berlin.de</who>
    <bug_when>2013-01-15 11:53:01 -0500</bug_when>
    <thetext>(In reply to comment #1)
&gt; Created attachment 225651 [details]
&gt; proposed test change
&gt; 
&gt; The proposed tiny change for the mentioned test.

Obviously, this requires the final solution from bug 381443, for which I&apos;m just doing a final test run before release.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2204111</commentid>
    <comment_count>3</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-01-17 07:02:02 -0500</bug_when>
    <thetext>Let&apos;s use this one:
&gt; @NonNull parameter not annotated in overriding method

Noopur, could you have a look? This bug is just about the preference (i.e. not about adding a quick fix / clean up).

When adding new options on the Errors/Warnings page, it&apos;s usually easiest to search for references or open a call hierarchy for a similar option (e.g. JavaCore.COMPILER_PB_REDUNDANT_NULL_ANNOTATION), and then imitate what&apos;s been done for that option.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2204598</commentid>
    <comment_count>4</comment_count>
      <attachid>225802</attachid>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-01-18 01:37:37 -0500</bug_when>
    <thetext>Created attachment 225802
Patch

Added the preference, &apos;@NonNull&apos; parameter not annotated in overriding method, for the JavaCore constant COMPILER_PB_NONNULL_PARAMETER_ANNOTATION_DROPPED.

Markus, thanks for the hint. Please review the patch.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2205616</commentid>
    <comment_count>5</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-01-21 13:43:40 -0500</bug_when>
    <thetext>Thanks, Noopur. Also for spotting and fixing the other problems nearby.

I know I said we&apos;re not looking at a quick fix / clean up, but when I checked the solution, I realized that the quick fix is already available. Bug 381443 just added an option to toggle this problem on and off. But now, the multi-fix didn&apos;t work any more in this example:

public class Bug381443 {
    private class Foo {
        void foo(@NonNull Integer foo) {
        }
    }

    private class Bar extends Foo {
        @Override void foo(Integer foo) {
        }
    }

    private class Bar2 extends Foo {
    	@Override void foo(Integer foo) {
    	}
    }
}

Fixed this in NullAnnotationsCleanUp and released the whole fix as http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=fd541d2f3fb968c3db6606d53a2e7b9cf084a389</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2205856</commentid>
    <comment_count>6</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-01-22 05:18:49 -0500</bug_when>
    <thetext>(In reply to comment #1)
&gt; Created attachment 225651 [details] [diff]
&gt; proposed test change
&gt; 
&gt; The proposed tiny change for the mentioned test.

I forgot to release this. Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=5f0b41f0164318b11e29d8d3ce49257248d5f6d1</thetext>
  </long_desc>
      
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>225651</attachid>
            <date>2013-01-15 11:50:00 -0500</date>
            <delta_ts>2013-01-15 11:50:28 -0500</delta_ts>
            <desc>proposed test change</desc>
            <filename>bug398211-test.patch</filename>
            <type>text/plain</type>
            <size>1558</size>
            <attacher name="Stephan Herrmann">stephan.herrmann@berlin.de</attacher>
            
              <token>1425706891-QL2-qsZquw8W1olf24oaX95lePN6DleBF9gbg_X4kHc</token>

          </attachment>
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>225802</attachid>
            <date>2013-01-18 01:37:00 -0500</date>
            <delta_ts>2013-01-18 01:37:37 -0500</delta_ts>
            <desc>Patch</desc>
            <filename>Bug-398211-UI-changes-for-bug-381443-NonNull-param.patch</filename>
            <type>text/plain</type>
            <size>8436</size>
            <attacher name="Noopur Gupta">noopur_gupta@in.ibm.com</attacher>
            
              <token>1425706891-sGD_UTr-9t8F5un3cmViAtJwO9ww_M_Hj8fbmEeAXyU</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>398112</bug_id>
          
          <creation_ts>2013-01-14 13:17:00 -0500</creation_ts>
          <short_desc>[save actions] Save Actions create inconsistency</short_desc>
          <delta_ts>2013-01-29 06:10:16 -0500</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>VERIFIED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>critical</bug_severity>
          <target_milestone>4.3 M5</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Lars Vogel">lars.vogel@vogella.com</reporter>
          <assigned_to name="Dani Megert">daniel_megert@ch.ibm.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>lars.vogel@vogella.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
    
    <cc>noopur_gupta@in.ibm.com</cc>
    
    <cc>pwebster@ca.ibm.com</cc>
    
    <cc>rgransberger@gmx.de</cc>
    
    <cc>wayne@eclipse.org</cc>
          
          <votes>0</votes>

      
          <token>1425706891-twaqsZZ01Fl5bQx7cmoGIqXn5K2mQOMk9N94EO2kSOI</token>

      

      

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2202592</commentid>
    <comment_count>0</comment_count>
    <who name="Lars Vogel">lars.vogel@vogella.com</who>
    <bug_when>2013-01-14 13:17:58 -0500</bug_when>
    <thetext>I activated the save actions in Eclipse 4.3 Integration build (format at save and organization of imports).

I&apos;m also using a type filter for java.awt.* and javax.swing.*

If I delete the import statements with Ctrl+D and save parts of the imports are created, except the import for the SWT Text widget because Eclipse has several possible imports.

So I use Ctrl+O to import the correct package. 

If I now try to save via Ctrl+S I get the information that the file is out-of-sync and that save failed (see attached screenshot).

This is repeatable, sometimes I have to do the whole thing 2-3 times to get this errors. Try the following steps with the attached project:

Setup:
1.) Activate Save Actions and Type filter as described above
2.) Import attacshed example project
3.) Open the TodoDetailPart class

Test
1.) Delete import statements via Ctrl+D
2.) Ctrl+S
3.) Ctrl+O select the SWT Text widget import
4.) Ctrl+S -&gt; should fail

If 4.) does not fail, repeat at least 5 times.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2202593</commentid>
    <comment_count>1</comment_count>
      <attachid>225585</attachid>
    <who name="Lars Vogel">lars.vogel@vogella.com</who>
    <bug_when>2013-01-14 13:19:13 -0500</bug_when>
    <thetext>Created attachment 225585
Screenshot of Error</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2202594</commentid>
    <comment_count>2</comment_count>
      <attachid>225586</attachid>
    <who name="Lars Vogel">lars.vogel@vogella.com</who>
    <bug_when>2013-01-14 13:19:42 -0500</bug_when>
    <thetext>Created attachment 225586
Example project</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2202814</commentid>
    <comment_count>3</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-01-15 03:23:33 -0500</bug_when>
    <thetext>Which build ID? Anything in .log?</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2202829</commentid>
    <comment_count>4</comment_count>
    <who name="Lars Vogel">lars.vogel@vogella.com</who>
    <bug_when>2013-01-15 03:48:19 -0500</bug_when>
    <thetext>Build id: N20130112-2000</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2202831</commentid>
    <comment_count>5</comment_count>
    <who name="Lars Vogel">lars.vogel@vogella.com</who>
    <bug_when>2013-01-15 03:52:00 -0500</bug_when>
    <thetext>And I don&apos;t see any additional Error log message related to this.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2202920</commentid>
    <comment_count>6</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-01-15 06:31:23 -0500</bug_when>
    <thetext>Noopur, please check whether you can reproduce this.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2203459</commentid>
    <comment_count>7</comment_count>
      <attachid>225685</attachid>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-01-16 01:30:49 -0500</bug_when>
    <thetext>Created attachment 225685
Error on importing the project

The attached error was logged in the Error Log View while importing the project for the first time. It is not happening again.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2203460</commentid>
    <comment_count>8</comment_count>
      <attachid>225686</attachid>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-01-16 01:33:26 -0500</bug_when>
    <thetext>Created attachment 225686
Error while trying to reproduce the issue

The attached error was logged in the Error Log View while trying to reproduce the issue mentioned in this bug. This happened only once and I am not able to reproduce it again.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2203465</commentid>
    <comment_count>9</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-01-16 01:43:11 -0500</bug_when>
    <thetext>The error logs attached above were obtained while trying to reproduce the issue mentioned in this bug. These logs are not consistent and were logged only once.

However, the issue of inconsistency in the save action is reproducible. There are no error logs produced when the save problem occurs.

It happens when we try to save the file immediately (using Ctrl+S) after selecting the SWT Text widget import using Ctrl+Shift+O.
If we give some time in between the selection of import and the save, the file is saved without any problem.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2203487</commentid>
    <comment_count>10</comment_count>
    <who name="Lars Vogel">lars.vogel@vogella.com</who>
    <bug_when>2013-01-16 02:57:41 -0500</bug_when>
    <thetext>Thanks for validating this. I also get this error frequently during development, but the deletion of imports is the easiest way to create this. I raise the prio of this bug, I don&apos;t think we want to ship Eclipse 4.3 with this error.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2203488</commentid>
    <comment_count>11</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-01-16 03:02:31 -0500</bug_when>
    <thetext>Noopur, please also check whether the bug also happens in 3.8 and 4.2. If not, please also check 3.8.1 and 4.2.1 to be sure we did not introduce it in SR1 .</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2203490</commentid>
    <comment_count>12</comment_count>
    <who name="Lars Vogel">lars.vogel@vogella.com</who>
    <bug_when>2013-01-16 03:04:32 -0500</bug_when>
    <thetext>FYI: I was using Eclipse 4.2.1 before and never had this issue before.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2203491</commentid>
    <comment_count>13</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-01-16 03:06:43 -0500</bug_when>
    <thetext>(In reply to comment #12)
&gt; FYI: I was using Eclipse 4.2.1 before and never had this issue before.

OK, then we should also check the M-builds produced today.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2203549</commentid>
    <comment_count>14</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-01-16 05:13:23 -0500</bug_when>
    <thetext>3.8.1 - Not reproducible
4.2.1 - Not reproducible

I20121218-1600 - Not reproducible

M20130104-1300 - Not reproducible
M20130109-1200 - Not reproducible

N20130111-2000 - Reproducible
N20130112-2000 - Reproducible</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2203844</commentid>
    <comment_count>15</comment_count>
    <who name="Lars Vogel">lars.vogel@vogella.com</who>
    <bug_when>2013-01-16 14:28:58 -0500</bug_when>
    <thetext>Copying Paul, in case platform has changed something recently in the save behavior.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2204003</commentid>
    <comment_count>16</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-01-17 00:16:01 -0500</bug_when>
    <thetext>M20130116-1800 - Not Reproducible
N20130116-2000 - Reproducible</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2204255</commentid>
    <comment_count>17</comment_count>
    <who name="Rabea Gransberger">rgransberger@gmx.de</who>
    <bug_when>2013-01-17 10:04:23 -0500</bug_when>
    <thetext>I have seen the error message related to the Save Action in 4.2 but never looked into the problem or how to reproduce it yet. I will have a look if it happens again for me.

There are also formatting issues where the Save-Action behaves differently than Strg+F and reformats my file.

In rare case the class declaration is lost on Save and the file starts with imports and somewhere at the field declarations. I will also look into it to have a description on how to reproduce this error.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2204256</commentid>
    <comment_count>18</comment_count>
    <who name="Lars Vogel">lars.vogel@vogella.com</who>
    <bug_when>2013-01-17 10:06:45 -0500</bug_when>
    <thetext>@Rabea see comment 15 and comment 14 in which releases this currently happens.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2204288</commentid>
    <comment_count>19</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-01-17 10:42:33 -0500</bug_when>
    <thetext>I can reproduce it. Note that it is Ctrl+Shift+O and not Ctrl+O. Also, I don&apos;t get any of the mentioned exceptions when starting with a new workspace.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2204333</commentid>
    <comment_count>20</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-01-17 11:32:15 -0500</bug_when>
    <thetext>This is caused by a temporary change which accidentally got committed. Only Kepler builds done after 2013-01-03 10:08:34 (EST) are affected.

Also, the bug only happens when quickly typing Ctrl+S directly after adding the import (Ctrl+Shift+O).

Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=51636e9b5ca9d6f5f642330ed00b8f7d7a8e0871</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2204773</commentid>
    <comment_count>21</comment_count>
    <who name="Lars Vogel">lars.vogel@vogella.com</who>
    <bug_when>2013-01-18 09:43:08 -0500</bug_when>
    <thetext>Thanks Dani!</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2204776</commentid>
    <comment_count>22</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-01-18 09:47:17 -0500</bug_when>
    <thetext>(In reply to comment #21)
&gt; Thanks Dani!

np, but please don&apos;t touch the bugzilla fields that I changed ;-).</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2209073</commentid>
    <comment_count>23</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-01-29 02:28:37 -0500</bug_when>
    <thetext>Verifying in I20130128-2000.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2209094</commentid>
    <comment_count>24</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-01-29 03:35:35 -0500</bug_when>
    <thetext>(In reply to comment #23)
&gt; Verifying in I20130128-2000.

Verified in build id: I20130128-2000.
The issue is not reproducible.</thetext>
  </long_desc>
      
          <attachment
              isobsolete="0"
              ispatch="0"
              isprivate="0"
          >
            <attachid>225585</attachid>
            <date>2013-01-14 13:19:00 -0500</date>
            <delta_ts>2013-01-14 13:19:13 -0500</delta_ts>
            <desc>Screenshot of Error</desc>
            <filename>Save Problems _001.png</filename>
            <type>image/png</type>
            <size>17330</size>
            <attacher name="Lars Vogel">lars.vogel@vogella.com</attacher>
            
              <token>1425706891-OD7hPL9Be3RJHE6yH7OeUnAK2KjHbUKBrshwVJi-h18</token>

          </attachment>
          <attachment
              isobsolete="0"
              ispatch="0"
              isprivate="0"
          >
            <attachid>225586</attachid>
            <date>2013-01-14 13:19:00 -0500</date>
            <delta_ts>2013-01-14 13:19:42 -0500</delta_ts>
            <desc>Example project</desc>
            <filename>jdtbug.zip</filename>
            <type>application/zip</type>
            <size>8698</size>
            <attacher name="Lars Vogel">lars.vogel@vogella.com</attacher>
            
              <token>1425706891-rTQvZIcti9ZS5aL4UjOau_ttGqhkXEbOFJAW9tX8h14</token>

          </attachment>
          <attachment
              isobsolete="0"
              ispatch="0"
              isprivate="0"
          >
            <attachid>225685</attachid>
            <date>2013-01-16 01:30:00 -0500</date>
            <delta_ts>2013-01-16 01:30:49 -0500</delta_ts>
            <desc>Error on importing the project</desc>
            <filename>error on importing project.txt</filename>
            <type>text/plain</type>
            <size>2294</size>
            <attacher name="Noopur Gupta">noopur_gupta@in.ibm.com</attacher>
            
              <token>1425706891-CxSBMV4H9ucmFyJvsQdo_eaBA7muGOZ_y5-tSHyx6LQ</token>

          </attachment>
          <attachment
              isobsolete="0"
              ispatch="0"
              isprivate="0"
          >
            <attachid>225686</attachid>
            <date>2013-01-16 01:33:00 -0500</date>
            <delta_ts>2013-01-16 01:33:26 -0500</delta_ts>
            <desc>Error while trying to reproduce the issue</desc>
            <filename>error log 1.txt</filename>
            <type>text/plain</type>
            <size>4806</size>
            <attacher name="Noopur Gupta">noopur_gupta@in.ibm.com</attacher>
            
              <token>1425706891-A2HdHwGR8tvKn8pb-vnMnUjqSGijoJdSkySa03TL0ZU</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>398076</bug_id>
          
          <creation_ts>2013-01-14 08:51:00 -0500</creation_ts>
          <short_desc>Add test cases for bug 357450</short_desc>
          <delta_ts>2013-01-21 23:37:47 -0500</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords>test</keywords>
          <priority>P3</priority>
          <bug_severity>enhancement</bug_severity>
          <target_milestone>4.3 M5</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Dani Megert">daniel_megert@ch.ibm.com</reporter>
          <assigned_to name="Noopur Gupta">noopur_gupta@in.ibm.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>noopur_gupta@in.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706891-0GQA9woxQJ-GzjDzhmD4Sj1qjx8hKR0m_WFsi-d4D6k</token>

      

      <flag name="review"
          id="55044"
          type_id="1"
          status="+"
          setter="daniel_megert@ch.ibm.com"
    />

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2202381</commentid>
    <comment_count>0</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-01-14 08:51:37 -0500</bug_when>
    <thetext>master.

We need to add test cases for bug 357450.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2202985</commentid>
    <comment_count>1</comment_count>
      <attachid>225630</attachid>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-01-15 08:40:27 -0500</bug_when>
    <thetext>Created attachment 225630
Patch-test cases for bug 357450

Added the test class &apos;ContentProviderTests6&apos; and also added it to the &apos;PackageExplorerTests&apos; suite.

The test class contains 4 test cases:
1. Add a file to class folder
2. Add a folder to class folder
3. Remove a file from class folder
4. Remove a folder from class folder

Each test case checks for the refreshed objects after the action is performed and verifies that both the library container and the class folder resource are refreshed.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2203467</commentid>
    <comment_count>2</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-01-16 01:48:37 -0500</bug_when>
    <thetext>One observation..
The field &apos;IPackageFragmentRoot classFolder&apos; should be renamed as &apos;fClassFolder&apos;.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2205427</commentid>
    <comment_count>3</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-01-21 08:10:26 -0500</bug_when>
    <thetext>Thanks for the patch Noopur!

The tests fail without the fix from bug 357450 and pass with the fix. I&apos;ve committed the patch to &apos;master&apos; after fixing the copyright (for new files we only have to add the current year, see code in &apos;master&apos;).

Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=9a9b9d6fd7d116505f8f2933d6c8047f391e366a


I see you copied the code from one of the other tests. Do you like that some of the fields are used only inside a single method but still declared as fields? I don&apos;t too much, so fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=d38770e79f7539a02c04283db1973de6d2729d5a</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2205765</commentid>
    <comment_count>4</comment_count>
    <who name="Noopur Gupta">noopur_gupta@in.ibm.com</who>
    <bug_when>2013-01-21 23:37:47 -0500</bug_when>
    <thetext>(In reply to comment #3)
&gt; Thanks for the patch Noopur!
&gt; 
&gt; The tests fail without the fix from bug 357450 and pass with the fix. I&apos;ve
&gt; committed the patch to &apos;master&apos; after fixing the copyright (for new files we
&gt; only have to add the current year, see code in &apos;master&apos;).
&gt; 
&gt; Fixed with
&gt; http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/
&gt; ?id=9a9b9d6fd7d116505f8f2933d6c8047f391e366a
&gt; 
&gt; 
&gt; I see you copied the code from one of the other tests. Do you like that some
&gt; of the fields are used only inside a single method but still declared as
&gt; fields? I don&apos;t too much, so fixed with
&gt; http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/
&gt; ?id=d38770e79f7539a02c04283db1973de6d2729d5a

Thanks Dani. I will take care of the above from now on i.e. adding copyright to new files and not declaring the variables used only inside a method as fields.</thetext>
  </long_desc>
      
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>225630</attachid>
            <date>2013-01-15 08:40:00 -0500</date>
            <delta_ts>2013-01-15 08:40:27 -0500</delta_ts>
            <desc>Patch-test cases for bug 357450</desc>
            <filename>Bug-398076-Add-test-cases-for-bug-357450.patch</filename>
            <type>text/plain</type>
            <size>9644</size>
            <attacher name="Noopur Gupta">noopur_gupta@in.ibm.com</attacher>
            
              <token>1425706891-5efjCj1LK0iDq1-QJyW02IqrYFU3eLFlqp9FCUfcR1k</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>397467</bug_id>
          
          <creation_ts>2013-01-04 12:57:00 -0500</creation_ts>
          <short_desc>Javadoc hover/view should linkify package</short_desc>
          <delta_ts>2013-03-12 11:42:41 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>VERIFIED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>enhancement</bug_severity>
          <target_milestone>4.3 M6</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Markus Keller">markus_keller@ch.ibm.com</reporter>
          <assigned_to name="Manju Mathew">manju656@gmail.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706891-qyK3ePL6A4-p6do_UrOVf6LJkrqep4apmr7BO-zU5Wc</token>

      

      <flag name="review"
          id="55385"
          type_id="1"
          status="+"
          setter="daniel_megert@ch.ibm.com"
    />

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2199060</commentid>
    <comment_count>0</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-01-04 12:57:06 -0500</bug_when>
    <thetext>Now that we can show package Javadoc, we should also linkify the package segments in Javadoc headers. We already have links for enclosing method/type of an element, and we should extend this to packages.

Package links should not span the whole qualified package name, but only simple names. E.g. for java.lang.ref.Reference,
- &quot;java&quot; should link to package &quot;java&quot;
- &quot;lang&quot; should link to package &quot;java.lang&quot;
- &quot;ref&quot; should link to package &quot;java.lang.ref&quot;

The advantage of separately linking super packages are that
- super packages become accessible
- the browser widget still allows the user to select only parts of a package (if the whole qualified name is a single link, then you cannot select &quot;java.lang&quot; any more)</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2211712</commentid>
    <comment_count>1</comment_count>
      <attachid>226502</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-02-04 08:33:42 -0500</bug_when>
    <thetext>Created attachment 226502
Proposed Fix.

Package name present in Javadoc hover and view header is now linked. User can now select individual package names and see the Javadoc if any provided for it. Enabled for PackageFragment and PackageDeclaration.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2211870</commentid>
    <comment_count>2</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-02-04 11:10:06 -0500</bug_when>
    <thetext>(In reply to comment #1)
&gt; Created attachment 226502 [details] [diff]
&gt; Proposed Fix.
&gt; 
&gt; Package name present in Javadoc hover and view header is now linked.
&gt; User
&gt; can now select individual package names and see the Javadoc if any provided
&gt; for it. Enabled for PackageFragment and PackageDeclaration.

This seems to work as desired.

For now, I only quickly looked at the patch since I do not understand why there are changes in &apos;JavaElementLabelComposer&apos;. If the idea was to use #getElementName, then I do not understand why you only made that refactoring at two places, and also not why it needs to be part of the fix for this bug.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2212120</commentid>
    <comment_count>3</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-02-05 00:04:38 -0500</bug_when>
    <thetext>(In reply to comment #2)

&gt; This seems to work as desired.
&gt; 
&gt; For now, I only quickly looked at the patch since I do not understand why
&gt; there are changes in &apos;JavaElementLabelComposer&apos;. If the idea was to use
&gt; #getElementName, then I do not understand why you only made that refactoring
&gt; at two places, and also not why it needs to be part of the fix for this bug.

JavaElementLinks has a class &quot;JavaElementLinkedLabelComposer&quot; which  extends &quot;JavaElementLabelComposer&quot;. JavaElementLabelComposer serves as a label provider for many ui components. getElementName() method is overridden, so depending on who invokes, either the simple name of the element or the  resolved link is returned. For other element types like methods, fields etc this is already taken care off, hence i had to modify only in 2 places to take care of the PackageFragment and the PackageDeclaration.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2212242</commentid>
    <comment_count>4</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-02-05 07:22:27 -0500</bug_when>
    <thetext>The patch is OK, but can be improved a bit:

- I don&apos;t think #getLastSegmentName is needed since the result is always
  individualSegmentNames[i], no?

- individualSegmentNames[i] could be extracted to a local variable

- &quot;linkIndividualPackageFragmentSegments&quot; should be renamed since the other
  #getElementName method also creates the links
  ==&gt; &quot;getPackageFragmentElementName&quot;  or &quot;getPackageFragmentName&quot;


Note, that I added a comment to JavaElementLabelComposer.getElementName(IJavaElement), i.e. make sure to pull this change before creating a new patch.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2212327</commentid>
    <comment_count>5</comment_count>
      <attachid>226570</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-02-05 09:40:12 -0500</bug_when>
    <thetext>Created attachment 226570
Updated Patch.

(In reply to comment #4)
&gt; The patch is OK, but can be improved a bit:
&gt; 
&gt; - I don&apos;t think #getLastSegmentName is needed since the result is always
&gt;   individualSegmentNames[i], no?
Yes, individualSegmentNames[i] has the last segment name. 

&gt; 
&gt; - individualSegmentNames[i] could be extracted to a local variable
reused individualSegmentNames[i] after extracting to a local variable.

&gt; 
&gt; - &quot;linkIndividualPackageFragmentSegments&quot; should be renamed since the other
&gt;   #getElementName method also creates the links
&gt;   ==&gt; &quot;getPackageFragmentElementName&quot;  or &quot;getPackageFragmentName&quot;
renamed to getPackageFragmentElementName.

&gt; 
&gt; Note, that I added a comment to
&gt; JavaElementLabelComposer.getElementName(IJavaElement), i.e. make sure to
&gt; pull this change before creating a new patch.
modified the Javadoc slightly.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2212414</commentid>
    <comment_count>6</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-02-05 11:20:25 -0500</bug_when>
    <thetext>(In reply to comment #5)
&gt; Created attachment 226570 [details] [diff]
&gt; Updated Patch.

This patch is not complete: it misses the changes for &apos;JavaElementLabelComposer&apos;. To avoid another ping-pong, I took the changes from the previous patch. Also, I did not use your change to the Javadoc but made another tweak myself (please review).

Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=3ee8f8c961ee91ef640925ef9adc08d3fa1034b9</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2212416</commentid>
    <comment_count>7</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-02-05 11:20:42 -0500</bug_when>
    <thetext>.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2212418</commentid>
    <comment_count>8</comment_count>
      <attachid>226570</attachid>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-02-05 11:21:16 -0500</bug_when>
    <thetext>Comment on attachment 226570
Updated Patch.

Setting &apos;iplog+&apos; since I missed to set the author when committing.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2229688</commentid>
    <comment_count>9</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-03-12 11:42:41 -0400</bug_when>
    <thetext>Verified in I20130311-2000.</thetext>
  </long_desc>
      
          <attachment
              isobsolete="1"
              ispatch="1"
              isprivate="0"
          >
            <attachid>226502</attachid>
            <date>2013-02-04 08:33:00 -0500</date>
            <delta_ts>2013-02-05 09:40:12 -0500</delta_ts>
            <desc>Proposed Fix.</desc>
            <filename>eclipse.jdt.ui.397467_20130204.patch</filename>
            <type>text/plain</type>
            <size>4326</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706891-aCBPb0t6beIgdt8rAwDsBWcMWi-BvUSGRSfRftUv8CI</token>

          </attachment>
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>226570</attachid>
            <date>2013-02-05 09:40:00 -0500</date>
            <delta_ts>2013-02-05 11:21:16 -0500</delta_ts>
            <desc>Updated Patch.</desc>
            <filename>eclipse.jdt.ui.397467_20130205.patch</filename>
            <type>text/plain</type>
            <size>3760</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706891-AEx2sbqhVBBtxEeHmV1oyyZHasGfF4bNt4llx0pRxls</token>
<flag name="iplog"
          id="55427"
          type_id="7"
          status="+"
          setter="daniel_megert@ch.ibm.com"
    />
          </attachment>
      

    </bug>
    <bug>
          <bug_id>397465</bug_id>
          
          <creation_ts>2013-01-04 12:34:00 -0500</creation_ts>
          <short_desc>[hovering] Open Declaration doesn&apos;t work in Javadoc hover on IPackageFragment</short_desc>
          <delta_ts>2013-01-30 08:25:02 -0500</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>VERIFIED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>normal</bug_severity>
          <target_milestone>4.3 M5</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Markus Keller">markus_keller@ch.ibm.com</reporter>
          <assigned_to name="Manju Mathew">manju656@gmail.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706891-J1l3L4V9AiYoSyBuJKD7MXm_YnzUOWW6_5gMCmdwnlg</token>

      

      

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2199051</commentid>
    <comment_count>0</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-01-04 12:34:26 -0500</bug_when>
    <thetext>Open Declaration doesn&apos;t work in Javadoc hover on IPackageFragment.

This action is available in the toolbar of the Javadoc view and in rich Javadoc hovers. It&apos;s also available via the element icon in the Javadoc header (the icon is a clickable link).

If there&apos;s a package-info.(java|class) or package.html file, then we should open that one in an editor. Otherwise, we should open the Package Explorer and select/reveal the package fragment.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2199054</commentid>
    <comment_count>1</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-01-04 12:43:37 -0500</bug_when>
    <thetext>Open Declaration (F3) and hyperlinking also doesn&apos;t work on package declarations or references. I think it would make sense to enable Open Declaration on packages in general.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2199224</commentid>
    <comment_count>2</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-01-05 04:19:31 -0500</bug_when>
    <thetext>(In reply to comment #1)
&gt; Open Declaration (F3) and hyperlinking also doesn&apos;t work on package
&gt; declarations or references. I think it would make sense to enable Open
&gt; Declaration on packages in general.

I disagree. I would not want the editor to open when I hit F3 on a package in the Package Explorer. And adding this inside the editor doesn&apos;t make much sense either for me.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2199226</commentid>
    <comment_count>3</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-01-05 04:25:38 -0500</bug_when>
    <thetext>&gt; Otherwise, we should open the Package Explorer and select/reveal the package
&gt; fragment.

So far, &apos;Open Declaration&apos; always opened the editor (and the icon indicates this too), but I&apos;m fine to stretch the concept here a bit.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2199731</commentid>
    <comment_count>4</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-01-07 12:32:55 -0500</bug_when>
    <thetext>I agree that selecting the package in the Package Explorer is stretching the concept. However, when there&apos;s no package-info, it&apos;s really the package directory that declares the package.

That&apos;s similar to a Java class that lacks an explicit constructor declaration: There, F3 on a class instance creation also jumps to the enclosing element -- the class declaration.

(In reply to comment #2)
&gt; And adding this inside the editor doesn&apos;t make much sense either for me.

Jumping to a package declaration can be handy if you need to add an annotation there (e.g. @NonNullByDefault). I don&apos;t see a big difference between jumping to a package declaration and jumping to any other element.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2199989</commentid>
    <comment_count>5</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-01-08 03:08:51 -0500</bug_when>
    <thetext>(In reply to comment #4)
&gt; I agree that selecting the package in the Package Explorer is stretching the
&gt; concept. However, when there&apos;s no package-info, it&apos;s really the package
&gt; directory that declares the package.

Open [*] is the concept that opens editors. I want to keep this clean. As discussed, we could alternatively open an editor with a template that can then be stored. Of course this only works for source. Seems like a bit overkill and/or a separate feature request.
 
&gt; That&apos;s similar to a Java class that lacks an explicit constructor
&gt; declaration: There, F3 on a class instance creation also jumps to the
&gt; enclosing element -- the class declaration.

But it stays in the editor.


&gt; (In reply to comment #2)
&gt; &gt; And adding this inside the editor doesn&apos;t make much sense either for me.
&gt; 
&gt; Jumping to a package declaration can be handy if you need to add an
&gt; annotation there (e.g. @NonNullByDefault). I don&apos;t see a big difference
&gt; between jumping to a package declaration and jumping to any other element.

Agreed.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2200093</commentid>
    <comment_count>6</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-01-08 06:57:54 -0500</bug_when>
    <thetext>OK, to summarize:

In the Javadoc view and in the Javadoc hover, the Open Declaration button should open the package info file if one exists, and fall back to selecting the package in the Package Explorer if no file is available.

In the editor, Open Declaration should only open the package info file if one exists, and otherwise show the error message like today.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2205442</commentid>
    <comment_count>7</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-01-21 08:50:10 -0500</bug_when>
    <thetext>Markus, below are the points taken care during fixing this bug.

1. Open declaration will open package-info.java, package-info.class or package.html files if it is present in source or binary container.

2. An exception to the above is for package.html present in a Jar file. I could not find a EditorUtilty that opens a normal file (i.e. not an IFile). Hence in this case the Javadoc Hover silently fails(nothing happens when the user clicks on Open Declaration), Javadoc View pops an error dialog.

3. The case when the package javadoc is retrieved from JavaElement.getAttachedJavadoc(), then open declaration has no file input to open the editor. The default behaviour in JavadocView is to pop an error dialog as in the above case. JavadocHover silently fails again.

4. If there is no package Javadoc file for a package present in source container, then Open Declaration selects the corresponding package in PackageExplorer View.

5. Regarding Junit testcases for these cases, since all the scenario is about opening the underlying resource associated and also an action is performed so as to activate the scenario, i am not able to figure out what kind of JUnits to write for them.

Let me know what were the expected behavior in the above cases/ have i handled them properly? Also what other cases needs to be handled?</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2205453</commentid>
    <comment_count>8</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-01-21 09:21:20 -0500</bug_when>
    <thetext>&gt; 1., 4.

Sounds good.

&gt; 2., 3.

See comment 6: we should not show an error dialog, but:
&gt; fall back to selecting the package in the Package Explorer if no file is
&gt; available.

I.e., in case the package file is not available as a file (e.g. it&apos;s in a Jar or an external URL), we also fall back to selecting the package in the PE. If there are multiple IPackageFragments that could be selected, use the first one on the build path.

&gt; 5. Junit testcases

That&apos;s OK. I think this is one of these &quot;end of the food chain&quot; areas, where writing and maintaining tests is more work than we want to spend, since the expected gains are not high enough.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2205822</commentid>
    <comment_count>9</comment_count>
      <attachid>225927</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-01-22 04:19:06 -0500</bug_when>
    <thetext>Created attachment 225927
Proposed Fix.

In this fix
1. If user invoke Open Declaration from Javadoc View or Javadoc Hover or from the Java editor, then the available package-info.java or package-info.class or package.html file of that package is opened in the corresponding editor.
2. If the file is present in an archive, or if there is no Javadoc file associated to that package, then the corresponding package is highlighted in the package explorer view.
3. If there are multiple IPackageFragments that could be selected, then the first one from the build path is selected.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2207874</commentid>
    <comment_count>10</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-01-25 12:46:43 -0500</bug_when>
    <thetext>(In reply to comment #9)
&gt; Created attachment 225927 [details] [diff]

I like the behavior, but it doesn&apos;t implement what comment 6 summarized:

&gt; In the editor, Open Declaration should only open the package info file if one &gt; exists, and otherwise show the error message like today.


Implementation comments:

1. JavaModelUtil#isBinary(IJavaElement) doesn&apos;t work for all arguments. Utility methods must not leave room for interpretation/surprises.

2. Code flow in JavadocHover.OpenDeclarationAction#openInEditor(IPackageFragment) is overly complicated. foundPackageJavadoc is not necessary. Use return statements.

3. OpenAction#getPackageFragmentObjectToOpen(IPackageFragment) is supposed to be a pure function that doesn&apos;t have side effects. The &quot;view.selectAndReveal...&quot; must be moved out. And you should use &quot;view.tryToReveal...&quot;, so that it works more like Show In &gt; Package Explorer (e.g. asks to remove filters).</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2208456</commentid>
    <comment_count>11</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-01-28 06:03:41 -0500</bug_when>
    <thetext>(In reply to comment #10)
The &quot;package info file&quot; here means all 3 variants. The important point is not to select the package fragment in the Package Explorer when Open Declaration is executed in the editor (but behave like before in this case).</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2208743</commentid>
    <comment_count>12</comment_count>
      <attachid>226214</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-01-28 12:30:12 -0500</bug_when>
    <thetext>Created attachment 226214
Proposed Fix.

Thanks Markus for the clarification. 

Now Open declaration from editor will show error message if the corresponding package Javadoc does not exist.

Took care of the code review comments.
1. Removed the utility method.
2. Refactored  JavadocHover.OpenDeclarationAction#openInEditor(IPackageFragment).
3. used view.tryToReveal(element) and is moved out of the getPackageFragmentObjectToOpen method.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2208864</commentid>
    <comment_count>13</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-01-28 15:26:27 -0500</bug_when>
    <thetext>(In reply to comment #12)
Changes in JavadocHover look mostly good, but the package should also be opened when I click the package icon in the hover.
Please rename &quot;iFile&quot; to &quot;file&quot; and make format all comments the same way, e.g.:
// select the package in the Package Explorer ...

In the editor, F3 shouldn&apos;t open an error dialog, but show the error in the status line like before.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2209010</commentid>
    <comment_count>14</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-01-28 18:28:33 -0500</bug_when>
    <thetext>Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=e775f37ffdd45a30062233ba3bde2bd8c413bbd4 , so that we can test it tomorrow.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2209810</commentid>
    <comment_count>15</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-01-30 08:25:02 -0500</bug_when>
    <thetext>Verified in I20130129-2000.</thetext>
  </long_desc>
      
          <attachment
              isobsolete="1"
              ispatch="1"
              isprivate="0"
          >
            <attachid>225927</attachid>
            <date>2013-01-22 04:19:00 -0500</date>
            <delta_ts>2013-01-28 12:30:12 -0500</delta_ts>
            <desc>Proposed Fix.</desc>
            <filename>eclipse.jdt.ui.20130122.patch</filename>
            <type>text/plain</type>
            <size>9691</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706891-CxcYezBYohrPFrGbQNLuNH3zFp_JbLQENI37mDhT72c</token>

          </attachment>
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>226214</attachid>
            <date>2013-01-28 12:30:00 -0500</date>
            <delta_ts>2013-01-28 12:30:12 -0500</delta_ts>
            <desc>Proposed Fix.</desc>
            <filename>eclipse.jdt.ui.20130128.patch</filename>
            <type>text/plain</type>
            <size>9068</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706891-kbe1dNSq7zO9aG7sYYtVrjr4ZOnYl08eeq6SL0BeXIE</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>397464</bug_id>
          
          <creation_ts>2013-01-04 12:32:00 -0500</creation_ts>
          <short_desc>No Javadoc for package-info.java in source attachment when package-info.class doesn&apos;t exist</short_desc>
          <delta_ts>2013-01-25 11:06:30 -0500</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>normal</bug_severity>
          <target_milestone>4.3 M5</target_milestone>
          
          <blocked>396809</blocked>
          <everconfirmed>1</everconfirmed>
          <reporter name="Markus Keller">markus_keller@ch.ibm.com</reporter>
          <assigned_to name="Manju Mathew">manju656@gmail.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>manju656@gmail.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706891-Ke6-qGousuD51_3aRhz0tPBibG5NRCkwLUrY1KdaKvM</token>

      

      

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2199049</commentid>
    <comment_count>0</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-01-04 12:32:56 -0500</bug_when>
    <thetext>Follow-up to bug 163633 comment 5:
&gt; Manju, there could be an additional complication with package-info in the
&gt; source attachment.
&gt; 
&gt; E.g. in jdk7, the src.zip contains java/lang/package-info.java, but since
&gt; the package declaration doesn&apos;t carry annotations, no package-info.class
&gt; file is generated. Hence, the IClassFile for package-info doesn&apos;t exist and
&gt; getSource() probably doesn&apos;t work. Once you&apos;ve verified that this is really
&gt; a problem, please file a bug for JDT/Core requesting that
&gt; IClassFile#getSource() should still work in this special case.

When I remove the Javadoc location for a JDK7 and leave the source attachment untouched, I don&apos;t get Javadoc in the view or hover for java.lang.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2199229</commentid>
    <comment_count>1</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-01-05 04:52:01 -0500</bug_when>
    <thetext>In the case of &apos;java.lang&apos; from source, we run into the NPE from bug 397455 and hence no Javadoc. But we also forgot to search the &apos;package-info.java&apos; in the source attachment.

Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=a7ec327fd0ef595c2c4bf8d664efb7ad16c44b25</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2199958</commentid>
    <comment_count>2</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-01-08 00:35:55 -0500</bug_when>
    <thetext>Dani, we had a discussion about searching the &apos;package-info.java&apos; file in the source attachment. It was concluded that for Java class files, core will make the necessary association after considering the source attachment path and thus through getSource() method we will get the source content. For HTML file we will explicitly make the search in the source attachment path.

So the current fix to search the source attachment path for package-info.java will not help, as we still need a Java element corresponding to the compilation unit and getJavaElement() on the compilation unit returns null in this particular scenario which Markus has pointed. JDT Core needs to give us a fix for this case.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2199985</commentid>
    <comment_count>3</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-01-08 02:57:17 -0500</bug_when>
    <thetext>(In reply to comment #2)
&gt; Dani, we had a discussion about searching the &apos;package-info.java&apos; file in
&gt; the source attachment. It was concluded that for Java class files, core will
&gt; make the necessary association after considering the source attachment path
&gt; and thus through getSource() method we will get the source content. 

Sure, but only if there is a class file.


&gt; So the current fix to search the source attachment path for
&gt; package-info.java will not help, as we still need a Java element
&gt; corresponding to the compilation unit and getJavaElement() on the
&gt; compilation unit returns null in this particular scenario which Markus has
&gt; pointed.

Please provide exact steps here, that show it doesn&apos;t work.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2200006</commentid>
    <comment_count>4</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-01-08 03:37:33 -0500</bug_when>
    <thetext>With the current fix, the string content of package-info.java is retrieved and this is used to create an ASTNode of type CompilationUnit. To get the Javadoc from this ASTNode we need its JavaElement. This is null. Without a proper Java element we cannot retrieve the Javadoc.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2200009</commentid>
    <comment_count>5</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-01-08 03:42:25 -0500</bug_when>
    <thetext>(In reply to comment #4)
&gt; With the current fix, the string content of package-info.java is retrieved
&gt; and this is used to create an ASTNode of type CompilationUnit. To get the
&gt; Javadoc from this ASTNode we need its JavaElement. This is null. Without a
&gt; proper Java element we cannot retrieve the Javadoc.

Well, I think my fix worked before (except for the NPE which didn&apos;t always occur) and now, due to the newly added assertions it will always fail.

Please add the steps as requested in comment 4 and take a look at a fix for the AST creation code. Thanks.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2200062</commentid>
    <comment_count>6</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-01-08 06:01:48 -0500</bug_when>
    <thetext>Let&apos;s take a step back here. JavadocContentAccess2#createAST(ITypeRoot typeRoot) is unnecessary and should be removed. Bindings are too expensive for Javadoc hovers, so the whole implementation has been written to work without bindings. (We only resolve links when the user actually clicked a link.)

#createAST(..) should be inlined again. The code is not reused/reusable, and the name is wrong (creates a cuNode, not an AST; creates a very specific temporary AST).

Then, you need a new method that works similar to #getJavadocNode(..). That method should use #createASTParser(..), but then it should create an AST from the whole package-info type root and then get the Javadoc via cuNode.getPackage().getJavadoc().


#getJavadocFromAST(..) will also be removed. BTW: The implementation of that method had two more problems:
- cuNode.getCommentList() is always non-null, so the null check is unnecessary
- cuNode.getCommentList() returns all comment nodes. If someone writes a package-info.java like this, you&apos;d get the wrong comment:
/** Doc */
package pack;
/** End */</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2200073</commentid>
    <comment_count>7</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-01-08 06:18:31 -0500</bug_when>
    <thetext>(In reply to comment #6)
&gt; - cuNode.getCommentList() returns all comment nodes. If someone writes a
&gt; package-info.java like this, you&apos;d get the wrong comment:
&gt; /** Doc */
&gt; package pack;
&gt; /** End */

Good catch!</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2200086</commentid>
    <comment_count>8</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-01-08 06:32:28 -0500</bug_when>
    <thetext>(In reply to comment #2)
&gt; So the current fix to search the source attachment path for
&gt; package-info.java will not help, as we still need a Java element
&gt; corresponding to the compilation unit and getJavaElement() on the
&gt; compilation unit returns null in this particular scenario which Markus has
&gt; pointed. JDT Core needs to give us a fix for this case.

Since we already have the code that opens the source attachment and looks for the package.html file there, I think we should just reuse that to find the package-info.java there as well. That will avoid special cases in JDT/Core to fake a package-info.class just to let us get the package-info.java&apos;s source.

=&gt; If we have an existing ITypeRoot for package-info, then we should use that one to create the AST. Otherwise, we look it up in the source attachment, and then we just use ASTParser#setSource(char[]) to create the AST.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2200675</commentid>
    <comment_count>9</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-01-09 09:48:58 -0500</bug_when>
    <thetext>Re resolving links in package-info.java via JavaElementLinks#parseURI(URI): 

For Javadoc on an IMember, we can use IType#resolveType(String) to resolve the second segment of the URI. But for the package-info.java, there&apos;s no similar API that resolves the imports of the package-info.java file. We could file an API request for IPackageDeclaration#resolveType(String), but that would only work as long as the package-info element exists. For the case were we use the package-info.java from the source attachment, that also wouldn&apos;t work.

I think the best solution is to implement this on our own for package-info.java: create an AST and try to resolve the type name against the non-static imports. For on-demand imports and if nothing matched, use IJavaProject#findType(..).</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2204681</commentid>
    <comment_count>10</comment_count>
      <attachid>225809</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-01-18 05:50:58 -0500</bug_when>
    <thetext>Created attachment 225809
Proposed Fix

This patch also contains the fix for bug 397455, as both the fix was related to the same file.

The review comments from Markus(https://bugs.eclipse.org/bugs/show_bug.cgi?id=397464#c6) is taken care off. Also we have handled re-resolving links in package-info.java when the corresponding class file does not exist. To resolve the links we are checking for the below condition
1. Whether the type is fully qualified 
2. Whether the type is from the enclosing package
3. Whether the type belongs to an on-demand-import or type import
4. Whether the type belongs to java.lang package</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2207794</commentid>
    <comment_count>11</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-01-25 10:52:15 -0500</bug_when>
    <thetext>(In reply to comment #10)
&gt; Created attachment 225809 [details] [diff]
&gt; Proposed Fix

The fix still had a few issues (e.g. it concatenated package-info.java content with &quot;class C{}&quot; and then created an AST on the bad source; fElements could contain bogus elements; links to members like {@link javax.annotation.Generated#date()} didn&apos;t work; problems in the source attachment lookup order).

The imports resolution in JavaElementLinks also didn&apos;t adhere to the JLS7 rules. However, when I was done with the correct implementation, I found that the scoping rules for Javadoc links in package-info.java are broken anyway, see bug 216451 comment 4. In the end, I commented out the implementation and went with what the javadoc.exe supports (only fully-qualified type references).

Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=3dc7c2a368684cdcd97bee9b8d41b031ee17aef3</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2207802</commentid>
    <comment_count>12</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-01-25 11:05:46 -0500</bug_when>
    <thetext>*** Bug 397455 has been marked as a duplicate of this bug. ***</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2207804</commentid>
    <comment_count>13</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-01-25 11:06:30 -0500</bug_when>
    <thetext>.</thetext>
  </long_desc>
      
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>225809</attachid>
            <date>2013-01-18 05:50:00 -0500</date>
            <delta_ts>2013-01-18 05:50:58 -0500</delta_ts>
            <desc>Proposed Fix</desc>
            <filename>eclipse.jdt.ui.20130118.patch</filename>
            <type>text/plain</type>
            <size>15142</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706892-H4ZBFgD-dDH3vBECX1rUeiyMPTzOOggil6CkJVuuAGM</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>397447</bug_id>
          
          <creation_ts>2013-01-04 09:24:00 -0500</creation_ts>
          <short_desc>[hovering] Code polishing for the package Javadoc hovering feature.</short_desc>
          <delta_ts>2013-01-29 02:32:49 -0500</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P2</priority>
          <bug_severity>normal</bug_severity>
          <target_milestone>4.3 M5</target_milestone>
          <dependson>398272</dependson>
          <blocked>396809</blocked>
          <everconfirmed>1</everconfirmed>
          <reporter name="Manju Mathew">manju656@gmail.com</reporter>
          <assigned_to name="Manju Mathew">manju656@gmail.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706892-tuGp4HOgncRIxh0zhGTjP3OqK53nw4Hwp-IDxVOCAxs</token>

      

      <flag name="review"
          id="55203"
          type_id="1"
          status="+"
          setter="daniel_megert@ch.ibm.com"
    />

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2198956</commentid>
    <comment_count>0</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-01-04 09:24:53 -0500</bug_when>
    <thetext>Some minor miscellaneous code changes for the package hovering feature.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2198959</commentid>
    <comment_count>1</comment_count>
      <attachid>225215</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-01-04 09:33:34 -0500</bug_when>
    <thetext>Created attachment 225215
The polished code is attached as patch</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2199228</commentid>
    <comment_count>2</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-01-05 04:49:22 -0500</bug_when>
    <thetext>I&apos;ve already fixed the toOSString() with the fix for bug 397464, so I only applied the change in ProposalInfo:

Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=046ee0128866e0a27a85f295b682656c3af84b92


Some other thing to polish: if no Javadoc is available (e.g. for &apos;sun.awt.im&apos;) we log an error. This is not good.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2199546</commentid>
    <comment_count>3</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-01-07 08:36:00 -0500</bug_when>
    <thetext>I also get exceptions when hovering over a field in the compare editor (e.g. when comparing org.eclipse.jdt.ui.wizards.NewJavaProjectWizardPageTwo with some older version and hover over &apos;fOrginalFolders&apos;:

!ENTRY org.eclipse.jdt.ui 4 10001 2013-01-07 14:33:46.863
!MESSAGE Internal Error
!STACK 1
Java Model Exception: Java Model Status [&lt;project root&gt; [in  ] is not on its project&apos;s build path]
	at org.eclipse.jdt.internal.core.JavaElement.newJavaModelException(JavaElement.java:508)
	at org.eclipse.jdt.internal.core.Openable.generateInfos(Openable.java:246)
	at org.eclipse.jdt.internal.core.JavaElement.openWhenClosed(JavaElement.java:521)
	at org.eclipse.jdt.internal.core.JavaElement.getElementInfo(JavaElement.java:258)
	at org.eclipse.jdt.internal.core.JavaElement.getElementInfo(JavaElement.java:244)
	at org.eclipse.jdt.internal.core.PackageFragmentRoot.getKind(PackageFragmentRoot.java:481)
	at org.eclipse.jdt.internal.corext.javadoc.JavaDocLocations.getExplanationForMissingJavadoc(JavaDocLocations.java:647)
	at org.eclipse.jdt.internal.ui.text.java.hover.JavadocHover.getHoverInfo(JavadocHover.java:651)
	at org.eclipse.jdt.internal.ui.text.java.hover.JavadocHover.internalGetHoverInfo(JavadocHover.java:567)
	at org.eclipse.jdt.internal.ui.text.java.hover.JavadocHover.getHoverInfo2(JavadocHover.java:559)
	at org.eclipse.jdt.internal.ui.text.java.hover.BestMatchHover.getHoverInfo2(BestMatchHover.java:163)
	at org.eclipse.jdt.internal.ui.text.java.hover.BestMatchHover.getHoverInfo2(BestMatchHover.java:129)
	at org.eclipse.jdt.internal.ui.text.java.hover.JavaEditorTextHoverProxy.getHoverInfo2(JavaEditorTextHoverProxy.java:85)
	at org.eclipse.jface.text.TextViewerHoverManager$4.run(TextViewerHoverManager.java:166)
!SUBENTRY 1 org.eclipse.jdt.core 4 1006 2013-01-07 14:33:46.863
!MESSAGE &lt;project root&gt; [in  ] is not on its project&apos;s build path</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2199569</commentid>
    <comment_count>4</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-01-07 09:14:57 -0500</bug_when>
    <thetext>(In reply to comment #3)
&gt; I also get exceptions when hovering over a field in the compare editor (e.g.
&gt; when comparing org.eclipse.jdt.ui.wizards.NewJavaProjectWizardPageTwo with
&gt; some older version and hover over &apos;fOrginalFolders&apos;:
&gt; 
Test Case:
1. paste this:
public class Bug {
	/**
	 * This works as it has Javadoc.
	 */
	void foo() {
	}
}
2. make a change and save
3. compare with previous version
4. on the right side hover over &apos;Bug&apos;
==&gt; exception and hover talking about the exception</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2199975</commentid>
    <comment_count>5</comment_count>
      <attachid>225325</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-01-08 02:10:50 -0500</bug_when>
    <thetext>Created attachment 225325
Fix

This patch contains the fix for 
1. if no Javadoc is available (e.g. for &apos;sun.awt.im&apos;) we log an error.
2. exceptions when hovering over a field in the compare editor.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2200112</commentid>
    <comment_count>6</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-01-08 07:36:48 -0500</bug_when>
    <thetext>(In reply to comment #5)
&gt; Created attachment 225325 [details] [diff]
&gt; Fix
&gt; 
&gt; This patch contains the fix for 
&gt; 1. if no Javadoc is available (e.g. for &apos;sun.awt.im&apos;) we log an error.

Not really. I still get:

!ENTRY org.eclipse.jdt.core 4 1008 2013-01-08 13:35:07.565
!MESSAGE Cannot retrieve the attached javadoc for sun.awt.im [in C:\JavaSDKs\jdk7-fcs-bin-b147\jre\lib\rt.jar]


&gt; 2. exceptions when hovering over a field in the compare editor.
This seems to be gone.


Did not look at the code.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2205926</commentid>
    <comment_count>7</comment_count>
      <attachid>225936</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-01-22 07:59:31 -0500</bug_when>
    <thetext>Created attachment 225936
Proposed Fix.

Since bug 398272 is resolved, the problem with throwing an exception when the Javadoc content is not available is resolved.

The fix for Javadoc hover showing an exception in compare editor is done.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2205979</commentid>
    <comment_count>8</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-01-22 09:47:12 -0500</bug_when>
    <thetext>Thanks for the patch Manju.

Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=9528419f8d69d6adccd9dc68a70e733ca59b54e3</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2206001</commentid>
    <comment_count>9</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-01-22 10:18:24 -0500</bug_when>
    <thetext>.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2209077</commentid>
    <comment_count>10</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-01-29 02:32:49 -0500</bug_when>
    <thetext>*** Bug 399291 has been marked as a duplicate of this bug. ***</thetext>
  </long_desc>
      
          <attachment
              isobsolete="1"
              ispatch="1"
              isprivate="0"
          >
            <attachid>225215</attachid>
            <date>2013-01-04 09:33:00 -0500</date>
            <delta_ts>2013-01-08 02:10:50 -0500</delta_ts>
            <desc>The polished code is attached as patch</desc>
            <filename>eclipse.jdt.ui.397447.20130104.patch</filename>
            <type>text/plain</type>
            <size>2294</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706892-_eOWb-B-uej11t5HRjNNO0uGWxpD3KR1abBjG-GkVAY</token>
<flag name="review"
          id="54857"
          type_id="6"
          status="+"
          setter="daniel_megert@ch.ibm.com"
    />
          </attachment>
          <attachment
              isobsolete="1"
              ispatch="1"
              isprivate="0"
          >
            <attachid>225325</attachid>
            <date>2013-01-08 02:10:00 -0500</date>
            <delta_ts>2013-01-08 07:37:48 -0500</delta_ts>
            <desc>Fix</desc>
            <filename>eclipse.jdt.ui.397447.20130108.patch</filename>
            <type>text/plain</type>
            <size>2067</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706892-6GsBS67V0O3azVODfkpix77WHO1t9rAnyzao5jcZHA0</token>

          </attachment>
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>225936</attachid>
            <date>2013-01-22 07:59:00 -0500</date>
            <delta_ts>2013-01-22 07:59:31 -0500</delta_ts>
            <desc>Proposed Fix.</desc>
            <filename>eclipse.jdt.ui.397447.20130122.patch</filename>
            <type>text/plain</type>
            <size>1332</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706892-tSZP6CNk7uH88ZYvEO-JzlRsGd_6il1Bbj2Nr4wd3CE</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>396823</bug_id>
          
          <creation_ts>2012-12-18 05:59:00 -0500</creation_ts>
          <short_desc>Use JavaModelUtil.isPackageInfo(ICompilationUnit) util where applicable</short_desc>
          <delta_ts>2013-01-31 08:41:49 -0500</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>enhancement</bug_severity>
          <target_milestone>4.3 M6</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Dani Megert">daniel_megert@ch.ibm.com</reporter>
          <assigned_to name="Manju Mathew">manju656@gmail.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706892-6J9yq4uXe6NXV70ewG3S8vtS-mI2u8nDqq6ZcmB7YHY</token>

      

      <flag name="review"
          id="55359"
          type_id="1"
          status="+"
          setter="daniel_megert@ch.ibm.com"
    />

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2195637</commentid>
    <comment_count>0</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2012-12-18 05:59:39 -0500</bug_when>
    <thetext>Use JavaModelUtil.isPackageInfo(ICompilationUnit) util where applicable.


This should only be done when the Package hover work is in &apos;master&apos;.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2209720</commentid>
    <comment_count>1</comment_count>
      <attachid>226303</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-01-30 05:00:45 -0500</bug_when>
    <thetext>Created attachment 226303
Proposed Fix.

JavadocView is modified to use the util method.

Did not make changes in ImportReferencesCollector as the code after refactoring looked complicated than before the change.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2210439</commentid>
    <comment_count>2</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-01-31 08:41:31 -0500</bug_when>
    <thetext>Thanks for the patch.

We could consider to change #isPackageInfo(ICompilationUnit) to #isPackageInfo(ITypeRoot) and then change the implementation that it works for IClassFile too, but that seems overkill at this point.

Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=52ff99eb9b2828612fe521d9d8c881b170bf8b02</thetext>
  </long_desc>
      
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>226303</attachid>
            <date>2013-01-30 05:00:00 -0500</date>
            <delta_ts>2013-01-31 08:41:49 -0500</delta_ts>
            <desc>Proposed Fix.</desc>
            <filename>eclipse.jdt.ui.20130130.patch</filename>
            <type>text/plain</type>
            <size>868</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706892-_pLYEwgJrCyX6zwAyS-ezxD6aECKHDFihukL3Gpnths</token>
<flag name="review"
          id="55363"
          type_id="6"
          status="+"
          setter="daniel_megert@ch.ibm.com"
    />
          </attachment>
      

    </bug>
    <bug>
          <bug_id>396809</bug_id>
          
          <creation_ts>2012-12-18 03:48:00 -0500</creation_ts>
          <short_desc>[hovering] Write JUnits for the package hovering feature</short_desc>
          <delta_ts>2013-02-05 08:33:35 -0500</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>PC</rep_platform>
          <op_sys>Windows 7</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P2</priority>
          <bug_severity>normal</bug_severity>
          <target_milestone>4.3 M6</target_milestone>
          <dependson>397447</dependson>
    
    <dependson>397464</dependson>
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Manju Mathew">manju656@gmail.com</reporter>
          <assigned_to name="Manju Mathew">manju656@gmail.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706892-J3SaysbFX6uffvXjT9Ff8dKTALTaaPirdkf-P3QMgzY</token>

      

      <flag name="review"
          id="55041"
          type_id="1"
          status="+"
          setter="daniel_megert@ch.ibm.com"
    />

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2195574</commentid>
    <comment_count>0</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2012-12-18 03:48:07 -0500</bug_when>
    <thetext>Write JUnit testcases for the package hovering feature.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2199022</commentid>
    <comment_count>1</comment_count>
      <attachid>225223</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-01-04 11:41:51 -0500</bug_when>
    <thetext>Created attachment 225223
JUnits Attached</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2199024</commentid>
    <comment_count>2</comment_count>
      <attachid>225224</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-01-04 11:45:42 -0500</bug_when>
    <thetext>Created attachment 225224
Test data binaries attached

The test data has to be unzipped and the containing 3 zip files are to be placed in org.eclipse.jdt.ui.tests\testresources folder before executing the testcases.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2205431</commentid>
    <comment_count>3</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-01-21 08:29:06 -0500</bug_when>
    <thetext>Thanks for the patch Manju. Some comments after review:

- the tests are hard to read because most of their source are creating
  the test expected result. Please also add the expected result (file) as test
  resource.

- the copyright is missing

- we must not use &apos;com.ibm&apos; or &apos;ibm&apos; in the test resources (use 
  &apos;org.eclipse.jdt.ui.tests&apos;)

- test resource also need a proper copyright

- use readable names: &quot;133534&quot; is meaningless, especially since it is not
  used in a test name (e.g. testForBug133534 or mentioned in Javadoc)

- use plural for the test suite name ==&gt; PackageJavadocTests

- I would put all test resource (in and out) into a new sub-folder:
  /org.eclipse.jdt.ui.tests/testresources/PackageJavadocTests

- test packages are usually marked as internal in the manifest since they
  are not considered API. The Quick Fix does not do this for us because
  the package name does not have &quot;.internal.&quot; in it</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2206377</commentid>
    <comment_count>4</comment_count>
      <attachid>225968</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-01-23 03:53:50 -0500</bug_when>
    <thetext>Created attachment 225968
Proposed Fix.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2206382</commentid>
    <comment_count>5</comment_count>
      <attachid>225970</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-01-23 04:06:04 -0500</bug_when>
    <thetext>Created attachment 225970
Test data Attached.

- the tests are hard to read because most of their source are creating
  the test expected result. Please also add the expected result (file) as test
  resource.
  
  Since we are comparing the resolved content of the Javadoc, we cannot put the expected result in a text file as the resolved path varies from machine to machine. Hence i have extracted methods from the common content of the expected result. Now the tests are almost readable.

- Added copyrights to all the Java resources, including the test resources.

- renamed the test resources to &apos;org.eclipse.jdt.ui.tests&apos;

- renamed test method to testForBug397455_NPEOnReferenceLinks and added Javadoc

- Renamed the testsuite to PackageJavadocTests

- testcases have been modified to read the testdata from 
  /org.eclipse.jdt.ui.tests/testresources/PackageJavadocTests

- marked the package &apos;org.eclipse.jdt.ui.tests.packageHover&apos; as internal in the manifest file.

The test &apos;testForBug397455_NPEOnReferenceLinks&apos; will fail as the bug 397455 is waiting to be reviewed.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2208709</commentid>
    <comment_count>6</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-01-28 11:49:58 -0500</bug_when>
    <thetext>(In reply to comment #5)
&gt; Created attachment 225970 [details]
&gt; Test data Attached.
&gt; 
&gt; - the tests are hard to read because most of their source are creating
&gt;   the test expected result. Please also add the expected result (file) as
&gt; test
&gt;   resource.
&gt;   
&gt;   Since we are comparing the resolved content of the Javadoc, we cannot put
&gt; the expected result in a text file as the resolved path varies from machine
&gt; to machine. Hence i have extracted methods from the common content of the
&gt; expected result. Now the tests are almost readable.

We should only test that the feature itself works i.e. only check that some basic text is served from the APIs. Otherwise we will always get failures due to small difference, e.g. all your tests fail on my machine because I use different fonts.


&gt; - Added copyrights to all the Java resources, including the test resources.
&gt; 
&gt; - renamed the test resources to &apos;org.eclipse.jdt.ui.tests&apos;

No, you did not. Please check the patch again.


&gt; - testcases have been modified to read the testdata from 
&gt;   /org.eclipse.jdt.ui.tests/testresources/PackageJavadocTests

Good, but please put the full directory structure into the test data ZIP, so that one can simply extract it to the root of the test bundle.


&gt; The test &apos;testForBug397455_NPEOnReferenceLinks&apos; will fail as the bug 397455
&gt; is waiting to be reviewed.

This one still fails, even if I adjust the font on my machine.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2208716</commentid>
    <comment_count>7</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-01-28 11:54:58 -0500</bug_when>
    <thetext>&gt; - use readable names: &quot;133534&quot; is meaningless, especially since it is not
&gt;   used in a test name (e.g. testForBug133534 or mentioned in Javadoc)

This is also not fixed. Please use a more meaningful name.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2209635</commentid>
    <comment_count>8</comment_count>
      <attachid>226293</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-01-30 00:11:55 -0500</bug_when>
    <thetext>Created attachment 226293
Test data binaries attached</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2209637</commentid>
    <comment_count>9</comment_count>
      <attachid>226294</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-01-30 00:20:43 -0500</bug_when>
    <thetext>Created attachment 226294
Updated Patch

Thanks for the review comments Dani. Please find the updated patch with the following updates.

- Testcases now checks the presence of part of the expected Javadoc rather than the complete Javadoc content.
- Removed all references to &quot;ibm&quot; in the test resources. Cross checked by searching all 3 zip contents.
- Testdata is now put in testresources folder, so that it can be directly unzipped in to &quot;org.eclipse.jdt.ui.tests&quot; bundle.
- renamed &apos;testForBug397455_NPEOnReferenceLinks&apos; to &apos;testPackageInfoWithReferenceLinks()&apos;
- added a testcase to check error message when there is no package Javadoc.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2211738</commentid>
    <comment_count>10</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-02-04 09:04:18 -0500</bug_when>
    <thetext>&gt;- use readable names: &quot;133534&quot; is meaningless, especially since it is not
&gt;  used in a test name (e.g. testForBug133534 or mentioned in Javadoc)

This was still not fixed. I&apos;ve now fixed it myself to avoid another ping pong. Also note that we do not use the @author tag. I&apos;ve remove that from the class comment and added the missing @since tag.

Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=d79155d1054134764d5883aa594c7cd7c1884ef1</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2211761</commentid>
    <comment_count>11</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-02-04 09:31:51 -0500</bug_when>
    <thetext>Thanks Dani. 

The review comment 
&quot;&gt;- use readable names: &quot;133534&quot; is meaningless, especially since it is not
&gt;  used in a test name (e.g. testForBug133534 or mentioned in Javadoc)&quot;

was totally misinterpreted. I was assuming it in the context of one of the testcase name which initially was test133534, So in my patches i modified the name of the testcase and also added some Javadoc to it. It did not cross my mind that the review comment was concerning the test data itself.

Will be more careful with the review comments in future.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2212271</commentid>
    <comment_count>12</comment_count>
      <attachid>226563</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-02-05 08:25:26 -0500</bug_when>
    <thetext>Created attachment 226563
Fix for the failing test case in the nightly build.

The test case &quot;testGetPackageAttacheddoc&quot; require net connection to download the attached Javadoc, since the machine where the nightly build runs was not equipped with net connection, this test case failed. The test case is now modified to check if the net connection is available and proceed accordingly.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2212276</commentid>
    <comment_count>13</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-02-05 08:33:35 -0500</bug_when>
    <thetext>(In reply to comment #12)
&gt; Created attachment 226563 [details] [diff]
&gt; Fix for the failing test case in the nightly build.
&gt; 
&gt; The test case &quot;testGetPackageAttacheddoc&quot; require net connection to download
&gt; the attached Javadoc, since the machine where the nightly build runs was not
&gt; equipped with net connection, this test case failed. The test case is now
&gt; modified to check if the net connection is available and proceed accordingly.

Committed patch to master with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=f747cca80cf934d4f9777294b175eebb3d262fc4</thetext>
  </long_desc>
      
          <attachment
              isobsolete="1"
              ispatch="1"
              isprivate="0"
          >
            <attachid>225223</attachid>
            <date>2013-01-04 11:41:00 -0500</date>
            <delta_ts>2013-01-23 03:53:50 -0500</delta_ts>
            <desc>JUnits Attached</desc>
            <filename>eclipse.jdt.ui.396809.20130104.patch</filename>
            <type>text/plain</type>
            <size>46092</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706892-wSB6cOTUSdY_F7FgHIVWfPWA3eLk7dftYQqk3sTRVBE</token>

          </attachment>
          <attachment
              isobsolete="1"
              ispatch="0"
              isprivate="0"
          >
            <attachid>225224</attachid>
            <date>2013-01-04 11:45:00 -0500</date>
            <delta_ts>2013-01-23 03:53:50 -0500</delta_ts>
            <desc>Test data binaries attached</desc>
            <filename>396809_testdata.zip</filename>
            <type>application/octet-stream</type>
            <size>6088</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706892-vaicWdiL-Wb2_QUc9oqrMPavuFK5qQYm-tIVM0s6U70</token>

          </attachment>
          <attachment
              isobsolete="1"
              ispatch="1"
              isprivate="0"
          >
            <attachid>225968</attachid>
            <date>2013-01-23 03:53:00 -0500</date>
            <delta_ts>2013-01-28 11:50:26 -0500</delta_ts>
            <desc>Proposed Fix.</desc>
            <filename>eclipse.jdt.ui.396809.20130123.patch</filename>
            <type>text/plain</type>
            <size>27765</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706892-NiQ_AeBrjlFID_muY4PgirNDQiTPiwvuLOgUbSjAl94</token>
<flag name="review"
          id="55309"
          type_id="6"
          status="-"
          setter="daniel_megert@ch.ibm.com"
    />
          </attachment>
          <attachment
              isobsolete="1"
              ispatch="0"
              isprivate="0"
          >
            <attachid>225970</attachid>
            <date>2013-01-23 04:06:00 -0500</date>
            <delta_ts>2013-01-28 11:50:32 -0500</delta_ts>
            <desc>Test data Attached.</desc>
            <filename>396809_testdata.zip</filename>
            <type>application/octet-stream</type>
            <size>7325</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706892-JNAB0syOLBq-9B9Ak_1YvBvS50QGpxpLwwncXWaD804</token>
<flag name="review"
          id="55310"
          type_id="6"
          status="-"
          setter="daniel_megert@ch.ibm.com"
    />
          </attachment>
          <attachment
              isobsolete="0"
              ispatch="0"
              isprivate="0"
          >
            <attachid>226293</attachid>
            <date>2013-01-30 00:11:00 -0500</date>
            <delta_ts>2013-01-30 00:11:55 -0500</delta_ts>
            <desc>Test data binaries attached</desc>
            <filename>testresources.zip</filename>
            <type>application/octet-stream</type>
            <size>9339</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706892-NvVBIiR8aCOBjgGFom7nX9Hep_YgLXEG7TG8YWXxNcE</token>

          </attachment>
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>226294</attachid>
            <date>2013-01-30 00:20:00 -0500</date>
            <delta_ts>2013-01-30 00:20:43 -0500</delta_ts>
            <desc>Updated Patch</desc>
            <filename>eclipse.jdt.ui.396809.20130130.patch</filename>
            <type>text/plain</type>
            <size>18606</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706892-invfOrAwhziQwATjZ0vX-LIYuBbsv9nB4Jn9URQ5tjM</token>

          </attachment>
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>226563</attachid>
            <date>2013-02-05 08:25:00 -0500</date>
            <delta_ts>2013-02-05 08:25:26 -0500</delta_ts>
            <desc>Fix for the failing test case in the nightly build.</desc>
            <filename>eclipse.jdt.ui.396809.20130105.patch</filename>
            <type>text/plain</type>
            <size>2224</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706892-LQ1cVFNFCx5FAvRI2JTBhvvhj-R0KQtcNsvb8ApLGPA</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>396808</bug_id>
          
          <creation_ts>2012-12-18 03:38:00 -0500</creation_ts>
          <short_desc>[hovering] Package hovering shows multiple hyperlinks if the package is present in multiple location in the build path.</short_desc>
          <delta_ts>2013-01-22 10:17:13 -0500</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P2</priority>
          <bug_severity>normal</bug_severity>
          <target_milestone>4.3 M5</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Manju Mathew">manju656@gmail.com</reporter>
          <assigned_to name="Manju Mathew">manju656@gmail.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706892-FOZeo4atRKBvqgJj75jswWQG0B8B7uSA2D6rrO8bteU</token>

      

      <flag name="review"
          id="55202"
          type_id="1"
          status="+"
          setter="daniel_megert@ch.ibm.com"
    />

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2195573</commentid>
    <comment_count>0</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2012-12-18 03:38:27 -0500</bug_when>
    <thetext>Hover over the package import java.lang.*; code present in a java file. Make sure the package is present in multiple jars and the jars are included in the classpath of the current project. While hovering multiple links of &quot;java.lang&quot; are displayed in the hover window and all of them point to the same Javadoc content.

Duplicate link should not be displayed in the hover window if the Javadoc contents are the same.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2204590</commentid>
    <comment_count>1</comment_count>
      <attachid>225801</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-01-17 23:38:49 -0500</bug_when>
    <thetext>Created attachment 225801
Proposed Fix

Initially proposed solution for removing duplicate links with identical Javadoc could not be implemented as we ran into problems when the Javadoc contained external links to be resolved. Though the content of the Javadoc was same, after resolving the links the relative path of the package Javadoc was different for each of the link.

The next best solution proposed was to show the multiple links along with the package fragment root from where the package is accessed. This way the user can decide which package Javadoc to view from a specific package fragment root.

java.lang - vm.jar
java.lang - jlm.jar
java.lang - resources.jar
java.lang - rt.jar

The current proposed patch is not complete as we are showing the complete path of the package fragment root and not just the name of the package fragment root.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2205408</commentid>
    <comment_count>2</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-01-21 07:02:32 -0500</bug_when>
    <thetext>(In reply to comment #1)
&gt; Created attachment 225801 [details] [diff]
&gt; Proposed Fix
&gt; 
&gt; Initially proposed solution for removing duplicate links with identical
&gt; Javadoc could not be implemented as we ran into problems when the Javadoc
&gt; contained external links to be resolved. Though the content of the Javadoc
&gt; was same, after resolving the links the relative path of the package Javadoc
&gt; was different for each of the link.
&gt; 
&gt; The next best solution proposed was to show the multiple links along with
&gt; the package fragment root from where the package is accessed. This way the
&gt; user can decide which package Javadoc to view from a specific package
&gt; fragment root.
&gt; 
&gt; java.lang - vm.jar
&gt; java.lang - jlm.jar
&gt; java.lang - resources.jar
&gt; java.lang - rt.jar
&gt; 
&gt; The current proposed patch is not complete as we are showing the complete
&gt; path of the package fragment root and not just the name of the package
&gt; fragment root.

As discussed this would be an acceptable approach. However, I thought about this a little longer and also discussed it quickly with Markus: except for the links, the doc is really the same (in the case of the IBM JRE they share the source and Javadoc attachment) and the user should not have to pick it manually. She won&apos;t be interested in the links in 99% of the cases.

So, if all the elements are package fragments with the same name, just iterate over them and take the first one which provides Javadoc and show it.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2205419</commentid>
    <comment_count>3</comment_count>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-01-21 07:46:12 -0500</bug_when>
    <thetext>Agreed that the Javadoc would be same in the case of java.lang and similar packages.

There could be a scenario where there are two Java projects with identical package name. Classes from these two packages are used within a third project. When user hover over the package name, then we get two package fragments. In this case the package Javadoc would be different for each of these packages and hence we need to show the two separate links for each of the packages. Isn&apos;t this a valid scenario to show multiple links?</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2205426</commentid>
    <comment_count>4</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-01-21 08:05:25 -0500</bug_when>
    <thetext>(In reply to comment #3)
&gt; Agreed that the Javadoc would be same in the case of java.lang and similar
&gt; packages.
&gt; 
&gt; There could be a scenario where there are two Java projects with identical
&gt; package name. Classes from these two packages are used within a third
&gt; project. When user hover over the package name, then we get two package
&gt; fragments. In this case the package Javadoc would be different for each of
&gt; these packages and hence we need to show the two separate links for each of
&gt; the packages. Isn&apos;t this a valid scenario to show multiple links?

No, because package names are not random. &quot;a.b&quot; should mean the same everywhere and hence also have the same Javadoc. If it doesn&apos;t then it&apos;s a bug of the provider and we don&apos;t have to support this broken setup.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2205468</commentid>
    <comment_count>5</comment_count>
      <attachid>225887</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-01-21 09:38:39 -0500</bug_when>
    <thetext>Created attachment 225887
Proposed Fix.

The fix returns the first package fragment with a valid Javadoc.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2205492</commentid>
    <comment_count>6</comment_count>
      <attachid>225887</attachid>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-01-21 10:20:49 -0500</bug_when>
    <thetext>Comment on attachment 225887
Proposed Fix.

The patch has several issues:
- I have no clue why you use a map or even a collection  ;-)
- if none of the packages has Javadoc it will show a link for each again
- exception handling is wrong: if one package fails we should try the next one
  and only if all fail with an exception, report it.
- the exception is not shown to the user but only logged and then all links are
  shown again in the hover. It should be handled like the other cases.
- &quot;getPackageFragmentWithValidJavadoc&quot; is a wrong name since this method can also
  return other kinds of elements. Maybe &quot;filterDuplicatePackages&quot;?
- &quot;if ( elements.length &gt; 1)&quot; has a superfluous space</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2205769</commentid>
    <comment_count>7</comment_count>
      <attachid>225922</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-01-22 00:33:40 -0500</bug_when>
    <thetext>Created attachment 225922
Proposed Fix.

In this fix,
1. reused the parameter array to return the package after removing duplicates.
2. iterate over the complete array to find a package with valid Javadoc, exception handling is modified.
3. If no package exists with a valid Javadoc, then returns the first package in the array. This way the user is informed about missing Javadoc using the existing framework.
4. renamed the method to filterDuplicatePackages.
5. removed the superfluous space.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2205837</commentid>
    <comment_count>8</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-01-22 04:53:41 -0500</bug_when>
    <thetext>(In reply to comment #7)
&gt; Created attachment 225922 [details] [diff]
&gt; Proposed Fix.
&gt; 
&gt; In this fix,
&gt; 1. reused the parameter array to return the package after removing
&gt; duplicates.
&gt; 2. iterate over the complete array to find a package with valid Javadoc,
&gt; exception handling is modified.
&gt; 3. If no package exists with a valid Javadoc, then returns the first package
&gt; in the array. This way the user is informed about missing Javadoc using the
&gt; existing framework.
&gt; 4. renamed the method to filterDuplicatePackages.
&gt; 5. removed the superfluous space.

Thanks Manju, the patch works and is almost perfect ;-)

Remaining issues:
- we don&apos;t need to log the exception (ignore it as it might
  even be logged again later when trying to get the Javadoc
- use early exit in your code, e.g. return after those checks:
  - elements[0] instanceof IPackageFragment
  - content == null
  this makes the code easier to ready and less indented
- the Javadoc can get a bit more love, e.g.
  @param elements whose Javadoc has to be found
  does not really apply. I&apos;d rather write:
  @param elements array from which to filter duplicate packages</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2205877</commentid>
    <comment_count>9</comment_count>
      <attachid>225932</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-01-22 05:50:18 -0500</bug_when>
    <thetext>Created attachment 225932
Proposed Fix.

In this fix

- exception thrown while filtering the packages is ignored.
- use early exit in your code, e.g. return after those checks:
  - elements[0] instanceof IPackageFragment - Done
  - content == null =&gt; here we do not exit, we need to continue and consider other     packages to retrieve a valid Javadoc
- updated the Javadoc for @param elements</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2205888</commentid>
    <comment_count>10</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-01-22 06:12:41 -0500</bug_when>
    <thetext>(In reply to comment #9)
&gt; Created attachment 225932 [details] [diff]
&gt; Proposed Fix.
&gt; 
&gt; In this fix
&gt; 
&gt; - exception thrown while filtering the packages is ignored.
&gt;   - content == null =&gt; here we do not exit, we need to continue and consider
&gt; other     packages to retrieve a valid Javadoc

Yes, but what if content != null? ;-)</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2205921</commentid>
    <comment_count>11</comment_count>
      <attachid>225935</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-01-22 07:48:53 -0500</bug_when>
    <thetext>Created attachment 225935
Proposed Fix.

Result is returned when content != null.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2205977</commentid>
    <comment_count>12</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-01-22 09:40:46 -0500</bug_when>
    <thetext>(In reply to comment #11)
&gt; Created attachment 225935 [details] [diff]
&gt; Proposed Fix.
&gt; 
&gt; Result is returned when content != null.

Thanks Manju, this patch is good.

Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=b07362bebd05c4fa6e7038aae57472cef42ba346

Note that it&apos;s hard to test because one runs into NPEs depending on what pacakge is used (see bug 397455).</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2205999</commentid>
    <comment_count>13</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-01-22 10:17:13 -0500</bug_when>
    <thetext>Markus reminded me that the filter method has a problem when there&apos;s only a package.html file in a package since that&apos;s not part of the children. Hence I removed the performance optimization that checks for children.</thetext>
  </long_desc>
      
          <attachment
              isobsolete="1"
              ispatch="1"
              isprivate="0"
          >
            <attachid>225801</attachid>
            <date>2013-01-17 23:38:00 -0500</date>
            <delta_ts>2013-01-21 07:03:06 -0500</delta_ts>
            <desc>Proposed Fix</desc>
            <filename>eclipse.jdt.ui.20130117.patch</filename>
            <type>text/plain</type>
            <size>1926</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706892-16RU8FaiLaVqhaob9xbFfVEIoL97iCMaMxgaZ799yPE</token>

          </attachment>
          <attachment
              isobsolete="1"
              ispatch="1"
              isprivate="0"
          >
            <attachid>225887</attachid>
            <date>2013-01-21 09:38:00 -0500</date>
            <delta_ts>2013-01-21 10:20:49 -0500</delta_ts>
            <desc>Proposed Fix.</desc>
            <filename>eclipse.jdt.ui.20130121.patch</filename>
            <type>text/plain</type>
            <size>3013</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706892-VBfYI3_RQilQtYHhoDOLeVPkNcYVdgTyg0OmFMb-yXk</token>
<flag name="review"
          id="55190"
          type_id="6"
          status="-"
          setter="daniel_megert@ch.ibm.com"
    />
          </attachment>
          <attachment
              isobsolete="1"
              ispatch="1"
              isprivate="0"
          >
            <attachid>225922</attachid>
            <date>2013-01-22 00:33:00 -0500</date>
            <delta_ts>2013-01-22 04:53:55 -0500</delta_ts>
            <desc>Proposed Fix.</desc>
            <filename>eclipse.jdt.ui.20130122.patch</filename>
            <type>text/plain</type>
            <size>4764</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706892-RkaiO0LgHxv9hv-LhO02wzTqhHD-ylw5lsWz35VloKI</token>

          </attachment>
          <attachment
              isobsolete="1"
              ispatch="1"
              isprivate="0"
          >
            <attachid>225932</attachid>
            <date>2013-01-22 05:50:00 -0500</date>
            <delta_ts>2013-01-22 06:14:42 -0500</delta_ts>
            <desc>Proposed Fix.</desc>
            <filename>eclipse.jdt.ui.20130122.patch</filename>
            <type>text/plain</type>
            <size>4779</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706892-D4XOCZYcm0OZZBWA9MwWPBLIZ8WnChVaJdhahAutwhg</token>
<flag name="review"
          id="55201"
          type_id="6"
          status="-"
          setter="daniel_megert@ch.ibm.com"
    />
          </attachment>
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>225935</attachid>
            <date>2013-01-22 07:48:00 -0500</date>
            <delta_ts>2013-01-22 09:40:57 -0500</delta_ts>
            <desc>Proposed Fix.</desc>
            <filename>eclipse.jdt.ui.20130122.patch</filename>
            <type>text/plain</type>
            <size>4763</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706892-Lhoi7rzBx4UYI0Hyfnz7mrMWTvRbfw2JMVggKIkUXQs</token>
<flag name="review"
          id="55204"
          type_id="6"
          status="+"
          setter="daniel_megert@ch.ibm.com"
    />
          </attachment>
      

    </bug>
    <bug>
          <bug_id>396087</bug_id>
          
          <creation_ts>2012-12-07 19:52:00 -0500</creation_ts>
          <short_desc>Merge in CBI patches from 4.2.2 into 4.3 (pom changes) for eclipse.jdt.ui</short_desc>
          <delta_ts>2012-12-10 09:38:05 -0500</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>PC</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>normal</bug_severity>
          <target_milestone>4.3 M4</target_milestone>
          
          <blocked>396082</blocked>
          <everconfirmed>1</everconfirmed>
          <reporter name="Thanh Ha">thanh.ha@alumni.carleton.ca</reporter>
          <assigned_to name="Dani Megert">daniel_megert@ch.ibm.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706892-7hpukT9b-4BndMO7JF-TB0V2a3ZVKyJZ5i3wGWS7Jus</token>

      

      

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2192057</commentid>
    <comment_count>0</comment_count>
      <attachid>224457</attachid>
    <who name="Thanh Ha">thanh.ha@alumni.carleton.ca</who>
    <bug_when>2012-12-07 19:52:05 -0500</bug_when>
    <thetext>Created attachment 224457
jdt.ui.poms.patch

Attached patch merges in all the CBI pom related changes from 4.2.2 into the master branch.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2192439</commentid>
    <comment_count>1</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2012-12-10 08:53:35 -0500</bug_when>
    <thetext>Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=5f7bb57b8210eb2cc852a72b647615ef084808bc

BTW: shouldn&apos;t the version in a/pom.xml be 3.9.0?</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2192472</commentid>
    <comment_count>2</comment_count>
    <who name="Thanh Ha">thanh.ha@alumni.carleton.ca</who>
    <bug_when>2012-12-10 09:38:05 -0500</bug_when>
    <thetext>(In reply to comment #1)
&gt; Fixed with
&gt; http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/
&gt; ?id=5f7bb57b8210eb2cc852a72b647615ef084808bc
&gt; 
&gt; BTW: shouldn&apos;t the version in a/pom.xml be 3.9.0?

The repo&apos;s parent pom version isn&apos;t really used anywhere other than for maven. So the build will still produce correctly regardless of this. However for consistency with the repo it is possible to change this to 3.9.0 but this would involve also modifying every pom under this pom to say that it&apos;s parent is now version 3.9.0.</thetext>
  </long_desc>
      
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>224457</attachid>
            <date>2012-12-07 19:52:00 -0500</date>
            <delta_ts>2012-12-07 19:52:05 -0500</delta_ts>
            <desc>jdt.ui.poms.patch</desc>
            <filename>jdt.ui.poms.patch</filename>
            <type>text/plain</type>
            <size>3788</size>
            <attacher name="Thanh Ha">thanh.ha@alumni.carleton.ca</attacher>
            
              <token>1425706892-rqUAI2ZhK46sQet7E1ri0eTxRq8uzJOhXDbNRx7WoWE</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>396083</bug_id>
          
          <creation_ts>2012-12-07 19:36:00 -0500</creation_ts>
          <short_desc>Merge in CBI patches from 4.2.2 into 4.3 (pom changes) for eclipse.jdt</short_desc>
          <delta_ts>2012-12-10 10:15:56 -0500</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>PC</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>normal</bug_severity>
          <target_milestone>4.3 M4</target_milestone>
          
          <blocked>396082</blocked>
          <everconfirmed>1</everconfirmed>
          <reporter name="Thanh Ha">thanh.ha@alumni.carleton.ca</reporter>
          <assigned_to name="Dani Megert">daniel_megert@ch.ibm.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706892-ZopIFp6AYPHHnYfRElEGuFazmNZLvUkl-NEW4elJIr8</token>

      

      

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2192051</commentid>
    <comment_count>0</comment_count>
      <attachid>224453</attachid>
    <who name="Thanh Ha">thanh.ha@alumni.carleton.ca</who>
    <bug_when>2012-12-07 19:36:18 -0500</bug_when>
    <thetext>Created attachment 224453
eclipse.jdt.patch

Attached is a patch that will update the eclipse.jdt.git master branch with all the pom changes missing from 4.2.2.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2192418</commentid>
    <comment_count>1</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2012-12-10 08:30:35 -0500</bug_when>
    <thetext>The patch did not apply via UI.

Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.git/commit/?id=7382d2f21077611d04020b2270b4e5b254ac523a</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2192510</commentid>
    <comment_count>2</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2012-12-10 10:15:56 -0500</bug_when>
    <thetext>(In reply to comment #1)
&gt; The patch did not apply via UI.

This was due to bug 396190.

 
&gt; Fixed with
&gt; http://git.eclipse.org/c/jdt/eclipse.jdt.git/commit/
&gt; ?id=7382d2f21077611d04020b2270b4e5b254ac523a

Sorry, I forgot to set the author. Setting iplog+ instead.</thetext>
  </long_desc>
      
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>224453</attachid>
            <date>2012-12-07 19:36:00 -0500</date>
            <delta_ts>2012-12-07 19:36:18 -0500</delta_ts>
            <desc>eclipse.jdt.patch</desc>
            <filename>eclipse.jdt.patch</filename>
            <type>text/plain</type>
            <size>2205</size>
            <attacher name="Thanh Ha">thanh.ha@alumni.carleton.ca</attacher>
            
              <token>1425706892-G-VaPEDDGr9sGS5F0GWW6ezFedrI92tovB_-0SH9DIs</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>395962</bug_id>
          
          <creation_ts>2012-12-06 12:26:00 -0500</creation_ts>
          <short_desc>[templates] JUnit templates rework</short_desc>
          <delta_ts>2013-04-29 12:34:18 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>enhancement</bug_severity>
          <target_milestone>4.3 M7</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Lars Vogel">lars.vogel@vogella.com</reporter>
          <assigned_to name="Dani Megert">daniel_megert@ch.ibm.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>lars.vogel@vogella.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
          
          <votes>1</votes>

      
          <token>1425706892-wjhmwlhEMW8YwSJGHkyvvnJPZFTf9vrMXqv5_kGGMso</token>

      

      <flag name="review"
          id="56916"
          type_id="1"
          status="+"
          setter="markus_keller@ch.ibm.com"
    />

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2191487</commentid>
    <comment_count>0</comment_count>
    <who name="Lars Vogel">lars.vogel@vogella.com</who>
    <bug_when>2012-12-06 12:26:19 -0500</bug_when>
    <thetext>I recently seen a lot of tips how to create &quot;correct&quot; JUnit test templates [links].

As I want to rework the SWT templates, shall I also create improved JUnit test templates?

I would also suggest to delete the JUnit 3 templates or at least put it into second position.

[links]
http://eclipsesource.com/blogs/2012/03/20/simple-junit4-templates-for-eclipse/
http://www.codeaffine.com/2012/11/26/working-efficiently-with-junit-in-eclipse-2/</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2193542</commentid>
    <comment_count>1</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2012-12-12 08:16:25 -0500</bug_when>
    <thetext>(In reply to comment #0)
&gt; As I want to rework the SWT templates, shall I also create improved JUnit
&gt; test templates?

Sure, why not.
 
&gt; I would also suggest to delete the JUnit 3 templates or at least put it into
&gt; second position.

I&apos;m OK to switch the position. Markus, any objection?</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2194053</commentid>
    <comment_count>2</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2012-12-13 06:34:00 -0500</bug_when>
    <thetext>&gt; &gt; I would also suggest to delete the JUnit 3 templates or at least put it into
&gt; &gt; second position.

-1 for deleting, since there are lots of existing JUnit 3 test cases that are still actively maintained.

Switching the position if JUnit 4 is available would be fine with me, but I&apos;m not sure if that&apos;s technically possible. Note that the JUnit 4 template is already on top if you write &quot;Test&quot; with a capital &quot;T&quot;.

But maybe we should rename the templates to &quot;test method (JUnit 3)&quot; and
&quot;@Test method&quot;?</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2226478</commentid>
    <comment_count>3</comment_count>
      <attachid>227969</attachid>
    <who name="Lars Vogel">lars.vogel@vogella.com</who>
    <bug_when>2013-03-05 16:58:59 -0500</bug_when>
    <thetext>Created attachment 227969
Patch for the test templates

Attached the patch for the test templates. I remove throw exception as this is not the typical test case and changed the names so that test is now before test (JUnit 3).

I also added templates for @Before and @After including constants for describing them. 

Let me know if I need to change something.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2226479</commentid>
    <comment_count>4</comment_count>
      <attachid>227970</attachid>
    <who name="Lars Vogel">lars.vogel@vogella.com</who>
    <bug_when>2013-03-05 17:00:19 -0500</bug_when>
    <thetext>Created attachment 227970
Patch with credentials

Same patch but I also added me to the credentials.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2249570</commentid>
    <comment_count>5</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-04-29 02:16:33 -0400</bug_when>
    <thetext>(In reply to comment #3)
&gt; Created attachment 227969 [details] [diff]
&gt; Patch for the test templates
&gt; 
&gt; Attached the patch for the test templates. I remove throw exception as this
&gt; is not the typical test case and changed the names so that test is now
&gt; before test (JUnit 3).
&gt; 
&gt; I also added templates for @Before and @After including constants for
&gt; describing them. 
&gt; 
&gt; Let me know if I need to change something.

I would prefer that the JUnit 4 templates are grouped together. If you use &quot;@test method&quot; as name, like Markus suggested, and &quot;@after method&quot; and &quot;@before method&quot; , then that could be achieved. I would also not mention JUnit 4 in the description, since this is obvious when we use the annotation in the name.

Markus, what&apos;s your final word on this?</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2249580</commentid>
    <comment_count>6</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-04-29 02:57:41 -0400</bug_when>
    <thetext>Internal note: all tests pass with the proposed patch.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2249620</commentid>
    <comment_count>7</comment_count>
    <who name="Lars Vogel">lars.vogel@vogella.com</who>
    <bug_when>2013-04-29 04:30:10 -0400</bug_when>
    <thetext>if I use @ in the beginning @Ctrl+Space does in my setup not trigger a template completion, that is why I have implemented it differently. @Ctrl+Space ends up in my case as &quot;@interface&quot;. 

I can remove the JUnit4 from the test, but I assume it is easier if you do it directly. If that assumption is incorrect, please let me know. I also personally would prefer to rename the JUnit3 template to something like &quot;JUnit3 test&quot; to have &quot;test&quot; for JUnit 4 only but I assume that is a controversial change, it avoid that.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2249630</commentid>
    <comment_count>8</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-04-29 04:52:42 -0400</bug_when>
    <thetext>(In reply to comment #7)
&gt; if I use @ in the beginning @Ctrl+Space does in my setup not trigger a
&gt; template completion, that is why I have implemented it differently.
&gt; @Ctrl+Space ends up in my case as &quot;@interface&quot;. 

Interesting. This looks like a bug in the template content assist processor when inside Java code. Inside Javadoc, @author works fine.


&gt; I also
&gt; personally would prefer to rename the JUnit3 template to something like
&gt; &quot;JUnit3 test&quot; to have &quot;test&quot; for JUnit 4 only but I assume that is a
&gt; controversial change, it avoid that.

-1 for that.


Let&apos;s wait what Markus prefers. I&apos;d rather fix the template processor or defer this fix than using something that&apos;s close but not what we really like in the end and change again later.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2249632</commentid>
    <comment_count>9</comment_count>
    <who name="Lars Vogel">lars.vogel@vogella.com</who>
    <bug_when>2013-04-29 04:57:08 -0400</bug_when>
    <thetext>&gt; Interesting. This looks like a bug in the template content assist processor
&gt; when inside Java code. Inside Javadoc, @author works fine.

Would be great to have that fixed.
 
&gt; &gt; I also
&gt; &gt; personally would prefer to rename the JUnit3 template to something like
&gt; &gt; &quot;JUnit3 test&quot; to have &quot;test&quot; for JUnit 4 only but I assume that is a
&gt; &gt; controversial change, it avoid that.
&gt; 
&gt; -1 for that.

Thought so. :-) 

&gt; Let&apos;s wait what Markus prefers. I&apos;d rather fix the template processor or
&gt; defer this fix than using something that&apos;s close but not what we really like
&gt; in the end and change again later.

IMHO would be great to have an improvement in 4.3 for the test templates. It feels to me that fixing the template processors is currently unrealistic for 4.3, at least definitely from me side.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2249636</commentid>
    <comment_count>10</comment_count>
    <who name="Lars Vogel">lars.vogel@vogella.com</who>
    <bug_when>2013-04-29 05:00:52 -0400</bug_when>
    <thetext>Opened Bug 406770 for the support of @ in the template content assist processor.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2249717</commentid>
    <comment_count>11</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-04-29 07:15:01 -0400</bug_when>
    <thetext>(In reply to comment #5)
&gt; I would prefer that the JUnit 4 templates are grouped together.

Actually, this is the case with your patch. We both should have tested the patch before making our comments: the JUnit 3 test template appears first and the JUnit 4 templates afterwards (grouped together). The reason for this, is that the template proposals are sorted by the complete display string. I filed bug 406784 for that.


Markus and I discussed what&apos;s best here. We decided to change the names as follows:

Test ==&gt; test
test ==&gt; test3

We will not add @After and @Before templates, since the New JUnit Test Case wizard can generate them when desired.


Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=932cf1260a5fe3600fe1dc38685d32c7d862c1d6</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2249718</commentid>
    <comment_count>12</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-04-29 07:15:12 -0400</bug_when>
    <thetext>.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2249719</commentid>
    <comment_count>13</comment_count>
    <who name="Lars Vogel">lars.vogel@vogella.com</who>
    <bug_when>2013-04-29 07:21:56 -0400</bug_when>
    <thetext>Thanks for the change (I refreshed my browser, my assumption is that I now don&apos;t reset any of the flag sets).</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2249844</commentid>
    <comment_count>14</comment_count>
      <attachid>230254</attachid>
    <who name="Lars Vogel">lars.vogel@vogella.com</who>
    <bug_when>2013-04-29 10:06:33 -0400</bug_when>
    <thetext>Created attachment 230254
N&amp;N patch

Suggestion to add this to the M7 N&amp;N.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2249863</commentid>
    <comment_count>15</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-04-29 10:28:31 -0400</bug_when>
    <thetext>&gt; (I refreshed my browser, my assumption is that I now
&gt; don&apos;t reset any of the flag sets).

It&apos;s difficult. Some browsers try to be helpful but cause confusion: On refresh, they reload the page from the server, but then they change all form fields to the value before the refresh. In that scenario, Bugzilla cannot know that the browser tricked you and hence it doesn&apos;t show an in-flight conflict.

Therefore, it&apos;s best to avoid refreshing a form page. Ctrl+L, Enter is a better solution, since it ensures that you get an untampered page from the server. Unfortunately, that doesn&apos;t work if there&apos;s a fragment in the URL (e.g. #c0), since page is not reloaded in that case.

The best solution is to open the bug again via Click or Ctrl+click on the bug number. This is readily available if you use our Greasemonkey script that fixes Bugzilla UI bloopers: http://www.eclipse.org/jdt/ui/dev.php#scripts</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2249966</commentid>
    <comment_count>16</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2013-04-29 12:34:18 -0400</bug_when>
    <thetext>(In reply to comment #14)
&gt; Created attachment 230254 [details] [diff]
&gt; N&amp;N patch
&gt; 
&gt; Suggestion to add this to the M7 N&amp;N.

I&apos;ve added an entry together with a screenshot.</thetext>
  </long_desc>
      
          <attachment
              isobsolete="1"
              ispatch="1"
              isprivate="0"
          >
            <attachid>227969</attachid>
            <date>2013-03-05 16:58:00 -0500</date>
            <delta_ts>2013-03-05 17:00:19 -0500</delta_ts>
            <desc>Patch for the test templates</desc>
            <filename>test_templates.patch</filename>
            <type>text/plain</type>
            <size>2924</size>
            <attacher name="Lars Vogel">lars.vogel@vogella.com</attacher>
            
              <token>1425706892-x7uW0H9jNRUxgM2RNefpAoq-8xhLWzscLtTQYIpWdco</token>

          </attachment>
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>227970</attachid>
            <date>2013-03-05 17:00:00 -0500</date>
            <delta_ts>2013-03-05 17:00:19 -0500</delta_ts>
            <desc>Patch with credentials</desc>
            <filename>test_templates.patch</filename>
            <type>text/plain</type>
            <size>3166</size>
            <attacher name="Lars Vogel">lars.vogel@vogella.com</attacher>
            
              <token>1425706892-CRPE9YJENXhnXdFpZ6j_lESjzbqJQxZ1fBore_982fo</token>

          </attachment>
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>230254</attachid>
            <date>2013-04-29 10:06:00 -0400</date>
            <delta_ts>2013-04-29 10:06:33 -0400</delta_ts>
            <desc>N&amp;N patch</desc>
            <filename>Test-templates.patch</filename>
            <type>text/plain</type>
            <size>699</size>
            <attacher name="Lars Vogel">lars.vogel@vogella.com</attacher>
            
              <token>1425706892-E8ODUjUcvkpcXDWcJAxLApu16fhHB0TSimc7sDVGkpQ</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>395007</bug_id>
          
          <creation_ts>2012-11-24 10:25:00 -0500</creation_ts>
          <short_desc>[package explorer] Refresh action not available on Java package folders</short_desc>
          <delta_ts>2012-12-21 14:44:35 -0500</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>VERIFIED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>normal</bug_severity>
          <target_milestone>4.3 M4</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Ed Willink">ed@willink.me.uk</reporter>
          <assigned_to name="Dani Megert">daniel_megert@ch.ibm.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>stephan.herrmann@berlin.de</cc>
          
          <votes>0</votes>

      
          <token>1425706892-rIF9npo5eD6SC5pU9fINzrKeqDnU3GkCEKUtFaYe8u8</token>

      

      

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2187240</commentid>
    <comment_count>0</comment_count>
    <who name="Ed Willink">ed@willink.me.uk</who>
    <bug_when>2012-11-24 10:25:34 -0500</bug_when>
    <thetext>M3.

F5 (Refresh) is available as a context menu entry for ordinary source folders but not for Java package folders in the e4 Java Package explorer.

Please restore the 3.x functionality.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2187402</commentid>
    <comment_count>1</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2012-11-26 05:17:06 -0500</bug_when>
    <thetext>Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=dcacd5c50334a9bb3dda82008045ee3041a1d8cf</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2192799</commentid>
    <comment_count>2</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2012-12-11 02:38:14 -0500</bug_when>
    <thetext>Verified in I20121210-2000.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2196919</commentid>
    <comment_count>3</comment_count>
    <who name="Ed Willink">ed@willink.me.uk</who>
    <bug_when>2012-12-21 06:46:35 -0500</bug_when>
    <thetext>Problem still exists in M4.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2196987</commentid>
    <comment_count>4</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2012-12-21 09:21:20 -0500</bug_when>
    <thetext>This works for me.

1. download M4:
http://download.eclipse.org/eclipse/downloads/drops4/S-4.3M4-201212140730/
2. start new workspace
3. create Java project &apos;P&apos;
4. paste this into &apos;Package Explorer&apos;:
package p;
class A {
}
5. in the &apos;Package Explorer&apos; open context menu on package &apos;p&apos;
==&gt; Refresh is there and enabled
6. open &apos;File&apos; main menu
==&gt; Refresh is there and enabled

Maybe your update to M4 went wrong or you installed additional stuff which breaks it. Please reopen with reproducible steps if you still see this using
http://download.eclipse.org/eclipse/downloads/drops4/S-4.3M4-201212140730/
or newer.

Also note that package in JARs can&apos;t be refreshed, hence you won&apos;t see it on packages inside JARs.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2196995</commentid>
    <comment_count>5</comment_count>
    <who name="Ed Willink">ed@willink.me.uk</who>
    <bug_when>2012-12-21 09:46:35 -0500</bug_when>
    <thetext>I&apos;m using the M4 you suggest, and with your repro (I never knew you could paste text) there is no Refresh on package P.

It must be something extra.

My first suspicion is jdtannot for @NonNull, which when patching seems to download a lot of JDT plugins. Perhaps this has taken JDT back to Juno. Is jdtannot actually an M4 patch?</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2197034</commentid>
    <comment_count>6</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2012-12-21 11:29:20 -0500</bug_when>
    <thetext>(In reply to comment #5)
&gt; I&apos;m using the M4 you suggest, and with your repro (I never knew you could
&gt; paste text) 

Cool, isn&apos;t it?

 
&gt; It must be something extra.
&gt; 
&gt; My first suspicion is jdtannot for @NonNull, which when patching seems to
&gt; download a lot of JDT plugins. Perhaps this has taken JDT back to Juno. Is
&gt; jdtannot actually an M4 patch?

Maybe you can try my steps first. If we&apos;re on the same page, we can take it further. Maybe Stephan&apos;s patch has an issue and isn&apos;t based on M4.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2197080</commentid>
    <comment_count>7</comment_count>
    <who name="Stephan Herrmann">stephan.herrmann@berlin.de</who>
    <bug_when>2012-12-21 14:21:17 -0500</bug_when>
    <thetext>(In reply to comment #6)
&gt; &gt; My first suspicion is jdtannot for @NonNull, which when patching seems to
&gt; &gt; download a lot of JDT plugins. Perhaps this has taken JDT back to Juno. Is
&gt; &gt; jdtannot actually an M4 patch?
&gt; 
&gt; Maybe you can try my steps first. If we&apos;re on the same page, we can take it
&gt; further. Maybe Stephan&apos;s patch has an issue and isn&apos;t based on M4.

I just double checked:
- install SDK 4.3M4
- install latest from http://www.eclipse.org/jdt/core/beta-null-annotations-for-fields/4.3milestones
  (to get source bundles uncheck &quot;Group items by category&quot;)
- try steps from comment 4
=&gt; OK

Open RefreshAction from ...jdt.ui.source and see that the change referenced in comment 1 is present.

In this configuration you should see plug-in version 3.9.0.201212161923 of org.eclipse.jdt.core, org.eclipse.jdt.annotation &amp; org.eclipse.jdt.ui (plus corresponding source bundles, if installed).</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2197094</commentid>
    <comment_count>8</comment_count>
    <who name="Ed Willink">ed@willink.me.uk</who>
    <bug_when>2012-12-21 14:44:35 -0500</bug_when>
    <thetext>Yes it&apos;s fine now.

However in my problem installation jdt.ui is 3.9.0.201211131918 so it looks as if I installed a jdtannot before M4 was available and so it migrated JDT backwards from M4 to M3.</thetext>
  </long_desc>
      
      

    </bug>
    <bug>
          <bug_id>393932</bug_id>
          
          <creation_ts>2012-11-08 17:14:00 -0500</creation_ts>
          <short_desc>[refactoring] pull-up with &quot;use the destination type where possible&quot; creates bogus import of nested type</short_desc>
          <delta_ts>2012-11-10 06:31:44 -0500</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>PC</rep_platform>
          <op_sys>Linux</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>normal</bug_severity>
          <target_milestone>4.3 M4</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Stephan Herrmann">stephan.herrmann@berlin.de</reporter>
          <assigned_to name="Markus Keller">markus_keller@ch.ibm.com</assigned_to>
          <cc>markus_keller@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706892-stGDAa0l2gOuuzo6p-mAAT8T70gPjVut7UlXjVvgTqk</token>

      

      

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2181547</commentid>
    <comment_count>0</comment_count>
    <who name="Stephan Herrmann">stephan.herrmann@berlin.de</who>
    <bug_when>2012-11-08 17:14:05 -0500</bug_when>
    <thetext>Given this class:

package p;

public class C {
	protected class I1 {
		
	}
	protected class I2 extends I1 {
		protected void foo() {
			
		}
	}
	void test(I2 i) {
		i.foo();
	}
}

When pulling up foo() to I1 and enabling &quot;use the destination type where possible&quot; the change in test(..) creates a bogus import of the inner class I1.

Result is:

package p;

import p.C.I1; // BUG

public class C {
	protected class I1 {

		protected void foo() {
			
		}
		
	}
	protected class I2 extends I1 {
	}
	void test(I1 i) {
		i.foo();
	}
}

The bug seems to originate from the fact that SuperTypeRefactoringProcessor.createCorrespondingNode(CompilationUnitRewrite, TType) calls ImportRewrite.addImportFromSignature(String,AST) with no proper ImportRewriteContext.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2181548</commentid>
    <comment_count>1</comment_count>
      <attachid>223371</attachid>
    <who name="Stephan Herrmann">stephan.herrmann@berlin.de</who>
    <bug_when>2012-11-08 17:16:45 -0500</bug_when>
    <thetext>Created attachment 223371
proposed patch

could it be as simple as this?

The patch fixes the immediate issue, not sure if more needs to be done for a full solution?</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2181832</commentid>
    <comment_count>2</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2012-11-09 09:22:05 -0500</bug_when>
    <thetext>Yes, it&apos;s really as simple as that, thanks for the patch.

Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=686e984f6a987f453770fc1ff7ed856e27238d93</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2182142</commentid>
    <comment_count>3</comment_count>
    <who name="Stephan Herrmann">stephan.herrmann@berlin.de</who>
    <bug_when>2012-11-10 06:31:44 -0500</bug_when>
    <thetext>(In reply to comment #2)
&gt; Fixed with
&gt; http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/
&gt; ?id=686e984f6a987f453770fc1ff7ed856e27238d93

Thanks</thetext>
  </long_desc>
      
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>223371</attachid>
            <date>2012-11-08 17:16:00 -0500</date>
            <delta_ts>2012-11-08 17:16:45 -0500</delta_ts>
            <desc>proposed patch</desc>
            <filename>Bug393932.patch</filename>
            <type>text/plain</type>
            <size>2755</size>
            <attacher name="Stephan Herrmann">stephan.herrmann@berlin.de</attacher>
            
              <token>1425706892-NKM2zIZOnEeDnxbUxkgTj21h_cbLzEea---PkDMbtwI</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>393147</bug_id>
          
          <creation_ts>2012-10-30 09:49:00 -0400</creation_ts>
          <short_desc>Bugs in AdvancedQuickAssistProcessor.getConvertIfElseToSwitchProposals</short_desc>
          <delta_ts>2012-11-09 12:53:58 -0500</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>normal</bug_severity>
          <target_milestone>4.3 M4</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Markus Keller">markus_keller@ch.ibm.com</reporter>
          <assigned_to name="Markus Keller">markus_keller@ch.ibm.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>deepakazad@gmail.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706892-7rCk3bZtNyP7WjM6xLRq3perbLecv_m0ZvZMyDP14-Y</token>

      

      

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2177432</commentid>
    <comment_count>0</comment_count>
      <attachid>222979</attachid>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2012-10-30 09:49:05 -0400</bug_when>
    <thetext>Created attachment 222979
Fix

Follow-up to bug 392847.

AdvancedQuickAssistProcessor.getConvertIfElseToSwitchProposals has more bugs, e.g.
- NPE for:
		if (equals(&quot;a&quot;)) {

- coverts this (left operand neither a String nor a primitive, nor an enum):
		if (this.equals(&quot;a&quot;)) {

The patch fixes these problems but is missing tests.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2177519</commentid>
    <comment_count>1</comment_count>
    <who name="Deepak Azad">deepakazad@gmail.com</who>
    <bug_when>2012-10-30 11:39:02 -0400</bug_when>
    <thetext>Ha! Didn&apos;t think of this case.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2181993</commentid>
    <comment_count>2</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2012-11-09 12:53:58 -0500</bug_when>
    <thetext>Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=f981ac7c0bb812e92f6f26b4de012b65550b5aa5

Also made the inner loop understandable by moving the constant check
&quot;currentIf != null&quot; out of the while expression.</thetext>
  </long_desc>
      
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>222979</attachid>
            <date>2012-10-30 09:49:00 -0400</date>
            <delta_ts>2012-10-30 09:49:05 -0400</delta_ts>
            <desc>Fix</desc>
            <filename>eclipse.jdt.ui.patch</filename>
            <type>text/plain</type>
            <size>9886</size>
            <attacher name="Markus Keller">markus_keller@ch.ibm.com</attacher>
            
              <token>1425706892-j_X6-bly8xRbkrQi44a5E5vG50dp1I_GZoPf_Y4DLSc</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>392946</bug_id>
          
          <creation_ts>2012-10-26 14:50:00 -0400</creation_ts>
          <short_desc>[quick fix] for unused type parameter</short_desc>
          <delta_ts>2013-01-11 08:16:46 -0500</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>enhancement</bug_severity>
          <target_milestone>4.3 M5</target_milestone>
          <dependson>385780</dependson>
    
    <dependson>397888</dependson>
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Markus Keller">markus_keller@ch.ibm.com</reporter>
          <assigned_to name="Manju Mathew">manju656@gmail.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706892-opyDZm5QNXJbLs0zbqsUw7fCsOp0hruf8jOQH_5HHF4</token>

      

      <flag name="review"
          id="54900"
          type_id="1"
          status="+"
          setter="markus_keller@ch.ibm.com"
    />

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2176440</commentid>
    <comment_count>0</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2012-10-26 14:50:56 -0400</bug_when>
    <thetext>Add quick fixes for unused type parameters.

This is similar to unused method parameters, so fixes will also be similar (remove, add documentation).

Don&apos;t add a clean up to remove all, since this would break existing references.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2199557</commentid>
    <comment_count>1</comment_count>
      <attachid>225278</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-01-07 08:57:52 -0500</bug_when>
    <thetext>Created attachment 225278
The proposed fix and the junits attached.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2200151</commentid>
    <comment_count>2</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-01-08 08:47:46 -0500</bug_when>
    <thetext>* RemoveUnusedTypeParameterOperation:
- This class is only ever used with a single SimpleName. The constructor should not take an array.

* RemoveUnusedTypeParameterOperation.removeUnusedName(..):
- FixMessages.UnusedCodeFix_RemoveUnusedType_description is wrong here

* UnusedCodeFix.createUnusedTypeParameterFix(..):
- &quot;if (isFormalParameterInEnhancedForStatement(name))&quot; doesn&apos;t make sense here.
- &quot;boolean removeAllAssignements&quot; has a typo, and doesn&apos;t make sense anyway. There are no assignments to a type parameter.

* The label of the quick fix should say &quot;type parameter&quot;, not just &quot;type&quot;.

* LocalCorrectionsSubProcessor#addUnusedTypeParameterProposal(..):
- &quot;if (problemId == IProblem.UnusedTypeParameter)&quot; is unnecessary (always true)

* JavadocTagsSubProcessor:
- label should be &quot;Document *type* parameter to ...&quot;
- quick fix doesn&apos;t work for a method type parameter
- formatting: put &quot;}&quot; and &quot;else {&quot; on one line. You can leave an empty line before if it makes the code more readable.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2201091</commentid>
    <comment_count>3</comment_count>
      <attachid>225427</attachid>
    <who name="Manju Mathew">manju656@gmail.com</who>
    <bug_when>2013-01-10 06:11:53 -0500</bug_when>
    <thetext>Created attachment 225427
Review comments taken care off and the updated junits attached</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2201431</commentid>
    <comment_count>4</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2013-01-10 14:35:43 -0500</bug_when>
    <thetext>Thanks, released as http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=b56753a7cc02eaccb8de11f721340572b0ac7be4
with these changes:
- reverted most of the changes in AddMissingJavadocTagProposal. The additional mode is not necessary.
- we format &quot;if (xxx)&quot; with a space
- removed two Javadocs that didn&apos;t add valuable information</thetext>
  </long_desc>
      
          <attachment
              isobsolete="1"
              ispatch="1"
              isprivate="0"
          >
            <attachid>225278</attachid>
            <date>2013-01-07 08:57:00 -0500</date>
            <delta_ts>2013-01-10 06:11:53 -0500</delta_ts>
            <desc>The proposed fix and the junits attached.</desc>
            <filename>eclipse.jdt.ui.20130107.patch</filename>
            <type>text/plain</type>
            <size>16281</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706892-Sk3c4noanqaTKYNSQSgW6UMmriO4Yeat6eyXxSeBRQM</token>

          </attachment>
          <attachment
              isobsolete="0"
              ispatch="1"
              isprivate="0"
          >
            <attachid>225427</attachid>
            <date>2013-01-10 06:11:00 -0500</date>
            <delta_ts>2013-01-10 06:11:53 -0500</delta_ts>
            <desc>Review comments taken care off and the updated junits attached</desc>
            <filename>eclipse.jdt.ui.20130110.patch</filename>
            <type>text/plain</type>
            <size>23230</size>
            <attacher name="Manju Mathew">manju656@gmail.com</attacher>
            
              <token>1425706892-4D229zrw6LxFaiw6gFgR7Ka2C7yXQGZpYkK8lUqudao</token>

          </attachment>
      

    </bug>
    <bug>
          <bug_id>392931</bug_id>
          
          <creation_ts>2012-10-26 12:31:00 -0400</creation_ts>
          <short_desc>Option to not create an @Override annotation when implementing interface method in 1.6</short_desc>
          <delta_ts>2012-10-29 04:43:36 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>enhancement</bug_severity>
          <target_milestone>4.3 M3</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Markus Keller">markus_keller@ch.ibm.com</reporter>
          <assigned_to name="Markus Keller">markus_keller@ch.ibm.com</assigned_to>
          <cc>jan.wloka@gmail.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706892-q3CebAex9AbVkYfs6fnE1KDSLPZe3jKai1uM3R81lxQ</token>

      

      

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2176370</commentid>
    <comment_count>0</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2012-10-26 12:31:18 -0400</bug_when>
    <thetext>Since Java 1.6, it&apos;s also legal to add an @Override annotation to a method that extends or implements an interface method. However, @Override annotations are not required anywhere, and some users prefer the 1.5 way
http://docs.oracle.com/javase/1.5.0/docs/api/java/lang/Override.html
over the 1.6 way (wrongly spec&apos;d in JavaSE 6 APIs, so better see JavaSE 7):
http://docs.oracle.com/javase/7/docs/api/java/lang/Override.html

We already have an Eclipse-specific compiler diagnostic for missing @Override annotations and a checkbox to include implementations of interface methods.

When that checkbox is checked and the diagnostic is set to error or warning, then we have to generate @Override. But when the checkbox is unchecked, we can also not add @Override.

Note that generation of @Override can be toggled on the Code Style preference page. I&apos;ll add a link there to configure the behavior for interface methods.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2176371</commentid>
    <comment_count>1</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2012-10-26 12:36:26 -0400</bug_when>
    <thetext>Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=8748c9f8b046a1a9a87e8c162d34ca14f14fd05c</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2176781</commentid>
    <comment_count>2</comment_count>
    <who name="Jan Wloka">jan.wloka@gmail.com</who>
    <bug_when>2012-10-29 04:43:36 -0400</bug_when>
    <thetext>That was quick. Thanks, Markus.</thetext>
  </long_desc>
      
      

    </bug>
    <bug>
          <bug_id>392847</bug_id>
          
          <creation_ts>2012-10-25 12:12:00 -0400</creation_ts>
          <short_desc>Endless loop in AdvancedQuickAssistProcessor.getConvertIfElseToSwitchProposals</short_desc>
          <delta_ts>2012-10-30 10:03:22 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>PC</rep_platform>
          <op_sys>Windows 7</op_sys>
          <bug_status>VERIFIED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>critical</bug_severity>
          <target_milestone>4.3 M3</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Markus Keller">markus_keller@ch.ibm.com</reporter>
          <assigned_to name="Deepak Azad">deepakazad@gmail.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>deepakazad@gmail.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706892-6WTdXHDm1x33t51AEcLtRS3hDa44bGwfSYZIer88i-g</token>

      

      

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2175973</commentid>
    <comment_count>0</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2012-10-25 12:12:46 -0400</bug_when>
    <thetext>Endless loop in AdvancedQuickAssistProcessor.getConvertIfElseToSwitchProposals:

	void foo(String[] args) {
		int n = 42;
		if (n == args.length)  // quick assist on &apos;if&apos;
			System.out.println();
		else {
		}
	}


&quot;main&quot; prio=6 tid=0x008ebc00 nid=0xcd0 runnable [0x003dd000]
   java.lang.Thread.State: RUNNABLE
        at java.util.HashMap.get(HashMap.java:303)
        at org.eclipse.jdt.core.dom.DefaultBindingResolver.resolveTypeBindingForName(DefaultBindingResolver.java:910)
        - locked &lt;0x17b345b0&gt; (a org.eclipse.jdt.core.dom.DefaultBindingResolver)
        at org.eclipse.jdt.core.dom.DefaultBindingResolver.resolveExpressionType(DefaultBindingResolver.java:693)
        - locked &lt;0x17b345b0&gt; (a org.eclipse.jdt.core.dom.DefaultBindingResolver)
        at org.eclipse.jdt.core.dom.Expression.resolveTypeBinding(Expression.java:108)
        at org.eclipse.jdt.internal.ui.text.correction.AdvancedQuickAssistProcessor.getConvertIfElseToSwitchProposals(AdvancedQuickAssistProcessor.jav
a:2494)
        at org.eclipse.jdt.internal.ui.text.correction.AdvancedQuickAssistProcessor.getConvertIfElseToSwitchProposals(AdvancedQuickAssistProcessor.jav
a:2439)
        at org.eclipse.jdt.internal.ui.text.correction.AdvancedQuickAssistProcessor.getAssists(AdvancedQuickAssistProcessor.java:197)
...


Furthermore, I saw code like this in that method:

    IVariableBinding binding= (IVariableBinding) qualifiedName.resolveBinding();
    if (binding.isEnumConstant()) { ... }</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2175978</commentid>
    <comment_count>1</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2012-10-25 12:14:36 -0400</bug_when>
    <thetext>Deepak, feel free to assign this bug to you if you want to fix it for M3 (till Monday).</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2176493</commentid>
    <comment_count>2</comment_count>
    <who name="Deepak Azad">deepakazad@gmail.com</who>
    <bug_when>2012-10-26 20:22:25 -0400</bug_when>
    <thetext>Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=bf4933469b8ce2514714df622c2d15a6e77db18a

Small bug caused big problem! Since the problem was serious, the feature should be tested a bit more to make sure no more holes remain.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2176695</commentid>
    <comment_count>3</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2012-10-28 14:52:57 -0400</bug_when>
    <thetext>Thanks for looking into this, Deepak.

I quickly looked at the code, but the 150 lines with two nested loops are not trivial to understand. If you remember the loop variants (i.e. what should make sure the loops do progress in each step), then some comments in the code could greatly help the next one who has to touch this.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2177177</commentid>
    <comment_count>4</comment_count>
    <who name="Deepak Azad">deepakazad@gmail.com</who>
    <bug_when>2012-10-29 19:57:30 -0400</bug_when>
    <thetext>(In reply to comment #3)
&gt; I quickly looked at the code, but the 150 lines with two nested loops are
&gt; not trivial to understand. If you remember the loop variants (i.e. what
&gt; should make sure the loops do progress in each step), then some comments in
&gt; the code could greatly help the next one who has to touch this.

I took a quick look, but am not sure if the complexity of the code can be easily explained in comments. There is already a comment which explains the purpose of the inner loop, which I thought was enough when I had originally adopted Raksha&apos;s patch.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2177401</commentid>
    <comment_count>5</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2012-10-30 09:14:14 -0400</bug_when>
    <thetext>Verified in 4.3-I20121029-2000.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2177438</commentid>
    <comment_count>6</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2012-10-30 10:03:22 -0400</bug_when>
    <thetext>Filed bug 393147 for some cleanup (post-M3, since those bugs are not new and not critical).</thetext>
  </long_desc>
      
      

    </bug>
    <bug>
          <bug_id>391927</bug_id>
          
          <creation_ts>2012-10-15 10:04:00 -0400</creation_ts>
          <short_desc>Speed up JDT UI tests by avoiding performDummySearch()</short_desc>
          <delta_ts>2012-10-15 12:25:58 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords>performance</keywords>
          <priority>P3</priority>
          <bug_severity>normal</bug_severity>
          <target_milestone>4.3 M3</target_milestone>
          
          
          <everconfirmed>1</everconfirmed>
          <reporter name="Markus Keller">markus_keller@ch.ibm.com</reporter>
          <assigned_to name="Markus Keller">markus_keller@ch.ibm.com</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>david_williams@us.ibm.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706893-NRrdalxbim8qyOKUs-HY0L3AaciC4cs0Ccw0vFJHRFs</token>

      

      

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2171783</commentid>
    <comment_count>0</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2012-10-15 10:04:44 -0400</bug_when>
    <thetext>Many jdt.ui and jdt.ui.refactoring tests call JavaProjectHelper#performDummySearch(IJavaSearchScope). This was added to synchronize with the indexer, to make sure subsequent file deletions don&apos;t fail because the indexer is still running and locks the file.

However, performDummySearch is quite costly and is most often not necessary. I&apos;ll comment out the search and rely on the try-catch-retry in JavaProjectHelper#delete(IResource) to handle the rare case where file locking is really a problem.

Initial measurements predict a speedup of 2.5 (AllJDTTests takes only 30 min instead of 75 min).</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2171788</commentid>
    <comment_count>1</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2012-10-15 10:07:27 -0400</bug_when>
    <thetext>http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=9b008aeb6f5070a3f16390883c8a40a0dd6e3505</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2171890</commentid>
    <comment_count>2</comment_count>
    <who name="David Williams">david_williams@us.ibm.com</who>
    <bug_when>2012-10-15 12:25:58 -0400</bug_when>
    <thetext>very nice. Thanks!</thetext>
  </long_desc>
      
      

    </bug>
    <bug>
          <bug_id>391520</bug_id>
          
          <creation_ts>2012-10-10 06:10:00 -0400</creation_ts>
          <short_desc>[preferences] UI addition: Warning for Unused Generic Parameter</short_desc>
          <delta_ts>2012-10-30 03:02:59 -0400</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>VERIFIED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>enhancement</bug_severity>
          <target_milestone>4.3 M3</target_milestone>
          <dependson>385780</dependson>
          <blocked>391643</blocked>
          <everconfirmed>1</everconfirmed>
          <reporter name="Manoj Palat">manpalat@in.ibm.com</reporter>
          <assigned_to name="Markus Keller">markus_keller@ch.ibm.com</assigned_to>
          <cc>jarthana@in.ibm.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
          
          <votes>0</votes>

      
          <token>1425706893-VgkfgjdNcU6FRwRW0Qrh_BKC4F9cGzNLL55jYk184lM</token>

      

      

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2169877</commentid>
    <comment_count>0</comment_count>
    <who name="Manoj Palat">manpalat@in.ibm.com</who>
    <bug_when>2012-10-10 06:10:26 -0400</bug_when>
    <thetext>- Ref bug 385780 (test case if required is mentioned in that bug).
- Need a UI for warning unused generic params - options : {ignore,warning, error}</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2176445</commentid>
    <comment_count>1</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2012-10-26 15:00:48 -0400</bug_when>
    <thetext>Fixed with http://git.eclipse.org/c/jdt/eclipse.jdt.ui.git/commit/?id=c6382f8284d9ab6aa8a2bdaf4700cfcb577a2223</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2176446</commentid>
    <comment_count>2</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2012-10-26 15:01:40 -0400</bug_when>
    <thetext>Filed bug 392946 to add quick fixes.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2177229</commentid>
    <comment_count>3</comment_count>
    <who name="Jay Arthanareeswaran">jarthana@in.ibm.com</who>
    <bug_when>2012-10-30 03:02:59 -0400</bug_when>
    <thetext>Verified for 4.3 M3 with build I20121029-2000</thetext>
  </long_desc>
      
      

    </bug>
    <bug>
          <bug_id>390915</bug_id>
          
          <creation_ts>2012-10-02 06:58:00 -0400</creation_ts>
          <short_desc>Migrate JDT website to Git</short_desc>
          <delta_ts>2012-11-08 12:59:27 -0500</delta_ts>
          <reporter_accessible>1</reporter_accessible>
          <cclist_accessible>1</cclist_accessible>
          <classification_id>2</classification_id>
          <classification>Eclipse</classification>
          <product>JDT</product>
          <component>UI</component>
          <version>4.3</version>
          <rep_platform>All</rep_platform>
          <op_sys>All</op_sys>
          <bug_status>RESOLVED</bug_status>
          <resolution>FIXED</resolution>
          
          
          <bug_file_loc></bug_file_loc>
          <status_whiteboard></status_whiteboard>
          <keywords></keywords>
          <priority>P3</priority>
          <bug_severity>enhancement</bug_severity>
          <target_milestone>4.3 M4</target_milestone>
          
          <blocked>324116</blocked>
          <everconfirmed>1</everconfirmed>
          <reporter name="Dani Megert">daniel_megert@ch.ibm.com</reporter>
          <assigned_to name="Eclipse Webmaster">webmaster@eclipse.org</assigned_to>
          <cc>daniel_megert@ch.ibm.com</cc>
    
    <cc>deepakazad@gmail.com</cc>
    
    <cc>duemir@gmail.com</cc>
    
    <cc>jarthana@in.ibm.com</cc>
    
    <cc>markus_keller@ch.ibm.com</cc>
    
    <cc>Olivier_Thomann@ca.ibm.com</cc>
    
    <cc>srikanth_sankaran@in.ibm.com</cc>
    
    <cc>stephan.herrmann@berlin.de</cc>
    
    <cc>webmaster@eclipse.org</cc>
          
          <votes>0</votes>

      
          <token>1425706893-b7_nDO9rL5jVj9phSbwpXY8kCwH6Z7DeOyEK6HX837k</token>

      

      

          <comment_sort_order>oldest_to_newest</comment_sort_order>  
          <long_desc isprivate="0" >
    <commentid>2166630</commentid>
    <comment_count>0</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2012-10-02 06:58:01 -0400</bug_when>
    <thetext>CVS path: www/jdt/ui

Markus, please fill in what we want to migrate and then move the request to the webmaster.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2166636</commentid>
    <comment_count>1</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2012-10-02 07:09:44 -0400</bug_when>
    <thetext>After opening bug 390916 and discussing with Markus, we concluded that it makes more sense to just have one JDT repository for the JDT website.

CVS path: www/jdt/*
ACL: &apos;eclipse.jdt.core&apos; and &apos;eclipse.jdt.ui&apos;

The Git repository will deny non-fast-forward and deletions.

Srikanth, please post in this bug what you&apos;d like to migrate.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2166638</commentid>
    <comment_count>2</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2012-10-02 07:10:24 -0400</bug_when>
    <thetext>*** Bug 390916 has been marked as a duplicate of this bug. ***</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2166772</commentid>
    <comment_count>3</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2012-10-02 10:20:53 -0400</bug_when>
    <thetext>I did a few &apos;du -sk * | sort -rn&apos; and found a few memory hogs, basically in 3 categories:

1) old patches (mostly in the Attic and no longer relevant)

=&gt; I guess we can just remove them from the CVS repo via ssh build.eclipse.org

2) update sites (for internal/supplementary projects like the ASTView, or beta-versions)
3) other larger files/directories (screencasts, code coverage / API tools reports)

=&gt; We can remove outdated stuff, but we need a transparent solution at least for the update sites.

@Webmaster: Can we just create a directory /home/data/httpd/download.eclipse.org/jdt , copy the bigger stuff there, remove the CVS files, and somehow add a soft link at the old location that points to the new location?
How would we create that soft link? Or is there a better solution?</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2167181</commentid>
    <comment_count>4</comment_count>
    <who name="Srikanth Sankaran">srikanth_sankaran@in.ibm.com</who>
    <bug_when>2012-10-03 03:06:45 -0400</bug_when>
    <thetext>(In reply to comment #1)

&gt; Srikanth, please post in this bug what you&apos;d like to migrate.

Olivier, Request you to weigh in on this: TIA.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2167372</commentid>
    <comment_count>5</comment_count>
    <who name="Eclipse Webmaster">webmaster@eclipse.org</who>
    <bug_when>2012-10-03 10:51:59 -0400</bug_when>
    <thetext>(In reply to comment #3)

&gt; @Webmaster: Can we just create a directory
&gt; /home/data/httpd/download.eclipse.org/jdt , copy the bigger stuff there,
&gt; remove the CVS files, and somehow add a soft link at the old location that
&gt; points to the new location?
&gt; How would we create that soft link? Or is there a better solution?

I can certainly create /home/data/httpd/download.eclipse.org/jdt for you, although perhaps archive.eclipse.org would be better if this data isn&apos;t expected to change (much).

As for the links, about the only real option is for us to rewrite/redirect specific URLs.  The question then becomes: how long do we keep these redirects?

-M.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2167642</commentid>
    <comment_count>6</comment_count>
    <who name="Deepak Azad">deepakazad@gmail.com</who>
    <bug_when>2012-10-03 20:24:12 -0400</bug_when>
    <thetext>(In reply to comment #3)
&gt; but we need a transparent solution at least
&gt; for the update sites.

If links for update site changes we need to also update the links in Eclipse Marketplace - http://marketplace.eclipse.org/content/ast-view/ and http://marketplace.eclipse.org/content/javaelement-view 

(I could do this once the migration is complete)</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2167775</commentid>
    <comment_count>7</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2012-10-04 07:07:14 -0400</bug_when>
    <thetext>(In reply to comment #5)
It&apos;s hard to believe that we&apos;re the first website that hosted a small update site in CVS and now needs a different solution since accumulating binaries in a Git repo is not a good solution. I guess I&apos;ll have to replace the update site with a composite repository [1] that points to the new location. 

In the near future, we will also need a BETA_JAVA8 update site, where we post previews of our Java 8 implementation. It&apos;s imperative that this update site is not mirrored anywhere outside eclipse.org. I guess archive.eclipse.org is the right place for that.

Webmaster, could you please create /home/data/httpd/archive.eclipse.org/jdt with write access for eclipse.jdt, so we can start experimenting?

[1] http://help.eclipse.org/juno/index.jsp?topic=/org.eclipse.platform.doc.isv/guide/p2_composite_repositories.htm</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2168123</commentid>
    <comment_count>8</comment_count>
    <who name="Olivier Thomann">Olivier_Thomann@ca.ibm.com</who>
    <bug_when>2012-10-04 16:03:35 -0400</bug_when>
    <thetext>(In reply to comment #4)
&gt; (In reply to comment #1)
&gt; Olivier, Request you to weigh in on this: TIA.
For jdt/core, we should move the update site to a different location as binary files don&apos;t work well with git.
It should also be a good time to clean up some really old bundles which are completely obsolete now.
So I would say, prior to the move, a cleanup should be done to minimize the size of data being moved to git.
So all what Markus said in comment 3 applies to JDT/Core as well.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2168234</commentid>
    <comment_count>9</comment_count>
    <who name="Deepak Azad">deepakazad@gmail.com</who>
    <bug_when>2012-10-04 20:11:20 -0400</bug_when>
    <thetext>(In reply to comment #7)
So people would go to an *archive* URL (http://www.archive.eclipse.org/jdt/) to download a BETA tool (BETA_JAVA8)? Feels a bit odd...</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2168372</commentid>
    <comment_count>10</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2012-10-05 05:23:49 -0400</bug_when>
    <thetext>&gt; So people would go to an *archive* URL (http://www.archive.eclipse.org/jdt/)
&gt; to download a BETA tool (BETA_JAVA8)? Feels a bit odd...

If the composite repository I mentioned in comment 7 works out, then the archive URL would only show up in the progress view during download.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2168539</commentid>
    <comment_count>11</comment_count>
    <who name="Denis Roy">denis.roy@eclipse.org</who>
    <bug_when>2012-10-05 11:09:38 -0400</bug_when>
    <thetext>&gt; It&apos;s hard to believe that we&apos;re the first website that hosted a small update
&gt; site in CVS

s/first/only/


(In reply to comment #7)
&gt; In the near future, we will also need a BETA_JAVA8 update site, where we
&gt; post previews of our Java 8 implementation. It&apos;s imperative that this update
&gt; site is not mirrored anywhere outside eclipse.org. I guess
&gt; archive.eclipse.org is the right place for that.

Or build.eclipse.org</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2168566</commentid>
    <comment_count>12</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2012-10-05 11:44:46 -0400</bug_when>
    <thetext>I created a forwarding update site http://www.eclipse.org/jdt/ui/update-site-new
that takes its contents from http://www.eclipse.org/jdt/ui/update-site .

That worked fine, so I&apos;d say /home/data/httpd/archive.eclipse.org/jdt is the way to go.

We need write access for at least &quot;eclipse.jdt&quot;, but optimally also for &quot;eclipse.jdt.core&quot; and &quot;eclipse.jdt.ui&quot;.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2168681</commentid>
    <comment_count>13</comment_count>
    <who name="Eclipse Webmaster">webmaster@eclipse.org</who>
    <bug_when>2012-10-05 15:04:26 -0400</bug_when>
    <thetext>(In reply to comment #7)

&gt; 
&gt; Webmaster, could you please create /home/data/httpd/archive.eclipse.org/jdt
&gt; with write access for eclipse.jdt, so we can start experimenting?

Done.

-M.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2169215</commentid>
    <comment_count>14</comment_count>
    <who name="Srikanth Sankaran">srikanth_sankaran@in.ibm.com</who>
    <bug_when>2012-10-09 00:59:35 -0400</bug_when>
    <thetext>(In reply to comment #8)
&gt; (In reply to comment #4)
&gt; &gt; (In reply to comment #1)
&gt; &gt; Olivier, Request you to weigh in on this: TIA.
&gt; For jdt/core, we should move the update site to a different location as
&gt; binary files don&apos;t work well with git.
&gt; It should also be a good time to clean up some really old bundles which are
&gt; completely obsolete now.
&gt; So I would say, prior to the move, a cleanup should be done to minimize the
&gt; size of data being moved to git.

Jay, can you please take a look into this as soon as possible ? TIA.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2169783</commentid>
    <comment_count>15</comment_count>
    <who name="Jay Arthanareeswaran">jarthana@in.ibm.com</who>
    <bug_when>2012-10-10 01:12:03 -0400</bug_when>
    <thetext>(In reply to comment #14)
&gt; Jay, can you please take a look into this as soon as possible ? TIA.

The last I checked, I don&apos;t have shell access. And I guess I will have to request Markus to do what he finds appropriate from the list Olivier mentioned.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2169814</commentid>
    <comment_count>16</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2012-10-10 03:48:37 -0400</bug_when>
    <thetext>(In reply to comment #15)
&gt; (In reply to comment #14)
&gt; &gt; Jay, can you please take a look into this as soon as possible ? TIA.
&gt; 
&gt; The last I checked, I don&apos;t have shell access. And I guess I will have to
&gt; request Markus to do what he finds appropriate from the list Olivier
&gt; mentioned.

You only need to say what you want to move where (confirm/verify Olivier&apos;s comment). Then the webmaster (or Markus) will do it.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2170374</commentid>
    <comment_count>17</comment_count>
    <who name="Jay Arthanareeswaran">jarthana@in.ibm.com</who>
    <bug_when>2012-10-11 00:39:49 -0400</bug_when>
    <thetext>(In reply to comment #16)
&gt; You only need to say what you want to move where (confirm/verify Olivier&apos;s
&gt; comment). Then the webmaster (or Markus) will do it.

I have nothing to add to what Olivier and Markus have already listed. So, what stated in comment #3 and #8 should be all.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2170790</commentid>
    <comment_count>18</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2012-10-11 16:59:27 -0400</bug_when>
    <thetext>OK, I&apos;m mostly done with jdt/ui and jdt/apt. Moved stuff that I think we should delete into /cvsroot/org.eclipse/www/jdt/unused/ .

Matt:
I moved a few files/directories directly on the server. This obviously didn&apos;t notify the webserver&apos;s CVS hook, so some removed files are still available, e.g. http://www.eclipse.org/jdt/ui/update-site-new/build.xml .

Can I somehow trigger a refresh of /cvsroot/org.eclipse/www/jdt/{ui,apt} ?</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2171042</commentid>
    <comment_count>19</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2012-10-12 08:29:12 -0400</bug_when>
    <thetext>(In reply to comment #17)
&gt; I have nothing to add to what Olivier and Markus have already listed. So,
&gt; what stated in comment #3 and #8 should be all.

Jay: OK, so please go and remove the outdated patches, previews, and code coverage reports via CVS. Also remove references to the removed stuff from the web pages.

I&apos;ve moved the content of jdt/core/tools/jdtcoretools/update-site to the archive and replaced the original update-site with a composite repository that transparently forwards to the repo in the archive.

Stephan: Can you do something similar for the beta-null-annotations-for-fields repo? Just use a modified copy of jdt/core/tools/jdtcoretools/update-site/build.xml and run it in the workbench VM. We can&apos;t use the website repo any more to host the update site, so you either have to send me the bits and I can put them to archive.eclipse.org, or you can also host the data anywhere outside of eclipse.org.

Once the checked-out size is down to 1 MB or so, we can ask the webmaster to move everything except for the Attic directories to Git. This will lose history of all deleted files, but that&apos;s what we want.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2171260</commentid>
    <comment_count>20</comment_count>
    <who name="Eclipse Webmaster">webmaster@eclipse.org</who>
    <bug_when>2012-10-12 13:34:16 -0400</bug_when>
    <thetext>(In reply to comment #18)
 
&gt; Can I somehow trigger a refresh of /cvsroot/org.eclipse/www/jdt/{ui,apt} ?

I&apos;ve forced the checkout to run.

-M.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2172316</commentid>
    <comment_count>21</comment_count>
    <who name="Jay Arthanareeswaran">jarthana@in.ibm.com</who>
    <bug_when>2012-10-16 06:50:05 -0400</bug_when>
    <thetext>(In reply to comment #19)
&gt; Jay: OK, so please go and remove the outdated patches, previews, and code
&gt; coverage reports via CVS. Also remove references to the removed stuff from
&gt; the web pages.

Markus, should I remove it only from HEAD? What about the history and the older revisions if there are any?</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2172390</commentid>
    <comment_count>22</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2012-10-16 09:19:25 -0400</bug_when>
    <thetext>(In reply to comment #21)
Yes, remove it from HEAD.

During the conversion to Git, the webmaster will remove all files that are not currently in HEAD, so the removed files will disappear along with all old revisions. Yes, this will also remove the history of other files that have been deleted in HEAD, but I don&apos;t think it&apos;s really worthwhile to keep deleted files from the website repo.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2172795</commentid>
    <comment_count>23</comment_count>
    <who name="Jay Arthanareeswaran">jarthana@in.ibm.com</who>
    <bug_when>2012-10-17 04:52:55 -0400</bug_when>
    <thetext>Srikanth,

We have a couple of junit test results (apparently run on beta Java 7) that are taking about 14 MB of space. Do you think we still need them?</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2172805</commentid>
    <comment_count>24</comment_count>
    <who name="Srikanth Sankaran">srikanth_sankaran@in.ibm.com</who>
    <bug_when>2012-10-17 05:17:41 -0400</bug_when>
    <thetext>(In reply to comment #23)
&gt; Srikanth,
&gt; 
&gt; We have a couple of junit test results (apparently run on beta Java 7) that
&gt; are taking about 14 MB of space. Do you think we still need them?

Since we didn&apos;t even know these existed, these shouldn&apos;t be needed :)</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2172839</commentid>
    <comment_count>25</comment_count>
    <who name="Jay Arthanareeswaran">jarthana@in.ibm.com</who>
    <bug_when>2012-10-17 06:36:29 -0400</bug_when>
    <thetext>I have removed the following stuff from the site:

1. All under codecoverage - All belong to 3.7 and before
2. All under patches - All from versions 3.5 and before
3. Really old previews 
4. An exclusive update site for a particular preview under r3.4
5. Few old junit test results etc.

Now the entire core folder (excluding beta-null-annotations-for-fields) takes about 1.5 MB.

Note: I have just disabled the links in the pages for the patches, leaving the other information about the patch in tact. It&apos;s just not worth for the pages that nobody looks at. If anyone thinks otherwise, let me know.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2173623</commentid>
    <comment_count>26</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2012-10-18 10:27:07 -0400</bug_when>
    <thetext>Oops, I just realized Stephan was not CCd on this bug.

Stephan, can you please read comment 19? Shall I move the three p2 repositories in beta-null-annotations-for-fields to the archive? If you have shell access on build.eclipse.org, you can also do it yourself if you want.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2173664</commentid>
    <comment_count>27</comment_count>
    <who name="Stephan Herrmann">stephan.herrmann@berlin.de</who>
    <bug_when>2012-10-18 11:01:35 -0400</bug_when>
    <thetext>(In reply to comment #26)
&gt; Oops, I just realized Stephan was not CCd on this bug.

yea, that should hopefully excuse my silence here :)

&gt; Stephan, can you please read comment 19? Shall I move the three p2
&gt; repositories in beta-null-annotations-for-fields to the archive? If you have
&gt; shell access on build.eclipse.org, you can also do it yourself if you want.

I would normally prefer to do this in a coordinated fashion between the repos and the wiki plus a note on the corresponding bugs, since these are published
URLS.

So, to double check the solution: I was advised to put this repo into the web-CVS for two reasons IIRC:
- use a URL that clearly belongs to JDT
- don&apos;t use a URL that is mirrored so we can remove it in a controlled way later

If www is no longer available I only see this option:
   http://archive.eclipse.org/jdt/

However, my shell access on build.eclipse.org does not buy me write access anywhere in that area.
Have group:
   eclipse.jdt.core
Need group:
   eclipse.jdt

What do you suggest from here?

Also: 

(In reply to comment #19)
&gt; Just use a modified copy of
&gt; jdt/core/tools/jdtcoretools/update-site/build.xml

Where would I find that? It&apos;s not on archive.

&gt; and run it in the workbench VM.

Why would I do this rather than just moving the existing repos?

&gt; ... or you can also host the data anywhere outside of eclipse.org.

Seems to contradict previous requirements? (see bug 331649 comment 44).</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2173681</commentid>
    <comment_count>28</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2012-10-18 11:35:17 -0400</bug_when>
    <thetext>Sorry, with &quot;move to the archive&quot;, I meant &quot;move to the archive&quot; + &quot;replace with a composite repository that forwards to the archive&quot;.

That way, the public url stays unchanged, and the download location change is completely transparent for users. Since archive.eclipse.org is not mirrored, we keep full control over the the update site and can remove stuff when the beta phase is over.

I just created 
/home/data/httpd/archive.eclipse.org/jdt/core/beta-null-annotations-for-fields
and added write access for the eclipse.jdt.core group. Can you try to touch a file there?

&gt; (In reply to comment #19)
&gt; &gt; Just use a modified copy of
&gt; &gt; jdt/core/tools/jdtcoretools/update-site/build.xml
&gt; 
&gt; Where would I find that? It&apos;s not on archive.

No, it&apos;s at the current website location in CVS (in /cvsroot/org.eclipse)

&gt; &gt; and run it in the workbench VM.
&gt; Why would I do this rather than just moving the existing repos?

That creates the composite*.jar files. Commit them, and the forwarding repo is live.

&gt; &gt; ... or you can also host the data anywhere outside of eclipse.org.
&gt; Seems to contradict previous requirements? (see bug 331649 comment 44).

That was mostly because &quot;objectteams&quot; in the public url looked strange. But for an internal forwarding url, that&apos;s OK.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2173690</commentid>
    <comment_count>29</comment_count>
    <who name="Stephan Herrmann">stephan.herrmann@berlin.de</who>
    <bug_when>2012-10-18 11:44:24 -0400</bug_when>
    <thetext>(In reply to comment #28)
&gt; Sorry, with &quot;move to the archive&quot;, I meant &quot;move to the archive&quot; + &quot;replace
&gt; with a composite repository that forwards to the archive&quot;.

Ah, now I see what you mean :)

&gt; I just created 
&gt; /home/data/httpd/archive.eclipse.org/jdt/core/beta-null-annotations-for-
&gt; fields
&gt; and added write access for the eclipse.jdt.core group. Can you try to touch
&gt; a file there?

I can. Interestingly, ls -l still says &quot;eclipse.jdt&quot; as the group. Is ls just truncating the name at the second &apos;.&apos;?? Nevermind, as it works now.

&gt; &gt; (In reply to comment #19)
&gt; &gt; &gt; Just use a modified copy of
&gt; &gt; &gt; jdt/core/tools/jdtcoretools/update-site/build.xml
&gt; &gt; 
&gt; &gt; Where would I find that? It&apos;s not on archive.
&gt; 
&gt; No, it&apos;s at the current website location in CVS (in /cvsroot/org.eclipse)

I&apos;ll look into that later today. 
If I have troubles with the ant file I&apos;ll just manually create the metadata :)</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2173696</commentid>
    <comment_count>30</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2012-10-18 11:52:27 -0400</bug_when>
    <thetext>&gt; I can. Interestingly, ls -l still says &quot;eclipse.jdt&quot; as the group.
That&apos;s because I didn&apos;t want to change the main group but added the core group via ACLs (use getfacl to see the whole story).

&gt; I&apos;ll look into that later today.
Great, thanks. No hurries, we still have a few CVS days left ;-)</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2173833</commentid>
    <comment_count>31</comment_count>
    <who name="Stephan Herrmann">stephan.herrmann@berlin.de</who>
    <bug_when>2012-10-18 16:17:28 -0400</bug_when>
    <thetext>All meaty files from beta-null-annotations-for-fields have been migrated to archive and the redirecting composites are in place and smoke-tests done.

(And I learned about running ant scripts in the workbench VM, thanks :) )</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2175606</commentid>
    <comment_count>32</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2012-10-24 14:50:19 -0400</bug_when>
    <thetext>Webmaster, we&apos;re ready for the ride to Git.

CVS path: www/jdt/*, but without:
- www/jdt/unused
- all Attic folders
- all empty folders, recursively (e.g. /www/jdt/core/codecoverage/ has a huge tree of folders that are only there to contain nested Attic folders)

ACL: &apos;eclipse.jdt.core&apos; and &apos;eclipse.jdt.ui&apos;.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2178861</commentid>
    <comment_count>33</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2012-11-02 08:02:17 -0400</bug_when>
    <thetext>(In reply to comment #32)
&gt; Webmaster, we&apos;re ready for the ride to Git.

Webmaster, please advise if I should prepare a separate folder with all the content to migrate.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2179581</commentid>
    <comment_count>34</comment_count>
    <who name="Eclipse Webmaster">webmaster@eclipse.org</who>
    <bug_when>2012-11-05 11:30:16 -0500</bug_when>
    <thetext>(In reply to comment #33)

&gt; Webmaster, please advise if I should prepare a separate folder with all the
&gt; content to migrate.

That would be awesome.

-M.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2179658</commentid>
    <comment_count>35</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2012-11-05 14:30:54 -0500</bug_when>
    <thetext>After a few &apos;rsync -avm --exclude=&quot;Attic&quot; xxx migrate-to-git/&apos;, all the content for the new Git repo is here:

/home/data/cvs/org.eclipse/www/jdt/migrate-to-git/</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2179721</commentid>
    <comment_count>36</comment_count>
    <who name="Eclipse Webmaster">webmaster@eclipse.org</who>
    <bug_when>2012-11-05 16:51:47 -0500</bug_when>
    <thetext>Done.  CVS is frozen, and the Git URLs are:

ssh://committer_id@git.eclipse.org/gitroot/www.eclipse.org/jdt.git

http://@git.eclipse.org/gitroot/www.eclipse.org/jdt.git

-M.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2180145</commentid>
    <comment_count>37</comment_count>
    <who name="Markus Keller">markus_keller@ch.ibm.com</who>
    <bug_when>2012-11-06 13:15:45 -0500</bug_when>
    <thetext>Thanks, looks good.

Just one thing: Shouldn&apos;t there be a jdt.git/hooks/update file? AFAICS, this is missing in most git/www.eclipse.org/*.git repos.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2181297</commentid>
    <comment_count>38</comment_count>
    <who name="Eclipse Webmaster">webmaster@eclipse.org</who>
    <bug_when>2012-11-08 11:44:10 -0500</bug_when>
    <thetext>We don&apos;t require the update hook for website repos, but if you want to use it I can certainly hook you up.  

-M.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2181325</commentid>
    <comment_count>39</comment_count>
    <who name="Dani Megert">daniel_megert@ch.ibm.com</who>
    <bug_when>2012-11-08 12:30:59 -0500</bug_when>
    <thetext>(In reply to comment #38)
&gt; We don&apos;t require the update hook for website repos, but if you want to use
&gt; it I can certainly hook you up.  
&gt; 
&gt; -M.

Yes, please.</thetext>
  </long_desc><long_desc isprivate="0" >
    <commentid>2181338</commentid>
    <comment_count>40</comment_count>
    <who name="Eclipse Webmaster">webmaster@eclipse.org</who>
    <bug_when>2012-11-08 12:59:27 -0500</bug_when>
    <thetext>Ok, I&apos;ve added the update hook to /gitroot/www.eclipse.org/jdt.git .

-M.</thetext>
  </long_desc>
      
      

    </bug>

</bugzilla>