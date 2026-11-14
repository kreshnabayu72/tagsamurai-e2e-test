# Eliminasi Step: Admin Console > SettingsDeviceCategory

Modul: SettingsDeviceCategory  
Sumber: specs/AdminConsole/SettingsDeviceCategory  
Tanggal: 2026-11-14

## Kriteria

- A. Persona Distributor atau Partner. Persona aktif dilacak per langkah dari Prerequisites dan langkah login, ganti akun, logout, atau ganti company. Langkah yang dijalankan saat persona Distributor/Partner aktif dikecualikan. Langkah login atau ganti akun yang menuju Distributor/Partner dikecualikan. Langkah yang kembali ke Principal dipertahankan. Verifikasi state hasil request atas nama Distributor/Partner dihitung sebagai bagian persona tersebut. Persona Client bukan Distributor atau Partner, sehingga tidak dikecualikan (masuk Ragu). Copy tooltip yang hanya menyebut Principal, Distributor, atau Partner tidak dikecualikan (masuk Ragu).
- B. Hanya halaman detail User di Admin Console > Settings > User List (termasuk tab dan sub-tab di dalamnya) dan halaman detail Client di Admin Console > Client List. Langkah yang membuka, memverifikasi, atau beroperasi di halaman itu dikecualikan, termasuk aksi yang masuk ke halaman itu (klik Name atau Company Name, menu Detail). Tidak termasuk B: detail User di Global Settings > User atau Fixed Asset > Settings > User, Detail Non-Login User, serta detail lain di Admin Console (Subscription, License, Device SKU, Stock, Role, Group, Plan, Partner, Distributor, dan sebagainya). Langkah login, buka List, dan Search yang mendahului halaman detail dipertahankan.
- C. Fitur AI: tidak ada di modul ini.
- D. Hanya menu Approval Admin Console (Admin Console > Approvals, sidebar atau halaman) dan langkah yang masuk atau beroperasi di dalamnya (Approve, Reject, Review di Approvals). Tidak termasuk: Approve/Reject lewat API di luar menu, approval di Fixed Asset, teks approval di dialog, serta sub-tab Pending Approvals pada Responsibilities detail User. Rangkaian langkah D lama dipertahankan hanya bila memuat atau didahului langkah yang menyebut Approvals, atau berada di spek bertajuk approval; langkah API dan Pending Approval dikeluarkan.
- E. Surface mobile atau Android, serta resize viewport desktop. Yang dikecualikan: langkah yang mengubah atau memulihkan ukuran viewport browser desktop, dan langkah verifikasi yang hanya ada karena resize itu (gulir horizontal, kolom beku, layout viewport sempit, walkthrough tertutup saat resize). Langkah campuran (resize bersama aksi lain dalam satu langkah) dipertahankan.

## Daftar Eliminasi

