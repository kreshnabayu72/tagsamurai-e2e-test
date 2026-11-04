---
id: TC-FA-RP-E2E-205-detail-role-kombinasi-dan-state-halaman-2
title: "Detail Role: kombinasi dan state halaman (2/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-676
  - TC-FA-RP-677
  - TC-FA-RP-1025
coverage:
  web: automated
---

# Detail Role: kombinasi dan state halaman (2/2)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Pre-setup #2); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`).
- Akun aktor (password hanya lewat env):

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Total Control (Siti Rahmawati) | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |

- Data Pre-setup (Company Alpha): #39 (Detail Role Group Role `Manage files`, 41 baris: 6 baris non-pola dan 35 baris pola Group Role. Baris non-pola: Ahmad Fauzi (Asset Custodian, Logistics) di `Data Center`; Budi Santoso (Warehouse Staff, Logistics) di `Helpdesk`; Citra Lestari (HR Officer, HR) di `Head Office`; Dimas Pranata (IT Support, IT Operations) di `Data Center`; Endah Susanti (Procurement Officer, Procurement) di `Rack A1`; Fitri Handayani (Finance Officer, Finance, Pending Email Confirmation, Temporary User Yes dengan Temporary Until terisi) di `Dock 1`; Detail Role Global Role `Manage Open API` dan `Manage accounting` terisi Ahmad Fauzi, Budi Santoso, Citra Lestari, Dimas Pranata. Baris pola `Manage files` ada pada tujuh group Pre-setup #18 untuk lima user pola: Admin Utama (System Administrator, IT Operations), Siti Rahmawati (Finance Officer, Accounting & Tax), Rina Wulandari (`Operations Manager, Region 1`, `Asset Management "North"`), Dewi Anggraini (Internal Auditor, Internal Audit), Maya Anggraeni (Compliance Analyst, Legal)) dan #18 (pohon group). Tidak diubah spec ini.
- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun, nama pengguna, group, dan nilai kolom yang diasersi ditambahkan tim FE.
- Kemampuan teknis (disediakan tim FE/BE): mengamati kembali isi Search dan node Sidebar Group Tree setelah muat ulang halaman.
- Pemulihan: preferensi Setup Column tabel yang disimpan spec ini dihapus di hook `after` (hapus preferensi kolom di browser, bukan `[Reset to Default]`; kemampuan disediakan tim FE); Pre-setup bersama tidak diubah kecuali dinyatakan di atas. Pemulihan ini belum terdaftar di `suite.md` (lihat Temuan untuk QA).

## Test Steps

### TC-FA-RP-676: Sidebar Group Tree menyaring Detail Role Group Role secara literal bersama Search

1. Klik Tab `System`
2. Klik Role Name `Manage files` pada section Group Role
3. Klik `All Groups` di Sidebar Group Tree
4. Klik node `Data Center`
5. Verifikasi tabel menampilkan baris Ahmad Fauzi dan Dimas Pranata di `Data Center` beserta lima baris pola Group Role `Manage files` (Admin Utama, Siti Rahmawati, Rina Wulandari, Dewi Anggraini, Maya Anggraeni; Pre-setup #39) di `Data Center`
6. Ketik Search `dimas`, tekan Enter
7. Verifikasi tabel menampilkan hanya baris Dimas Pranata (Search tetap aktif)
8. Klik node `Head Office`
9. Verifikasi tabel menampilkan empty state `No results found` karena Dimas Pranata tidak ditugaskan langsung di `Head Office` dan Search `dimas` tetap aktif
10. Klik `(←)` pada kotak Search, lalu klik `All Groups` di Sidebar Group Tree

### TC-FA-RP-677: State Detail Role dipertahankan setelah F5 dan Back dari halaman lain

11. Klik node `Data Center`, ketik Search `ahmad`, tekan Enter
12. Muat ulang halaman (F5)
13. Verifikasi node `Data Center` tetap terpasang setelah F5
14. Verifikasi Search `ahmad` tetap terpasang setelah F5
15. Klik segmen `System` pada Breadcrumb lalu buka kembali Detail Role `Manage files`
16. Verifikasi Detail Role dibuka dari awal: kotak Search tidak berisi `ahmad` dan node `Data Center` tidak terpilih

### TC-FA-RP-1025: Detail Role Group Role: kolom Group tidak pernah kosong pada setiap baris

17. Klik `All Groups` di Sidebar Group Tree, lalu ubah ukuran halaman menjadi 50
18. Verifikasi kolom Group tampil dengan badge group tempat penugasan pada seluruh 41 baris (6 non-pola dan 35 baris pola, Pre-setup #39): Ahmad Fauzi `Data Center`, Budi Santoso `Helpdesk`, Citra Lestari `Head Office`, Dimas Pranata `Data Center`, Endah Susanti `Rack A1`, Fitri Handayani `Dock 1`; setiap baris pola (lima user pola pada tujuh group) berisi badge group tempat baris itu berada
19. Verifikasi tidak ada sel kolom Group yang kosong atau berisi `—`

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-676, 677, 1025). Seluruh TC berpost condition `-`; tidak ada asersi tambahan dari Post Condition.
- Langkah penghubung (tanpa awalan `Verifikasi`; dipakai untuk membuka konteks, menutup popup atau panel, membersihkan state, dan memulihkan kolom): langkah 1, 10.
- Temuan untuk QA:
  - TC-FA-RP-677 expected b ("Detail Role dibuka dari awal") tidak merinci state awalnya; spec mengasersi Search kosong dan node `Data Center` tidak terpilih.
