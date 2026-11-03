---
id: TC-FA-FAAM-E2E-243-sinkron-registrasi-aset-asset-name-menjadi-excess
title: "Sinkron Registrasi Aset: Asset Name yang Menjadi Excess Setelah Dipilih Ditolak Server saat Submit"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAM-675
coverage:
  web: automated
---

# Sinkron Registrasi Aset: Asset Name yang Menjadi Excess Setelah Dipilih Ditolak Server saat Submit

## Prerequisites

- Mode: FE+BE.
- Hook suite: login akun default, sesi API aktor, seed API per TC, dan pemulihan state global mengikuti `suite.md`.
- Akun aktor: Total Control pada client plan cap 4 (Tabel Data Uji Pre-setup No. 20b); email dan kredensial disediakan tim FE (Email akun ini tidak tertulis di Pre-setup TC; lihat Temuan untuk QA), `Spectra.env.FA_CAP4_TC_PASSWORD` (nama baru, didaftarkan di `spectra.config.ts` dan `.env.example` oleh pemilik repo). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Env var: `FA_CAP4_TC_PASSWORD`.
- Data Pre-setup (Pre-setup No. 20b, client dedicated; nama literal karena client dipakai satu TC ini saja): Asset Name `Race Alpha`, `Race Beta`, `Race Gamma`, `Race Delta` (urut pembuatan, `Race Delta` terbaru), cap plan 4. Hook `before` memastikan cap plan 4 dan hook `after` memulihkan cap 4 lewat seed API.
- Kemampuan teknis: menurunkan cap plan client dari 4 menjadi 3 lewat seed API hingga tersimpan; membuka Registrasi Aset dan Fixed Asset > Assets; membaca jumlah aset sebelum aksi.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): pulihkan cap plan 4 dan hapus aset yang mungkin terbuat lewat API.
- State global yang diubah: cap plan client Pre-setup No. 20b (dipulihkan seperti di atas). Suite berjalan serial (`parallel: false`).
- Precondition TC-FA-FAAM-675: login sebagai Total Control pada client plan cap 4.

## Test Steps

1. Buka Fixed Asset > Assets
2. Catat jumlah aset client sebagai baseline R
3. Buka Fixed Asset > Assets > Registration
4. Buka form Registrasi Aset
5. Pilih Asset Name `Race Delta`
6. Turunkan cap plan client dari 4 menjadi 3 lewat seed API hingga tersimpan sehingga `Race Delta` berstatus excess
7. Isi field wajib lain
8. Klik `[Submit]`
9. Verifikasi server menolak Submit dengan `422`
10. Verifikasi field Asset Name ter-clear di form Registrasi Aset
11. Buka Fixed Asset > Assets
12. Verifikasi jumlah aset client sama dengan baseline R pada langkah 2 (tidak ada aset baru yang dibuat)

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 1, 3, 11 (navigasi) dan langkah 2 (mencatat baseline).
- Pelaku perubahan state (cap plan) adalah seed API, bukan konteks UI kedua.
- Temuan untuk QA:
  - Pre-setup No. 20b tidak menyebut akun Total Control untuk client cap 4.
  - TC-FA-FAAM-675 butir a ("tidak ada aset baru yang dibuat") diasersi sebagai jumlah aset terhadap baseline, bukan absence murni.
  - TC-FA-FAAM-675 tidak menyebut field wajib Registrasi Aset yang diisi pada langkah 3; spec menulis "Isi field wajib lain" (kebutuhan disediakan tim FE).
