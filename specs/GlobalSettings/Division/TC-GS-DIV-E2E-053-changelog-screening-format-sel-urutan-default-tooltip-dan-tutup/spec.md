---
id: TC-GS-DIV-E2E-053-changelog-screening-format-sel-urutan-default-tooltip-dan-tutup
title: "Modal Changelog: Screening, Format Sel, Urutan Default, Tooltip Toolbar, Nilai Panjang, dan Tutup"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-188
  - TC-GS-DIV-189
  - TC-GS-DIV-190
  - TC-GS-DIV-224
  - TC-GS-DIV-211
  - TC-GS-DIV-230
coverage:
  web: automated
---

# Modal Changelog: Screening, Format Sel, Urutan Default, Tooltip Toolbar, Nilai Panjang, dan Tutup

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini (kredensial `Spectra.env.GS_TC_PASSWORD`); akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Halaman awal: Global Settings > User > Division.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Seeding minimal (S-11; lewat API oleh akun Sari Dewi di hook `before`, urutan sebagai berikut). Hanya data yang dipakai `Verifikasi` yang di-seed: satu entri Action Create (Old Value `—`, Modified By `Sari D`), satu entri Action Delete (New Value `—`), dan entri Create Division 120 karakter. Urutan Date descending (TC-GS-DIV-190, langkah 14 dan 15) diasersi pada entri dengan Date menit berbeda. Jaminan dua nilai Date berbeda (Date berketelitian menit, S-12) berlaku tanpa syarat: hook `before` mencatat menit saat seeding dimulai, menjalankan seeding Division 120 karakter (dilewati bila sudah ada; entri Create lamanya tidak dipakai sebagai entri pertama), lalu selalu menjeda sampai menit berganti (jeda maksimum 60 detik; pengecualian atas jeda pendek karena Date berketelitian menit; bagian hook dan bukan langkah `Tunggu N detik`), baru kemudian seeding `Log Del Div` dibuat; jeda tetap dijalankan juga bila Division 120 karakter sudah ada. Dengan demikian ada minimal dua entri Changelog dengan Date menit berbeda (entri Create Division 120 karakter, lama atau baru, lebih awal dari entri Create dan Delete `Log Del Div`).
  - Division 120 karakter D-03 (setara TC-GS-DIV-37): Name `Divisions of Corporate Strategy and Long Range Planning for Regional Expansion and Partnership Development Programs APAC`, Code `LONG120`. Nama literal 120 karakter tanpa suffix per run karena suffix melampaui batas 120 karakter (pengecualian S-12 untuk Division D-03: seeding idempotent, dilewati bila sudah ada; cleanup hanya menghapus yang dibuat spec ini; suite serial). Pembuatan mencatat entri Changelog Action Create oleh `Sari D` (Old Value `—`).
  - Division pembantu `Log Del Div {runId}-053` dibuat lalu dihapus oleh Sari Dewi (entri Action Delete, New Value `—`), dilakukan sesudah seeding Division 120 karakter dan sesudah jeda pergantian menit di atas, supaya entri Create dan Delete tersebut menjadi entri terbaru dengan Date berbeda dari entri Create Division 120 karakter.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API Division 120 karakter bila dibuat spec ini. Entri Changelog tidak bisa dihapus.
- Kapasitas: Master Data Count Limit environment automation cukup untuk Division Pre-setup (6) dan Division milik spec ini (disediakan tim FE).
- Kemampuan teknis: hover (tooltip); mengklik area gelap di luar modal; membaca format tanggal dan jam General Settings yang berlaku di Client A (spec tidak mengubahnya).
- Precondition TC-GS-DIV-188, 189, 190, 224, 211, 230: login sebagai Total Control dan berada di Global Settings > User > Division; riwayat Changelog Division terisi (Create, Edit, Delete oleh `Sari D`). TC-GS-DIV-230 tambahan: Division 120 karakter sudah dibuat.
- Suite serial (`parallel: false`) karena Division D-03 bernama literal dan dipakai bersama spec lain.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State global yang dipulihkan: tidak ada (spec hanya membaca).

## Test Steps

### TC-GS-DIV-188: Screening Modal Changelog: Division

1. Klik icon Changelog di Table Tools
2. Verifikasi bagian Header: Title `Changelog: Division`
3. Verifikasi bagian Header: icon close `[✕]`
4. Verifikasi bagian Header: Toolbar `Search | Filter | Download`
5. Verifikasi bagian Body: kolom `Date (sortable) | Action (sortable) | Division Name (sortable) | Field (sortable) | Old Value (sortable) | New Value (sortable) | Modified By (sortable) | Actions (⋯) (unsortable)`
6. Klik header kolom `Actions (⋯)` Modal Changelog
7. Verifikasi bagian Body: overlay Column Visibility terbuka
8. Verifikasi bagian Body: overlay memuat item `Setup Column...`
9. Tutup overlay Column Visibility
10. Verifikasi bagian Body: tidak ada kolom checkbox
11. Verifikasi bagian Body: tidak ada row action
12. Verifikasi bagian Body: Filter Panel tersembunyi secara default
13. Verifikasi bagian Footer: Pagination default 10 data per halaman

### TC-GS-DIV-190: Urutan default Modal Changelog adalah tanggal terbaru di atas

14. Verifikasi baris terurut Date descending (terbaru di atas)
15. Verifikasi ikon sort kolom Date menunjukkan Newest First

