---
id: TC-FA-TAG-E2E-299-derivasi-non-standard-reported-dan-not-paired-yet-bagian-3
title: "Derivasi Not Paired Yet: Aset Non-TAG dan Asset Name BLE dan GPS Tidak Dihitung"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-1480
  - TC-FA-TAG-1481
coverage:
  web: automated
---

# Derivasi Not Paired Yet: Aset Non-TAG dan Asset Name BLE dan GPS Tidak Dihitung

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Total Control [TC] `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`).
- Login di hook `before` spec ini sebagai akun aktor pertama; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (kunci disediakan).
- Seed dan pemulihan idempotent lewat fixture backend (disediakan tim FE/BE, lihat `suite.md`): aset, Tag per status registri, stok Tag per tipe, laporan Tag, dan entri log.
- Data Pre-setup tab Paired (TC): Excavator 20 Ton / Plant A / RFID / Total 20 / Reported 0 / Non-standard 0 / Not Paired Yet 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC dan QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0. Grup Excavator 20 Ton / Plant B memuat lima aset acuan: AST-0011 ('Excavator 20 Ton - 11'), AST-0020 ('- 20'), AST-0021 ('- 21'), AST-0043 ('- 43'), AST-0044 ('- 44').
- Data tambahan (TC, tanpa suffix): grup Forklift Manual / Plant A / Non TAG memuat 10 aset ber-Tag Paired ditambah 'Forklift Manual - 74' (AST-0074, Plant A, Asset Name Non-TAG) tanpa Tag Paired; Asset Name 'Beacon Unit' (TAG Type BLE dan GPS) dengan tiga aset Active di Plant A: 'Beacon Unit - 701' (AST-0701) ber-Tag RFID `RF-00800` Paired, 'Beacon Unit - 702' (AST-0702) dan 'Beacon Unit - 703' (AST-0703) tanpa Tag Paired.
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; Lampiran A belum memuat butir modul ini sehingga seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE (suite serial) dicatat sebagai kebutuhan.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan TAG Type Asset Name, aset, Tag, laporan, dan sesi ke akun default suite lewat fixture backend.
- State global: tidak ada yang diubah spec ini selain data seed. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1480: aset Non-TAG tanpa Tag Paired tidak dihitung Not Paired Yet

1. Verifikasi kolom `Not Paired Yet` baris grup 'Forklift Manual' / Plant A bernilai `0` dan kolom `Total Assets` bernilai 10
2. Klik Asset Name 'Forklift Manual' pada baris grup Plant A untuk membuka Popup Detail
3. Verifikasi field `Not Paired Yet` di Popup Detail bernilai `0` tanpa tombol `Show`
4. Verifikasi baris 'Forklift Manual - 74' tidak tampil di tabel T-TAG-02 dan tidak ada row action `Pair TAG` untuknya

### TC-FA-TAG-1481: Asset Name dengan TAG Type hanya BLE dan GPS tidak dihitung Not Paired Yet

5. Tutup Popup Detail
6. Verifikasi kolom `Not Paired Yet` baris grup 'Beacon Unit' / Plant A bernilai `0` dan kolom `Total Assets` bernilai 1
7. Verifikasi kartu `Not Paired Yet` bernilai 4 (hanya aset dari Data Pre-setup), tidak bertambah oleh 'Beacon Unit - 702' dan 'Beacon Unit - 703'
8. Klik Asset Name 'Beacon Unit' pada baris grup Plant A untuk membuka Popup Detail
9. Verifikasi field `Not Paired Yet` di Popup Detail bernilai `0` tanpa tombol `Show`
10. Verifikasi baris 'Beacon Unit - 702' dan 'Beacon Unit - 703' tidak tampil di tabel T-TAG-02 dan tidak ada row action `Pair TAG` untuk keduanya

## Notes

- Mode: FE+BE.
- Langkah penghubung (S-03): 5 (menutup Popup Detail).
- Absence: baris 'Forklift Manual - 74' dan baris 'Beacon Unit - 702', 'Beacon Unit - 703' tidak tampil didahului `Verifikasi` field `Not Paired Yet` Popup Detail yang sama sebagai anchor positif (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-TAG-1481 precondition d (bukan c) menyebut Asset Name 'Beacon Unit' dengan BLE dan GPS; TC-FA-TAG-1322 memakai 'Beacon Unit' dengan TAG Type BLE saja. Data seed kedua TC berbeda dan dipulihkan sesuai TC masing-masing.
  - TC-FA-TAG-1481 Expected a menyebut 'Total Assets bernilai 1' karena tiga aset tidak terhitung kecuali yang ber-Tag; spec mengasersi sesuai TC.
