---
id: TC-AC-CS-E2E-156-subscription-log-urutan-immutability-dan-edit-no-op
title: "Subscription Log: Urutan, Immutability, dan Edit No-Op"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-CS-609
coverage:
  web: automated
---

# Subscription Log: Urutan, Immutability, dan Edit No-Op

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Create-Only Distributor (Pre-setup #6) `createOnlySub_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`), password `Spectra.env.AC_SUB_CREATE_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, Pre-setup #1).
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.
- Data milik spec (S-06, S-12; bersuffix `+{runId}-156`), dibuat lewat sesi API aktor Create-Only di hook `before` dan dibersihkan di hook `after`: term `[Subscription ID term seed]` (setara Pre-setup #49: Client `Apotek Sehat Sentosa+{runId}-156`, FAMS, Growth, Waiting for Approval, milik `Fajar Nugroho`) dengan entri `Subscription created` dan satu entri `Subscription edited` (Duration `1` ke `2`) yang disiapkan di hook `before` (aksi pada kolom Dependensi TC-AC-CS-223; endpoint tulis tidak tertulis di TC, PRD, atau LLD sehingga disediakan tim FE/BE, lihat Temuan untuk QA). Spec ini mengubah Duration term seed dari `2` ke `3` lewat Edit UI; karena term itu milik spec, perubahan dan entri Subscription Log serta Changelog-nya ikut dibersihkan di hook `after` (tidak ada state global yang diubah).
- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor; membaca jumlah entri Subscription Log sebagai baseline.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09; flag Guided Tooltip diatur `seen`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-609: Subscription Log terbaru di atas, entri lama tidak berubah, Edit No-Op dan pembacaan tidak dicatat

1. Ketik Search `[Subscription ID term seed]`, tekan Enter
2. Klik ikon `⋯` pada baris `[Subscription ID term seed]`, klik `Subscription Log`
3. Catat seluruh entri Subscription Log (judul, Date & Time, dan baris Description) sebagai baseline
4. Klik `[✕]`
5. Klik ikon `⋯` pada baris `[Subscription ID term seed]`, klik `Edit`
6. Ubah Duration dari `2` menjadi `3`
7. Klik `[Save]`
8. Tunggu aksi selesai
9. Klik ikon `⋯` pada baris `[Subscription ID term seed]`, klik `Subscription Log`
10. Verifikasi entri baru `Subscription edited by Fajar Nugroho` dengan `Duration: 3 year(s)` muncul paling atas
11. Verifikasi entri lama (created dan edited sebelumnya) identik dengan baseline langkah 3
12. Klik `[✕]`
13. Catat jumlah entri Subscription Log sebagai baseline kedua
14. Klik ikon `⋯` pada baris `[Subscription ID term seed]`, klik `Edit`
15. Klik `[Save]` tanpa mengubah nilai
16. Verifikasi toast netral tampil
17. Klik `[✕]`
18. Klik ikon `⋯` pada baris `[Subscription ID term seed]`, klik `Subscription Log`
19. Verifikasi jumlah entri sama dengan baseline kedua (Edit tanpa perubahan tidak menambah entri)
20. Klik ikon Copy pada header modal
21. Verifikasi jumlah entri tetap sama dengan baseline kedua (pembukaan modal dan penyalinan Subscription ID tidak menambah entri)

## Notes

- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target, R-16), langkah 4, 12, dan 17 (menutup modal Subscription Log atau Edit), langkah 8 (tunggu aksi selesai, bagian 8b butir 8), dan langkah 13 (mencatat baseline).
- Temuan untuk QA:
  - TC-AC-CS-609 langkah 4 menyebut "toast netral" tanpa teks toast; spec memverifikasi toast netral tampil tanpa menyebut teksnya (S-02). Teks perlu dilengkapi QA.
  - TC-AC-CS-609 langkah 2 menyebut Edit tanpa nama row action dan alur setelah `[Save]` (kembali ke List atau Detail) tidak tertulis; spec memakai item `Edit` dan kembali ke List.
  - TC-AC-CS-609 Expected d tidak menyebut surface pembanding selain Subscription Log; spec hanya mengasersi jumlah entri Subscription Log.
  - Aksi pemicu Edit awal (Dependensi TC-AC-CS-223) tidak punya endpoint tulis di TC, PRD, atau LLD (S-13).
