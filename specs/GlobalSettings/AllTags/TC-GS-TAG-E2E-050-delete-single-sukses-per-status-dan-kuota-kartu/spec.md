---
id: TC-GS-TAG-E2E-050-delete-single-sukses-per-status-dan-kuota-kartu
title: "Delete Single Berhasil: Available, Damaged/Missing, dan Retired (Kuota Kembali / Tidak), TAG Log Ikut Terhapus"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-142
  - TC-GS-TAG-143
coverage:
  web: automated
---

# Delete Single Berhasil: Available, Damaged/Missing, dan Retired (Kuota Kembali / Tidak), TAG Log Ikut Terhapus

## Prerequisites

- Mode: FE+BE (backend nyata). Spec ini menghapus data registri (aksi destruktif di akhir spec; TC-GS-TAG-142 dijalankan terakhir).
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; hook `after` mengembalikan sesi ke akun default suite.
- Layar awal: hook `beforeEach` membuka Global Settings > TAG > Tab All.
- Data Pre-setup: Seed Registri A (Client A, DD-01..DD-30; kartu RFID – Object TAG `21 of 50`, NFC `3 of 30`). Target hapus: DD-08 `E2801160600002054D8A0008` (RFID Retired), DD-12 `E2801160600002054D8A0012` (RFID Object Available), DD-04 `AABBCCDDEE80` (BLE Damaged/Missing). Identifier tetap, tidak bisa bersufiks `{runId}` (S-12, Q-4); seeding idempotent lewat fixture BE memulihkan kondisi awal sebelum spec. Kartu NFC `3 of 30` pada precondition TC-GS-TAG-142 dipakai sebagai precondition, tidak diasersi.
- Kemampuan teknis (disediakan tim FE/BE): seed dan reset idempotent Seed Registri A; pembacaan TAG Log tag yang sudah dihapus (untuk Expected d TC-GS-TAG-142); pembacaan nilai kartu BLE terpakai.
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): kembalikan Seed Registri A (DD-04, DD-08, DD-12) lewat fixture BE.
- Suite serial (`parallel: false`). Spec tidak mengubah state global selain sesi akun.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate`, lihat `suite.md`.

## Test Steps

### TC-GS-TAG-143: Delete tag Retired tidak mengembalikan slot kuota

1. Catat nilai kartu RFID – Object TAG (`21 of 50`)
2. Buka menu baris DD-08 (Retired), lalu klik `Delete`
3. Klik `Delete` pada dialog
4. Verifikasi toast sukses `Success, TAG has been deleted.`
5. Tutup toast
6. Verifikasi baris DD-08 hilang dari registri
7. Verifikasi kartu RFID – Object TAG tetap `21 of 50`

### TC-GS-TAG-142: Delete tag Available dan Damaged/Missing, slot kuota kembali

8. Catat nilai kartu RFID – Object TAG dan nilai terpakai kartu BLE
9. Buka menu baris DD-12 (RFID Object, Available), lalu klik `Delete`
10. Klik `Delete` pada dialog
11. Verifikasi toast sukses `Success, TAG has been deleted.`
12. Tutup toast
13. Buka menu baris DD-04 (BLE, Damaged/Missing), lalu klik `Delete`
14. Klik `Delete` pada dialog
15. Verifikasi toast sukses `Success, TAG has been deleted.`
16. Verifikasi baris DD-12 hilang dari registri
17. Verifikasi baris DD-04 hilang dari registri
18. Verifikasi kartu RFID – Object TAG terpakai berkurang 1 (`20 of 50`)
19. Verifikasi nilai terpakai kartu BLE berkurang 1
20. Verifikasi TAG Log DD-12 dan DD-04 ikut terhapus (pembacaan lewat fixture BE)

## Notes

- Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular.
- Perubahan urutan (S-05 butir terakhir): TC-GS-TAG-143 dijalankan sebelum TC-GS-TAG-142 karena TC-GS-TAG-143 mengasersi kartu RFID – Object TAG tetap `21 of 50`, sedangkan TC-GS-TAG-142 mengurangi kartu itu menjadi `20 of 50`; urutan TC sumber akan menggeser baseline. Penghapusan Available/Damaged/Missing (aksi yang mengubah kartu) tetap di akhir.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): 1 dan 8 (mencatat baseline kartu), 5 dan 12 (menutup toast sukses sebelum toast berikutnya diasersi, S-09).
- Asersi tambahan di luar Expected TC (S-03): tidak ada.
- Temuan untuk QA:
  - Q-4: identifier Seed Registri A tetap dan kartu `21 of 50` valid hanya bila Seed Registri A dipulihkan sebelum spec.
  - TC-GS-TAG-142 precondition d menyebut NFC `3 of 30` tetapi penghapusan melibatkan tag BLE (DD-04); nilai awal kartu BLE tidak ditulis TC sehingga Expected c dibaca sebagai berkurang 1 dari baseline.
  - TC-GS-TAG-142 Expected d (TAG Log ikut terhapus) tidak menyebut cara mengamati tag yang sudah hilang dari registri; spec memakai pembacaan lewat fixture BE (disediakan tim FE/BE).
  - Post Condition TC-GS-TAG-142 butir c ("Event Log mencatat dua baris Activity Delete") tidak punya langkah observasi di TC dan tidak diasersi; butir a, b, d identik dengan Expected b, c, d.
  - Post Condition TC-GS-TAG-143 identik dengan Expected a dan b.
