---
id: TC-GS-DIV-E2E-055-changelog-search-kolom-searchable-dan-kontrol
title: "Modal Changelog: Search Kolom Searchable dan Kontrol Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-193
  - TC-GS-DIV-194
  - TC-GS-DIV-225
coverage:
  web: automated
---

# Modal Changelog: Search Kolom Searchable dan Kontrol Search

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini (kredensial `Spectra.env.GS_TC_PASSWORD`); akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Halaman awal: Global Settings > User > Division.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Seeding minimal (S-11; lewat API oleh akun Sari Dewi di hook `before`, urutan sebagai berikut). Hanya dua Division milik spec ini yang dipakai `Verifikasi`, bernama bersuffix `{runId}-055`:
  - Hook `before` lebih dulu menghapus lewat API sisa Division run lama yang namanya bersuffix `-055` (termasuk yang Code-nya `ACC-055`, `PRC-055`, atau `PROC-055`), tanpa menghapus berdasarkan Code saja.
  - Seed `Accounting {runId}-055` (Code `ACC-055`) dan `Procurement {runId}-055` (Code `PRC-055`) oleh Sari Dewi (setara TC-GS-DIV-30). Tiap Create mencatat entri Changelog Action Create oleh `Sari D` (Old Value `—`).
  - Edit oleh Sari Dewi lewat API pada Division milik spec ini (setara TC-GS-DIV-101 dan TC-GS-DIV-102): Name `Accounting {runId}-055` diubah menjadi `Accounting and Tax {runId}-055`, dan Code `Procurement {runId}-055` diubah dari `PRC-055` menjadi `PROC-055` (entri Action Edit, Field `Division Name` dan `Code`, oleh `Sari D`). Entri ini dipakai TC-GS-DIV-193 (precondition d).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API Division yang dibuat spec ini (`Accounting and Tax {runId}-055` dan `Procurement {runId}-055`). Entri Changelog tidak bisa dihapus.
- Kapasitas: Master Data Count Limit environment automation cukup untuk Division Pre-setup (6) dan Division milik spec ini (disediakan tim FE).
- Kemampuan teknis: mengetik di kotak Search modal; menyalin teks sel kolom Date.
- Precondition TC-GS-DIV-193, 194, 225: login sebagai Total Control dan berada di Global Settings > User > Division; riwayat Changelog terisi. TC-GS-DIV-193 tambahan: entri hasil TC-GS-DIV-101 dan TC-GS-DIV-102 oleh `Sari D` tersedia.
- Suite serial (`parallel: false`) karena tabel Division dan Changelog dipakai bersama spec lain.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State global yang dipulihkan: tidak ada (spec hanya membaca).

## Test Steps

### TC-GS-DIV-225: Search Modal Changelog: reveal, auto-focus, submit lewat Enter, clear, dan collapse

1. Klik icon Changelog di Table Tools
2. Klik icon Search di modal
3. Verifikasi search bar melebar
4. Verifikasi kursor auto-focus pada input Search
5. Ketik `edit` pada input Search
6. Verifikasi tabel belum tersaring (baris Action `Create` masih tampil)
7. Verifikasi icon `(✕)` muncul
8. Tekan Enter
9. Verifikasi baris Action `Edit` tampil
10. Verifikasi tabel tersaring (baris Action `Create` tidak tampil)
11. Klik icon `(✕)`
12. Verifikasi input Search kosong
13. Verifikasi baris Action `Edit` tetap tampil
14. Verifikasi tabel tidak di-reset (baris Action `Create` tetap tidak tampil)
15. Tekan Enter pada input kosong
16. Verifikasi tabel di-reset (baris Action `Create` tampil kembali)
17. Ketik Search `edit`, tekan Enter
18. Klik icon panah `(←)`
19. Verifikasi search bar tertutup
20. Verifikasi tabel langsung di-reset (baris Action `Create` tampil kembali)

