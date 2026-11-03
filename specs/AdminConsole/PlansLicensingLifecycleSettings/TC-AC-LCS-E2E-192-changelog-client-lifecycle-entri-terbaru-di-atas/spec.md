---
id: TC-AC-LCS-E2E-192-changelog-client-lifecycle-entri-terbaru-di-atas
title: "Isi Entri Changelog Client Lifecycle: Entri Terbaru di Atas Setelah Save Baru pada Dataset L"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-438
coverage:
  web: automated
---

# Isi Entri Changelog Client Lifecycle: Entri Terbaru di Atas Setelah Save Baru pada Dataset L

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`), password `Spectra.env.AC_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif).
- Konfigurasi ketujuh tab pada nilai default (Pre-setup 7) dipulihkan lewat Fixture BE di hook `beforeEach` dan `after` suite (kemampuan disediakan tim FE/BE).
- Hook `before` men-seed Dataset L (27 entri Changelog tab Client Lifecycle, Pre-setup 8: entri ke-n pada n May 26 pukul 10:00, Action Edit, Old Value 5n, New Value 5n+3, Modified By berupa John Doe, Sarah Thompson, Budi Santoso) lewat Fixture BE (kemampuan disediakan tim FE/BE; menimpa riwayat tab itu sehingga total tepat 27); hook `after` mengembalikan dataset ke keadaan awal.
- Kemampuan teknis (disediakan tim FE/BE): Fixture BE untuk menimpa atau mengosongkan riwayat Changelog per tab, idempotent (Lampiran A-15; dinyatakan di `suite.md`).
- Jam server dan jam browser sinkron; Date entri baru dibandingkan dengan waktu Save dengan toleransi satu menit karena kolom Date berketelitian menit (S-12).
- Data uji: Grace Period Duration `20` (dari `30`).
- General Settings: Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC (tidak diubah spec ini).
- Data uji mengacu ke berkas `fixtures/lifecycle-settings.json` (`Fixture.lifecycleSettings.<kunci>`: nilai default tiap tab dan dataset Changelog).
- Konfigurasi Lifecycle Settings bersifat platform-wide dan Changelog bersifat permanen; suite berjalan serial (`parallel: false`).
- Env var: `AC_TC_PASSWORD` (password Total Control Admin Console, satu nama satu arti).

## Test Steps

### TC-AC-LCS-438: Modal Changelog Client Lifecycle menampilkan entri terbaru di atas setelah Save baru

1. Klik tab Client Lifecycle
2. Klik icon Changelog di pojok kanan atas panel tab Client Lifecycle
3. Tutup modal dengan `[✕]`
4. Ubah Grace Period Duration dari `30` menjadi `20`
5. Klik `[Save]`
6. Tunggu aksi Save selesai (state loading pada `[Save]` hilang)
7. Catat waktu sesudah Save selesai sebagai waktu Save
8. Klik icon Changelog di pojok kanan atas panel tab Client Lifecycle
9. Verifikasi baris 1: Date tanggal hari ini sesuai waktu Save, Action `Edit`, Field `Grace Period Duration`, Old Value `30`, New Value `20`, Modified By `Andi W`
10. Verifikasi footer `1–10 of 28`

## Notes

- Langkah penghubung: langkah 6 (menunggu Save selesai sebelum membuka modal, bagian 8b butir 8) dan pencatatan waktu Save.
- Pengecualian A-15: footer `1-10 of 28` diasersi sebagai angka absolut karena riwayat tab Client Lifecycle ditimpa lewat Fixture BE menjadi tepat 27 entri (Dataset L) di hook `before` sebelum modal dibuka, sehingga total sesudah satu Save adalah 28; hook `after` suite mengembalikan dataset Changelog.
- TC-AC-LCS-469 ada di spec 119 (`TC-AC-LCS-E2E-119-changelog-client-lifecycle-sembilan-entri`).
- Temuan untuk QA:
  - TC-AC-LCS-438: Expected tidak menyebut toast sukses sesudah `[Save]`; spec hanya menunggu aksi selesai tanpa asersi.
  - TC-AC-LCS-438: Post Condition "Satu entri baru pada Changelog Client Lifecycle" tidak punya langkah observasi tersendiri; Expected footer `1–10 of 28` menjadi observasinya.
