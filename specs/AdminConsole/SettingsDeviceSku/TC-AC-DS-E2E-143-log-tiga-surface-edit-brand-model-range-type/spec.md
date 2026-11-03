---
id: TC-AC-DS-E2E-143-log-tiga-surface-edit-brand-model-range-type
title: "Log Tiga Surface: Edit Brand, Model/Type, dan Range Type"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-470
  - TC-AC-DS-471
  - TC-AC-DS-472
coverage:
  web: automated
---

# Log Tiga Surface: Edit Brand, Model/Type, dan Range Type

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup: SKU inti `HHR-ARC-200` (Device Name `UHF Handheld Reader`, Brand `Arcturus`, Model/Type `H200`, Range Type `Short Range`, stok 0) serta seed (#29, #30), pohon Category (#25), Device Name (#26), Brand Principal `Arcturus`, `Veltrix` (#27), file foto uji (#37), General Settings Date Format `dd/MM/yy`, 24 jam, Asia/Jakarta (#35), riwayat Changelog Principal (#33). Nilai dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).
- Edit yang diuji (parameter langkah 2 sampai 18; setiap TC mengubah satu field berbeda sehingga tidak saling mengganggu):

  | TC | Field | Old Value | New Value |
  |---|---|---|---|
  | TC-AC-DS-470 | `Brand` | `Arcturus` | `Veltrix` |
  | TC-AC-DS-471 | `Model/Type` | `H200` | `H201` |
  | TC-AC-DS-472 | `Range Type` | `Short Range` | `Long Range` |

- Data yang diubah (target aksi tulis): SKU Pre-setup `HHR-ARC-200` (Brand, Model/Type, Range Type). TC menetapkan baris ini sebagai Pre-setup bersama; pemulihan ke `Arcturus`, `H200`, `Short Range` dijamin fixture BE (disediakan tim FE/BE) di hook `before` dan `after`. Efek: Last Modified `HHR-ARC-200` berubah dan Changelog, System Log, serta Activity Log bertambah entri permanen.
- Kemampuan teknis (disediakan tim FE/BE): pemulihan data di atas; pembacaan jumlah entri (baseline) Changelog Principal, System Log aktor `Jane Setiawan`, dan Activity Log tab User Action sebelum dan sesudah aksi (audit trail permanen; 8b butir 10); jam server dan jam browser sinkron untuk asersi Date.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar disediakan tim FE (lihat Temuan untuk QA).

## Test Steps

1. Untuk setiap baris tabel "Edit yang diuji" lakukan langkah 2 sampai 18
2. Catat baseline jumlah entri Changelog Principal, System Log aktor `Jane Setiawan`, dan Activity Log tab User Action
3. Ketik Search `HHR-ARC-200`, tekan Enter
4. Klik ⋯ pada baris `HHR-ARC-200`, pilih `Edit`
5. Verifikasi Popup Edit SKU tampil dengan field terisi
6. Ubah field dari Old Value menjadi New Value
7. Klik `[Save]`
8. Tunggu aksi selesai: Popup Edit SKU tertutup
9. Catat waktu aksi
10. Klik ikon Changelog
11. Verifikasi modal "Changelog: Device SKU" tampil dengan entri baru Action `Edit`, SKU `UHF Handheld Reader (HHR-ARC-200)`, Field sesuai tabel, Old Value dan New Value sesuai tabel, Modified By `Jane S` di baris pertama
12. Verifikasi Date entri itu sesuai waktu aksi menurut General Settings (toleransi satu menit)
13. Buka Settings > User, cari user `totalControlSku_automated_{namaCompany}@qwertysystem.net`, buka Detail, buka tab System Log
14. Verifikasi System Log aktor `Jane Setiawan` memuat entri Action `Edit`, Object `Device SKU`, Name `HHR-ARC-200`, Field, Old Value, dan New Value sesuai tabel
15. Buka Activity Log, buka tab User Action
16. Verifikasi Activity Log tab User Action memuat entri Action `Edit`, Object `Device SKU`, Name `UHF Handheld Reader (HHR-ARC-200)`, Field, Old Value, dan New Value sesuai tabel, Modified By `Jane S`
17. Verifikasi jumlah entri pada ketiga surface bertambah tepat 1 dari baseline langkah 2 (tidak ada entri log ganda)
18. Buka Settings > Device > Device SKU

## Notes

- Langkah 2 sampai 18 diulang tiga kali (ekspansi 51 langkah). Alasan melewati sekitar 35 langkah: tiga iterasi identik satu kelas (pencatatan log tiga surface) dengan parameter di tabel "Edit yang diuji"; sebagian besar langkah adalah blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom log; langkah 10 sampai 17) yang menurut bagian 3 prinsip 13 tidak dihitung sebagai langkah smell; tiap iterasi berdiri sendiri karena memakai field berbeda.
- Langkah penghubung tanpa `Verifikasi`: langkah 2 (baseline, S-12), langkah 3 (Search untuk menemukan baris target, R-16), langkah 9 (mencatat waktu aksi), dan langkah 18 (kembali ke List, S-03, S-09).
- Expected tiap TC butir a dipecah: kolom entri Changelog dalam satu `Verifikasi` (langkah 11) dan Date terpisah (langkah 12); butir b langkah 14; butir c langkah 16; Post Condition "tidak ada entri log ganda" ditutup langkah 17 (selisih baseline).
- Temuan untuk QA:
  - S-12: nilai literal Pre-setup (`HHR-ARC-200`, `H200`, `Arcturus`) mengikuti TC tanpa suffix; pengecualian modul belum ada di Lampiran A (butuh keputusan: seeding idempotent, serial, pemulihan fixture BE).
  - S-06: TC mengubah baris Pre-setup `HHR-ARC-200`; pemulihannya bergantung fixture BE yang belum ada.
  - S-13: pencarian user di Settings > User memakai email bersuffix `{namaCompany}`; TC hanya menyebut nama `Jane Setiawan`.
  - Fixture rancangan Pre-setup #33 belum terverifikasi ada di environment; fixture `settingsDeviceSku` dan 23 env var `AC_DS_*` (termasuk `AC_DS_TC_PASSWORD`) belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; flag-nya belum dinyatakan di `suite.md`.
