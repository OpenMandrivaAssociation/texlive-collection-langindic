# revision 25494
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-langindic
Epoch:		1
Version:	20120302
Release:	1
Summary:	Indic scripts
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langindic.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-bangtex
Requires:	texlive-bengali
Requires:	texlive-burmese
Requires:	texlive-devnag
Requires:	texlive-ebong
Requires:	texlive-hyphen-indic
Requires:	texlive-hyphen-sanskrit
Requires:	texlive-malayalam
Requires:	texlive-sanskrit
Requires:	texlive-velthuis
Requires:	texlive-wnri
Requires:	texlive-wnri-latex
Requires:	texlive-xetex-devanagari
Requires:	texlive-collection-basic

%description
Support for typesetting some Indic scripts.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
