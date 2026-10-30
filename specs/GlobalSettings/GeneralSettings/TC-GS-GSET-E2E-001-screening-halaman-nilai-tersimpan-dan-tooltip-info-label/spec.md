---
id: TC-GS-GSET-E2E-001-screening-halaman-nilai-tersimpan-dan-tooltip-info-label
title: "Screening halaman, nilai tersimpan, tooltip ikon info"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-01
  - TC-GS-GSET-02
  - TC-GS-GSET-06
coverage:
  web: automated
---

# Screening halaman, nilai tersimpan, tooltip ikon info

## Prerequisites

- Mode: FE+BE.
- Hook suite (`suite.md`): login akun aktor, flag Guided Tooltip `guided_tooltip_seen_gs-general-settings` disetel seen, record Client A dipulihkan ke baseline, dan halaman Global Settings > General Settings dibuka di `beforeEach`.
- Akun aktor: Total Control (Budi Santoso, Pre-setup No 1) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login sekali di hook `before`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup No 10 (record Client A, hanya dibaca): Currency Code `IDR` (label `Rp - Indonesian Rupiah`), Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `Asia/Jakarta` (label `(UTC+07:00) Bangkok, Hanoi, Jakarta`), Session Idle Timeout `30 minutes`. Nilai dibaca dari `Fixture.generalSettings.<kunci>` (berkas `fixtures/generalSettings.json` belum ada; ditandai untuk tahap script).
- Spec tidak membuat data, tidak menekan `[Save]`, dan tidak mengubah state global.

## Test Steps

### TC-GS-GSET-01: Screening halaman (Total Control)

1. Verifikasi Breadcrumb menampilkan segmen tunggal "General Settings"
2. Verifikasi segmen Breadcrumb "General Settings" aktif dan tidak dapat diklik
3. Verifikasi icon button Changelog tampil di pojok kanan atas halaman
4. Verifikasi icon button Changelog adalah satu-satunya toolbar icon di header
5. Verifikasi SectionCard "Currency" tampil dengan Select (varian Searchable) "Currency Code"
6. Verifikasi Select "Currency Code" disertai ikon info
7. Verifikasi Preview text Currency "Rp 5.000,00"
8. Verifikasi SectionCard "Date & Time" tampil dengan Select "Date Format" bernilai `dd/MM/yy`
9. Verifikasi Select "Time Format" bernilai `HH:mm`
10. Verifikasi Select "Time Zone" bervarian Searchable
11. Verifikasi Select "Time Zone" disertai ikon info
12. Verifikasi Select "Time Zone" bernilai `Asia/Jakarta`
13. Verifikasi Preview text Date & Time "17/03/23 14:30"
14. Verifikasi SectionCard "Security" tampil dengan Select "Session Idle Timeout"
15. Verifikasi Select "Session Idle Timeout" disertai ikon info
16. Verifikasi Select "Session Idle Timeout" bernilai `30 minutes`
17. Verifikasi Select "Date Format" dan "Time Format" tidak punya ikon info
18. Verifikasi field pada ketiga SectionCard tidak memakai tanda `*`
19. Verifikasi tidak ada field "Currency Symbol", tidak ada field "Decimal Places", tidak ada tombol `[Clear Field]`, dan tidak ada placeholder "-- Select --"
20. Verifikasi Button "Save" berwarna success (hijau)
21. Verifikasi Button "Save" menempel di bawah halaman
22. Verifikasi Button "Save" disabled
23. Verifikasi tidak ada tombol Cancel pada halaman

### TC-GS-GSET-02: Halaman menampilkan nilai record tersimpan

24. Muat ulang halaman Global Settings > General Settings (F5)
25. Verifikasi Select "Currency Code" bernilai `IDR`
26. Verifikasi Select "Date Format" bernilai `dd/MM/yy`
27. Verifikasi Select "Time Format" bernilai `HH:mm`
28. Verifikasi Select "Time Zone" bernilai `Asia/Jakarta`
29. Verifikasi Select "Session Idle Timeout" bernilai `30 minutes`
30. Verifikasi Button "Save" disabled (state Unchanged)

### TC-GS-GSET-06: Tooltip ikon info label

31. Hover ikon info di samping label "Currency Code"
32. Verifikasi tooltip "Currency used to display amounts across all products. Changing it does not convert existing amounts."
33. Hover ikon info di samping label "Time Zone"
34. Verifikasi tooltip "Time zone used to display dates and times across all products."
35. Hover ikon info di samping label "Session Idle Timeout"
36. Verifikasi tooltip "How long a user can stay idle before being logged out automatically."
37. Verifikasi label "Date Format" dan "Time Format" tidak punya ikon info

## Notes

- Sumber: `global-settings/general-settings/TestCases/tc-general-settings.md`. Spec ini 37 langkah nominal tanpa langkah berulang (ekspansi sama), melewati sekitar 35 langkah. Alasan: satu kelas (screening halaman satu layar, hanya membaca, tanpa seeding dan tanpa mengubah state), tiga TC memakai akun, layar, dan record yang sama, dan Expected TC-GS-GSET-01 berderet banyak klausa independen yang masing-masing mendapat satu `Verifikasi` (S-01).
- Subjudul `###` memetakan langkah ke id TC granular. TC-GS-GSET-01 langkah 1 (Buka General Settings) dan langkah 2 (Amati halaman) dipenuhi hook `beforeEach` suite; spec langsung mengasersi.
- Pengecualian S-01 daftar elemen yang sama-sama tidak ada dipakai di langkah 19 (empat elemen yang disebut utuh di Expected b iv). Langkah 17 dan 37 mengasersi hal yang sama untuk dua TC berbeda (TC-GS-GSET-01 b iv dan TC-GS-GSET-06 d).
- Pecahan Expected TC-GS-GSET-01: a i menjadi langkah 1 dan 2; b i menjadi langkah 5 sampai 7; b ii menjadi langkah 8 sampai 13; b iii menjadi langkah 14 sampai 16; c menjadi langkah 20 sampai 23. Klausa yang bisa gagal sendiri dipecah per klausa: varian Searchable, ikon info, dan nilai (langkah 5 dan 6, 10 sampai 12, 14 sampai 16) serta warna success dan posisi menempel di bawah halaman Button "Save" (langkah 20 dan 21).
- Langkah penghubung (tanpa `Verifikasi`): langkah 24 (muat ulang agar TC-GS-GSET-02 mengamati pembukaan halaman sendiri), langkah 31, 33, 35 (hover pemicu tooltip; tooltip diasersi segera setelah hover, sebelum langkah berikutnya mengubah state).
- Asersi absence (langkah 17, 19, 23, 37) didahului asersi positif atas elemen lain pada halaman yang sama (langkah 3 sampai 16 dan 20 sampai 21), sehingga halaman terbukti sudah termuat.
- Temuan untuk QA:
  - TC-GS-GSET-01 b ii menyebut nilai Time Zone `Asia/Jakarta`, sedangkan yang tampil pada Select adalah label opsi `(UTC+07:00) Bangkok, Hanoi, Jakarta` (PRD §4.3a). Spec mengasersi nilai terpilih sesuai TC (kunci IANA) dan label yang tampil dibaca dari opsi terpilih; QA perlu menegaskan apakah yang diasersi kunci atau label. Hal yang sama berlaku untuk Currency Code `IDR` (label `Rp - Indonesian Rupiah`) pada langkah 5 dan 25.
  - TC-GS-GSET-01 menyatakan "Button Save berwarna success (hijau)"; TC tidak menyebut cara mengamati warna (token atau nilai). Spec mengasersi atribut varian success pada tombol.
