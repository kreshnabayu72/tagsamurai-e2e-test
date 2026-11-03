---
id: TC-FA-RP-E2E-154-tab-total-control-isi-sel-dan-badge-1
title: "Tab Total Control: isi sel dan badge (1/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1014
  - TC-FA-RP-1022
  - TC-FA-RP-1023
coverage:
  web: automated
---

# Tab Total Control: isi sel dan badge (1/2)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #36 (Tab Total Control terisi sembilan baris), #37 (Tab Read Only empat baris), #22 (Custom Field aktif `Cost Center`, `Joined Date`, `Badge No` beserta nilai Ahmad Fauzi), dan #44 (Tantri Wijayanti, Active, Activated, tanpa Position, Division, TAG, dan nilai Custom Field; dijadikan Total Control lewat seed API hanya pada TC-FA-RP-1023).
- Kemampuan teknis (disediakan tim FE/BE): menetapkan Tantri Wijayanti sebagai Total Control dan melepasnya lewat sesi API aktor.
- Date Format General Settings (#34) tidak diubah spec ini; Last Updated diasersi mengikuti format yang berlaku.
- State yang diubah: konfigurasi kolom Setup Column Tab Total Control (disimpan di browser; hook `after` menghapus preferensi kolom di browser, bukan `[Reset to Default]`, kemampuan disediakan tim FE) dan penugasan Tantri Wijayanti sebagai Total Control (hook `after` melepasnya lewat sesi API).

## Test Steps

### Status badge Reflected tanpa aksi ubah status (TC-FA-RP-1014)

1. Klik Tab `Total Control`
2. Klik `[⋯]` pada baris Siti Rahayu (Status `Inactive`)
3. Verifikasi menu `[⋯]` hanya memuat `Remove`; tidak ada aksi mengaktifkan, menonaktifkan, atau mengubah status
4. Tutup menu dengan Esc
5. Klik badge `Inactive` pada baris Siti Rahayu
6. Verifikasi tidak ada toast yang muncul
7. Verifikasi tidak ada dialog yang terbuka
8. Verifikasi badge `Inactive` pada baris Siti Rahayu tidak berubah (status tidak berubah)

### Modified By dan Last Updated tidak pernah kosong (TC-FA-RP-1022)

9. Verifikasi Modified By baris Admin Utama bernilai `System`
10. Verifikasi Last Updated baris Admin Utama berisi tanggal dan jam pembuatan record sesuai Date Format General Settings, bukan `—`
11. Verifikasi sedikitnya satu baris selain Admin Utama tampil pada tabel (pembanding)
12. Verifikasi Modified By pada delapan baris lainnya berisi nama pelaku (mis. `Admin U`, `Siti R`, `Prasetyo H`)
13. Verifikasi Last Updated pada delapan baris lainnya berisi tanggal
14. Verifikasi tidak ada sel `—` pada kolom Modified By dan Last Updated delapan baris lainnya
15. Klik Tab `Read Only`
16. Verifikasi seluruh empat baris Tab Read Only berisi nama pelaku pada Modified By dan tanggal pada Last Updated
17. Verifikasi tidak ada sel `—` pada kolom Modified By dan Last Updated Tab Read Only
18. Klik Tab `Total Control`

### Nilai kosong tampil `—` (TC-FA-RP-1023)

19. Tetapkan Tantri Wijayanti sebagai Total Control lewat sesi API hingga tersimpan
20. Muat ulang halaman (F5)
21. Klik header `(⋯)` kolom Column Visibility, klik `Setup Column...`, centang `Temporary Until`, `TAG`, `Cost Center`, `Joined Date`, dan `Badge No`, lalu klik `[Save]`
22. Verifikasi sel Position, Division, Temporary Until, TAG, Cost Center, Joined Date, dan Badge No pada baris Tantri Wijayanti menampilkan `—` (em dash)
23. Verifikasi sel-sel itu bukan sel blank
24. Verifikasi sel-sel itu bukan teks `null`
25. Verifikasi sel TAG `TAG-1001`, Cost Center `CC-100`, Badge No `BN-77`, dan Joined Date baris Ahmad Fauzi terisi
26. Verifikasi tidak ada `—` pada kolom yang bernilai pada baris Ahmad Fauzi
27. Lepaskan Tantri Wijayanti dari Total Control lewat sesi API hingga tersimpan

## Notes

- Langkah penghubung (S-03, tanpa `Verifikasi`): klik tab (langkah 1, 15, 18); menutup menu dengan Esc (langkah 4); membuka Setup Column dan menyimpan kolom (langkah 21); memuat ulang halaman setelah seed (langkah 20).
- Langkah 11 adalah pembanding generik "sedikitnya satu baris" sebelum asersi universal (bagian 8b butir 2); ditambahkan spec, bukan dari Expected TC.
- Langkah 19 adalah seeding API sebagai precondition TC-FA-RP-1023 (Pre-setup #44), tidak diasersi; Tantri tidak ada di tabel saat TC-FA-RP-1014 dan TC-FA-RP-1022 berjalan sehingga "delapan baris lainnya" tetap benar. Langkah 27 melepasnya; hook `after` menjadi cadangan.
- Post Condition TC-FA-RP-1023 menyebut Setup Column dikembalikan lewat Reset to Default; spec memulihkan lewat hook `after` (menghapus preferensi kolom di browser, bagian 4 konvensi).
- Temuan untuk QA:
  - TC-FA-RP-1014 Expected b tidak menyebut cara membuktikan "tidak mengubah status"; spec mengamati badge `Inactive` tetap setelah klik.
  - TC-FA-RP-1022 Expected a hanya menyebut Last Updated "berisi tanggal dan jam" tanpa nilai persis; spec mengasersi hanya bahwa sel berisi tanggal dan jam dan bukan `—`.
  - Precondition TC-FA-RP-1014, TC-FA-RP-1022, dan TC-FA-RP-1023 menyebut Pre-setup #37 atau #22 yang tidak dipakai semua langkah; spec memakai #37 hanya pada TC-FA-RP-1022 dan #22 hanya pada TC-FA-RP-1023.
