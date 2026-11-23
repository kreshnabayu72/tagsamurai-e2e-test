# Serah-terima FE/BE/QA: spec Fixed Asset > Settings > Accounting (2026-11-23)

Dibuat setelah arsip modul Accounting Period dan penambahan End-of-Life Treatment. Daftar ini hanya
menunjuk; teks lengkap tiap butir ada di `## Notes` (bagian "Temuan untuk QA") spec yang disebut.
Semua spec berstatus `draft`; butir di sini adalah syarat sebelum bisa dijalankan.

Cakupan suite: `FixedAsset/SettingsAccountingPreferences` (spec baru 181-185 untuk V-10 dan threshold), `FixedAsset/AssetClass` (spec 207-215 baru),
`FixedAsset/TaxDepreciationClass` (spec 279-289 baru).

## A. Fixture dan seed (FE/BE)

| # | Kebutuhan | Spec |
|---|---|---|
| A-1 | Berkas `fixtures/fixed-asset-asset-class.json` (belum ada); kunci ditetapkan FE | AssetClass 207-215 |
| A-2 | Seed idempotent Asset Class literal: `B-EOLSWAP`, `B-EOLUSED`, `B-EOLLOG`, `B-V39`, dan data spec 209; dipulihkan di hook `before` dan `after` | AssetClass 209-211, 213-215 |
| A-3 | Seed Tax Depreciation Class literal: `DBE-01` s.d. `DBE-17`, `R-API1` s.d. `R-API4`, `LAND3`; hook `before` menghapus sisa run lama | TDC 279-288 |
| A-4 | Master Tax Depreciation Class `Bukan bangunan – Kelompok 3` dan `Kelompok 1` beserta nilai End-of-Life Treatment fiskal (TC tidak menyebut nilainya) | AssetClass 208, 209 |
| A-5 | Plan Multi Depreciation (Enterprise), Max depreciation methods minimal 2 | AssetClass 209 |
| A-6 | Kemampuan fixture: atur dan pulihkan Exported through; Run Posted; baca jumlah baris Changelog, System Log, Activity Log | Preferences 017, 067-069, 072, 079, 087; TDC 073, 075, 127, 204, 221, 223, 262, 271 |
| A-7 | Nilai awal Exported through yang dipakai spec adalah tebakan penulis spec; mohon tetapkan: 127 = Nov 2026; 221 dan 262 = belum mencapai Des 2026; 223 dan 271 = Nov 2025 | TDC 127, 221, 223, 262, 271 |
| A-8 | Fixture harus bisa memundurkan atau mengosongkan Exported through (urutan Des 2026, Nov 2026, kosong) | TDC 073 |
| A-9 | Seed Pre-setup PC-23 sampai PC-31 (Opening balance aset lama, status Damaged dan Missing, New value change dibatalkan, Disposal Posted, Disposal Executed 15 Mei 2026, Depreciation Run belum Posted); TC tidak menyebut cara seed | Preferences 039, 045-048, 071, 080, 181-184 |
| A-10 | Akun Budi Santoso (Manage accounting): email dan password tidak ada di TC | Preferences 149 |

## B. Fakta UI dan API yang TC tidak sebut (FE)

