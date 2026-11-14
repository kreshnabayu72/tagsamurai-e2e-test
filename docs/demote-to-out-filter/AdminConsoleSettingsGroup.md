# Eliminasi Step: Admin Console > SettingsGroup

Modul: SettingsGroup  
Sumber: specs/AdminConsole/SettingsGroup  
Tanggal: 2026-11-14

## Kriteria
- A. Persona Distributor atau Partner aktif (login `Distributor`/`Partner`, ganti akun, atau sesi API atas nama akun Distributor/Partner). Persona Principal tetap; Client tidak termasuk (lihat Ragu).
- B. Hanya halaman detail User di Admin Console > Settings > User List (termasuk tab dan sub-tab di dalamnya) dan halaman detail Client di Admin Console > Client List. Langkah yang membuka, memverifikasi, atau beroperasi di halaman itu dikecualikan, termasuk aksi yang masuk ke halaman itu (klik Name atau Company Name, menu Detail). Tidak termasuk B: detail User di Global Settings > User atau Fixed Asset > Settings > User, Detail Non-Login User, serta detail lain di Admin Console (Subscription, License, Device SKU, Stock, Role, Group, Plan, Partner, Distributor, dan sebagainya). Langkah login, buka List, dan Search yang mendahului halaman detail dipertahankan.
- C. Fitur AI: tidak ada.
- D. Hanya menu Approval Admin Console (Admin Console > Approvals, sidebar atau halaman) dan langkah yang masuk atau beroperasi di dalamnya (Approve, Reject, Review di Approvals). Tidak termasuk: Approve/Reject lewat API di luar menu, approval di Fixed Asset, teks approval di dialog, serta sub-tab Pending Approvals pada Responsibilities detail User. Rangkaian langkah D lama dipertahankan hanya bila memuat atau didahului langkah yang menyebut Approvals, atau berada di spek bertajuk approval; langkah API dan Pending Approval dikeluarkan.
- E. Surface mobile atau Android, serta resize viewport desktop. Yang dikecualikan: langkah yang mengubah atau memulihkan ukuran viewport browser desktop, dan langkah verifikasi yang hanya ada karena resize itu (gulir horizontal, kolom beku, layout viewport sempit, walkthrough tertutup saat resize). Langkah campuran (resize bersama aksi lain dalam satu langkah) dipertahankan.
- Persona aktif dilacak dari Prerequisites dan langkah login, ganti akun, logout per spek. Nomor langkah mengikuti Test Steps.

## Ringkasan
- Spek: 116; spek dengan eliminasi: 53
- Langkah bernomor (Test Steps): 3391; dikecualikan: 1338; tersisa: 2053
- Item di Ragu: 9

## Daftar Eliminasi

