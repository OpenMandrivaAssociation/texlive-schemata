%global tl_name schemata
%global tl_revision 76178

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5
Release:	%{tl_revision}.1
Summary:	Print topical diagrams
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/schemata
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/schemata.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/schemata.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/schemata.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package facilitates the creation of "topical schemata", i.e.
outlines that use braces (or facsimiles thereof) to illustrate the
breakdown of concepts and categories in Scholastic thought from late
medieval and early modern periods.

