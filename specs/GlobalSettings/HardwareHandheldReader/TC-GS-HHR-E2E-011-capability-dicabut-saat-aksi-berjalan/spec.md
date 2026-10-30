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
| Manage hardware (Update) | Agus Wijaya | `manageHardwareUpdate_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_UPDATE_PASSWORD` |

- Login Agus Wijaya dilakukan di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Layar awal: Global Settings > Hardware > Handheld Reader dibuka di hook `beforeEach` dan dimuat sebelum pencabutan capability (halaman tidak dimuat ulang oleh spec sebelum langkah Save).
- Pelaku pencabutan capability (admin lain): sesi API yang mencabut capability Manage hardware dari Agus Wijaya; akun admin tersebut tidak ada di Tabel Data Uji Pre-setup TC dan disediakan tim FE (tanpa sesi UI kedua karena hasil di sesi itu tidak diasersi, P-2 konvensi bagian 3). Kemampuan API pencabutan dan pemulihan capability disediakan tim FE/BE; endpoint-nya tidak didefinisikan di TC, PRD, atau LLD dan tidak ditulis di spec ini.
- Data: Client A dengan Seed Reader A; target aksi DD-01 (`Zebra RFID Reader - 1`, `Alias Name` `—`). Spec tidak mengubah data DD-01 bila penolakan server berjalan benar. Data Dinamis: Alias Name `Reader Dock 01-{runId}-011`.
- Pemulihan: hook `after` memulihkan capability Manage hardware level Update milik Agus Wijaya dan memulihkan Seed Reader A (cadangan bila Save keliru diterima).
- State global yang diubah: capability akun Agus Wijaya (dicabut lalu dipulihkan).

## Test Steps

### Pencabutan capability di tengah aksi

1. Cabut capability Manage hardware dari Agus Wijaya lewat sesi API admin lain hingga tersimpan
2. Tunggu aksi selesai
3. Buka Overlay row action DD-01, klik `Edit Alias Name`
4. Isi `Alias Name` dengan `Reader Dock 01-{runId}-011`
5. Klik `[Save]`
6. Verifikasi muncul toast error "You don't have permission to do this."
7. Verifikasi UI di-refresh dan elemen mutasi yang tidak berhak tersembunyi
8. Verifikasi tidak ada redirect ke halaman lain
9. Verifikasi `Alias Name` DD-01 tetap `—`

## Notes

- Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (section 2). TC berlabel Manual Only (d): butuh dua sesi atau pengguna paralel; kebutuhan ditulis di Prerequisites (pencabutan lewat sesi API admin lain, langkah 1).
- Langkah "Tunggu aksi selesai" (langkah 2) adalah langkah penghubung tanpa `Verifikasi`: aksi berpindah dari sesi API ke sesi UI aktor (bagian 8b butir 8).
- Temuan untuk QA:
  - TC-GS-HHR-50 tidak menyebut siapa admin yang mencabut capability dan caranya; spec memakai sesi API admin lain yang disediakan tim FE tanpa mengarang endpoint atau akun.
  - TC-GS-HHR-50 butir b ("elemen mutasi yang tidak berhak tersembunyi") tidak menyebut elemen mana yang dicek setelah UI di-refresh; spec memakai satu `Verifikasi` umum.
  - TC-GS-HHR-50 butir c menyatakan `Alias Name` DD-01 tetap `—`, tetapi TC tidak menyebut cara membaca kolom tersebut setelah capability dicabut (akun yang kehilangan capability Manage hardware dan bukan Total Control atau Read Only tidak lagi melihat halaman, lihat TC-GS-HHR-33 dan TC-GS-HHR-35); spec mengikuti TC.
