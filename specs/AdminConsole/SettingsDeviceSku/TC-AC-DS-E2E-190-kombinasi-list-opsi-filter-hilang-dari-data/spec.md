---
id: TC-AC-DS-E2E-190-kombinasi-list-opsi-filter-hilang-dari-data
title: "Kombinasi List: Opsi Filter yang Dipakai Filter Aktif Hilang dari Data"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DS-335
coverage:
  web: automated
---

# Kombinasi List: Opsi Filter yang Dipakai Filter Aktif Hilang dari Data

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima, `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Pelaku kedua lewat sesi API aktor (login API password, bukan sesi web; kemampuan disediakan tim BE/FE, dinyatakan di `suite.md`): Total Control Principal kedua `totalControlSku2_automated_{namaCompany}@qwertysystem.net` (Budi Kurniawan), `Spectra.env.AC_DS_TC2_PASSWORD` (Pre-setup #2).
- Data Pre-setup #29 (SKU Principal inti) dan #30 (`SEED-001` sampai `SEED-119`; total 129 SKU Principal), dipasang idempoten oleh seeding di hook `before`. Target aksi hapus adalah SKU Pre-setup `BLE-KIN-GW1` (Brand `Kinetia`, stok 8), satu-satunya SKU Brand `Kinetia`; data ini tidak dapat dimiliki spec karena asersi bergantung pada Brand `Kinetia` yang dipakai satu SKU saja (S-06, pengecualian data Pre-setup).
- Kemampuan teknis: fixture BE untuk mengosongkan seluruh unit `BLE-KIN-GW1` (stok 8 menjadi 0) dan untuk memulihkan `BLE-KIN-GW1` (kode, Device Name `BLE Gateway`, Brand `Kinetia`, Model/Type `GW-1`, stok 8, 1 foto) dan entri Changelog-nya ke keadaan Pre-setup #29 dan #33. Disediakan tim FE/BE. Pemulihan dijalankan di hook `before` dan `after` serta sebagai langkah penghubung di langkah 13. Efek: Last Modified dan entri Changelog `BLE-KIN-GW1` kembali ke nilai Pre-setup; jumlah SKU kembali 129.
- Suite berjalan serial (`parallel: false`).
- Nilai data diacu lewat `Fixture.deviceSku.<kunci>`; berkas fixture disediakan tim FE.

## Test Steps

1. Klik ikon Filter
2. Pada field Brand pilih `Kinetia`
3. Klik `[Apply]`
4. Tunggu aksi selesai
5. Kosongkan seluruh unit `BLE-KIN-GW1` lewat fixture BE (stok 8 menjadi 0)
6. Hapus SKU `BLE-KIN-GW1` lewat sesi API Total Control Principal kedua hingga penghapusan tersimpan
7. Pada sesi pertama klik `[Apply]` lagi pada Filter Panel
8. Verifikasi Table Tools List tetap tampil tanpa pesan error
9. Verifikasi tabel menyesuaikan kriteria yang tersisa
10. Buka dropdown Brand
11. Verifikasi opsi Brand `Arcturus` tampil
12. Verifikasi opsi `Kinetia` tidak ada lagi pada dropdown Brand karena sudah tidak muncul di data tabel
13. Tekan Esc, lalu pulihkan `BLE-KIN-GW1` lewat fixture BE

## Notes

- Langkah penghubung (S-03): langkah 4 menunggu `[Apply]` selesai sebelum aktor berpindah; langkah 13 memulihkan data Pre-setup yang dihapus di langkah 6; keduanya tanpa asersi.
- Langkah 8 dan 11 adalah anchor positif tambahan (bukan Expected TC) untuk asersi "tanpa pesan error" dan absence opsi `Kinetia`.
- Klasifikasi: pelaku kedua memicu perubahan state lewat sesi API, bukan konteks UI kedua; TC-AC-DS-335 diberi `Manual Only` pada kriteria dua sesi paralel di TC sumber. TC-AC-DS-330 sampai TC-AC-DS-332 ada di spec TC-AC-DS-E2E-097.
- Temuan untuk QA:
  - TC-AC-DS-335 Expected a ("tabel menyesuaikan kriteria yang tersisa tanpa pesan error") tidak menyebut isi tabel setelah `Kinetia` hilang (kosong atau filter dilepas); spec mengikuti redaksi TC.
  - TC-AC-DS-335 menyatakan pemulihan data oleh baseline tetapi `suite.md` belum menyatakan pengecualian S-06 untuk data Pre-setup yang dihapus dan dipulihkan lewat fixture BE; perlu keputusan.
  - S-12: asersi bergantung pada nama literal Pre-setup #29 (`BLE-KIN-GW1`, Brand `Kinetia`). Lampiran A tidak memuat butir modul ini; keputusan pengecualian nama literal masih terbuka.
  - Env `AC_DS_TC_PASSWORD` dan `AC_DS_TC2_PASSWORD` serta berkas fixture `Fixture.deviceSku` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE. Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag-nya belum ditetapkan.
