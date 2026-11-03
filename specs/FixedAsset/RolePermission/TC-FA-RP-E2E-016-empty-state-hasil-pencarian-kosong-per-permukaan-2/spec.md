---
id: TC-FA-RP-E2E-016-empty-state-hasil-pencarian-kosong-per-permukaan-2
title: "Empty state hasil pencarian kosong per permukaan (2/2)"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-59
  - TC-FA-RP-60
  - TC-FA-RP-61
  - TC-FA-RP-62
coverage:
  web: automated
---

# Empty state hasil pencarian kosong per permukaan (2/2)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control Company Alpha (Pre-setup #2); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`). Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `FA_TC_PASSWORD`).
- Akun aktor (password hanya lewat env); urutan baris = urutan pemakaian:

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Total Control (Siti Rahmawati), Company Alpha | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |
| Total Control pada `Company Changelog` | #24 | disediakan tim FE (email tidak tertulis di Pre-setup TC; lihat Temuan untuk QA) | `Spectra.env.FA_CHANGELOG_TC_PASSWORD` |

- Data Pre-setup: #15 (pool pengguna), #18 (pohon group), #19 (seed Role Transaksi pada `IT Infrastructure` sub-tab Disposal: Asset Admin Nadia Putri dan Approver Pandu Wijaya), #24 (`Company Changelog`: log 25 entri campuran, Total Control dan Read Only).
- Data uji: keyword Search `zzzz`; tidak menghasilkan baris pada permukaan mana pun.
- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun dan keyword ditambahkan tim FE.
- Kemampuan teknis: akun Total Control `Company Changelog` disediakan tim FE. Spec hanya membaca; tidak mengubah data atau state global.

## Test Steps

### TC-FA-RP-62: Popup Assign, empty state hasil pencarian kosong

1. Klik `[+ Assign]` di Tab `Total Control`
2. Ketik Search `zzzz` pada popup, tekan Enter
3. Verifikasi Illustration dengan Title `No results found` dan Description `Try adjusting your search or filter.`
4. Verifikasi tabel tidak menampilkan baris
5. Klik `[✕]` untuk menutup popup

### TC-FA-RP-59: Tabel Approver, empty state hasil pencarian kosong

6. Klik Tab `Transaction Role`, klik node `IT Infrastructure`, lalu klik sub-tab `Disposal`
7. Ketik Search `zzzz` pada section Approver, tekan Enter
8. Verifikasi Illustration dengan Title `No results found` dan Description `Try adjusting your search or filter.`
9. Verifikasi tabel tidak menampilkan baris
10. Klik `(←)` pada kotak Search section Approver untuk menutup Search dan mereset tabel

### TC-FA-RP-60: Tabel Asset Admin, empty state hasil pencarian kosong

11. Ketik Search `zzzz` pada section Asset Admin, tekan Enter
12. Verifikasi Illustration dengan Title `No results found` dan Description `Try adjusting your search or filter.`
13. Verifikasi tabel tidak menampilkan baris
14. Klik `(←)` pada kotak Search section Asset Admin untuk menutup Search dan mereset tabel

### Ganti akun ke Total Control Company Changelog

15. Logout dari akun Total Control Company Alpha, lalu login sebagai Total Control `Company Changelog` dengan `Spectra.env.FA_CHANGELOG_TC_PASSWORD`
16. Buka menu Settings > Role & Permission dari sidebar

### TC-FA-RP-61: Modal Changelog, empty state hasil pencarian kosong

17. Klik ikon `Changelog` pada toolbar Tab Total Control
18. Ketik Search `zzzz` pada modal Changelog, tekan Enter
19. Verifikasi Illustration dengan Title `No results found` dan Description `Try adjusting your search or filter.`
20. Verifikasi tabel tidak menampilkan baris
21. Klik `[✕]` untuk menutup modal Changelog

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-59, 60, 61, 62). Spec ditulis per blok akun karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`); ganti akun pada langkah 15.
- Urutan TC di spec: TC-FA-RP-62, 59, 60 (Company Alpha), lalu TC-FA-RP-61 (`Company Changelog`); urutan dipilih supaya ganti akun hanya satu kali.
- Langkah penghubung (tanpa awalan `Verifikasi`): klik tab, node, dan sub-tab; membuka popup dan modal; menutup Search dengan `(←)` atau menutup popup dan modal dengan `[✕]`; ganti akun dan membuka menu.
- Temuan untuk QA:
  - TC-FA-RP-61 merujuk Pre-setup #24 (`Company Changelog`); akun Total Control company itu tidak tertulis di Pre-setup TC dan disediakan tim FE. Bila #24 hanya data pada Company Alpha, langkah ganti akun tidak diperlukan.
  - TC-FA-RP-59 dan TC-FA-RP-60 menyebut "Buka Search pada section"; spec memakai langkah Search atomik (ketik lalu Enter).
  - Post Condition TC-FA-RP-59, 60, 61, dan 62 tidak memberi langkah observasi tambahan; tidak diasersi.
