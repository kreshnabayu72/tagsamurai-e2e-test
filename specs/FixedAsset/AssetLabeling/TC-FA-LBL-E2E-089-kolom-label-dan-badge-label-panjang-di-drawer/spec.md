---
id: TC-FA-LBL-E2E-089-kolom-label-dan-badge-label-panjang-di-drawer
title: "Kolom Label dan Badge Label Panjang di Drawer"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-370
  - TC-FA-LBL-371
  - TC-FA-LBL-501
coverage:
  web: automated
---

# Kolom Label dan Badge Label Panjang di Drawer

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

- Data Pre-setup #22 (hanya dibaca, di Company Extra, Pre-setup #56): label 120 karakter `Fixture.assetLabeling.labelPanjang120` (kata `Alpha` dipisah spasi tunggal dan ditutup akhiran unik per run `{runId}-22`, `{runId}` hanya digit; total tepat 120 karakter termasuk akhiran) terpasang pada aset `Laptop Dell - 8`.
- Akun ganti: Total Control Company Extra (Pre-setup #56: salinan label Pre-setup #12 plus seed tambahan), `Fixture.assetLabeling.akun.totalControlExtra`. Nama company, email akun (pola `totalControl_automated_{namaCompany}@qwertysystem.net`), dan nama env password belum ada, disediakan tim FE; tidak diisi di spec. Dipakai pada langkah 15 sampai 17 (ganti akun, S-07). Hook `after` suite mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`).
- Data Dinamis: tidak ada. Spec tidak membuat atau mengubah data backend.
- State global yang diubah: konfigurasi kolom Setup Column Drawer Tagged Asset (kolom `Label` ditampilkan pada langkah 3 dan dipulihkan pada langkah 13, lalu ditampilkan lagi pada langkah 20 dan dipulihkan pada langkah 24); hook `after` suite menghapus preferensi kolom di browser sebagai cadangan, bukan `[Reset to Default]`.

## Test Steps

### TC-FA-LBL-370: Kolom Label di Drawer: 1-2 badge lalu +N more dan popover Labels

1. Klik chip `Finance Department` di kolom Label
2. Klik header kolom Actions (⋯) Drawer, lalu klik `Setup Column...`
3. Centang `Label`, lalu klik `[Save]`
4. Verifikasi baris `Printer HP - 3` menampilkan dua badge berwarna hex label berurut A-Z (`Audit Ready`, `Finance Department`)
5. Verifikasi baris `Printer HP - 3` menampilkan chip `+1 more` sesudah kedua badge
6. Klik chip `+1 more`
7. Verifikasi popover `Labels` berisi `Audit Ready`, `Finance Department`, `Maintenance Due` berurut A-Z
8. Tutup popover `Labels` dengan menekan Esc

### TC-FA-LBL-501: Kolom Label Drawer: aset dengan 1 dan 2 label menampilkan badge tanpa chip +N more

9. Verifikasi `Laptop Dell - 2` menampilkan satu badge `Finance Department`
10. Verifikasi `Laptop Dell - 2` tanpa chip `+N more`
11. Verifikasi `Laptop Dell - 1` menampilkan dua badge berurut A-Z `Finance Department` lalu `High Priority`
12. Verifikasi `Laptop Dell - 1` tanpa chip `+N more`
13. Pulihkan konfigurasi kolom: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, klik `[Reset to Default]`, lalu klik `[Save]`
14. Klik icon `[✕]` pada Drawer

### TC-FA-LBL-371: Chip Label panjang pada kolom Label Drawer mengikuti truncation badge kontekstual

15. Ganti akun: logout dari Total Control Company Alpha
16. Login sebagai Total Control Company Extra (`Fixture.assetLabeling.akun.totalControlExtra`)
17. Buka Fixed Asset > Settings > Asset Master > tab Labels
18. Ketik Search `Fixture.assetLabeling.labelPanjang120` di kotak Search Labels List, tekan Enter
19. Klik chip label 120 karakter di kolom Label
20. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, centang `Label`, lalu klik `[Save]`
21. Verifikasi badge label pada `Laptop Dell - 8` menampilkan 12 huruf pertama (`Alpha Alpha `) + `..` + 12 huruf terakhir nama yang berakhir pada akhiran `{runId}-22`
22. Hover badge label pada `Laptop Dell - 8`
23. Verifikasi tooltip menampilkan nama penuh 120 karakter (`Fixture.assetLabeling.labelPanjang120`)
24. Pulihkan konfigurasi kolom: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, klik `[Reset to Default]`, lalu klik `[Save]`
25. Tutup Drawer dengan `[✕]`, lalu klik `(←)` pada kotak Search Labels List

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`, section 4c (Drawer Tagged Asset).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah TC-FA-LBL-501 yang menampilkan kolom `Label` lewat Setup Column tidak diulang: konfigurasi kolom dari langkah 3 tersimpan di browser dan mencentang ulang `Label` akan menyembunyikannya. Konfigurasi dipulihkan ke default di langkah 13 sebelum ganti akun, lalu TC-FA-LBL-371 menampilkan kolom `Label` sendiri (langkah 20) sesuai langkah TC, sehingga tidak bergantung pada apakah preferensi kolom browser bertahan lintas login (S-09).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): menutup popover `Labels`; menutup Drawer sebelum membuka label lain; Search label 120 karakter pada Labels List untuk menemukan baris target (label tambahan Pre-setup #22 mungkin tidak berada di halaman pertama); ganti akun ke Company Extra (langkah 15 sampai 17, S-07); pemulihan konfigurasi kolom (langkah 13 dan 24); membersihkan Search Labels List di langkah terakhir. `[Save]` Setup Column adalah aksi sisi klien (bagian 8b butir 8).
- Urutan TC: TC-FA-LBL-370 dan TC-FA-LBL-501 memakai satu pembukaan Drawer label `Finance Department` di Company Alpha (tanpa perubahan state); TC-FA-LBL-371 memakai Drawer label lain di Company Extra sehingga ditaruh terakhir.
- Pembagian TC lintas spec: TC-FA-LBL-490 dan TC-FA-LBL-491 (truncation badge Brand, Model/Type, Group, Category) ada di spec 169.
- Temuan untuk QA:
  - TC-FA-LBL-371 tidak menyebut apakah aset `Laptop Dell - 8` memiliki label lain; spec mengasersi badge label 120 karakter pada baris itu.
  - TC-FA-LBL-371 Expected a menyebut 12 huruf terakhir hanya sebagai 'nama yang berakhir pada akhiran `{runId}-22`'; spec mengasersi 12 huruf pertama literal dan 12 huruf terakhir dari nama fixture, tanpa literal `{runId}`.
