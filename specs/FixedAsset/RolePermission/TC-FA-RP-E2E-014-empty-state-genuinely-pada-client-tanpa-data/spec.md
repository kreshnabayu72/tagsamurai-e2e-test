---
id: TC-FA-RP-E2E-014-empty-state-genuinely-pada-client-tanpa-data
title: "Empty state genuinely pada client tanpa data"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-15
  - TC-FA-RP-46
  - TC-FA-RP-48
  - TC-FA-RP-49
  - TC-FA-RP-50
  - TC-FA-RP-51
  - TC-FA-RP-53
  - TC-FA-RP-54
coverage:
  web: automated
---

# Empty state genuinely pada client tanpa data

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control `Company Kosong` (Pre-setup #27); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`). Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `FA_TC_PASSWORD`).
- Akun aktor (password hanya lewat env):

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Total Control pada `Company Kosong` | #27 | disediakan tim FE (email tidak tertulis di Pre-setup TC; lihat Temuan untuk QA) | `Spectra.env.FA_EMPTY_TC_PASSWORD` |

- Data Pre-setup: #27 (`Company Kosong`: hanya Default User dan Total Control; tanpa Read Only, Group Manager, penugasan Role Transaksi, penugasan Group Role atau Global Role individual, dan tanpa entri log) dan #18 (node `IT Infrastructure` untuk TC-FA-RP-50 dan TC-FA-RP-51, disediakan tim FE pada `Company Kosong` tanpa penugasan; lihat Temuan untuk QA). Seluruh user eligible company itu sudah berstatus Total Control atau Default User (precondition TC-FA-RP-54).
- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun dan nama group ditambahkan tim FE.
- Kemampuan teknis: akun Total Control `Company Kosong` dan node `IT Infrastructure` tanpa penugasan pada company itu disediakan tim FE; jumlah user pemegang baris pola Group Role (Default User dan Total Control) pada `Company Kosong` dibaca lewat kemampuan baca state yang disediakan tim FE/BE (tanpa endpoint karangan) untuk langkah 13. Spec hanya membaca; tidak mengubah data atau state global.

## Test Steps

### TC-FA-RP-46 dan TC-FA-RP-53: Tab Read Only kosong dan Modal Changelog kosong

1. Klik Tab `Read Only`
2. Verifikasi Illustration dengan Title `No users assigned` dan Description `Assign users to grant permissions for this role.`
3. Klik ikon `Changelog` pada toolbar Tab Read Only
4. Verifikasi modal menampilkan Illustration dengan Title `No changelog yet` dan Description `Activities and changes will appear here.`
5. Klik `[✕]` untuk menutup modal Changelog

### TC-FA-RP-49: Tab Group Manager kosong

6. Klik Tab `Group Manager`
7. Verifikasi Illustration dengan Title `No group managers yet` dan Description `Assign group managers to delegate administrative control.`

### TC-FA-RP-54: Popup Assign tanpa kandidat

8. Klik Tab `Total Control`, lalu klik `[+ Assign]`
9. Verifikasi popup tetap terbuka dengan Illustration, Title `All eligible users have been assigned`, dan Description `There are no additional eligible users available to select.`
10. Klik `[✕]` untuk menutup popup

### TC-FA-RP-15 dan TC-FA-RP-48: Tab System dan Detail Role tanpa penugasan individual

11. Klik Tab `System`
12. Verifikasi sedikitnya satu baris Group Role tampil
13. Verifikasi seluruh baris Group Role selain `Manage user & role` menampilkan Users sama dengan jumlah user pemegang baris pola pada `Company Kosong` (Default User dan Total Control), bukan `0`, tanpa penugasan individual yang menambah hitungan
14. Verifikasi baris `Manage user & role` menampilkan Users `0` karena dikecualikan dari pola (`FARP-LOGIC-24`)
15. Klik Role Name `Manage Open API` pada section Global Role
16. Verifikasi Illustration dengan Title `No users assigned` dan Description `Assign users to grant them access with this capability.`

### TC-FA-RP-50 dan TC-FA-RP-51: Tabel Role Transaksi kosong

17. Klik Tab `Transaction Role`, klik node `IT Infrastructure`, lalu klik sub-tab `Disposal`
18. Verifikasi section Approver tampil dengan Illustration, Title `No approvers assigned`, dan Description `Assign approvers to handle approval workflows for this transaction.`
19. Verifikasi section Approver tetap tampil
20. Verifikasi section Asset Admin menampilkan Title `No Asset Admin assigned` dengan Description `Assign users to this role for this transaction.`
21. Verifikasi section Monitoring & Report menampilkan Title `No Monitoring & Report assigned` dengan Description `Assign users to this role for this transaction.`
22. Verifikasi section Staff menampilkan Title `No Staff assigned` dengan Description `Assign users to this role for this transaction.`

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-15, 46, 48, 49, 50, 51, 53, 54). Empty state hasil pencarian kosong ada di spec `TC-FA-RP-E2E-015-empty-state-hasil-pencarian-kosong-per-permukaan-1` dan `TC-FA-RP-E2E-016-empty-state-hasil-pencarian-kosong-per-permukaan-2`.
- Urutan TC di spec berbeda dari urutan TC sumber supaya tab dikunjungi sekali: Read Only (TC-FA-RP-46, 53), Group Manager (TC-FA-RP-49), popup Assign Tab Total Control (TC-FA-RP-54), Tab System (TC-FA-RP-15, 48), lalu Transaction Role (TC-FA-RP-50, 51).
- Langkah penghubung (tanpa awalan `Verifikasi`): klik tab, node, dan sub-tab; membuka Detail Role; membuka popup `[+ Assign]`; menutup modal dan popup dengan `[✕]`.
- Asersi universal Users pada baris Group Role Tab System (langkah 13) didahului `Verifikasi` sedikitnya satu baris Group Role tampil (langkah 12, 8b butir 2).
- Temuan untuk QA:
  - TC-FA-RP-50 dan TC-FA-RP-51 merujuk Pre-setup #27 dan #18 dan memakai node `IT Infrastructure`, sedangkan #27 (`Company Kosong`) hanya memuat Default User dan Total Control; TC-FA-RP-34 memakai company tanpa node group. Spec mengasumsikan `Company Kosong` memiliki node `IT Infrastructure` tanpa penugasan; QA mengonfirmasi data yang berlaku dan hubungannya dengan TC-FA-RP-34.
  - Akun Total Control `Company Kosong` tidak tertulis di Pre-setup TC dan disediakan tim FE.
  - TC-FA-RP-15 memakai Pre-setup #27 untuk Tab System walau section Group Role katalog ada pada semua company; spec memverifikasi seluruh baris Group Role pada `Company Kosong` (selain `Manage user & role`, yang berhitung `0`). Expected TC-FA-RP-15 diberi tanda "selaraskan setelah PRD final" dan tidak menyebut angka jumlah pemegang pola.
  - TC-FA-RP-53 membuka Changelog dari toolbar Tab Read Only walau precondition menyebut Tab Total Control; spec mengikuti langkah TC (Tab Read Only).
  - Post Condition TC-FA-RP-15, 46, 48, 49, 50, 51, 53, dan 54 tidak memberi langkah observasi tambahan; tidak diasersi.
