---
id: TC-AC-CS-E2E-143-klik-ganda-cancel-request-dan-save-edit-state-submitting-save
title: "Klik Ganda Cancel Request dan Save Edit, State Submitting Save"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-CS-525
  - TC-AC-CS-526
  - TC-AC-CS-238
coverage:
  web: automated
---

# Klik Ganda Cancel Request dan Save Edit, State Submitting Save

## Prerequisites

- Mode: FE+BE. Respons endpoint ditahan (delay) lewat `Spectra.intercept()` di atas backend nyata untuk mengamati state submitting; penahanan respons bukan kelas fault injection (bagian 3 prinsip 13b).
- Akun aktor: Create-Only Distributor (Pre-setup #6) `createOnlySub_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`, requester), password `Spectra.env.AC_SUB_CREATE_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, Pre-setup #1).
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.
- State global: toggle Require Approval for Allocation PT Maju Bersama diatur ON oleh fixture backend yang disediakan tim FE/BE di hook `before` dan dipulihkan di hook `after` (S-06, pengecualian 2026-10-30). Suite berjalan serial.
- Data milik spec, dibuat lewat API di hook `before` dan dibersihkan di hook `after` (S-06, S-12; bersuffix `+{runId}-143`): pengajuan Waiting for Approval `W525`, `W526`, dan `W238` (masing-masing Subscription ID dibaca lewat API seeding) milik `Fajar Nugroho` (setara `SUBS-20260819-00001`, Pre-setup #49: Client Apotek Sehat Sentosa, FAMS, Growth, Plan Owner PT Maju Bersama) dengan Duration awal `1` untuk `W526` dan `W238`. Jumlah entri log Action berawalan `Edit` pada `W526` dan Reserve Wallet pengajuan dicatat sebagai baseline sebelum langkah pertama (S-12).
- Kemampuan teknis (disediakan tim FE/BE): menahan dan melepas respons endpoint Cancel Request dan Save Edit lewat `Spectra.intercept()` (path tidak tertulis di TC, PRD, atau LLD, S-13); klik dua kali cepat (dua klik terkirim) oleh runner; membaca Reserve Wallet, status pengajuan, dan entri log sebagai state data.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09; flag Guided Tooltip diatur `seen`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-525: Klik ganda Cancel Request

1. Tahan respons endpoint Cancel Request lewat `Spectra.intercept()`
2. Ketik Search `W525`, tekan Enter
3. Klik ikon `⋯` pada `W525`, klik `Cancel Request` (dialog terbuka)
4. Klik tombol `[Cancel Request]` dua kali cepat
5. Lepas tahanan respons
6. Verifikasi dialog Cancel Request tertutup (respons selesai diproses)
7. Verifikasi hanya satu pembatalan diproses untuk `W525` dan Reserve dilepas sekali
8. Verifikasi re-cancel tidak mengubah status (status `W525` hanya berubah satu kali ke Canceled)

### TC-AC-CS-526: Klik ganda Save pada Edit

9. Tahan respons endpoint Save Edit lewat `Spectra.intercept()`
10. Ganti isi kotak search dengan `W526`, tekan Enter
11. Klik ikon `⋯` pada `W526`, klik `Edit`, ubah Duration `1` menjadi `2`
12. Klik tombol `[Save]` dua kali cepat
13. Lepas tahanan respons
14. Verifikasi modal Edit tertutup (respons selesai diproses)
15. Verifikasi hanya satu Edit diproses dan hanya satu entri log Action berawalan `Edit` per field yang berubah
16. Verifikasi Reserve disesuaikan sekali

### TC-AC-CS-238: Save memasuki state submitting dan menonaktifkan kontrol

17. Tahan respons endpoint Save Edit lewat `Spectra.intercept()`
18. Ganti isi kotak search dengan `W238`, tekan Enter
19. Klik ikon `⋯` pada `W238`, klik `Edit` (modal Edit Subscription terbuka ter-isi dari record)
20. Ubah Duration menjadi `2`, klik `[Save]`
21. Verifikasi `[Save]` menampilkan loading dan Disabled
22. Verifikasi input, `[Clear Field]`, dan `[✕]` Disabled selama permintaan berjalan
23. Lepas tahanan respons
24. Verifikasi modal tertutup
25. Verifikasi toast sukses tampil

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. TC-AC-CS-524, 527, dan 267 (klik ganda Cancel Subscription dan Convert) ada di spec 142.
- Langkah penghubung (S-03): langkah 5, 13, 23 (melepas tahanan respons). Asersi state sementara (loading, Disabled) pada langkah 21 dan 22 diletakkan sebelum respons dilepas (bagian 8b butir 5).
- Langkah 6, 14, dan 24 adalah anchor bahwa respons sudah diproses sebelum membaca hasil (bagian 8b butir 11).
- Temuan untuk QA:
  - TC-AC-CS-238 Expected c menyebut "toast sukses" tanpa teks; hanya kehadiran toast diasersi (S-02).
  - TC-AC-CS-525 dan 526 memakai istilah "tombol konfirmasi" tanpa label; spec memakai `[Cancel Request]` (sesuai TC-AC-CS-277) dan `[Save]`.
  - TC-AC-CS-525, 526, 238 memakai record Pre-setup (#49) sebagai target aksi tulis; spec memakai record milik spec (S-06).
  - TC-AC-CS-526 Expected a ("hanya satu entri log ... per field yang berubah") tidak menyebut surface log; spec memakai selisih jumlah entri yang dibaca fixture BE.
