# revision 30372
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-langindic
Epoch:		1
Version:	20131013
Release:	5
Summary:	Indic scripts
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langindic.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-basic
Requires:	texlive-bangtex
Requires:	texlive-bengali
Requires:	texlive-burmese
Requires:	texlive-devnag
Requires:	texlive-ebong
Requires:	texlive-hyphen-indic
Requires:	texlive-hyphen-sanskrit
Requires:	texlive-sanskrit
Requires:	texlive-velthuis
Requires:	texlive-wnri
Requires:	texlive-wnri-latex
Requires:	texlive-xetex-devanagari

%description
Support for Indic scripts.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
