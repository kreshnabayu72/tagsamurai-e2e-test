---
id: TC-AC-PF-E2E-049-plan-name-create-custom-plan-batas-panjang-trim-emoji-dan-fallback-server
title: "Plan Name Create Custom Plan: Batas Panjang, Trim, Emoji, dan Fallback Server"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-PF-114
  - TC-AC-PF-115
  - TC-AC-PF-116
  - TC-AC-PF-121
  - TC-AC-PF-122
coverage:
  web: automated
---

# Plan Name Create Custom Plan: Batas Panjang, Trim, Emoji, dan Fallback Server

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Principal), akun #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.AC_TC_PASSWORD`); halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_ac-plans-features` true dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): sesi API aktor dan fixture backend idempoten untuk memulihkan Dataset Pre-setup dan menghapus plan buatan spec. General Settings (Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC) disiapkan fixture sebagai precondition TC dan tidak diubah spec.
- Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12): nilai Pre-setup dirujuk lewat kunci fixture yang dibuat tim FE; password dan token tidak ditulis di spec.
- Data Pre-setup: Dataset Plan A (default plan FAMS `Growth` aktif sebagai Template).
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup (`Growth`) dipakai apa adanya, hanya dibaca; pemulihan Dataset dijamin fixture backend idempoten yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` spec ini.
- Data Dinamis: Plan Name bersuffix `-{runId}-049`; Plan Name panjang dihitung termasuk suffix (R-06): 121 karakter pada TC-AC-PF-115 dan tepat 120 karakter pada TC-AC-PF-114. Plan yang tersimpan: nama 120 karakter dan `Paket Trim-{runId}-049`.
- Kemampuan teknis tambahan: tempel teks dari clipboard dan injeksi nilai langsung ke DOM field Plan Name (melewati filter keystroke FE) seperti yang dituliskan TC-AC-PF-121 dan TC-AC-PF-122.
- State global: Dataset Pre-setup bersama; suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Pembersihan: hook `after` menghapus plan buatan spec ini (nama bersuffix `-{runId}-049`) lewat fixture backend, memulihkan Dataset, dan mengembalikan sesi ke akun default suite.

## Test Steps

### Emoji diblok (TC-AC-PF-121)

1. Buka tab `Custom`, sub-tab `Active`
2. Klik `+ Custom Plan` pada toolbar
3. Klik field Plan Name lalu ketik `😊` dan tempel `Paket 🔥`
4. Verifikasi karakter emoji tidak pernah masuk ke field Plan Name (field kosong atau hanya `Paket `)
5. Verifikasi tidak ada pesan error di bawah field Plan Name
6. Kosongkan isi field Plan Name

### 121 karakter (TC-AC-PF-115)

7. Pilih Product `FAMS` dan Template `Growth`
8. Isi Plan Name 121 karakter: `Paket` diikuti huruf `a` sehingga total 121 karakter termasuk suffix `-{runId}-049`
9. Verifikasi pesan `Max. 120 characters` muncul langsung saat melebihi batas tanpa menunggu Submit
10. Klik `[Submit]`
11. Verifikasi Submit diblok dan form tetap terbuka tanpa berpindah ke Plan Detail (tidak ada plan baru)

### Fallback server (TC-AC-PF-122)

12. Injeksi nilai `Paket 😊-{runId}-049` langsung ke DOM field Plan Name (melewati filter keystroke FE)
13. Klik `[Submit]`
14. Verifikasi pesan inline `Plan name contains invalid characters` muncul
15. Verifikasi plan tidak tersimpan dan form tetap terbuka

### 120 karakter (TC-AC-PF-114)

16. Ganti isi Plan Name dengan 120 karakter: `Paket` diikuti huruf `a` sehingga total 120 karakter termasuk suffix `-{runId}-049`
17. Verifikasi tidak ada pesan `Max. 120 characters`
18. Klik `[Submit]`
19. Verifikasi plan tersimpan dan Plan Detail terbuka dengan judul memuat nama 120 karakter dan `– v1`

### Trim otomatis (TC-AC-PF-116)

20. Klik breadcrumb sub-tab `Active`
21. Klik `+ Custom Plan` pada toolbar
22. Pilih Product `FAMS` dan Template `Growth`
23. Isi Plan Name dengan 3 spasi di awal, `Paket Trim-{runId}-049`, dan 3 spasi di akhir
24. Verifikasi tidak ada pesan error panjang karakter
25. Klik `[Submit]`
26. Verifikasi Plan Detail menampilkan judul `Paket Trim-{runId}-049 – v1` tanpa spasi di ujung
27. Klik breadcrumb sub-tab `Active`, lalu ketik Search `Paket Trim-{runId}-049`, tekan Enter
28. Verifikasi baris list menampilkan `Paket Trim-{runId}-049` ter-trim

## Notes

- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 1, 6, 20, 27.
- Pengecualian `P-5`: TC-AC-PF-122 (fallback server, kelas a objek-uji ringan, tanpa harness eksternal dan tanpa state berat) berada di spec fungsional ini bersama TC-AC-PF-121 yang menguji field Plan Name yang sama; hanya satu TC objek-uji ringan di spec ini.
- Langkah penghubung: Search pada langkah akhir untuk menemukan baris target dan `Kosongkan isi field Plan Name` setelah TC-AC-PF-121 agar TC berikutnya tidak bergantung pada isi field sebelumnya; breadcrumb sub-tab `Active` membawa kembali ke daftar. Spec berakhir pada daftar tanpa form dirty.
- Urutan TC di spec: TC-AC-PF-121 lalu TC-AC-PF-115 dan TC-AC-PF-122 (penolakan) sebelum TC-AC-PF-114 dan TC-AC-PF-116 (tersimpan), mengikuti prinsip validasi diblokir sebelum aksi sukses (S-10).
- Temuan untuk QA: (1) TC-AC-PF-121 menggunakan Expected "field kosong atau hanya `Paket `" sehingga hasil pasti tempel emoji tergantung implementasi FE; spec mengasersi keduanya sebagai valid. (2) Post Condition TC-AC-PF-114 dan TC-AC-PF-116 menyebut Plan Name tersimpan tanpa langkah observasi tambahan selain Expected; tidak diasersi terpisah.