| Spek | Judul | Langkah dikecualikan | Kriteria | Alasan | Dependensi |
|---|---|---|---|---|---|
| TC-AC-DC-E2E-014-mobile-android-sidebar-dan-filter | Mobile Android: Sidebar Category Tampil lewat Floating Toggle, Aksi per Node, Filter Langsung Berlaku, All Categories, dan Changelog sebagai Bottom Sheet | 1-26 | E | E: spek seluruhnya menguji surface Android (native, card list dan bottom sheet) | Spek seluruhnya Android; tidak ada langkah tersisa. |
| TC-AC-DC-E2E-015-mobile-android-crud-dan-read-only | Mobile Android: Add dan Edit Memakai Input Inline, Delete dan Unsaved Changes sebagai Bottom Sheet, serta Read Only Tanpa Ikon Aksi | 1-30 | E | E: spek seluruhnya menguji surface Android (native, card list dan bottom sheet) | Spek seluruhnya Android; tidak ada langkah tersisa. |
| TC-AC-DC-E2E-016-role-matrix-negatif-entity-distributor | Role Matrix Negatif: Akses Entity Distributor ke Category | 1-20 | A | A: seluruh spek dijalankan sebagai persona Distributor | Seluruh spek adalah persona Distributor; tidak ada langkah tersisa. |
| TC-AC-DC-E2E-017-role-matrix-negatif-partner-client-tanpa-capability | Role Matrix Negatif: Partner, Client, dan Principal Tanpa Capability Ditolak | 1-6 | A | A: langkah 1-5 dijalankan atau menuju persona Distributor/Partner; A: langkah 6 dijalankan atau menuju persona Partner | Langkah 7-23 (Client, Ragu) tetap dan tidak bergantung pada langkah 1-6. |
| TC-AC-DC-E2E-025-defense-request-langsung-per-role-dan-entity | Defense-in-Depth: Request Langsung per Role dan Entity Ditolak 403 | 25-31 | A | A: langkah 25-30 dijalankan atau menuju persona Distributor; A: langkah 31 dijalankan atau menuju persona Partner | Langkah 29-31 (verifikasi data setelah request Distributor/Partner) ikut dikecualikan. Langkah 32 (Client, Ragu) tetap. |
| TC-AC-DC-E2E-060-changelog-empty-state-principal-baru | Modal Changelog Category: Empty State Principal Tanpa Riwayat dan Transisi Keluar dari Empty State | 7-9 | B | B: langkah 7-9 membuka, memverifikasi, atau mengakses halaman Detail User (tab System Log) (jalur masuk termasuk) | Langkah 10-35 (Activity Log dan Device Name) tetap; tidak bergantung pada langkah 7-9. |
| TC-AC-DC-E2E-081-log-system-log-dan-activity-log | System Log Aktor dan Activity Log Admin Console Mencatat Create, Edit, dan Delete Category | 9-17 | B | B: langkah 9-17 membuka, memverifikasi, atau mengakses halaman Detail User (tab System Log) (jalur masuk termasuk) | Langkah 18-32 tetap; entri Activity Log dibuat sendiri pada langkah 21-26. |
| TC-AC-DC-E2E-082-log-sinkron-tiga-surface-dan-aktor | Satu Aksi Edit Sinkron di Tiga Surface Log dan Modified By Mengikuti Aktor | 10-13 | B | B: langkah 10-13 membuka, memverifikasi, atau mengakses halaman Detail User (tab System Log) (jalur masuk termasuk) | Langkah 14-17 dan 18-28 tetap; tidak bergantung pada langkah 10-13. |
| TC-AC-DC-E2E-083-log-absence-no-op-dan-gagal | Absence Log: Save Tanpa Perubahan dan Edit No-op Tidak Menulis Entri | 23-25 | B | B: langkah 23-25 membuka, memverifikasi, atau mengakses halaman Detail User (tab System Log) (jalur masuk termasuk) | Langkah 26-28 (Activity Log) bergantung pada baseline B223 di langkah 15 (Ragu B). |
| TC-AC-DC-E2E-089 | Sidebar Category: Auto-Collapse di Bawah 1280px Tidak Menimpa Preferensi dan Default Open saat localStorage Tidak Tersedia | 1-7 | E | E: langkah 1, 3-4, 6 resize viewport desktop; langkah 2, 5, 7 verifikasi setelah resize viewport desktop (preferensi sidebar saat auto-collapse dan setelah viewport dipulihkan) | - |

## Ragu / Perlu Konfirmasi
- TC-AC-DC-E2E-017-role-matrix-negatif-partner-client-tanpa-capability, langkah 7-13: persona Client (bukan Distributor/Partner, tidak termasuk kriteria A).
- TC-AC-DC-E2E-025-defense-request-langsung-per-role-dan-entity, langkah 32: Request baca memakai token Client; Client bukan Distributor/Partner sehingga bukan kriteria A.
- TC-AC-DC-E2E-083-log-absence-no-op-dan-gagal, langkah 2, 8-9, 14-15: Cek atau baseline System Log aktor bersama Changelog dan Activity Log; bila lewat Detail User termasuk B.
- Detail User tanpa jalur navigasi eksplisit (mis. "Buka Detail User X > tab System Log", "User Detail > System Log") dianggap Admin Console > Settings > User List dan dihitung B. Konfirmasi bukan Global Settings > User.
