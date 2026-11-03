---
id: TC-AC-LA-E2E-012-guided-tooltip-interupsi-keyboard-dan-halaman-lain
title: "Guided Tooltip: Resize, Target Permanen, Keyboard, dan Halaman Approvals"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-LA-51
  - TC-AC-LA-52
  - TC-AC-LA-53
  - TC-AC-LA-54
coverage:
  web: automated
---

# Guided Tooltip: Resize, Target Permanen, Keyboard, dan Halaman Approvals

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal (Pre-setup #1) `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun berikutnya (ganti akun dengan langkah eksplisit di Test Steps): Total Control Distributor (Pre-setup #10) `totalControlDistLic_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`), password `Spectra.env.AC_LA_TC_DIST_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.
- Kemampuan teknis (disediakan tim FE/BE): baca, hapus, dan setel flag `guided_tooltip_seen_ac-license-allocation-license` per akun; atur ukuran viewport browser. Flag disimpan per akun dan dibaca lewat kemampuan itu.
- Kemampuan teknis tambahan: `Spectra.intercept()` atas respons list License Allocation di atas backend nyata (respons kosong untuk TC-AC-LA-52); endpoint list tidak tertulis di TC dan ditulis tim FE (S-13). Intercept dilepas segera sesudah TC-AC-LA-52 (S-09).
- TC-AC-LA-54: flag seen halaman License Allocation untuk akun `totalControlDistLic` bernilai true sesuai hook `before` suite (tidak diubah spec).
- page_key walkthrough List: `ac-license-allocation-license`. Hook `after` memulihkan nilai awal flag dan ukuran viewport.
- Tabel parameter Target Step (langkah yang diulang per baris tabel pada TC-AC-LA-52):

| Step | Target |
|---|---|
| 1 | Tabs |
| 2 | Table |
| 3 | Breadcrumb |
| 4 | header kolom Status |
| 5 | ikon Changelog |

- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`). Flag Guided Tooltip `guided_tooltip_seen_ac-license-allocation-license` diatur spec ini sendiri sesudah hook suite (kemampuan baca dan setel flag disediakan tim FE/BE); hook `after` memulihkan nilai awal flag.

## Test Steps

### TC-AC-LA-51: Resize di tengah walkthrough menutup tanpa menyimpan flag seen

1. Hapus flag `guided_tooltip_seen_ac-license-allocation-license` akun `totalControlLic`
2. Klik menu `License Allocation` di sidebar hingga walkthrough tampil
3. Klik `[Next]` sekali
4. Verifikasi Step 2 tampil dengan indikator `Step 2 of 5`
5. Ubah ukuran viewport browser
6. Verifikasi walkthrough tertutup saat resize
7. Verifikasi flag seen tidak tersimpan untuk akun `totalControlLic`
8. Pulihkan ukuran viewport browser ke ukuran awal
9. Muat ulang halaman
10. Verifikasi walkthrough muncul lagi dari Step 1

### TC-AC-LA-52: Target walkthrough adalah elemen permanen dan satu halaman

11. Pasang intercept respons list License Allocation: respons kosong
12. Muat ulang halaman Allocation > License Allocation (flag seen belum ada, tabel kosong)
13. Verifikasi empty state tab Current tampil dengan Title `No current license allocations`
14. Verifikasi walkthrough menyorot elemen pada kolom Target baris tabel Step yang aktif (langkah 14 sampai 15 diulang untuk Step 1 sampai 4)
15. Klik `[Next]`
16. Verifikasi Step 5 menyorot ikon Changelog
17. Verifikasi walkthrough tidak berpindah halaman selama lima step
18. Verifikasi walkthrough tidak membuka dialog selama lima step
19. Klik `[Done]` dan lepas intercept respons list

### TC-AC-LA-53: Keyboard pada walkthrough

20. Hapus flag `guided_tooltip_seen_ac-license-allocation-license` akun `totalControlLic`
21. Klik tombol `[?]` di sebelah kanan Breadcrumb untuk memulai walkthrough
22. Tekan `Enter` di Step 1
23. Verifikasi walkthrough maju ke Step 2
24. Tekan panah kanan
25. Verifikasi walkthrough maju ke Step 3
26. Tekan panah kiri
27. Verifikasi walkthrough kembali ke Step 2
28. Tekan `Esc`
29. Verifikasi walkthrough tertutup
30. Verifikasi flag seen tersimpan untuk akun `totalControlLic`

### TC-AC-LA-54: Walkthrough hanya untuk halaman List

31. Ganti akun: Logout lalu login sebagai Total Control Distributor (`totalControlDistLic`)
32. Buka Admin Console > Approvals > License Allocation
33. Verifikasi halaman Approvals > License Allocation terbuka
34. Verifikasi walkthrough License Allocation tidak berjalan di halaman Approvals

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah hapus flag, langkah pasang dan lepas intercept, langkah memulihkan viewport, langkah `Klik [Next]` yang berpindah Step, langkah `Klik [Done]` yang menutup walkthrough sebelum TC berikutnya, dan ganti akun eksplisit (S-07).
- Spec ini sekitar 35 langkah dengan ekspansi (langkah 14 sampai 15 diulang empat kali); semua blok satu topik (Guided Tooltip List) dan berbagi satu flag. Asersi absence atas walkthrough di halaman Approvals memakai halaman Approvals yang sudah termuat sebagai anchor permukaan (bagian 8b butir 2).
- Walkthrough Approvals (page_key `ac-approvals`) diuji di TC modul Approvals dan tidak diasersi di spec ini.
- Akun `totalControlDistLic` (Pre-setup #10) dipakai untuk TC-AC-LA-54; akun pertama `totalControlLic`.
- Temuan untuk QA:
  - TC-AC-LA-52 mensyaratkan tabel kosong (empty state), sedangkan seed Pre-setup #54 men-seed minimal 30 alokasi pada scope akun; spec memakai respons list yang di-intercept kosong.
  - TC-AC-LA-51 Expected a (`Walkthrough tertutup saat resize tanpa menyimpan flag seen`) tidak memberi cara mengamati flag; spec memakai kemampuan baca flag yang disediakan tim FE/BE.
  - TC-AC-LA-51 langkah 2 tidak menyebut ukuran viewport tujuan; spec mengubah ukuran viewport dan memulihkannya sebagai langkah penghubung.
  - TC-AC-LA-54 langkah 1 tidak menyebut cara menuju Admin Console > Approvals > License Allocation; spec memakai menu sidebar Approvals.