### TC-GS-DIV-189: Format isi sel Modal Changelog: strip, nama singkat, dan hover Modified By

16. Verifikasi Old Value pada baris Action Create tampil `—`
17. Verifikasi New Value pada baris Action Delete tampil `—`
18. Verifikasi Modified By tampil `Sari D`
19. Hover `Sari D` pada kolom Modified By
20. Verifikasi Tooltip `Sari Dewi`
21. Verifikasi kolom Action tampil sebagai teks biasa (bukan badge)
22. Verifikasi Date tampil memakai format tanggal General Settings
23. Verifikasi Date tampil memakai format jam General Settings

### TC-GS-DIV-224: Hover icon toolbar Modal Changelog menampilkan tooltip

24. Hover icon Search
25. Verifikasi Tooltip `Search`
26. Hover icon Filter
27. Verifikasi Tooltip `Filter`
28. Hover icon Download
29. Verifikasi Tooltip `Download`

### TC-GS-DIV-230: Nilai panjang pada kolom Old Value dan New Value tampil penuh

30. Ketik Search `Divisions of Corporate Strategy and Long Range Planning for Regional Expansion and Partnership Development Programs APAC` di modal, tekan Enter
31. Verifikasi baris Action Create dengan Division Name 120 karakter tampil
32. Verifikasi Division Name tampil utuh tanpa pemotongan `..`
33. Verifikasi New Value tampil utuh tanpa pemotongan `..`
34. Verifikasi kolom melebar atau teks wrap natural mengikuti isi
35. Klik icon panah `(←)` untuk menutup Search

### TC-GS-DIV-211: Modal Changelog ditutup lewat icon close dan klik di luar modal

36. Klik icon `[✕]`
37. Verifikasi modal Changelog tertutup lewat icon close
38. Klik icon Changelog di Table Tools
39. Klik area gelap di luar modal
40. Verifikasi modal Changelog tertutup lewat klik di luar modal

## Notes

- Mode: FE+BE. Sumber: `global-settings/division/TestCases/tc-division.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-GS-DIV-188, 190, 189, 224, 230, 211. Alasan: screening (188) di awal, urutan default (190) diamati sebelum ada sort, TC-GS-DIV-230 memakai Search sehingga sesudah TC tanpa aksi, dan kasus menutup modal (211) di akhir (bagian 3 konvensi). Modal Changelog dibuka sekali di langkah 1 dan dipakai berurutan; langkah Changelog di TC-GS-DIV-189, 190, 224, dan 230 sudah terpenuhi oleh langkah 1.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 9 (menutup overlay Column Visibility sesudah asersi langkah 7 dan 8) dan langkah 35 (menutup Search agar tabel kembali tanpa saringan). Langkah 6 (klik header `Actions (⋯)`) adalah aksi yang membuka overlay pada Expected b.ii TC-GS-DIV-188. Langkah 30 (Search nama Division 120 karakter) adalah cara TC-GS-DIV-230 mencari entri Create Division 120 karakter.
- Asersi pada spec ini tidak menghitung jumlah baris, sehingga entri Create/Delete bernama sama dari run atau spec lain tidak memengaruhi hasil. Division 120 karakter bernama literal sesuai Tabel Data Uji Dinamis (D-03); spec Changelog lain men-seed Division yang sama secara idempotent.
- Langkah 31 (baris Action Create Division 120 karakter tampil) adalah anchor positif untuk asersi langkah 32 sampai 34 (S-03, bagian 8b butir 2); Expected TC-GS-DIV-230 tidak memuatnya.
- Format tanggal General Settings yang diubah (bukan format yang berlaku) diuji di spec 052; langkah 22 dan 23 hanya memeriksa bahwa Date mengikuti format tanggal dan jam yang berlaku di Client A.
- Precondition TC menyebut Population, entri Edit, dan Modified By `Sari D`, `Rina M`, `Agus W`, `Dewi L`; spec ini hanya men-seed entri yang dipakai `Verifikasi` (Create, Delete, Division 120 karakter, semua oleh `Sari D`, S-11).
- Spec melewati sekitar 35 langkah (40 langkah) karena tiap klausa Expected TC-GS-DIV-188 dan TC-GS-DIV-189 menjadi satu `Verifikasi` (S-01); semuanya satu kelas harness (screening satu Modal Changelog), satu akun, dan satu dataset. Blok 188, 190, 189, 224, dan 230 memakai Modal Changelog yang dibuka sekali di langkah 1; hanya blok 211 membuka modal sendiri.
- Temuan untuk QA:
  - TC-GS-DIV-189 Expected e tidak menyebut format tanggal dan jam konkret; spec mengasersi kesesuaian dengan format General Settings yang berlaku dan cara membaca format itu disediakan tim FE.
  - TC-GS-DIV-230 langkah 2 "Cari entri Create Division 120 karakter" tidak menyebut caranya; spec memakai Search nama utuh.
  - Date pada Modal Changelog berketelitian menit, sehingga entri seeding bisa memiliki Date yang sama; hook `before` menjamin minimal dua entri dengan Date menit berbeda (Create Division 120 karakter, lalu jeda sampai menit berganti, lalu Create dan Delete `Log Del Div`) sebelum urutan Date descending diasersi; urutan antar-entri bernilai sama tidak teramati.
