---
id: TC-GS-HHR-E2E-005-guided-tooltip-konten-navigasi-keyboard
title: "Guided Tooltip Halaman Handheld Reader: Konten Tiga Step, Navigasi Back di Step 1 dan 2, dan Navigasi Keyboard"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-23
  - TC-GS-HHR-28
  - TC-GS-HHR-30
coverage:
  web: automated
---

# Guided Tooltip Halaman Handheld Reader: Konten Tiga Step, Navigasi Back di Step 1 dan 2, dan Navigasi Keyboard

## Prerequisites

- Mode: FE+BE (backend nyata). Suite `parallel: false`.
- Akun aktor: Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup 1, Client A). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: kunjungan ke halaman Handheld Reader adalah pemicu auto-open Guided Tooltip, sehingga langkah buka ditulis di `## Test Steps` dan bukan di hook `beforeEach`.
- Guided Tooltip (page_key `gs-handheld-reader`): spec ini menguji flag `guided_tooltip_seen_gs-handheld-reader` sendiri, sehingga dikecualikan dari penyetelan true oleh hook suite `before` (lihat `suite.md`). Hook `before` mencatat nilai awal flag akun Total Control lalu mereset flag ke belum ada (precondition "flag belum pernah diset" TC-GS-HHR-23, 28, dan 30). Flag di-reset ulang sebagai langkah penghubung sebelum TC-GS-HHR-28 dan 30 karena TC sebelumnya menutup walkthrough dan menandai seen. Hook `after` memulihkan nilai awal flag. Mekanisme baca, reset, dan pemulihan flag disediakan tim FE/BE (tidak didefinisikan di TC, PRD, atau LLD).
- Data Pre-setup (Client A, plan Growth, General Settings `dd/MM/yy` 24-hour): Seed Reader A (DD-01 s.d. DD-10) dipulihkan fixture backend (disediakan tim FE) sebelum spec berjalan; spec tidak membaca atau mengubah isi baris. Data Dinamis: tidak ada.
- Kemampuan teknis: input keyboard (`Enter`, `→`, `←`, `Esc`); pembacaan fokus keyboard pada kotak tooltip; pembacaan state spotlight (elemen yang disorot); muat ulang halaman dengan `F5`.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan seperti di atas).

## Test Steps

### TC-GS-HHR-23: Isi tiga langkah Guided Tooltip halaman Handheld Reader

1. Buka Global Settings > Hardware > Handheld Reader lewat address bar
2. Amati walkthrough pada Step 1
3. Verifikasi Step 1 menyorot (spotlight) License Counter Cards
4. Verifikasi Step 1 judul `License Counter`
5. Verifikasi Step 1 deskripsi `Monitor the remaining handheld reader license quota.`
6. Klik `[Next]`
7. Verifikasi Step 2 menyorot (spotlight) tombol `[+ Activate Reader]`
8. Verifikasi Step 2 judul `Add Hardware`
9. Verifikasi Step 2 deskripsi `Start USB synchronization to activate a handheld reader.`
10. Klik `[Next]`
11. Verifikasi Step 3 menyorot (spotlight) header kolom `Device Name`
12. Verifikasi Step 3 judul `Reader Detail`
13. Verifikasi Step 3 deskripsi `Click a device name to view its usage, including the most recent scan.`
14. Verifikasi tombol `[Next]` pada Step 3 berubah menjadi `[Done]`
15. Klik `[Skip]` untuk menutup walkthrough
16. Reset flag `guided_tooltip_seen_gs-handheld-reader` akun Total Control ke belum ada

### TC-GS-HHR-28: Tombol Back tersembunyi di Step 1 dan kembali ke langkah sebelumnya dari Step 2

