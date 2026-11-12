---
id: TC-FA-TAG-E2E-331-resilience-error-load-try-again-halaman-tab-paired-dan-to-be-returned
title: "Resilience: Error Load Tab Paired dan To Be Returned (5xx) dan Pemulihan lewat Try Again"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-16
  - TC-FA-TAG-17
  - TC-FA-TAG-87
coverage:
  web: automated
---

# Resilience: Error Load Tab Paired dan To Be Returned (5xx) dan Pemulihan lewat Try Again

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata).
- Akun aktor: Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) `Spectra.intercept` parsial yang memaksa respons 5xx pada pengambilan data tab Paired dan pada request daftar To Be Returned, dan melepas intercept; hook `after` melepas semua intercept; (2) seed dan pemulihan idempotent lewat fixture backend untuk dataset Paired dan Tag To Be Returned. Tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Grup tab Paired | 'Excavator 20 Ton' / Plant A / RFID / Total 20 / Reported 0 / Non-standard 0 / Not Paired Yet 2; 'Excavator 20 Ton' / Plant B / RFID / 20 / 2 / 5 / 0; 'Laptop Pro 14' / HQ / NFC, QR / 25 / 1 / 0 / 2; 'Forklift Manual' / Plant A / Non TAG / 10 / 0 / 3 / 0 | `grupPaired` |
| Tag To Be Returned (himpunan minimum; jumlah total tidak diasersi) | [RFID] RF-00071 (Last Asset 'Excavator 20 Ton - 2', Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.); [RFID] RF-00088 ('Excavator 20 Ton - 5', Disposal Center, Dedi K.); [NFC] NF-00092 ('Laptop Pro 14 - 8', HQ Warehouse, Rina T.) | `tbr` |

- State yang diubah dan pemulihannya: intercept 5xx dipasang di langkah 1 dan 8 dan dilepas di langkah 4 dan 11; hook `after` melepas intercept walau spec gagal di tengah.
- Nilai literal Pre-setup (Asset Name, kode Tag RF-*/NF-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.

## Test Steps

1. Pasang intercept 5xx pada pengambilan data tab Paired
2. Buka menu Fixed Asset > TAG
3. Verifikasi area tabel menampilkan `Unable to load this data.` dengan tombol `[Try Again]`
4. Lepas intercept (pulihkan server)
5. Klik `[Try Again]`
6. Verifikasi data dimuat ulang: kartu dan empat baris grup tampil
7. Verifikasi pesan `Unable to load this data.` hilang
8. Pasang intercept 5xx pada request daftar To Be Returned
9. Klik tab `To Be Returned`
10. Verifikasi tampil pesan "Unable to load this data." bersama tombol "Try Again"
11. Lepas intercept (pulihkan respons server)
12. Klik tombol "Try Again"
13. Verifikasi baris Tag tampil, sedikitnya RF-00071, RF-00088, dan NF-00092

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-16, 17, 87). Tidak ada TC hanya-BE.
- TC-FA-TAG-17 bergantung pada TC-FA-TAG-16 (kolom Dependensi TC); langkah 1 s.d. 3 menjalankan TC-FA-TAG-16, langkah 4 s.d. 7 menjalankan TC-FA-TAG-17 pada keadaan error yang sama, tanpa membuka halaman ulang.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1 dan 8 (memasang intercept sebagai precondition TC), 4 dan 11 (melepas intercept, sudah menjadi langkah TC "Pulihkan server" untuk TC-FA-TAG-17 dan TC-FA-TAG-87).
- Langkah 13 mengasersi sedikitnya tiga baris Pre-setup `tbr` (relatif, bukan literal 3; keputusan user 2026-11-04, bagian 8b butir 10); himpunan Tag To Be Returned dapat memuat Tag lain.
- A-15: nilai literal Pre-setup (Asset Name, kode Tag RF-*/NF-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - TC-FA-TAG-16 menulis precondition "User berada di Fixed Asset > TAG > Paired" bersamaan dengan "Server mengembalikan 5xx"; spec memasang intercept sebelum membuka halaman agar error muncul saat load pertama.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
