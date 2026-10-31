---
id: TC-GS-GSET-E2E-045-multi-konteks-konkurensi-dua-admin-last-write-wins
title: "Dua admin"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-GSET-145
coverage:
  web: automated
---

# Dua admin

## Prerequisites

- Mode: FE+BE.
- Akun Sesi 1 (admin utama): Total Control, Budi Santoso (`Budi S`), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No 1), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi.
- Akun Sesi 2 (admin kedua): Total Control, Andi Wijaya (`Andi W`), `totalControlGlobalSettingsB_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No 2), kredensial `Spectra.env.GS_TCB_PASSWORD` (nama env baru). Hasil Save di sesi ini diasersi (toast dan tidak ada dialog konflik), sehingga Sesi 2 adalah sesi UI.
- Environment variable: `GS_TC_PASSWORD` dan `GS_TCB_PASSWORD`. Password tidak ditulis di spec atau fixture. Nama `GS_TCB_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example` (didaftarkan pada tahap script).
- Dua sesi browser (kelas multi-konteks): Sesi 1 dan Sesi 2 berjalan di konteks browser terpisah dengan sesi login sendiri. Keduanya login di hook `before` spec ini (seedSession, kredensial dari env var). Hook `after` menutup konteks Sesi 2 dan mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`). Hook `beforeEach` membuka Global Settings > General Settings di Sesi 1.
- Hook suite (flag Guided Tooltip `guided_tooltip_seen_gs-general-settings` untuk kedua akun dan pemulihan record ke baseline Pre-setup No 10): lihat `suite.md`, bagian Hook suite; spec ini tidak mengatur flag sendiri.
- Data: record General Settings Client A pada baseline Pre-setup No 10 (`IDR`, `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`, `30 minutes`). Nilai yang disimpan: Sesi 1 Session Idle Timeout `1 hour`; Sesi 2 Session Idle Timeout `4 hours`. Spec tidak membuat data dinamis.
- Baseline log (S-12): `{nSI0}` (jumlah hasil Search `Session Idle Timeout` pada Modal Changelog) dicatat pada langkah 2, sebelum Save pertama.
- Kemampuan teknis: dua konteks browser paralel dalam satu spec; langkah ditandai `[Sesi 1]` dan `[Sesi 2]`; membaca jumlah hasil Search pada Modal Changelog.
- State global yang diubah: Session Idle Timeout record General Settings Client A, dipulihkan oleh hook `after` dan `beforeEach` suite lewat PUT API. Entri Changelog bersifat audit trail permanen dan tidak dihapus. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-GSET-145: Dua admin menyimpan perubahan pada field yang sama, Save terakhir menimpa tanpa dialog konflik

1. [Sesi 2] Buka Global Settings > General Settings
2. [Sesi 1] Buka Modal Changelog, ketik Search `Session Idle Timeout`, tekan Enter, catat jumlah hasil sebagai `{nSI0}`, lalu tutup modal
3. [Sesi 1] Pilih Session Idle Timeout `1 hour`
4. [Sesi 1] Klik `[Save]`
5. [Sesi 1] Verifikasi toast sukses `Success, general settings has been saved.`
6. [Sesi 2] Tanpa memuat ulang halaman, pilih Session Idle Timeout `4 hours`
7. [Sesi 2] Klik `[Save]`
8. [Sesi 2] Verifikasi toast sukses `Success, general settings has been saved.`
9. [Sesi 2] Verifikasi tidak ada dialog konflik
10. [Sesi 1] Muat ulang halaman (F5)
11. [Sesi 1] Verifikasi Session Idle Timeout `4 hours` (Save terakhir menang)
12. [Sesi 1] Buka Modal Changelog, ketik Search `Session Idle Timeout`, tekan Enter
13. [Sesi 1] Verifikasi jumlah hasil Search `{nSI0}` + 2 (2 baris Field `Session Idle Timeout`, satu per Save)
14. [Sesi 1] Tutup Modal Changelog

## Notes

- Sumber TC: `global-settings/general-settings/TestCases/tc-general-settings.md` (TC-GS-GSET-145). Mode: FE+BE. Kelas: multi-konteks (dua admin, prinsip 13 butir c).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 2, 12, dan 14 (membuka halaman Sesi 2, mencatat baseline, dan membuka serta menutup Modal Changelog). Sesi 2 membuka halaman pada langkah 1, sebelum Save Sesi 1, sehingga form Sesi 2 tetap bernilai `30 minutes` (belum di-refresh, sesuai TC).
- Asersi toast Sesi 1 (langkah 5) dilakukan sebelum Sesi 2 bertindak, dan toast Sesi 2 (langkah 8) sebelum langkah berikutnya (asersi state sementara tepat waktu, bagian 8b butir 5).
- Asersi Changelog memakai selisih jumlah hasil Search terhadap baseline (S-12) dan tidak mengasersi isi Old Value atau New Value kedua baris karena Expected TC (butir d) hanya menyebut dua baris satu per Save.
- Dependensi TC-GS-GSET-145 adalah "-" pada TC.
- Temuan untuk QA:
  - TC-GS-GSET-145 tidak menyebut Old Value baris Save kedua (`1 hour` dari server atau `30 minutes` dari form yang basi); spec tidak mengasersinya.