| Spek | Judul | Langkah dikecualikan | Kriteria | Alasan | Dependensi |
|---|---|---|---|---|---|
| TC-AC-SG-E2E-004 | Empty State Entitas Tanpa Group dan Entitas dengan Satu Group | 1-5 (A); 6-12 (A) (total 12) | A | 1-5: persona Distributor Tanpa Group; 6-12: persona Distributor Satu Group | - |
| TC-AC-SG-E2E-011 | Total Member Node: Active/Suspended Langsung, Tidak Rekursif, Nilai 0 Tetap Link, dan Archived Tidak Dihitung | 19-26 (A) (total 26) | A | 19-26: persona Distributor Hapus Utama | - |
| TC-AC-SG-E2E-013 | Guided Tooltip Settings > Group: Tidak Muncul Lagi Setelah Selesai, Resize Menutup Tanpa Seen, dan Keyboard | 12-13 (E) (total 26) | E | 12-13:  | - |
| TC-AC-SG-E2E-014 | Mobile Android: Card List, Bottom Sheet Tree, dan Toolbar Settings > Group | 1-23 (E) (total 23) | E | 1-23: surface mobile/Android | - |
| TC-AC-SG-E2E-015 | Mobile Android: Long-Press Masuk Selection Mode dan Bulk Delete Tersedia | 1-22 (E) (total 22) | E | 1-22: surface mobile/Android | - |
| TC-AC-SG-E2E-016 | Role Matrix: Entity Gate Distributor, Partner, dan Client pada Settings > Group | 1-5 (A); 6-12 (A) (total 19) | A | 1-5: persona Distributor Jaringan; 6-12: persona Partner Jaringan | - |
| TC-AC-SG-E2E-024 | Manage group Delete: Menghapus Group lewat Checkbox Bulk dan Delete | 1-12 (A) (total 12) | A | 1-12: persona Distributor Hapus Utama | - |
| TC-AC-SG-E2E-027 | Create Group: Stay on Form, Trim, dan Nama Sama pada Parent atau Entitas Berbeda | 32-41 (A) (total 41) | A | 32-41: persona Distributor Pembanding | - |
| TC-AC-SG-E2E-033 | Create Subgroup dan Hierarchy Depth Limit: Limit-1, Sama dengan Limit, Limit+1, Level 1, Cek Ulang Server, dan Penurunan Limit | 1-42 (A) (total 42) | A | 1-42: persona Distributor Pohon Dalam | - |
| TC-AC-SG-E2E-038 | Delete Group: Dialog Warning D-04, Cancel, Backdrop, Tooltip Full Path, dan Elipsis Sidebar | 1-33 (A) (total 33) | A | 1-33: persona Distributor Hapus Utama | - |
| TC-AC-SG-E2E-039 | Delete Group Diblok karena Entitas Menempel (D-03): Langsung, Descendant, Archived, Partner, dan Distributor Principal | 1-23 (A) (total 31) | A | 1-23: persona Distributor Hapus Utama | - |
| TC-AC-SG-E2E-040 | Delete Group Diblok karena Group Terakhir (D-02) dan Guard Seluruh Group | 1-12 (A); 13-18 (A); 19-26 (A) (total 26) | A | 1-12: persona Distributor Satu Group; 13-18: persona Distributor Tiga Group; 19-26: persona Distributor Dua Group | - |
| TC-AC-SG-E2E-041 | Delete Group: Konfirmasi Menghapus Subtree, Pelepasan Group Role dan Group Manager, dan Klik Ganda | 1-20 (A); 21-23 (A,B); 24-26 (A) (total 26) | A,B | 1-20: persona Distributor Hapus Utama; 21-23: halaman detail User; persona Distributor Hapus Utama; 24-26: persona Distributor Hapus Utama | - |
| TC-AC-SG-E2E-042 | Bulk Delete: Bulk Actions Bar, Select All dan Unselect All, serta Checkbox Header | 1-30 (A) (total 30) | A | 1-30: persona Distributor Hapus Utama | - |
| TC-AC-SG-E2E-043 | Bulk Delete: Seleksi Lintas Halaman dan Search, Reset oleh Node, Batas Node Terpilih, dan Cancel | 1-49 (A) (total 49) | A | 1-49: persona Distributor Hapus Utama | - |
| TC-AC-SG-E2E-044 | Bulk Delete: Homogen Tanpa Entitas, Campuran dengan Skip Member, dan Seluruh Baris Punya Member | 1-25 (A) (total 25) | A | 1-25: persona Distributor Hapus Utama | - |
| TC-AC-SG-E2E-045 | Bulk Delete: Collapse ke Dialog Single, Nama Baris Terpilih Saja, dan Reset Seleksi Setelah Commit | 1-35 (A) (total 35) | A | 1-35: persona Distributor Hapus Utama | - |
| TC-AC-SG-E2E-046 | Bulk Delete: Guard Menghabiskan Seluruh Group per Entitas (D-08) | 1-7 (A); 8-16 (A); 17-29 (A) (total 29) | A | 1-7: persona Distributor Dua Group; 8-16: persona Distributor Satu Group; 17-29: persona Distributor Tiga Group | - |
| TC-AC-SG-E2E-047 | Bulk Delete: Selection Limit 100 pada Seleksi Manual dan Select All | 1-17 (A) (total 17) | A | 1-17: persona Distributor Seleksi Besar | - |
| TC-AC-SG-E2E-066 | Isi File Export: Sel Numerik XLSX, Full Path Kolom Group, dan Snapshot Path Changelog | 8-17 (A); 18-39 (A) (total 39) | A | 8-17: persona Distributor Changelog; 18-39: persona Distributor Race | - |
| TC-AC-SG-E2E-067 | Modal Changelog: Screening, Empty State, dan Tampilan Data Kolom | 1-26 (A); 27-31 (A) (total 31) | A | 1-26: persona Distributor Changelog; 27-31: persona Distributor Changelog Kosong | - |
| TC-AC-SG-E2E-068 | Modal Changelog: Search Kolom Action, Group Name, dan Field | 1-25 (A) (total 25) | A | 1-25: persona Distributor Changelog | - |
| TC-AC-SG-E2E-069 | Modal Changelog: Search Kolom Old Value, New Value, dan Modified By | 1-24 (A) (total 24) | A | 1-24: persona Distributor Changelog | - |
| TC-AC-SG-E2E-070 | Modal Changelog: Search Date, Panel Filter, dan Opsi Action serta Group Name | 1-28 (A) (total 28) | A | 1-28: persona Distributor Changelog | - |
| TC-AC-SG-E2E-071 | Modal Changelog: Filter Group Name, Modified By, Date, Kombinasi AND, dan Independensi Kontrol | 1-37 (A) (total 37) | A | 1-37: persona Distributor Changelog | - |
| TC-AC-SG-E2E-072 | Modal Changelog: Sort Kolom Date, Action, Group Name, dan Field | 1-27 (A) (total 27) | A | 1-27: persona Distributor Changelog | - |
| TC-AC-SG-E2E-073 | Modal Changelog: Sort Kolom Old Value, New Value, Modified By, dan Pagination | 1-25 (A) (total 25) | A | 1-25: persona Distributor Changelog | - |
| TC-AC-SG-E2E-074 | Modal Changelog: Setup Column, Tutup Modal, dan Snapshot Immutable | 1-17 (A); 18-29 (A) (total 29) | A | 1-17: persona Distributor Changelog; 18-29: persona Distributor Race | - |
| TC-AC-SG-E2E-078 | Popup Users: Panel Filter, Opsi dan Filter Group Role, dan Tier Tanpa Pemegang | 25-33 (A) (total 33) | A | 25-33: persona Distributor Tiga Group | - |
| TC-AC-SG-E2E-082 | Popup Users: Setup Column, Cache Terpisah, dan Max Visible Columns | 29-39 (A) (total 39) | A | 29-39: persona Distributor Custom Field | - |
| TC-AC-SG-E2E-083 | Popup Total Member Detail: Screening, Empty 0, Kolom Type, Penutupan, dan Tree Distributor | 26-38 (A) (total 38) | A | 26-38: persona Distributor Anggota | - |
| TC-AC-SG-E2E-087 | Pencatatan Create dan Edit Group: Changelog, System Log, dan Activity Log | 10-11 (B); 40-41 (B); 46-47 (B) (total 47) | B | 10-11: halaman detail User; 40-41: halaman detail User; 46-47: halaman detail User | - |
| TC-AC-SG-E2E-088 | Pencatatan Delete Single dan Bulk: Satu Entri per Node dan per Group, Pelepasan Group Manager | 1-12 (A); 13-14 (A,B); 15-36 (A); 37-38 (A,B); 39-44 (A); 45-49 (A,B) (total 49) | A,B | 1-12: persona Distributor Hapus Utama; 13-14: persona Distributor Hapus Utama; halaman detail User; 15-36: persona Distributor Hapus Utama; 37-38: persona Distributor Hapus Utama; halaman detail User; 39-44: persona Distributor Hapus Utama; 45-49: persona Distributor Hapus Utama; halaman detail User | - |
| TC-AC-SG-E2E-089 | Pencatatan Seed Onboarding Default Group dan Activity Log Entity-Bound | 1-7 (A); 8-15 (A) (total 15) | A | 1-7: persona Distributor Baru {runId}-089; 8-15: persona Distributor Pembanding | - |
| TC-AC-SG-E2E-090 | Absence Log Edit Group Tanpa Perubahan di Changelog, Activity Log, dan System Log | 29-30 (B); 43-44 (B) (total 44) | B | 29-30: halaman detail User; 43-44: halaman detail User | - |
| TC-AC-SG-E2E-091 | Absence Log Delete: Cancel, Skip pada Bulk, dan Diblok Dialog | 1-46 (A) (total 46) | A | 1-46: persona Distributor Hapus Utama | - |
| TC-AC-SG-E2E-092 | Sinkron Lintas Modul: Group Baru dan Rename Terefleksi di Settings > User dan Role & Permission | 6-9 (B); 19-23 (B) (total 31) | B | 6-9: halaman detail User; 19-23: halaman detail User | - |
| TC-AC-SG-E2E-093 | Sinkron Lintas Modul: Reassign Entitas, Total User dari Group Role dan Read Only, serta Create Distributor | 21-23 (B); 47-50 (A) (total 50) | A,B | 21-23: halaman detail User; 47-50: persona Distributor Baru {runId}-093 | - |
| TC-AC-SG-E2E-094 | Sinkron Lintas Modul setelah Delete: Settings > User, Tab Role, Group Manager List, dan Akses History | 1-7 (A); 8-12 (A,B); 13-14 (A); 15-16 (A,B); 17-21 (A); 22-25 (A,B); 26-33 (A); 34-36 (A,B); 37-42 (A); 43-44 (A,D); 45 (A) (total 45) | A,B,D | 1-7: persona Distributor Hapus Utama; 8-12: persona Distributor Hapus Utama; halaman detail User; 13-14: persona Distributor Hapus Utama; 15-16: persona Distributor Hapus Utama; halaman detail User; 17-21: persona Distributor Hapus Utama; 22-25: persona Distributor Hapus Utama; halaman detail User; 26-33: persona Distributor Hapus Utama; 34-36: persona Distributor Hapus Utama; halaman detail User; 37-42: persona Distributor Hapus Utama; 43-44: persona Distributor Hapus Utama; menu Approvals; 45: persona Distributor Hapus Utama | - |
| TC-AC-SG-E2E-095 | Defense-in-Depth: Isolasi Entitas dan Penolakan 403 per Role lewat Request Langsung | 1-7 (A) (total 35) | A | 1-7: persona Distributor Pembanding | - |
| TC-AC-SG-E2E-096 | Defense-in-Depth: Root All Groups, Parent, Duplikat, Depth Limit, Guard Delete, dan Selection Limit lewat Request Langsung | 19-22 (A); 23-26 (A); 27-30 (A) (total 30) | A | 19-22: persona Distributor Hapus Utama; 23-26: persona Distributor Satu Group; 27-30: persona Distributor Seleksi Besar | - |
| TC-AC-SG-E2E-098 | State Tenant: Write-Lockdown Suspended pada Create, Edit, Delete, Bulk Delete, dan Add Subgroup di Batas Kedalaman | 1-36 (A); 37-56 (A) (total 56) | A | 1-36: persona Distributor Suspended; 37-56: persona Distributor Suspended Dalam | - |
| TC-AC-SG-E2E-099 | State Tenant: Write-Lockdown Expired, Grace Pasca-Expired, dan Archive, serta Grace Downgrade yang Tidak Memblokir | 1-27 (A); 28-37 (A); 38-47 (A); 48-53 (A) (total 53) | A | 1-27: persona Distributor Expired; 28-37: persona Distributor Grace Expired; 38-47: persona Distributor Archive; 48-53: persona Distributor Grace Downgrade | - |
| TC-AC-SG-E2E-100 | Konkurensi Dua Admin: Create Duplikat, Edit Bersamaan, Refresh SSE, dan Fallback F5 | 1-49 (A) (total 49) | A | 1-49: persona Distributor Race | - |
| TC-AC-SG-E2E-101 | Konkurensi Dua Admin: Perubahan saat Delete Menunggu Konfirmasi dan Member Baru saat Bulk Delete | 1-29 (A) (total 29) | A | 1-29: persona Distributor Race | - |
| TC-AC-SG-E2E-102 | Konkurensi Dua Admin: Target Sudah Dihapus Admin Lain pada Add Subgroup, Edit, Delete, dan Bulk Delete | 1-45 (A) (total 45) | A | 1-45: persona Distributor Race | - |
| TC-AC-SG-E2E-103 | Konkurensi Dua Admin: Delete Bersamaan Menghabiskan Group dan Invarian Minimal Satu Group | 1-19 (A) (total 19) | A | 1-19: persona Distributor Dua Group | - |
| TC-AC-SG-E2E-105 | Resilience Distributor: Gagal Server pada Delete, Bulk Delete, dan Download Changelog | 1-25 (A); 26-33 (A) (total 33) | A | 1-25: persona Distributor Hapus Utama; 26-33: persona Distributor Changelog | - |
| TC-AC-SG-E2E-107 | Mobile Android: Akses Changelog dari Header dan Popup Create, Edit, serta Delete sebagai Bottom Sheet | 1-30 (E) (total 30) | E | 1-30: surface mobile/Android | - |
| TC-AC-SG-E2E-110 | Delete Group: Fallback Seleksi ke All Groups Setelah Node Header atau Ancestor Terhapus | 1-24 (A) (total 24) | A | 1-24: persona Distributor Hapus Utama | - |
| TC-AC-SG-E2E-111 | Bulk Delete: Guard Entitas Tiga Campur, Dua dari Tiga Group Lolos dan Ketiganya Lolos karena Satu Di-skip | 1-15 (A) (total 15) | A | 1-15: persona Distributor Tiga Campur | - |
| TC-AC-SG-E2E-114 | Modal Changelog: Download CSV dan XLSX dengan Filename Changelog-Group | 1-16 (A) (total 16) | A | 1-16: persona Distributor Changelog | - |
| TC-AC-SG-E2E-116 | Absence Log Pelepasan Group Role akibat Delete dan Tanpa Notifikasi In-App | 1-2 (A,B); 3-7 (A); 8-10 (A,B); 11-15 (A); 16 (A,B); 17-26 (A); 27-29 (A,B); 30-42 (A) (total 42) | A,B | 1-2: persona Distributor Hapus Utama; halaman detail User; 3-7: persona Distributor Hapus Utama; 8-10: persona Distributor Hapus Utama; halaman detail User; 11-15: persona Distributor Hapus Utama; 16: persona Distributor Hapus Utama; halaman detail User; 17-26: persona Distributor Hapus Utama; 27-29: persona Distributor Hapus Utama; halaman detail User; 30-42: persona Distributor Hapus Utama | - |

