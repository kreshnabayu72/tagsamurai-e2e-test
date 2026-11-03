---
id: TC-FA-SU-E2E-209-modal-changelog-user-global-role-setup-column-bagian-2
title: "Modal Changelog User > Global Role: Setup Column (Bagian 2)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-629
coverage:
  web: automated
---

# Modal Changelog User > Global Role: Setup Column (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Changelog (#27). Pengguna target: Budi Santoso. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Modal Changelog Budi Santoso > Global Role (Pre-setup #27, 5 baris; urutan default Date descending). Alias baris yang dipakai langkah (Action | Role Name | Field; Modified By):
  - G-1: `Remove` | `Manage global license` | `Manage global license`; Modified By `Lina M`
  - G-2: `Remove (via Total Control)` | `Manage global license` | `Access`; Modified By `Ahmad D`
  - G-3: `Assign (via Total Control)` | `Import Data` | `Access`; Modified By `Ahmad D`
  - G-4: `Edit` | `Manage asset master data` | `Manage asset master data — Delete`; Modified By `Ahmad D`
  - G-5: `Assign` | `Manage accounting` | `Manage accounting`; Modified By `Ahmad D`
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed Changelog #27 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface Changelog dan tidak menambah entri pada Budi Santoso.
- Tabel parameter "Urutan drag kolom Hideable" (urutan awal: `Date`, `Action`, `Role Name`, `Field`, `Old Value`, `New Value`, `Modified By`; arah ditetapkan spec, drag berurutan kumulatif):

| No | Kolom yang di-drag | Arah (satu posisi) | Urutan kolom sesudah drag |
|---|---|---|---|
| 1 | `Date` | bawah | `Action`, `Date`, `Role Name`, `Field`, `Old Value`, `New Value`, `Modified By` |
| 2 | `Action` | bawah | `Date`, `Action`, `Role Name`, `Field`, `Old Value`, `New Value`, `Modified By` |
| 3 | `Role Name` | atas | `Date`, `Role Name`, `Action`, `Field`, `Old Value`, `New Value`, `Modified By` |
| 4 | `Field` | bawah | `Date`, `Role Name`, `Action`, `Old Value`, `Field`, `New Value`, `Modified By` |
| 5 | `Old Value` | atas | `Date`, `Role Name`, `Old Value`, `Action`, `Field`, `New Value`, `Modified By` |
| 6 | `New Value` | bawah | `Date`, `Role Name`, `Old Value`, `Action`, `Field`, `Modified By`, `New Value` |
| 7 | `Modified By` | atas | `Date`, `Role Name`, `Old Value`, `Action`, `Modified By`, `Field`, `New Value` |
- Pemulihan preferensi kolom: kemampuan menghapus preferensi kolom tabel di browser (bukan `[Reset to Default]`) disediakan tim FE; dijalankan sebagai langkah penghubung dan di hook `after`. Preferensi kolom disimpan per perangkat (browser) sehingga spec ini tidak memengaruhi tabel lain.

## Test Steps

### TC-FA-SU-629: Geser (drag reorder) kelas Hideable

1. Buka Detail pengguna Budi Santoso, klik tab Role, klik sub-tab Global Role, lalu klik icon Changelog
2. Buka Setup Column
3. Untuk setiap baris tabel "Urutan drag kolom Hideable" (langkah 3 sampai 4): drag kolom baris itu satu posisi sesuai kolom "Arah" baris itu
4. Verifikasi urutan Live Preview sama dengan kolom "Urutan kolom sesudah drag" baris itu
5. Klik `[Save]`
6. Verifikasi urutan kolom tabel sama dengan kolom "Urutan kolom sesudah drag" baris terakhir
7. Klik F5
8. Verifikasi urutan kolom tabel tetap sama dengan baris terakhir tabel parameter setelah refresh (F5)
9. Hapus preferensi kolom tabel di browser lalu muat ulang halaman (kemampuan disediakan tim FE)

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Langkah berulang (idiom bagian 8b butir 7): langkah 3 sampai 4 dijalankan 7 kali, satu iterasi per baris tabel "Urutan drag kolom Hideable" (9 langkah tertulis, 21 dengan ekspansi, di bawah ambang sekitar 35).
- TC-FA-SU-630 (pin dan unpin modal Global Role) ada di spec 213.
- Temuan untuk QA (S-15): (1) TC tidak menyebut cara menguji kolom yang menjadi satu-satunya kolom visible; spec menguji lima kolom pertama bersamaan lalu kolom terakhir terpisah setelah kolom lain dicentang kembali. Post Condition preferensi kolom tersimpan per perangkat tidak punya langkah observasi dan tidak diasersi. (2) TC tidak menyebut arah drag; spec menetapkan arah tiap kolom pada tabel "Urutan drag kolom Hideable" (satu posisi, kolom tetangga bertukar tempat) dan mengasersi urutan kumulatif setelah tiap drag, setelah `[Save]`, dan setelah F5, karena tujuh drag berurutan disimpan dengan satu `[Save]` sehingga posisi akhir tiap kolom tidak berdiri sendiri.
