---
id: TC-GS-HHR-E2E-011-capability-dicabut-saat-aksi-berjalan
title: "Capability Manage hardware Dicabut Saat Sesi Berjalan: Aksi Tulis Ditolak Server dan UI Di-refresh"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-HHR-50
coverage:
  web: automated
---

# Capability Manage hardware Dicabut Saat Sesi Berjalan: Aksi Tulis Ditolak Server dan UI Di-refresh

## Prerequisites

- Mode: FE+BE. Kelas harness: multi-konteks (kelas c, perubahan izin di tengah aksi). Suite `parallel: false`.
- Flag Guided Tooltip halaman Handheld Reader: diatur hook suite untuk akun aktor spec ini (lihat `suite.md`, Hook suite).
- Akun aktor (Tabel Data Uji Pre-setup #5, Client A):

| Role | Nama user | Email | Env var password |
|---|---|---|---|
| Manage hardware (Update) | Agus Wijaya | `manageHardwareUpdate_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_HW_UPDATE_PASSWORD` |
| Total Control (pencabut capability dan pengamat akhir) | Sari Dewi | `totalControl_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |

- Login Agus Wijaya dilakukan di hook `before`; Langkah 10 mengganti sesi UI ke Sari Dewi (langkah ganti akun eksplisit). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Layar awal: Global Settings > Hardware > Handheld Reader dibuka di hook `beforeEach` dan dimuat sebelum pencabutan capability (halaman tidak dimuat ulang oleh spec sebelum langkah Save).
- Pelaku pencabutan capability: Total Control Client A (Sari Dewi, Pre-setup #1) lewat sesi API (sesi API aktor tidak dihitung sebagai sesi web, lihat `suite.md`, Sesi admin kedua). Kemampuan API pencabutan dan pemulihan capability disediakan tim FE/BE; endpoint-nya tidak didefinisikan di TC, PRD, atau LLD dan tidak ditulis di spec ini.
- Data: Client A dengan Seed Reader A; target aksi DD-01 (`Zebra RFID Reader - 1`, `Alias Name` `—`). Spec tidak mengubah data DD-01 bila penolakan server berjalan benar. Data Dinamis: Alias Name `Reader Dock 01-{runId}-011`.
- Pemulihan: hook `after` memulihkan capability Manage hardware level Update milik Agus Wijaya dan memulihkan Seed Reader A (cadangan bila Save keliru diterima).
- State global yang diubah: capability akun Agus Wijaya (dicabut lalu dipulihkan).

## Test Steps

### Pencabutan capability di tengah aksi

1. Cabut capability Manage hardware dari Agus Wijaya lewat sesi API Sari Dewi (Total Control) hingga tersimpan
2. Tunggu aksi selesai
3. Buka Overlay row action DD-01, klik `Edit Alias Name`
4. Isi `Alias Name` dengan `Reader Dock 01-{runId}-011`
5. Klik `[Save]`
6. Verifikasi muncul toast error "You don't have permission to do this."
7. Verifikasi UI di-refresh dan elemen mutasi yang tidak berhak tersembunyi
8. Verifikasi dialog Edit Alias Name tertutup
9. Verifikasi tidak ada redirect ke halaman lain
10. Logout, lalu login sebagai Sari Dewi (Total Control, Client A)
11. Muat ulang Global Settings > Hardware > Handheld Reader
12. Verifikasi kolom `Alias Name` baris DD-01 tetap `—`

## Notes

- Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (section 2). TC berlabel Manual Only (d): butuh dua sesi atau pengguna paralel; kebutuhan ditulis di Prerequisites (pencabutan lewat sesi API Sari Dewi, langkah 1).
- Langkah "Tunggu aksi selesai" (langkah 2) adalah langkah penghubung tanpa `Verifikasi`: aksi berpindah dari sesi API ke sesi UI aktor (bagian 8b butir 8). Langkah 10 dan 11 (ganti akun ke Total Control dan muat ulang) adalah langkah penghubung menuju pengamatan Expected c TC-GS-HHR-50.
- Langkah 8 (dialog Edit Alias Name tertutup bersama refresh UI) memenuhi Expected b TC-GS-HHR-50 sesuai PRD T-14 (§7.3); dialog sudah tertutup sebelum `Logout` pada langkah 10, sehingga tidak ada penutupan lewat `✕` atau `Unsaved Changes`.
- Temuan untuk QA:
  - TC-GS-HHR-50 butir b ("elemen mutasi yang tidak berhak tersembunyi") tidak menyebut elemen mana yang dicek setelah UI di-refresh; spec memakai satu `Verifikasi` umum.
