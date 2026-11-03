---
id: TC-FA-CAID-E2E-029-defense-in-depth-save-saat-master-switch-off
title: "Defense-in-Depth: Request Save Langsung Saat Master Switch OFF Diproses Seperti Save Biasa"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CAID-333
coverage:
  web: automated
---

# Defense-in-Depth: Request Save Langsung Saat Master Switch OFF Diproses Seperti Save Biasa

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control Company Alpha (Pre-setup No 1, pengguna Sarah Johnson, `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`); halaman Fixed Asset > Settings > Asset Master > Custom Asset ID dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip disetel seen untuk akun UI suite; konfigurasi Company Alpha dipulihkan ke baseline B1 dan aset A1 sampai A5 (Pre-setup No 11) ke kondisi awal di `beforeEach` dan `after` lewat sesi API aktor (klien HTTP dan token sesi API disediakan tim FE; token tidak dihitung sebagai sesi web).
- Data Pre-setup No 10: baseline B1 dengan Master Switch OFF (Separator `/ (Slash)`, segmen tercentang Group Code, Category Code, Asset Name Code, Purchase Date, Asset Increment, tanpa Initial Company) dan Data Pre-setup No 11 dengan Asset ID A1, A2, A3 berupa nomor Increment polos `1`, `2`, `3`; keduanya di-seed lewat sesi API aktor pada langkah 1. Nilai dibaca dari `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE).
- Data Pre-setup No 27: General Settings Company Alpha Date Format `dd/MM/yy` dan Time Format 24 jam; dipakai sebagai precondition TC, tidak diasersi.
- Kemampuan teknis (disediakan tim FE/BE): klien API untuk mengirim request Save langsung ke server dengan token sesi API Total Control (Pre-setup No 26); kemampuan membaca jumlah entri Modal Changelog: Custom Asset ID, System Log pada Detail User Sarah Johnson, dan Activity Log (Object `Custom Asset ID`) sebelum aksi sebagai baseline (langkah 2).
- State: spec ini menyimpan Separator `- (Dash)` dan menambah entri pada tiga surface log (tidak dihapus). Pemulihan lewat hook `after` suite.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-333: Request Save langsung saat Master Switch OFF diproses seperti Save biasa

1. Setel konfigurasi Company Alpha ke baseline B1 dengan Master Switch OFF dan Asset ID A1, A2, A3 menjadi nomor Increment polos `1`, `2`, `3` lewat sesi API aktor hingga tersimpan, lalu muat ulang halaman
2. Catat jumlah entri Modal Changelog: Custom Asset ID, System Log pada Detail User Sarah Johnson, dan Activity Log tab User Action dengan Object `Custom Asset ID` sebagai baseline
3. Kirim request Save konfigurasi langsung ke server dengan token sesi API Total Control, Separator `- (Dash)`, dan formula valid delapan segmen
4. Tunggu aksi selesai
5. Muat ulang halaman
6. Verifikasi Separator tersimpan `- (Dash)`
7. Verifikasi Master Switch tetap pada posisi OFF
8. Verifikasi kontrol form tetap di-dim dan disabled
9. Buka Fixed Asset > Assets > All Assets
10. Verifikasi kolom Asset ID baris A1 tetap `1`
11. Verifikasi kolom Asset ID baris A2 tetap `2`
12. Verifikasi kolom Asset ID baris A3 tetap `3`
13. Buka Modal Changelog: Custom Asset ID
14. Verifikasi jumlah entri Changelog bertambah tepat satu dibanding baseline
15. Verifikasi entri baru berupa satu baris Edit Separator Old Value `Slash` New Value `Dash`
16. Tutup Modal Changelog: Custom Asset ID
17. Buka Global Settings > User > Detail pengguna Sarah Johnson > tab System Log
18. Verifikasi jumlah entri System Log bertambah tepat satu dibanding baseline
19. Verifikasi entri baru System Log memuat Object `Custom Asset ID` dan Name `—`
20. Verifikasi entri System Log tanpa Modified By
21. Buka Fixed Asset > Activity Log > tab User Action
22. Verifikasi jumlah entri Activity Log bertambah tepat satu dibanding baseline
23. Verifikasi entri baru Activity Log memuat Object `Custom Asset ID` dan Name `—`
24. Verifikasi entri Activity Log memiliki Modified By `Sarah J`

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- `K-1`: spec defense-in-depth dengan Expected respons API dan state data tetap FE+BE walau tumpang tindih dengan `tc-settings-custom-asset-id-backend.md`; TC granular tetap sumber dan BE mencatatnya pada tingkat endpoint.
- Langkah 3 mengirim request langsung lewat klien HTTP tanpa browser; asersinya adalah state data yang dibaca lewat UI (bagian 8b butir 1). Asersi respons tidak ditulis karena Expected TC tidak menyebut status respons.
- Langkah penghubung (tanpa `Verifikasi`): langkah 1 (seed precondition), langkah 2 (baseline jumlah entri sebelum aksi pemicu, S-12), langkah 4 (Tunggu aksi selesai karena langkah 5 memuat ulang halaman), langkah 9, 13, 17, dan 21 (membuka surface), langkah 16 (menutup modal), dan langkah 5 (memuat ulang agar form membaca konfigurasi tersimpan).
- S-01: kolom Object dan Name pada langkah 19 dan 23 adalah dua kolom satu baris log yang diamati dari satu entri, sehingga masing-masing satu `Verifikasi`; jumlah entri, kolom Modified By, dan Asset ID tiap aset dipecah sendiri.
- Temuan untuk QA:
  - Expected TC-FA-CAID-333 c menyebut System Log "tanpa Modified By"; TC tidak menyebut apakah kolom Modified By ada pada tabel System Log. Spec mengasersi entri System Log tidak memuat nilai Modified By (langkah 20).
  - Kolom Date entri log tidak diasersi karena TC tidak memintanya.