## Ragu / Perlu Konfirmasi
1. Persona Client (SG-016 blok TC-59, langkah 13-19, `Client Jaringan`): tidak dikecualikan, karena kriteria A hanya menyebut Distributor dan Partner. Konfirmasi apakah Client ikut dikecualikan.
2. Akun `Lia Marlina` dan `Nina Amelia` tidak punya email atau entitas di Pre-setup; spek menyebutnya sebagai user Pre-setup #21 (entitas `Distributor Hapus Utama`). Login ke keduanya (SG-094 langkah 42-45, SG-116 langkah 35-42) dianggap persona Distributor (kriteria A). Konfirmasi.
3. Popup `Total User Detail` / `Total Member Detail` (SG-075, SG-083) adalah popup di Settings > Group, bukan halaman detail User List/Client List; tidak dikecualikan. Konfirmasi.
4. SG-002 langkah 30 (`Verifikasi tidak ada aksi Detail pada Overlay Row Action`) dan SG-092 langkah 30 (`Detail Group Role` di Settings > Role & Permission): tidak dikecualikan. Yang pertama memverifikasi ketiadaan aksi pada grup, bukan halaman detail User; yang kedua halaman Role, bukan detail user.
5. SG-066 langkah 1-7 (blok TC-233 dan TC-236): tabel Prerequisites mencatat akun pertama sebagai Total Control entitas Principal, tetapi tidak ada baris 'Login di hook'. Diperlakukan sebagai Principal.
6. SG-089 langkah 1 berupa `Ganti akun` ke `Distributor Baru {runId}-089`; seluruh langkah spek dianggap persona Distributor setelah hook `before` (login Principal) selesai.
7. SG-094 langkah 43-44 (`Buka history Approvals`, `Verifikasi halaman Approvals tampil`) dikecualikan sebagai kriteria D. Langkah 34-36 (Detail user `Lia Marlina`) juga dikecualikan sebagai B.
8. Tidak ditemukan fitur AI (kriteria C) di modul ini.
9. Kriteria D dihitung dengan heuristik: rangkaian langkah D lama dipertahankan hanya bila memuat atau didahului langkah yang menyebut Approvals, atau berada di spek bertajuk approval; langkah API dan Pending Approval dikeluarkan. Konfirmasi.
