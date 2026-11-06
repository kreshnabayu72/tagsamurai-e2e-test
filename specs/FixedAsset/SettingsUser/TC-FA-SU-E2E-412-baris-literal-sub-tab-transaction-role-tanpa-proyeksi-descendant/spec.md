---
id: TC-FA-SU-E2E-412-baris-literal-sub-tab-transaction-role-tanpa-proyeksi-descendant
title: "Baris Literal Sub-tab Transaction Role per Node Penugasan: Descendant yang Hanya Tercakup Tidak Diproyeksikan sebagai Baris atau Badge"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1112
coverage:
  web: automated
---

# Baris Literal Sub-tab Transaction Role per Node Penugasan: Descendant yang Hanya Tercakup Tidak Diproyeksikan sebagai Baris atau Badge

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21: Region Jawa dengan anak Jakarta Selatan Distribution Center; Finance & Accounting dengan anak Accounts Payable).
- Pengguna target: Rina Susanti (Pre-setup #49 seed `FaUserOV`; tanpa Global Role dan Group Role; 5 baris Transaction Role, label `5 roles`): Disposal × Asset Admin (Region Jawa), Disposal × Approver (Region Jawa), Disposal × Monitoring & Report (Jakarta Selatan Distribution Center), Damaged × Staff (Finance & Accounting), Transfer × Monitoring & Report (Jakarta Selatan Distribution Center). Seed `FaUserOV` wajib disediakan tim FE/BE sebelum eksekusi.
- Rina Susanti juga akun aktor Read Only (Pre-setup #5, `Spectra.env.FA_MURG_RO_PASSWORD`); di spec ini hanya menjadi pengguna target dan tidak dipakai login.
- Data uji: Search `Jakarta` pada Table Tools Sub-tab Transaction Role; popup Assign Group baris Disposal × Asset Admin.
- Kemampuan teknis (disediakan tim FE/BE): seed `FaUserOV` (Pre-setup #49). Selektor badge Group dan node pohon disediakan tim FE.
- State global yang diubah: tidak ada data yang disimpan; popup ditutup lewat `[Cancel]`. Suite berjalan serial.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-1112: Sub-tab Transaction Role menampilkan baris literal per node penugasan: descendant yang hanya tercakup tidak diproyeksikan sebagai baris atau badge

1. Ketik Search `Rina Susanti`, tekan Enter, lalu klik Name `Rina Susanti`
2. Klik Tab Role lalu Sub-tab Transaction Role
3. Verifikasi tabel memuat tepat lima baris sesuai penugasan tersimpan: Disposal × Asset Admin (Region Jawa), Disposal × Approver (Region Jawa), Disposal × Monitoring & Report (Jakarta Selatan Distribution Center), Damaged × Staff (Finance & Accounting), dan Transfer × Monitoring & Report (Jakarta Selatan Distribution Center)
4. Verifikasi baris Disposal × Asset Admin menampilkan badge Group literal `Region Jawa` saja
5. Verifikasi baris Damaged × Staff menampilkan badge Group literal `Finance & Accounting` saja
6. Verifikasi Jakarta Selatan Distribution Center tidak muncul sebagai badge pada baris Disposal × Asset Admin
7. Verifikasi Accounts Payable tidak muncul pada baris Damaged × Staff
8. Verifikasi tidak ada baris tambahan untuk node yang hanya tercakup
9. Verifikasi Disposal × Monitoring & Report pada Jakarta Selatan Distribution Center tetap tampil sebagai baris sendiri walau ancestor-nya (Region Jawa) memegang Asset Admin (overlap tidak menggabungkan atau menyembunyikan baris)
10. Ketik Search `Jakarta`, tekan Enter
11. Klik `(←)` pada kotak Search
12. Klik `[Assign Group]` pada baris Disposal × Asset Admin
13. Verifikasi Region Jawa tercentang di popup
14. Verifikasi Jakarta Selatan Distribution Center tidak tercentang
15. Verifikasi Jakarta Selatan Distribution Center tidak Disabled
16. Klik `[Cancel]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1, 2, 11 dan 16. Search `Rina Susanti` pada langkah 1 menemukan baris target (R-16, R-23). Langkah 11 menutup kotak Search Table Tools dan mereset tabel sebelum langkah 12 mengandalkan baris Disposal × Asset Admin (S-09).
- Langkah 10 (Search `Jakarta`) adalah langkah TC tanpa Expected; spec tidak menambah asersi untuknya (S-02).
- Asersi "hanya `Region Jawa`" dan "hanya `Finance & Accounting`" (langkah 4, 5) dibuktikan oleh badge literal ditambah langkah 6 dan 7 sebagai pembanding yang dijamin tidak tampil (bagian 8b butir 2). Langkah 3 (lima baris) menjadi anchor positif bagi asersi tidak ada baris tambahan (langkah 8).
- Langkah 14 dan 15 mengasersi Jakarta Selatan Distribution Center pada popup yang sama dengan anchor Region Jawa tercentang (langkah 13). Popup Assign Group dibatalkan lewat `[Cancel]` tanpa perubahan data.
- Temuan untuk QA:
  - Seed #49 `FaUserOV` (Rina Susanti tanpa Global Role dan Group Role, 5 penugasan Transaction Role, label `5 roles`) wajib disediakan tim FE/BE. Rina Susanti juga akun aktor Read Only (Pre-setup #5): spec ini memakainya hanya sebagai target.
  - TC-FA-SU-1112 langkah 3 (Search `Jakarta` lalu hapus Search) tidak punya Expected, sehingga hasil penyaringan tidak diasersi; mohon dikonfirmasi apakah hasil Search per kolom Group perlu Expected.
  - TC-FA-SU-1112 Post Condition "Tidak ada perubahan data" tidak punya langkah observasi di TC sehingga tidak diasersi.
