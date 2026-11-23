---
id: TC-FA-FAAC-E2E-213-log-edit-end-of-life-treatment-tiga-surface
title: "Log Edit End-of-Life Treatment: Teks Opsi pada Old Value dan New Value di Changelog, System Log, dan Activity Log"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-733
sourceRules: ["FLD-33", "FAAC-LOGIC-02h", "L-02"]
smoke: []
dependsOn: []
trace:
  "FLD-33": [9, 13, 17, 20]
  "FAAC-LOGIC-02h": [9, 17, 20]
  "L-02": [8, 9, 16, 17, 19, 20]
coverage:
  web: automated
---

# Log Edit End-of-Life Treatment: Teks Opsi pada Old Value dan New Value di Changelog, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Nama tampil akun pada kolom Modified By: `Rina W` (format [First Name] [Last Initial], menurut TC-541 sampai TC-550). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data Pre-setup bernama literal (seed idempotent, dipulihkan ke nilai awal oleh fixture BE di hook `before` dan `after`): Asset Class `B-EOLLOG` (belum dipakai aset; Method `Declining Balance`, Useful Life 48, Declining Rate 50, End-of-Life Treatment `Switch to straight-line`, Tax Depreciation Class `Bukan bangunan – Kelompok 1`, Tax Method `Declining Balance`). Nilai mengacu ke `Fixture.fixed-asset-asset-class.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Data Dinamis: tidak ada. Spec mengubah End-of-Life Treatment `B-EOLLOG` menjadi `Keep depreciating`; nilai dipulihkan fixture BE.
- Kemampuan teknis (disediakan tim FE/BE): kemampuan baca jumlah entri Changelog, System Log aktor, dan Activity Log FAMS dibaca tepat sebelum aksi pemicu (audit trail permanen, total tidak diturunkan dari seeding, S-12); fixture BE untuk seed dan pemulihan.
- State global: entri Changelog, System Log, dan Activity Log yang tercatat adalah audit trail permanen dan tidak dipulihkan.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di `suite.md`.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

1. Catat jumlah entri Changelog (Nc), System Log aktor (Ns), dan Activity Log FAMS (Na) sebagai baseline lewat kemampuan baca log
2. Ketik Search `B-EOLLOG`, tekan Enter
3. Klik link Class Code `B-EOLLOG` di tabel
4. Klik tab `Depreciation`
5. Ubah End-of-Life Treatment menjadi `Keep depreciating` lalu klik `Save`
6. Tunggu aksi selesai
7. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
8. Verifikasi jumlah entri Changelog bertambah tepat 1 dari Nc
9. Verifikasi baris Changelog: Action `Edit`, Class Code `B-EOLLOG`, Field `End-of-Life Treatment`, Old Value `Switch to straight-line`, New Value `Keep depreciating`, Modified By `Rina W`
10. Klik icon Filter di modal
11. Buka dropdown Field
12. Ketik `End-of-Life` di kotak search dropdown Field
13. Verifikasi opsi Field memuat `End-of-Life Treatment`
14. Tutup modal Changelog
15. Buka Global Settings > User > Detail User milik aktor > Tab System Log
16. Verifikasi jumlah entri System Log bertambah tepat 1 dari Ns
17. Verifikasi baris teratas System Log: Action `Edit`, Object `Asset Class`, Name `B-EOLLOG`, Field `End-of-Life Treatment`, Old Value `Switch to straight-line`, New Value `Keep depreciating`
18. Buka Activity Log FAMS
19. Verifikasi jumlah entri Activity Log bertambah tepat 1 dari Na
20. Verifikasi baris teratas Activity Log: Action `Edit`, Object `Asset Class`, Name `B-EOLLOG`, Field `End-of-Life Treatment`, Old Value `Switch to straight-line`, New Value `Keep depreciating`, Modified By `Rina W`

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (TC-FA-FAAC-733). Tidak ada TC hanya-BE di spec ini. Klausa log yang diasersi di sini adalah klausa presence (entri Edit tercatat); tidak ada klausa "tidak ada log" pada TC-733.
- Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1 (baseline log, S-12), langkah 2 (Search untuk menemukan baris target, R-16 dan bagian 8b butir 13), langkah 6 ("Tunggu aksi selesai" sesudah aksi tulis yang hasilnya tidak diasersi langsung, sebelum membuka log, bagian 8b butir 8), dan langkah 14 (menutup modal Changelog). Langkah 7, 15, dan 18 membuka Changelog, System Log, dan Activity Log sebagai langkah observasi TC.
- Entri baru dibaca pada baris teratas urutan default `Date` terbaru setelah selisih jumlah dari baseline dibuktikan (S-14).
- Langkah 11 dan 12 mengikuti bagian 8b butir 15c: opsi dropdown Field pada surface audit trail permanen diasersi sesudah mengetik di kotak search dropdown; TC-733 hanya menyebut "buka dropdown Field", sehingga langkah 12 adalah langkah penghubung tanpa `Verifikasi`.
- Pengecualian nama literal (S-06, S-12; pengecualian beralasan yang disetujui user): `B-EOLLOG` adalah seed bertanda `B-*` per TC yang dipakai apa adanya dan dipulihkan fixture BE.
- Temuan untuk QA: (a) TC-733 butir a menyebut Modified By "aktor"; spec memakai nama tampil `Rina W` seperti spec log lain di suite ini. (b) TC-733 tidak menyebut cara membuka Filter modal Changelog; spec memakai icon Filter di modal seperti spec Changelog lain. (c) TC-733 butir c dan d menyebut kolom System Log dan Activity Log tanpa menyebut kolom Modified By pada System Log; spec hanya mengasersi kolom yang disebut.
