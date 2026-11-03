---
id: TC-AC-PF-E2E-224-resilience-create-dan-edit-default-plan-5xx-dan-tanpa-respons
title: "Resilience: Create dan Edit Default Plan Gagal 5xx dan Tanpa Respons"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PF-193
  - TC-AC-PF-717
  - TC-AC-PF-235
  - TC-AC-PF-719
coverage:
  web: automated
---

# Resilience: Create dan Edit Default Plan Gagal 5xx dan Tanpa Respons

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; TC mengasersi state backend).
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite). Kelas harness: b fault injection / resilience.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active). Tidak ada ganti akun di tengah spec.
- Data Pre-setup (hook `before`): Dataset Plan V2 (Pre-setup #47; default FAMS dengan 2 Paid aktif `Growth` v5 dan `Professional`, Free `Starter` sudah archived, satu slot Paid tersisa; SAMS belum memiliki default plan sehingga slot Free SAMS tersedia).
- Data dinamis milik spec (nama bersuffix, S-12): `Paket Gagal Default {runId}-224` (TC-AC-PF-193, tidak boleh terbentuk) dan `Supply Timeout {runId}-224` (TC-AC-PF-717). Hook `after` membersihkan plan yang terbentuk (archive lalu delete) lewat fixture BE; entri Changelog Default `Create` bersifat permanen.
- Baseline (dicatat di hook `before` lewat kemampuan baca fixture BE sebelum aksi pertama): Version `Growth` (`v5`).
- Pengecualian S-06/S-12 butir A-14: `Growth` v5 Pre-setup literal tanpa suffix menjadi target Edit yang digagalkan intercept; spec tidak mengubah data itu karena seluruh request gagal. Pemulihan Dataset lewat fixture BE yang idempoten (disediakan tim FE/BE) dijalankan di hook `before` dan `after`; suite berjalan serial.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): `Spectra.intercept` parsial atas respons Create Default Plan dan Save Edit Default Plan (endpoint diidentifikasi tim FE; tidak tercantum di sumber TC): (a) respons server error 5xx dan (b) respons tidak pernah diterima FE. Intercept dilepas segera setelah pemicu (S-09). Fixture BE untuk membaca daftar default plan dan Version serta membersihkan plan; sesi API aktor.
- Env var: hanya `Spectra.env.AC_TC_PASSWORD`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PF-193: Create Default Plan gagal 5xx: form tetap terbuka, input dipertahankan, tidak ada plan

1. Buka form New Default Plan
2. Pilih Product `FAMS`, pilih Pricing Type `Paid`, dan isi Plan Name `Paket Gagal Default {runId}-224`
3. Pasang intercept: respons Create Default Plan dijawab server error
4. Klik `[Submit]`
5. Lepas intercept
6. Verifikasi muncul toast error: "Error, failed to create plan."
7. Verifikasi form tetap terbuka
8. Verifikasi input dipertahankan: Product `FAMS`, Pricing Type `Paid`, dan Plan Name `Paket Gagal Default {runId}-224`
9. Verifikasi tombol `[Submit]` aktif kembali
10. Verifikasi (dibaca lewat fixture BE) tidak ada plan `Paket Gagal Default {runId}-224`

### TC-AC-PF-717: Create Default Plan tanpa respons (timeout atau jaringan terputus): toast Connection problem, form terbuka, input dipertahankan

11. Dismiss toast error
12. Pilih Product `SAMS`, pilih Pricing Type `Free`, dan ganti isi Plan Name dengan `Supply Timeout {runId}-224`
13. Pasang intercept: respons Create Default Plan tidak pernah diterima FE
14. Klik `[Submit]` dan tunggu sampai FE menampilkan kegagalan
15. Lepas intercept
16. Verifikasi muncul toast error: "Connection problem. Please try again."
17. Verifikasi form tetap terbuka
18. Verifikasi input dipertahankan: Product `SAMS`, Pricing Type `Free`, dan Plan Name `Supply Timeout {runId}-224`
19. Verifikasi tombol `[Submit]` aktif kembali untuk retry manual
20. Klik segmen Breadcrumb `Plans & Features`
21. Verifikasi dialog `Unsaved Changes` tampil
22. Klik `[Leave]`

