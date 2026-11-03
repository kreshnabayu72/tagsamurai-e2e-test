---
id: TC-FA-TAG-E2E-003-state-loading-respons-ditunda-tab-paired-kartu-dan-to-be-returned
title: "State Loading Saat Respons Ditunda pada Tab Paired, Kartu Filter, dan Tabel To Be Returned"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-14
  - TC-FA-TAG-29
  - TC-FA-TAG-86
coverage:
  web: automated
---

# State Loading Saat Respons Ditunda pada Tab Paired, Kartu Filter, dan Tabel To Be Returned

## Prerequisites

- Mode: FE+BE (backend nyata; `Spectra.intercept` parsial hanya menunda respons, tidak mengubah isinya).
- Akun: Total Control, `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite (lihat suite.md); spec ini tidak mengubahnya.
- Data Pre-setup (hanya dibaca, tidak diubah): dataset tab Paired (Excavator 20 Ton / Plant A, Excavator 20 Ton / Plant B, Laptop Pro 14 / HQ, Forklift Manual / Plant A) dan tab To Be Returned dengan 3 Tag: [RFID] `RF-00071` (Last Asset `Excavator 20 Ton - 2`, Reason `Disposal`, Return Group `Disposal Center`, Current Holder `Dedi K.`); [RFID] `RF-00088` (`Excavator 20 Ton - 5`, `Disposal Center`, `Dedi K.`); [NFC] `NF-00092` (`Laptop Pro 14 - 8`, `HQ Warehouse`, `Rina T.`).
- Kemampuan teknis: `Spectra.intercept` untuk menunda respons (tahan lalu lepas) request data tab Paired, request data kartu, dan request daftar To Be Returned. Endpoint tidak didefinisikan di TC maupun PRD yang dibaca; dipilih tahap script (S-13). Tahanan respons dilepas pada langkah 5, 12, dan 17 dan dipastikan terlepas di hook `after` bila spec gagal di tengah.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (ditandai untuk tim FE); data di atas dirujuk lewat `Fixture.fixed-asset-tag.<kunci>` setelah berkas itu dibuat. Seeding dan pemulihan idempotent lewat fixture backend (kemampuan disediakan tim FE/BE, dilewati bila data sudah ada). Nama dan kode literal tidak diberi suffix `{runId}` karena asersi bergantung pada kode dan jumlah (suite.md).
- Tidak ada state global yang diubah selain intercept di atas.

## Test Steps

### TC-FA-TAG-14: State loading tab Paired saat data diambil

1. Tunda respons data tab Paired lewat intercept
2. Buka menu Fixed Asset > TAG lewat sidebar
3. Verifikasi kartu filter menampilkan Shimmer
4. Verifikasi tabel grup menampilkan state loading mengikuti prd-conventions §7
5. Lepas tahanan respons data tab Paired
6. Verifikasi Shimmer pada kartu filter hilang
7. Verifikasi nilai kartu serta baris grup tampil

### TC-FA-TAG-29: Kartu menampilkan Shimmer saat loading

8. Tunda respons data kartu lewat intercept
9. Buka menu Fixed Asset > TAG lewat sidebar
10. Amati kartu sebelum data tiba
11. Verifikasi ketiga kartu menampilkan Shimmer
12. Lepas tahanan respons data kartu
13. Verifikasi nilai kartu tampil

### TC-FA-TAG-86: State loading tabel To Be Returned saat data dimuat

14. Tunda respons request daftar To Be Returned lewat intercept
15. Klik Tab `To Be Returned`
16. Verifikasi tabel menampilkan loading component selama respons tertunda
17. Lepas tahanan respons daftar To Be Returned
18. Verifikasi 3 baris Tag tampil

## Notes

- Langkah 1, 8, dan 14 adalah langkah pemicu (menahan respons) dan langkah 5, 12, 17 adalah pelepasnya; penahanan respons hanya untuk mengamati state UI sehingga bukan kelas b (bagian 3 prinsip 13b). Langkah 10 adalah langkah penghubung tanpa asersi (S-03).
- Langkah 15 membuka tab To Be Returned dari tab Paired karena request daftar To Be Returned dipicu saat tab dibuka; "Buka Fixed Asset > TAG > To Be Returned" pada TC dipenuhi lewat langkah 2 (halaman) dan 15 (tab).
- Temuan untuk QA:
  - TC-FA-TAG-14, 29, dan 86 menulis "respons ditunda" sebagai kondisi state loading biasa, bukan kegagalan; spec memperlakukannya sebagai fungsional (bagian 3 prinsip 13b) dan bukan kelas b.
  - TC-FA-TAG-14 dan TC-FA-TAG-29 tidak menyebut apakah kartu dan tabel dimuat dari satu request atau dua; spec menahan "respons data tab Paired" untuk TC-FA-TAG-14 dan "respons data kartu" untuk TC-FA-TAG-29, dan pemetaan ke request nyata diserahkan ke tahap script.
  - TC-FA-TAG-86 tidak menyebut kriteria "loading component" (spinner atau skeleton); spec mengasersi keberadaannya sesuai kata TC.
