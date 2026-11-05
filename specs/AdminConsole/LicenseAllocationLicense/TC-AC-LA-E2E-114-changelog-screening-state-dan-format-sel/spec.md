---
id: TC-AC-LA-E2E-114-changelog-screening-state-dan-format-sel
title: "Modal Changelog: Screening, Cakupan Seluruh Alokasi, Format Sel, Empty State, dan Tutup"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-354
  - TC-AC-LA-355
  - TC-AC-LA-356
  - TC-AC-LA-357
  - TC-AC-LA-359
coverage:
  web: automated
---

# Modal Changelog: Screening, Cakupan Seluruh Alokasi, Format Sel, Empty State, dan Tutup

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var di atas adalah usulan yang belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; didaftarkan tim FE.
- Data seed Pre-setup #54 (minimal 30 alokasi lintas enam status pada kedua tab dan 25 entri Changelog) dan Pre-setup #55 (alokasi dengan riwayat log lengkap, termasuk entri `Create` oleh `Dewi A` (Dewi Anggraini)) bersifat baca-saja untuk spec ini. Allocation ID alokasi Expired (tab History), alokasi tab Current, dan alokasi Pre-setup #55 dirujuk lewat `Fixture.license-allocation-license`. Changelog adalah audit trail permanen yang tumbuh; asersi isi hanya atas baris yang dijamin berada pada halaman teramati dengan Search Allocation ID seed (S-12, S-14).
- Kemampuan teknis: `Spectra.intercept()` atas respons list Changelog License Allocation di atas backend nyata (respons kosong untuk langkah 32); endpoint tidak tertulis di TC, kebutuhan intercept ditulis oleh tim FE (S-13). Intercept dilepas segera setelah dipakai (S-09). Membaca berkas hasil unduhan Changelog (hanya ada tidaknya entri alokasi) disediakan tim FE.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation pada tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### TC-AC-LA-354: Screening Modal Changelog

1. Klik ikon Changelog di toolbar tab Current
2. Verifikasi Header: judul `Changelog: License Allocation`
3. Verifikasi Header: tombol silang tampil
4. Verifikasi Header: toolbar `Search | Filter | Download` tampil
5. Verifikasi Body: kolom `Date (sortable)`, `Action (sortable)`, `Allocation ID (sortable)`, `Field (sortable)`, `Old Value (sortable)`, `New Value (sortable)`, `Modified By (sortable)`, dan `Column Visibility (⋯)`
6. Verifikasi urutan default Date Newest First
7. Verifikasi Footer: pagination default 10

### TC-AC-LA-355: Cakupan seluruh alokasi

8. Ketik Search `<Allocation ID alokasi Expired>` pada Search Changelog, tekan Enter
9. Verifikasi entri alokasi Expired (tab History) tampil
10. Ganti isi kotak search dengan `<Allocation ID alokasi tab Current>`, tekan Enter
11. Verifikasi entri alokasi tab Current tampil
12. Klik ikon panah `(←)` pada Search Changelog
13. Download as CSV pada Modal Changelog
14. Verifikasi berkas Changelog memuat entri alokasi Expired dan alokasi tab Current (scope sama dengan Changelog)

### TC-AC-LA-356: Format sel Changelog

15. Ketik Search `<Allocation ID alokasi Pre-setup #55>` pada Search Changelog, tekan Enter
16. Verifikasi sedikitnya satu baris tampil
17. Verifikasi baris Create: Old Value `—`
18. Verifikasi baris Create: Field `Allocation Details`
19. Hover nilai Modified By pada baris Create
20. Verifikasi Modified By `Dewi A`
21. Verifikasi tooltip `Dewi Anggraini`
22. Klik Allocation ID pada baris Create
23. Verifikasi Allocation ID teks biasa, tidak berupa link
24. Verifikasi Action dan nilai kolom ditulis sebagai teks biasa tanpa badge

### TC-AC-LA-359: Tutup Modal Changelog

25. Klik area backdrop
26. Verifikasi modal tidak tertutup
27. Klik `[×]`
28. Verifikasi modal tertutup
29. Klik ikon Changelog
30. Tekan `Esc`
31. Verifikasi modal tertutup

### TC-AC-LA-357: Empty state Modal Changelog

32. Pasang intercept respons list Changelog License Allocation: respons kosong
33. Klik ikon Changelog
34. Verifikasi Illustration tampil
35. Verifikasi Title `No changelog yet`
36. Verifikasi Description `Activities and changes will appear here.`
37. Klik `[×]` pada Modal Changelog
38. Lepas intercept respons list Changelog

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC dalam spec: TC-AC-LA-354, TC-AC-LA-355, TC-AC-LA-356, TC-AC-LA-359, TC-AC-LA-357, supaya intercept dibangun terakhir dan dilepas segera (S-09, S-10).
- Langkah `Download as CSV` berarti: klik ikon Download lalu pilih opsi dengan nama itu.
- Langkah penghubung (S-03): langkah 8, 10, 15 (Search untuk menemukan baris target, R-16), langkah 12 (menutup search bar), langkah 37 dan 38.
- Alasan spec melewati sekitar 35 langkah: semua blok satu topik (Modal Changelog) pada satu dataset baca-saja; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-AC-LA-357 mensyaratkan Principal baru tanpa entri Changelog, sedangkan Pre-setup #54 men-seed 25 entri Changelog pada scope Principal #1 dan Tabel Pre-setup TC tidak memuat tenant kosong; spec memakai respons list Changelog yang di-intercept kosong. Butuh keputusan QA: akun atau tenant kosong atau intercept.
  - TC-AC-LA-355 butir b ("Download Changelog mengikuti scope yang sama") tidak menyebut cara membuktikan scope; spec membaca berkas Changelog untuk entri alokasi Expired dan alokasi tab Current (kemampuan baca berkas disediakan tim FE).
  - TC-AC-LA-356 tidak menyebut Allocation ID entri Create oleh Dewi A; spec memakai alokasi Pre-setup #55 dan mengasumsikan entri `Create` oleh `Dewi A` ada pada alokasi itu.
  - TC-AC-LA-356 butir b ("Allocation ID teks biasa, tidak berupa link") tidak menyebut pengamatan klik; spec mengasersi klik tidak menavigasi atau membuka apa pun.
  - TC-AC-LA-354 baris Body menyebut `Column Visibility (⋯)` sebagai kolom; spec mengasersinya sebagai bagian daftar kolom apa adanya.
