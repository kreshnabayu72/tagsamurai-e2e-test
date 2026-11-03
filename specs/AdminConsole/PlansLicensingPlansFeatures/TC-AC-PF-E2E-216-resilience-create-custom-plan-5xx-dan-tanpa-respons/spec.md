---
id: TC-AC-PF-E2E-216-resilience-create-custom-plan-5xx-dan-tanpa-respons
title: "Resilience: Create Custom Plan Gagal 5xx, Tanpa Respons, dan Retry Setelah Timeout"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PF-164
  - TC-AC-PF-165
  - TC-AC-PF-716
coverage:
  web: automated
---

# Resilience: Create Custom Plan Gagal 5xx, Tanpa Respons, dan Retry Setelah Timeout

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; TC mengasersi state backend).
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite). Kelas harness: b fault injection / resilience.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active). Tidak ada ganti akun di tengah spec.
- Data Pre-setup (hook `before`): Dataset Plan A (Pre-setup #21; default `Growth` sebagai Template) dan Dataset Plan V2 (Pre-setup #47; default FAMS dengan 2 Paid aktif `Growth` dan `Professional`, Free `Starter` sudah archived, satu slot Paid tersisa).
- Data dinamis milik spec (nama bersuffix, S-12): `Paket Gagal {runId}-216` (TC-AC-PF-164, tidak boleh terbentuk), `Paket Timeout Dua {runId}-216` (TC-AC-PF-716), dan `Paket Timeout {runId}-216` (TC-AC-PF-165, tersimpan oleh server). Hook `after` membersihkan plan yang terbentuk (archive lalu delete) lewat fixture BE; entri Changelog Custom `Create` bersifat permanen.
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): `Spectra.intercept` parsial atas respons Create Custom Plan (endpoint diidentifikasi tim FE; tidak tercantum di sumber TC): (a) respons server error 5xx, (b) respons tidak pernah diterima FE, dan (c) respons tidak diteruskan ke FE sementara request tetap sampai ke server dan tersimpan. Intercept dilepas segera setelah pemicu (S-09). Fixture BE untuk membaca daftar custom plan dan membersihkan plan; sesi API aktor.
- Pengecualian S-06/S-12 butir A-14: nama Plan Pre-setup literal tanpa suffix (`Growth` sebagai Template) dipakai; spec hanya membaca data itu. Pemulihan Dataset lewat fixture BE yang idempoten dijalankan di hook `before` dan `after`; suite berjalan serial.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Jeda nyata: langkah 7 menunggu 6 detik tanpa men-dismiss toast error (batas 30 detik); jeda ini objek uji TC-AC-PF-164.
- Env var: hanya `Spectra.env.AC_TC_PASSWORD`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PF-164: Create Custom Plan gagal 5xx: form tetap terbuka, input dipertahankan, tombol aktif kembali, tidak ada plan

1. Klik tab Custom, lalu buka form New Custom Plan
2. Isi Product `FAMS`, Template `Growth`, dan Plan Name `Paket Gagal {runId}-216`
3. Pasang intercept: respons Create Custom Plan dijawab server error
4. Klik `[Submit]`
5. Lepas intercept
6. Verifikasi muncul toast error: "Error, failed to create plan."
7. Verifikasi toast error tetap tampil setelah 6 detik tanpa di-dismiss
8. Verifikasi form tetap terbuka
9. Verifikasi seluruh input dipertahankan: Product `FAMS`, Template `Growth`, dan Plan Name `Paket Gagal {runId}-216`
10. Verifikasi tombol `[Submit]` aktif kembali
11. Verifikasi (dibaca lewat fixture BE) tidak ada plan `Paket Gagal {runId}-216`

### TC-AC-PF-716: Create Custom Plan tanpa respons (timeout atau jaringan terputus): toast Connection problem, form terbuka, input dipertahankan

12. Dismiss toast error
13. Ganti isi Plan Name dengan `Paket Timeout Dua {runId}-216`
14. Pasang intercept: respons Create Custom Plan tidak pernah diterima FE
15. Klik `[Submit]` dan tunggu sampai FE menampilkan kegagalan
16. Lepas intercept
17. Verifikasi muncul toast error: "Connection problem. Please try again."
18. Verifikasi form tetap terbuka
19. Verifikasi seluruh input dipertahankan: Product `FAMS`, Template `Growth`, dan Plan Name `Paket Timeout Dua {runId}-216`
20. Verifikasi tombol `[Submit]` aktif kembali untuk retry manual

### TC-AC-PF-165: Create Custom Plan timeout lalu retry manual tidak menghasilkan plan ganda berkat keunikan nama

21. Dismiss toast error
22. Ganti isi Plan Name dengan `Paket Timeout {runId}-216`
23. Pasang intercept: respons Create Custom Plan pertama tidak pernah diterima FE sementara request sampai ke server dan tersimpan
24. Klik `[Submit]` dan tunggu sampai FE menampilkan kegagalan
25. Lepas intercept
26. Klik `[Submit]` lagi
27. Verifikasi retry ditolak dengan pesan `Plan name already exists` (tidak membuat plan kedua)
28. Klik segmen Breadcrumb `Plans & Features`
29. Verifikasi dialog `Unsaved Changes` tampil
30. Klik `[Leave]`
31. Klik tab Custom
32. Ketik Search `Paket Timeout {runId}-216`, tekan Enter
33. Verifikasi list tab Custom hanya memuat satu baris `Paket Timeout {runId}-216`
34. Klik `(←)` pada kotak Search

## Notes

- Penyimpangan urutan (S-10): TC-AC-PF-716 ditulis sebelum TC-AC-PF-165 karena TC-AC-PF-165 membuat plan yang tersimpan di server; form yang sama dipakai berulang dengan input dipertahankan (bagian 3 prinsip 13, halaman yang sama dipakai berulang) dan baru ditutup di langkah 28 sampai 30.
- Langkah penghubung (S-03): langkah 1 mengarahkan layar ke tab Custom; langkah 12 dan 21 meng-dismiss toast error agar asersi toast berikutnya bukan toast lama (R-12); langkah 31 dan 32 menemukan baris target (R-16); langkah 34 mengosongkan Search.
- Langkah 11 membaca daftar custom plan lewat fixture BE (state data) dengan anchor positif toast error langkah 6; layar form masih dirty sehingga list UI tidak dibuka sebelum langkah 28.
- Plan Name memakai nama bersuffix `{runId}-216` (S-12) sebagai ganti `Paket Gagal`, `Paket Timeout Dua`, dan `Paket Timeout`.
- Temuan untuk QA:
  - TC-AC-PF-164 dan TC-AC-PF-165: langkah "Isi Product, Template, dan Plan Name" tidak menyebut nilai Product dan Template; spec memakai Product `FAMS` dan Template `Growth` (konsisten dengan TC-AC-PF-569 dan TC-AC-PF-801).
  - TC-AC-PF-165: precondition "respons Create pertama tidak pernah diterima FE tetapi server sudah menyimpan" mensyaratkan intercept yang meneruskan request tetapi menahan respons; mekanisme itu tidak dijelaskan di TC dan disediakan tim FE/BE.
  - TC-AC-PF-716: TC tidak menyatakan apakah server menyimpan plan pada skenario "tanpa respons"; spec tidak mengasersi keberadaan `Paket Timeout Dua {runId}-216`.
