Name:		kokoro-voice-jm_kumo
Version:	1.0
Release:	1
Summary:	Japanese male Kokoro voice jm_kumo
URL:		https://huggingface.co/hexgrad/Kokoro-82M/tree/main/voices
License:	Apache-2.0
BuildArch:	noarch
Group:		System/Multimedia
Provides:	kokoro-voice
Provides:	kokoro-voice-ja
Requires:	kokoro-model >= 1.0

%sourcelist
https://huggingface.co/hexgrad/Kokoro-82M/resolve/main/voices/jm_kumo.pt

%description
%{summary}.
Uses the shared checkpoint in kokoro-model.
Japanese grapheme-to-phoneme support is not part of python-misaki yet, so synthesis with this voice stops until that support is packaged.
Select it with: kokoro -m jm_kumo

%install
mkdir -p %{buildroot}%{_datadir}/kokoro/voices
install -c -m 644 %{S:0} %{buildroot}%{_datadir}/kokoro/voices/jm_kumo.pt

%files
%{_datadir}/kokoro/voices/jm_kumo.pt
