---
id: TC-FA-RP-E2E-188-tabel-role-transaksi-tampilan-section-header-keterangan-3
title: "Tabel Role Transaksi: tampilan section, header, keterangan approver, dan state (3/3)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1054
  - TC-FA-RP-1109
coverage:
  web: automated
---

# Tabel Role Transaksi: tampilan section, header, keterangan approver, dan state (3/3)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Pre-setup #2); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`).
- Akun aktor (password hanya lewat env):

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Total Control (Siti Rahmawati) | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |

- Data Pre-setup (Company Alpha): #18 (pohon group; node `IT Infrastructure`), #19 dan #40 (tabel Role Transaksi `IT Infrastructure` sub-tab `Disposal`: Asset Admin Nadia Putri, Ahmad Fauzi, Dimas Pranata; Monitoring & Report Oscar Pratama; Staff Putri Wulandari; Approver Pandu Wijaya). Tidak diubah spec ini.
- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun, nama pengguna, group, dan nilai kolom yang diasersi ditambahkan tim FE.
- Kemampuan teknis (disediakan tim FE/BE): hover dan klik pada header section dan sub-tab.
- Pemulihan: preferensi Setup Column tabel yang disimpan spec ini dihapus di hook `after` (hapus preferensi kolom di browser, bukan `[Reset to Default]`; kemampuan disediakan tim FE); Pre-setup bersama tidak diubah kecuali dinyatakan di atas. Pemulihan ini belum terdaftar di `suite.md` (lihat Temuan untuk QA).

## Test Steps

### TC-FA-RP-1054: State buka tutup section dipertahankan saat ganti node dan sub-tab

1. Klik Tab `Transaction Role`
2. Klik sub-tab `Disposal`
3. Klik node `IT Infrastructure` di Sidebar Group Tree
4. Tutup section `Asset Admin` dan buka section `Monitoring & Report`
5. Klik node `Data Center`
6. Verifikasi section `Monitoring & Report` tetap terbuka pada node `Data Center`
7. Verifikasi section `Asset Admin` tetap tertutup pada node `Data Center`
8. Klik sub-tab `Damaged`
9. Verifikasi section `Monitoring & Report` tetap terbuka dan `Asset Admin` tetap tertutup pada sub-tab `Damaged`
10. Verifikasi section `Staff` tidak tampil pada sub-tab `Damaged`
11. Klik kembali sub-tab `Disposal`
12. Verifikasi section `Staff` tampil kembali
13. Verifikasi section `Staff` memiliki state buka atau tutup yang sama seperti sebelum sub-tab diganti (tertutup)

### TC-FA-RP-1109: State Search tabel dipegang per section pada tiap sub-tab dan dipulihkan saat kembali

14. Klik node `IT Infrastructure`, tutup section `Monitoring & Report`, lalu buka section `Asset Admin` (mengembalikan state default sebelum TC ini)
15. Buka section `Monitoring & Report`
16. Ketik Search `nadia` pada section `Asset Admin`, tekan Enter
17. Verifikasi tabel section `Asset Admin` tersaring ke baris Nadia Putri
18. Verifikasi tabel section `Monitoring & Report` tidak tersaring dan menampilkan Oscar Pratama
19. Klik sub-tab `Damaged`
20. Verifikasi kotak Search section `Asset Admin` pada sub-tab `Damaged` tidak berisi keyword `nadia`
21. Klik kembali sub-tab `Disposal`
22. Verifikasi kotak Search section `Asset Admin` pada sub-tab `Disposal` kembali berisi `nadia`
23. Verifikasi tabel section `Asset Admin` tersaring ke baris Nadia Putri
24. Klik `(←)` pada kotak Search section `Asset Admin`

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-1054, 1109). Seluruh TC berpost condition `-`; tidak ada asersi tambahan dari Post Condition.
- Langkah penghubung (tanpa awalan `Verifikasi`; dipakai untuk membuka konteks, menutup popup atau panel, membersihkan state, dan memulihkan kolom): langkah 1, 14, 24.
- Temuan untuk QA:
  - TC-FA-RP-1109 langkah 2 menulis "buka section `Monitoring & Report`" tanpa menyebut state section setelah TC-FA-RP-1054; spec mengembalikan state default dulu (langkah penghubung) agar section `Asset Admin` terbuka dan section `Monitoring & Report` dibuka oleh langkah TC.
  - TC-FA-RP-1054 expected c menyebut state buka atau tutup section `Staff` "sama seperti sebelum sub-tab diganti" tanpa menyebut nilainya; spec memakai tertutup (state default section `Staff`).