17. Buka Global Settings > Hardware > Handheld Reader lewat address bar
18. Amati tombol pada Step 1
19. Verifikasi Step 1 menampilkan tombol `[Skip]` dan `[Next]`
20. Verifikasi tombol `[Back]` Hidden pada Step 1
21. Klik `[Next]`
22. Verifikasi Step 2 menampilkan tombol `[Back]`
23. Klik `[Back]`
24. Verifikasi klik `[Back]` kembali ke Step 1 (judul `License Counter`)
25. Klik `[Skip]` untuk menutup walkthrough
26. Reset flag `guided_tooltip_seen_gs-handheld-reader` akun Total Control ke belum ada

### TC-GS-HHR-30: Keyboard pada walkthrough

27. Buka Global Settings > Hardware > Handheld Reader lewat address bar
28. Verifikasi tooltip box mendapat keyboard focus saat tampil
29. Tekan `Enter`
30. Verifikasi `Enter` berpindah ke Step 2 (judul `Add Hardware`)
31. Tekan `→`
32. Verifikasi `→` berpindah ke Step 3 (judul `Reader Detail`)
33. Tekan `←`
34. Verifikasi `←` kembali ke Step 2 (judul `Add Hardware`)
35. Tekan `Esc`
36. Verifikasi `Esc` menutup walkthrough
37. Muat ulang halaman dengan `F5`
38. Verifikasi License Counter Cards tampil
39. Verifikasi walkthrough tidak muncul otomatis (`Esc` menyetel flag)

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec mengikuti TC sumber (23, 28, 30). Tiap TC butuh flag belum ada sehingga flag di-reset sebagai langkah penghubung di akhir TC-GS-HHR-23 dan 28; TC-GS-HHR-30 menyetel flag lewat `Esc` dan dipulihkan hook `after`. Perilaku auto-open, Done, Skip, klik overlay, replay `[?]`, resize, dan navigasi keluar halaman diuji di spec 006 (TC-GS-HHR-24, 25, 26, 27, 29, 453); step yang dilewati (Read Only dan kolom `Device Name` tersembunyi) diuji di spec 007 (TC-GS-HHR-31, 32).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 15 dan 25 (klik `[Skip]` penutup walkthrough), langkah 16 dan 26 (reset flag), langkah 1, 17, dan 27 (membuka halaman lewat address bar sebagai pemicu auto-open; pada TC-GS-HHR-28 dan 30 langkah buka ini juga langkah TC), dan langkah 37 (muat ulang untuk mengamati efek `Esc` terhadap flag).
- TC-GS-HHR-30 Expected e ("`Esc` menutup walkthrough dan menyetel flag") tidak punya langkah observasi flag di TC; Verifikasi "menyetel flag" ditulis lewat muat ulang `F5` (langkah 37 sampai 39) mengikuti pola TC-GS-HHR-24 sampai 27. Langkah 38 (License Counter Cards tampil) adalah anchor positif absence walkthrough sesudah `F5` (konvensi bagian 8b butir 2) dan bukan asersi dari TC.
- TC-GS-HHR-23 tidak memuat langkah menutup walkthrough pada Step 3 (Expected d hanya menyatakan `[Next]` berubah menjadi `[Done]`); walkthrough ditutup dengan `[Skip]` (langkah 15) sebagai langkah penghubung.
- Spec melewati sekitar 35 langkah (39 langkah). Seluruhnya satu kelas (Guided Tooltip halaman Handheld Reader: konten dan navigasi), tiap blok TC berdiri sendiri karena flag di-reset sebelum tiap blok, dan kegagalan satu blok tidak menghilangkan makna blok lain.
- Temuan untuk QA:
  - TC-GS-HHR-23, 28, dan 30 mensyaratkan flag belum pernah diset tanpa menyebut cara mereset; mekanismenya disediakan tim FE/BE.
  - TC-GS-HHR-23 Expected a sampai c tidak menyebut indikator "Step N of M"; spec tidak mengasersi indikator dan memakai judul step sebagai penanda posisi.
  - TC-GS-HHR-30 Expected e tidak punya langkah observasi flag; spec menambah langkah muat ulang (lihat Notes).