### TC-GS-DIV-193: Search Modal Changelog per kolom searchable (substring dan tanpa membedakan huruf besar kecil)

21. Ketik Search `edit` di modal, tekan Enter
22. Verifikasi Action: hasil memuat baris Action `Edit`
23. Ganti isi kotak search dengan `accounting and`, tekan Enter
24. Verifikasi Division Name: hasil memuat baris `Accounting and Tax {runId}-055`
25. Ganti isi kotak search dengan `code`, tekan Enter
26. Verifikasi Field: hasil memuat baris Field `Code`
27. Ganti isi kotak search dengan `prc`, tekan Enter
28. Verifikasi Old Value: hasil memuat baris Old Value `PRC-055`
29. Ganti isi kotak search dengan `proc`, tekan Enter
30. Verifikasi New Value: hasil memuat baris New Value `PROC-055`
31. Verifikasi hasil juga memuat baris Create `Procurement {runId}-055` (substring)
32. Ganti isi kotak search dengan `sari`, tekan Enter
33. Verifikasi Modified By: hasil memuat baris Modified By `Sari D`

### TC-GS-DIV-194: Kolom Date tidak dapat dicari lewat Search Modal Changelog

34. Salin teks tanggal pada kolom Date salah satu baris yang tampil (format yang tampil di kolom itu)
35. Ganti isi kotak search dengan teks tanggal yang disalin, tekan Enter
36. Verifikasi pesan `No results found`

## Notes

- Mode: FE+BE. Sumber: `global-settings/division/TestCases/tc-division.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-GS-DIV-225, 193, 194. Alasan: TC-GS-DIV-225 menguji kontrol Search dan hanya membaca (screening lebih dulu, bagian 3 konvensi); TC-GS-DIV-193 dan 194 memakai Search dengan beberapa kata kunci, dan TC-GS-DIV-194 di akhir karena memakai teks tanggal baris yang tampil. Modal Changelog dibuka sekali di langkah 1 untuk ketiga TC.
- Langkah penghubung: tidak ada langkah tanpa `Verifikasi` yang tidak berasal dari TC. Pada TC-GS-DIV-193 setiap kata kunci baru menggantikan kata kunci sebelumnya di input Search yang sama. Langkah 21 (langkah atomik "Ketik Search") membuka kembali Search yang ditutup `(←)` di langkah 18.
- Asersi memakai pola baris (bukan jumlah baris), sehingga entri Changelog dari run atau spec lain tidak memengaruhi hasil.
- Precondition TC menyebut Population dan Modified By `Sari D`, `Rina M`, `Agus W`, `Dewi L`; spec ini hanya men-seed `Accounting {runId}-055` dan `Procurement {runId}-055` oleh `Sari D`, yaitu data yang dipakai `Verifikasi` (S-11).
- Langkah 9 dan 13 `Verifikasi` baris Action `Edit` tampil adalah anchor positif untuk asersi ketiadaan baris Action `Create` (S-03, bagian 8b butir 2); Expected TC-GS-DIV-225 tidak memuatnya.
- Spec mencapai sekitar 35 langkah (36 langkah) karena tiap kata kunci TC-GS-DIV-193 memerlukan aksi Search dan `Verifikasi` sendiri (S-01); semua blok satu kelas harness (Search Modal Changelog), satu akun, dan satu dataset. Ketiga blok memakai Modal Changelog yang dibuka sekali di langkah 1.
- Temuan untuk QA: (1) TC-GS-DIV-194 Expected "penyaringan tanggal hanya lewat Filter Panel" adalah pernyataan perilaku yang tidak punya langkah observasi di TC; spec hanya mengasersi `No results found`, dan penyaringan Date lewat Filter diuji di spec 057. (2) TC-GS-DIV-225 Expected b/d tidak menyebut cara mengamati "tabel belum tersaring"; spec memakai ada atau tidaknya baris Action `Create` sebagai penanda.