| # | Pertanyaan | Spec |
|---|---|---|
| B-1 | Label tombol di dialog Apply Changes (spec memakai `Apply`) | AssetClass 211 |
| B-2 | Apakah Drawer Create/Edit dan dialog D-09 tertutup setelah `[Submit]`/`[Apply]` sukses | TDC 282-285; AssetClass 209-211 |
| B-3 | Apakah `[Clear Field]` lalu `[×]` memunculkan Unsaved Changes; apakah `[Clear Field]` juga mengosongkan Asset Type dan Allowed Methods | TDC 281 |
| B-4 | Apakah dropdown tertutup setelah memilih opsi yang sudah terpilih | TDC 279 |
| B-5 | Bentuk visual indikator wajib pada label End-of-Life Treatment | AssetClass 207 |
| B-6 | Teks yang diketik pada field read-only dan nilai End-of-Life Treatment fiskal pada master | AssetClass 208 |
| B-7 | Status HTTP penolakan request langsung (V-39 Asset Class; request ditolak pada TDC) dan pesan untuk nilai EoL `Switch to declining` | AssetClass 214, 215; TDC 287, 288 |
| B-8 | Endpoint dan bentuk request untuk request langsung (tidak ada di TC/PRD/LLD) | AssetClass 214, 215; TDC 287, 288 |
| B-9 | Cara membuka Filter modal Changelog dan nilai Modified By pada log | AssetClass 213 |
| B-10 | Pesan V-17 untuk nilai dengan lebih dari 2 desimal (TC-956) | TDC 287 |
| B-11 | Action dan nilai kolom log L-01 pada TC-958 | TDC 286 |
| B-12 | Email akun Total Control dan identitas company uji (TC tidak menulisnya) | TDC 279-289 |
| B-13 | Env var password aktor (`Spectra.env.FA_TC_PASSWORD`, nama perlu dikonfirmasi) | Preferences (semua) |
| B-14 | Apakah perubahan Default Capitalization Threshold saja memunculkan dialog Save Changes (TC-643 langkah 3 ya; spec 054 dan 056 tidak). Spec 185 langkah 9 mengikuti TC dan dihapus bila tidak ada dialog | Preferences 185, 054, 056 |
| B-15 | Layar tempat mengamati Accounting Treatment aset (daftar atau Detail) dan menu daftar aset yang dipakai TC-643 | Preferences 185 |
| B-16 | Nama kolom tanggal pada Disposal non-Executed (TC-635, 636 hanya menulis "bertanggal") | Preferences 182 |
| B-17 | Tanggal aksi 20 Mei 2026 pada TC-432/433: diatur lewat kendali jam atau input modul pemilik (Assign/Borrow) | Preferences 139 |

## C. Keputusan QA

| # | Butir | Rujukan |
|---|---|---|
| C-1 | Pengecualian Class Code literal tanpa suffix `{runId}` (batas 15 karakter) | `docs/e2e-conventions.md` A-21 `[USULAN]` |
| C-2 | Effective From "Jan 2026" pada TC TDC 946-949, 951, 953, 954 mengasumsikan tahun pajak 2026 belum tertutup (Exported through belum mencapai Des 2026) | TDC 284, 285, 286 |

## D. Keputusan pemilik TC/PRD

| # | Butir |
|---|---|
| D-1 | Kalender periode (Derived view, `FAPREF-LOGIC-02p`) tidak punya layar sendiri. TC-522 dan TC-412 sudah diselaraskan dengan itu; spec 080 dan 134 mengikuti. Konfirmasi bahwa tidak akan ada layar pengamatan kalender. |
| D-2 | TC-394, 395, 510 menyebut kalender hanya di kolom Post Condition (state); spec 131 tidak mengasersi isi kalender. Konfirmasi cukup begitu, atau tambahkan cara pengamatan di PRD. |
| D-3 | Langkah tambahan di luar TC: AssetClass 100 (langkah 11-15 penutup dialog) dan Preferences 131 (dua langkah baseline Changelog). Setujui atau minta dihapus. |
| D-5 | Spec 139: `caseType` masih Positive padahal TC-432 dan 433 Negative (TC-431 Positive). Tentukan jenis kasus spec campuran. |
| D-6 | TC-643 langkah 3 (dialog Save Changes untuk threshold saja) bertentangan dengan pola spec 054 dan 056; pemilik TC menetapkan salah satunya (lihat B-14). |
| D-7 | `FAPREF-LOGIC-03d` dirujuk TC-605 tetapi tidak ada langkah yang menguji khusus rule itu; spec 149 tidak memasukkannya ke `sourceRules`. |
| D-8 | Folder/id spec 045-048 masih memuat "transaksi-bertanggal" (V-10 kini "catatan berefek akuntansi terawal"). Bagian dari D-4. |
| D-4 | Slug folder/id spec yang masih memuat istilah lama (mis. "pembangunan-ulang-periode", "closed", "lost") tidak diganti. Putuskan apakah id perlu diganti (mengubah id di spec, coverage, dan mapping). |
