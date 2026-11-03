---
id: TC-FA-LBL-E2E-170-setup-column-drawer-ceklis-dan-unceklis-kolom-hideable
title: "Setup Column Drawer: Ceklis dan Unceklis Kolom Hideable"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-364
coverage:
  web: automated
---

# Setup Column Drawer: Ceklis dan Unceklis Kolom Hideable

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, pengguna Sarah Johnson), `Fixture.assetLabeling.akun.totalControl` (email pola `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Hook suite (`before`, `beforeEach`, `after` di `suite.md`) berlaku; spec ini tidak menulis ulang isinya.
- Fixture `fixtures/asset-labeling.json` (fixture baru; isi identitas data ditetapkan tim FE).
- Data Pre-setup #12 dan #13 (Company Alpha; hanya dibaca, tidak diubah). Label `Finance Department` (`#3B82F6`, Total Asset 5) memiliki lima aset aktif berikut; `Scanner Zebra - 6` (Deleted) terpasang label yang sama dan tidak dihitung:

  | Aset | Asset ID | Status | Brand | Model/Type | Group | Category | Label lain | Last Updated |
  |---|---|---|---|---|---|---|---|---|
  | `Laptop Dell - 1` | `AST-0001` | `Available` | `Dell` | `Latitude 5440` | `Head Office > Floor 1` | `IT Equipment > Laptop` | `High Priority` | 14 Sep 2026 09:00 |
  | `Laptop Dell - 2` | `AST-0002` | `Borrowed` | `Dell` | `Latitude 5440` | `Head Office > Floor 2` | `IT Equipment > Laptop` | - | 13 Sep 2026 09:00 |
  | `Printer HP - 3` | `AST-0003` | `Draft` | `HP` | `LaserJet Pro` | `Head Office` | `Printer` | `Audit Ready`, `Maintenance Due` | 12 Sep 2026 09:00 |
  | `Monitor LG - 4` | `AST-0004` | `Waiting for Approval` | `LG` | `UltraWide 34` | `Head Office` | `Monitor` | - | 11 Sep 2026 09:00 |
  | `Projector Epson - 5` | `AST-0005` | `Disposed` | `Epson` | `EB-X49` | `Warehouse` | `Projector` | - | 10 Sep 2026 09:00 |

- Data Dinamis: tidak ada. Spec tidak membuat atau mengubah data backend.
- Tabel "Kolom Hideable" (parameter langkah berulang 3 sampai 4 dan 6 sampai 7): `Name`, `Asset ID`, `TAG`, `Brand`, `Model/Type`, `Group`, `Status`.
- State global yang diubah: konfigurasi kolom Setup Column Drawer Tagged Asset (disimpan lewat `[Save]`). Dipulihkan dengan menyimpan kedelapan kolom Hideable pada langkah 14 dan oleh hook `after` suite (hapus preferensi kolom di browser; kemampuan disediakan tim FE).
- Kemampuan teknis: muat ulang halaman dengan F5 (`beforeunload` tidak dipicu karena tidak ada form dirty).

## Test Steps

### TC-FA-LBL-364: Setup Column Drawer: ceklis dan unceklis kelas Hideable

1. Klik chip `Finance Department` di kolom Label
2. Klik header kolom Actions (⋯) Drawer, lalu klik `Setup Column...`
3. Untuk setiap kolom pada tabel "Kolom Hideable" (langkah 3 sampai 4): hapus centang kolom tersebut pada daftar Setup Column
4. Verifikasi kolom tersebut langsung hilang dari Live Preview
5. Verifikasi hanya `Last Updated` tersisa di Live Preview
6. Untuk setiap kolom pada tabel "Kolom Hideable" (langkah 6 sampai 7): centang kembali kolom tersebut pada daftar Setup Column
7. Verifikasi kolom tersebut muncul kembali di Live Preview pada posisi semula
8. Hapus centang `Last Updated`, klik `[Save]`
9. Tutup Drawer dengan `[✕]`, tekan F5, lalu klik chip `Finance Department` di kolom Label (membuka Drawer kembali)
10. Verifikasi `Last Updated` tidak tampil dan tetap tersembunyi setelah reload
11. Verifikasi ketujuh kolom lain tampil
12. Klik header kolom Actions (⋯) Drawer, lalu klik `Setup Column...`
13. Centang `Last Updated`, klik `[Save]`
14. Verifikasi kedelapan kolom Hideable tampil

## Notes

- Mode: FE+BE (backend nyata; konfigurasi kolom tersimpan di browser). Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`, section 4c (Drawer Tagged Asset).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah berulang (bagian 8b butir 7): tujuh kolom Hideable dengan parameter di tabel "Kolom Hideable" pada Prerequisites, tanpa langkah bersyarat. Langkah yang diulang: hapus centang beserta `Verifikasi` hilang dari Live Preview (langkah 3 sampai 4), dan centang kembali beserta `Verifikasi` muncul kembali (langkah 6 sampai 7). Ambang langkah dihitung dengan ekspansi (tujuh kali dua langkah pada tiap putaran), sehingga spec berisi sekitar 38 langkah. Alasan melewati sekitar 35 langkah: spec berisi satu TC (satu TC satu spec) dengan satu kelas harness dan satu dataset, jadi tidak dapat dibagi.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): menutup Drawer, F5, dan membuka Drawer kembali. `[Save]` Setup Column adalah aksi sisi klien (bagian 8b butir 8).
- Pembagian TC lintas spec: TC-FA-LBL-362, TC-FA-LBL-363, TC-FA-LBL-365, dan TC-FA-LBL-369 ada di spec 099; TC-FA-LBL-366 ada di spec 101; TC-FA-LBL-367 dan TC-FA-LBL-368 ada di spec 100.
- Temuan untuk QA:
  - TC-FA-LBL-364 menyatakan kolom hilang 'langsung' dari Live Preview; spec mengasersi tiap kolom satu per satu sesuai langkah TC.
  - Langkah penutupan Drawer pada TC-FA-LBL-364 menutup Drawer, memuat ulang, dan membuka kembali Drawer tanpa menyebut label yang dibuka; spec memakai `Finance Department` seperti langkah pembukaan Drawer pertama.
