---
id: TC-FA-GRP-E2E-018-group-manager-scope-region-west-sidebar-ancestor-context-dan-metrik-exact-match
title: "Group Manager Scope Region West: Sidebar Scope + Ancestor Context, Ancestor Tidak Bisa Dipilih, Metrik Exact-Match, dan Node di Luar Scope"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-56
  - TC-FA-GRP-57
  - TC-FA-GRP-61
  - TC-FA-GRP-74
coverage:
  web: automated
---

# Group Manager Scope Region West: Sidebar Scope + Ancestor Context, Ancestor Tidak Bisa Dipilih, Metrik Exact-Match, dan Node di Luar Scope

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Group Manager scope Region West (Pre-setup No 4) `groupManagerGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GM_PASSWORD`.
- Login di hook `before` spec ini sebagai Group Manager; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `fa-settings-groups` untuk akun Group Manager disetel `seen` di hook `before` spec ini dan dipulihkan di hook `after` (kemampuan disediakan tim FE/BE); hook suite hanya menyetel akun aktor default suite.
- Data Pre-setup (hanya dibaca, tidak diubah): pohon group baku Tabel A (Pre-setup No 9): Global HQ > Region West > Branch West 1 > Room 301; Region East (di luar scope). Region West 0 aset langsung dan Branch West 1 punya 3 aset aktif (precondition TC-FA-GRP-61).
- Kemampuan teknis: fixture BE dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah data maupun state global.

## Test Steps

### TC-FA-GRP-56: Sidebar menampilkan scope, descendant aktif, dan ancestor context

1. Klik toggle expand-all pada sidebar
2. Verifikasi Region West, Branch West 1, dan Room 301 tampil normal dengan elipsis
3. Verifikasi Global HQ (ancestor) greyed-out tanpa elipsis, dengan spacer sehingga dot tetap sejajar
4. Verifikasi Region East tidak tampil sama sekali

### TC-FA-GRP-57: Ancestor context tidak dapat dipilih

5. Catat isi tabel dan node terpilih saat ini
6. Hover Global HQ
7. Verifikasi tooltip `You don't have access to this group — shown for context only.`
8. Klik Global HQ
9. Verifikasi klik tidak memilih node: node `All Groups` tetap terpilih
10. Verifikasi Group Context Header tidak berubah menjadi Global HQ
11. Verifikasi tabel tidak berubah dari keadaan yang dicatat pada langkah 5
12. Verifikasi Global HQ tidak pernah muncul sebagai baris tabel

### TC-FA-GRP-61: Metrik aktor scoped tetap exact-match

13. Klik Region West di sidebar
14. Verifikasi Total Asset di header Region West `0` (exact-match, bukan 3)
15. Verifikasi baris Branch West 1 di tabel menampilkan Total Asset `3`

### TC-FA-GRP-74: Node di luar scope tidak ditemukan

16. Ketik Search sidebar `Region East`, tekan Enter
17. Verifikasi area tree menampilkan `No results found`
18. Verifikasi Region East tidak ditemukan pada tree
19. Klik `✕` pada Search sidebar, tekan Enter

## Notes

- Spec 19 langkah, di bawah batas sekitar 35 langkah.
- Langkah penghubung (S-03): langkah 1 (expand-all), langkah 5 (mencatat keadaan sebagai pembanding langkah 11), langkah 13 (memilih Region West), langkah 19 (mengosongkan Search sidebar).
- Urutan TC dalam spec: 56, 57, 61, 74.
- Temuan untuk QA:
  - TC-FA-GRP-57 butir b menyebut "tabel tidak berubah" tanpa isi; spec memakai pembanding yang dicatat sebelum klik.
  - TC-FA-GRP-74 menyebut "Region East tidak ditemukan (tidak dikembalikan API)"; spec mengasersi dari sisi UI (`No results found`) dan tidak membaca respons API (bagian 8b butir 1 tidak berlaku karena langkahnya lewat browser).