### TC-AC-PF-235: Edit Default Plan gagal 5xx: form tetap terbuka dan versi tidak naik

23. Klik tab Default, lalu buka Overlay Row Action `Growth` → klik `Edit`
24. Ubah Group count menjadi `25`
25. Pasang intercept: respons Save Edit Default Plan dijawab server error
26. Klik `[Save]`
27. Lepas intercept
28. Verifikasi toast error: "Error, failed to update plan."
29. Verifikasi form tetap terbuka
30. Verifikasi input dipertahankan: Group count `25`
31. Verifikasi (dibaca lewat fixture BE) Version `Growth` tetap `v5`

### TC-AC-PF-719: Edit Default Plan tanpa respons (timeout atau jaringan terputus): toast Connection problem, form terbuka, input dipertahankan

32. Dismiss toast error
33. Pilih ulang Group count `25`
34. Pasang intercept: respons Save Edit Default Plan tidak pernah diterima FE
35. Klik `[Save]` dan tunggu sampai FE menampilkan kegagalan
36. Lepas intercept
37. Verifikasi muncul toast error: "Connection problem. Please try again."
38. Verifikasi form tetap terbuka
39. Verifikasi perubahan dipertahankan: Group count `25`
40. Verifikasi tombol `[Save]` aktif kembali untuk retry manual
41. Klik segmen Breadcrumb `Plans & Features`
42. Verifikasi dialog `Unsaved Changes` tampil
43. Klik `[Leave]`

## Notes

- Alasan di atas sekitar 35 langkah (43 langkah): keempat blok satu kelas harness (b, kegagalan atau tanpa respons yang dipaksakan pada form default plan), berdiri sendiri, dan tiap pasangan blok (5xx lalu tanpa respons) memakai form yang sama dengan input dipertahankan sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Pemecahan lebih lanjut menambah login, hook, dan seeding Dataset per spec.
- Penyimpangan urutan (S-10): urutan sourceTc mengikuti nomor TC; urutan langkah mengelompokkan Create lalu Edit dan tiap pasangan 5xx lalu tanpa respons pada form yang sama.
- Langkah penghubung (S-03): langkah 1 dan 23 membuka form yang dibutuhkan precondition (langkah 23 juga mengklik tab Default sebagai halaman tujuan sesudah `[Leave]`); langkah 11 dan 32 meng-dismiss toast error agar asersi toast berikutnya bukan toast lama (R-12); langkah 20 sampai 22 dan 41 sampai 43 menutup form dirty secara deterministik (S-08).
- Langkah 10 dan 31 membaca state data lewat fixture BE karena form masih terbuka; anchor positif untuk asersi tidak adanya plan (langkah 10) adalah toast error langkah 6.
- Plan Name memakai nama bersuffix `{runId}-224` (S-12) sebagai ganti `Paket Gagal Default` dan `Supply Timeout`.
- Temuan untuk QA:
  - TC-AC-PF-717: precondition menyebut Dataset Plan A, sedangkan TC-AC-PF-193 memakai Dataset Plan V2; spec memakai Dataset Plan V2 untuk seluruh blok karena SAMS tidak dipengaruhi perbedaan itu (Dataset Plan A dan V2 hanya berbeda pada FAMS).
  - TC-AC-PF-235 dan TC-AC-PF-719: nilai Group count tidak disebut; spec memakai `25`.
  - TC-AC-PF-717: TC tidak menyatakan apakah server menyimpan plan pada skenario "tanpa respons"; spec tidak mengasersi keberadaan `Supply Timeout {runId}-224`.
