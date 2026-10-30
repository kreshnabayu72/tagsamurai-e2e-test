---
id: TC-GS-POS-E2E-010-capability-dicabut-saat-aksi-berjalan
title: "Save Edit Position Ditolak setelah Capability Update Dicabut di Tengah Sesi"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-POS-294
coverage:
  web: automated
---

# Save Edit Position Ditolak setelah Capability Update Dicabut di Tengah Sesi

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (parallel: false): spec mengubah capability role akun Update-Only (data Pre-setup bersama) sehingga tidak boleh berjalan paralel dengan spec lain yang memakai akun itu (spec 007 dan 009).
- Dua konteks browser (kelas multi-konteks/izin) dalam satu spec, ditandai `[Sesi A]` dan `[Sesi B]`:
  - Sesi A (aktor): Manage user and role: Update-Only `manageUserRoleUpdate_automated_{namaCompany}@qwertysystem.net` (Pre-setup 6), `Spectra.env.GS_UPDATE_PASSWORD`. Login di hook `before`; layar awal Global Settings > User > Position dibuka hook `beforeEach`.
  - Sesi B (pencabut capability, Total Control lain): Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1), `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` pada konteks browser terpisah.
  - Password tidak ditulis di spec atau fixture.
- Data Dinamis (nama bersuffix per run; milik spec ini): `Legal Counsel {runId}-010` di-seed lewat API di hook `before` (bebas relasi); nama hasil perubahan yang tidak pernah tersimpan: `Legal Manager {runId}-010`. Fixture baru `Fixture.position.capabilityRevoke010`.
- State global yang diubah: capability Update pada akun Update-Only (Pre-setup 6) dicabut di langkah 4; capability Read tetap. Hook `after` memulihkan capability Update akun itu ke nilai awal (dicatat di hook `before`) walau spec gagal di tengah, serta menutup konteks Sesi B dan mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`). Efek ke akun lain: selama capability dicabut, akun Update-Only tidak dapat mengedit.
- Kemampuan teknis: dua konteks browser paralel; pencabutan dan pemulihan capability Update pada akun Update-Only oleh Total Control lain (mekanisme lewat UI manajemen role Total Control atau API disediakan tim FE/BE; tidak didefinisikan di TC, PRD, atau LLD); pengamatan toast.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` true untuk akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Legal Counsel {runId}-010` dan `Legal Manager {runId}-010` bila masih ada; pulihkan capability, konteks, dan sesi seperti di atas.

## Test Steps

### TC-GS-POS-294: Save Edit setelah capability Update dicabut di tengah sesi

1. [Sesi A] Ketik Search `Legal Counsel {runId}-010`, tekan Enter
2. [Sesi A] Klik `⋯` pada `Legal Counsel {runId}-010`, pilih `Edit`
3. [Sesi A] Ganti nilai Position Name menjadi `Legal Manager {runId}-010` (belum disimpan)
4. [Sesi B] Cabut capability Update dari akun Update-Only (Pre-setup 6) hingga pencabutan tersimpan; capability Read tetap
5. [Sesi A] Klik `[Save]`
6. [Sesi A] Verifikasi muncul toast error: "You don't have permission to do this."
7. [Sesi A] Verifikasi tidak ada redirect (tetap di Global Settings > User > Position)
8. [Sesi A] Klik `✕` di header popup Edit
9. [Sesi A] Verifikasi dialog Unsaved Changes muncul
10. [Sesi A] Klik `[Leave]`
11. [Sesi A] Verifikasi baris `Legal Counsel {runId}-010` tampil di tabel
12. [Sesi A] Verifikasi menu `⋯` pada baris `Legal Counsel {runId}-010` tidak tampil, sehingga row action `Edit` Hidden

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`. Kelas harness: multi-konteks/izin (dua sesi, capability role diubah), serial.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (tanpa `Verifikasi`): Search pada langkah 1 untuk menemukan baris; langkah 4 menjalankan "Sesi Total Control lain (Pre-setup No. 1) mencabut capability Update dari akun aktor (Pre-setup No. 6)" dari TC sumber; langkah 8 dan 10 aksi, langkah 9 `Verifikasi` tambahan agar penutupan form dirty deterministik (S-08), sehingga baris di bawah popup Edit dapat diamati pada langkah 11 dan 12. Langkah 11 adalah `Verifikasi` tambahan di luar Expected TC-GS-POS-294 yang menjadi anchor positif (baris tampil) bagi asersi absence menu `⋯` pada langkah 12 (butir 2 bagian 8b konvensi).
- Langkah 6 (toast) diasersi sebelum langkah 7 dan 12 karena toast bersifat sementara.
- Temuan untuk QA:
  - Post Condition TC-GS-POS-294 ("Record tetap `Legal Counsel`; tidak ada entri Changelog") tidak punya langkah observasi di TC dan tidak punya Expected padanan, sehingga tidak diasersi (S-01). Pengembalian capability Update setelah TC dikerjakan hook `after` dan tidak diasersi; kalimat pemulihan itu ditambahkan editor TC pada Post Condition dan bukan fakta PRD.
  - TC-GS-POS-294 menyebut Sesi Total Control lain (Pre-setup No. 1) mencabut capability Update dari akun Pre-setup No. 6 (Read tetap) tetapi tidak menyebut mekanismenya; spec memulihkan capability itu di `after`, sehingga mekanisme pencabutan dan pemulihan disediakan tim FE/BE. Karena akun itu data Pre-setup bersama, spec ini serial.
  - TC-GS-POS-294 tidak mendefinisikan state modal Edit setelah toast error 403 (tetap terbuka atau tertutup); spec menutup popup lewat `✕`, dialog Unsaved Changes, dan `[Leave]` (langkah 8 sampai 10), sehingga langkah itu gagal bila modal tertutup sendiri. Menunggu jawaban QA.
  - TC-GS-POS-294 Expected b menyebut "UI di-refresh" tanpa cara mengamatinya; spec hanya mengasersi akibatnya pada langkah 12 (menu `⋯` tidak tampil).
  - Sesi B (Total Control kedua) berjalan sebagai konteks browser UI karena TC-GS-POS-294 menyebut sesi Total Control lain; konvensi P-2 memakai sesi API untuk pelaku kedua yang hanya memicu perubahan state. Menunggu konfirmasi QA.
  - TC-GS-POS-294 menyebut Record `Legal Counsel` ada dari TC-GS-POS-53 (Data Dinamis 5); spec men-seed `Legal Counsel {runId}-010` sendiri.
