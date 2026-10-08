# Coverage E2E — Admin Console > Settings > Group

Sumber: `admin-console/settings-group/TestCases/tc-settings-group.md` (189 TC granular aktif) dan `admin-console/settings-group/TestCases/tc-settings-group-backend.md`.
Referensi: `admin-console/settings-group/TestCases/tc-settings-group-frontend.md`.
Suite: `specs_dummy/AdminConsole/SettingsGroup/`.
Prefix Modul: `AC` + `SG` (`TC-AC-SG-E2E-*`).
Status semua spec: `draft`.

---

## 1. Pemetaan TC Granular → Spec E2E (64 Spec Atomik)

| Spec | Isi / Judul | Mode | TC Sumber |
|---|---|:---:|---|
| TC-AC-SG-E2E-001 | Screening tabel utama, toolbar, breadcrumb, dan hover baris Settings > Group | FE+BE | TC-AC-SG-1, TC-AC-SG-3, TC-AC-SG-7, TC-AC-SG-173, TC-AC-SG-174, TC-AC-SG-175, TC-AC-SG-176 |
| TC-AC-SG-E2E-002 | Inisialisasi data seed entitas baru dan tampilan empty state hasil search/filter | FE+BE | TC-AC-SG-2, TC-AC-SG-4 |
| TC-AC-SG-E2E-003 | Tampilan empty state genuinely-kosong ketika entitas memiliki nol group level 1 | FE+BE | TC-AC-SG-184 |
| TC-AC-SG-E2E-004 | Loading skeleton dan pemulihan error load data via tombol Try Again | mock | TC-AC-SG-5, TC-AC-SG-6 |
| TC-AC-SG-E2E-005 | Siklus lengkap Guided Tooltip kunjungan pertama, replay manual, dan tombol navigasi | FE+BE | TC-AC-SG-163, TC-AC-SG-164 |
| TC-AC-SG-E2E-006 | Sidebar default state dan render tabel flat lintas semua level saat All Groups aktif | FE+BE | TC-AC-SG-8, TC-AC-SG-167 |
| TC-AC-SG-E2E-007 | Pencarian sidebar, hierarchy toggle expand/collapse all, dan persistensi state sidebar | FE+BE | TC-AC-SG-9, TC-AC-SG-10, TC-AC-SG-223 |
| TC-AC-SG-E2E-008 | Filtering eksklusif rekursif via klik node sidebar, toggle off, dan immutabilitas root All Groups | FE+BE | TC-AC-SG-11, TC-AC-SG-12, TC-AC-SG-13, TC-AC-SG-187 |
| TC-AC-SG-E2E-009 | Karakteristik Group Context Header murni display dan kesetaraan dual entry point | FE+BE | TC-AC-SG-15, TC-AC-SG-16, TC-AC-SG-17, TC-AC-SG-29 |
| TC-AC-SG-E2E-010 | Empty state No subgroup yet saat node tanpa child dipilih dan transisi keluar saat buat anak pertama | FE+BE | TC-AC-SG-185, TC-AC-SG-195 |
| TC-AC-SG-E2E-011 | Fallback seleksi ke All Groups saat node header dihapus dan transisi ke empty state No subgroup yet | FE+BE | TC-AC-SG-193, TC-AC-SG-194 |
| TC-AC-SG-E2E-012 | Role Matrix Positif: Akses penuh seluruh tree untuk Total Control, Default User, dan Manage group | FE+BE | TC-AC-SG-18, TC-AC-SG-25 |
| TC-AC-SG-E2E-013 | Role Matrix Negatif: Penolakan mutasi dan elipsis tersembunyi untuk Read Only dan Manage group R-only | FE+BE | TC-AC-SG-19, TC-AC-SG-179 |
| TC-AC-SG-E2E-014 | Role Matrix Negatif: Penolakan akses menu Settings > Group untuk Group Manager, Client, dan role lain | FE+BE | TC-AC-SG-21, TC-AC-SG-26 |
| TC-AC-SG-E2E-015 | Visibilitas kolom Checkbox bulk select berdasarkan kepemilikan capability Delete | FE+BE | TC-AC-SG-27, TC-AC-SG-156, TC-AC-SG-157 |
| TC-AC-SG-E2E-016 | Guided Tooltip otomatis melewati Step 3 untuk aktor tanpa tombol aksi mutasi | mock | TC-AC-SG-222 |
| TC-AC-SG-E2E-017 | Kebijakan Entity Suspended: Penonaktifan seluruh kontrol mutasi Create, Edit, dan Delete | mock | TC-AC-SG-68, TC-AC-SG-169 |
| TC-AC-SG-E2E-018 | Validasi field Group Name form Create: kosong, batas panjang, reserved name, dan duplikat sibling | FE+BE | TC-AC-SG-34, TC-AC-SG-35, TC-AC-SG-36, TC-AC-SG-37, TC-AC-SG-38 |
| TC-AC-SG-E2E-019 | Siklus penutupan modal Create: form pristine, form dirty memicu dialog Unsaved Changes, dan Clear Field | FE+BE | TC-AC-SG-180, TC-AC-SG-181, TC-AC-SG-188 |
| TC-AC-SG-E2E-020 | Pembuatan group level 1 sukses dan perilaku checkbox Stay on this form after submitting | FE+BE | TC-AC-SG-32, TC-AC-SG-39 |
| TC-AC-SG-E2E-021 | Penanganan kegagalan submit Form Create Level 1 saat server error 5xx atau timeout | mock | TC-AC-SG-40 |
| TC-AC-SG-E2E-022 | Perlindungan double-click submit pada Form Create Level 1 | FE+BE | TC-AC-SG-110 |
| TC-AC-SG-E2E-023 | Pembuatan subgroup sukses via row action dan sidebar serta verifikasi display parent path | FE+BE | TC-AC-SG-41, TC-AC-SG-42, TC-AC-SG-43, TC-AC-SG-44 |
| TC-AC-SG-E2E-024 | Pencegahan penambahan subgroup melebihi batas Hierarchy Depth Limit platform | FE+BE | TC-AC-SG-45, TC-AC-SG-46 |
| TC-AC-SG-E2E-025 | Validasi form Edit Group: nama kosong, duplikat sibling, dan penanganan kegagalan simpan | FE+BE | TC-AC-SG-52, TC-AC-SG-53, TC-AC-SG-55 |
| TC-AC-SG-E2E-026 | Siklus modal Edit Group: form pristine, form dirty dengan dialog Unsaved Changes, dan Clear Field | FE+BE | TC-AC-SG-182, TC-AC-SG-183, TC-AC-SG-189, TC-AC-SG-190 |
| TC-AC-SG-E2E-027 | Pembaruan tanpa perubahan nama (Edit No-Op): verifikasi toast netral No changes to save dan zero logging | FE+BE | TC-AC-SG-159 |
| TC-AC-SG-E2E-028 | Pengubahan nama group sukses (termasuk Default Group) dan retensi referensi sistem | FE+BE | TC-AC-SG-49, TC-AC-SG-51 |
| TC-AC-SG-E2E-029 | Guard Delete Single Kondisi #1: Pemblokiran penghapusan satu-satunya group milik entitas | FE+BE | TC-AC-SG-57, TC-AC-SG-58 |
| TC-AC-SG-E2E-030 | Guard Delete Single Kondisi #2: Pemblokiran penghapusan group yang masih memiliki Total Member > 0 | FE+BE | TC-AC-SG-59 |
| TC-AC-SG-E2E-031 | Pembatalan dialog Delete dan perlindungan double-click pada tombol konfirmasi Delete | FE+BE | TC-AC-SG-65, TC-AC-SG-111 |
| TC-AC-SG-E2E-032 | Eksekusi Delete Single sukses dengan cascade subtree dan peringatan pelepasan user | FE+BE | TC-AC-SG-60, TC-AC-SG-61, TC-AC-SG-62, TC-AC-SG-63 |
| TC-AC-SG-E2E-033 | Penanganan kegagalan Delete Single saat server error 5xx dan retensi integritas record | mock | TC-AC-SG-153 |
| TC-AC-SG-E2E-034 | Selection Limit: Live-block seleksi manual saat checkbox ke-1001 dicentang | mock | TC-AC-SG-151 |
| TC-AC-SG-E2E-035 | Selection Limit: Auto-cap Server Select All pada hasil filtered melebihi 1000 baris | FE+BE | TC-AC-SG-152 |
| TC-AC-SG-E2E-036 | Siklus seleksi massal: kemunculan Bulk Action Bar, persistensi seleksi lintas halaman, dan Server Select All | FE+BE | TC-AC-SG-69, TC-AC-SG-96, TC-AC-SG-148 |
| TC-AC-SG-E2E-037 | Perilaku Bulk Delete N=1: konversi otomatis ke dialog konfirmasi tunggal (aman maupun terblokir) | FE+BE | TC-AC-SG-170, TC-AC-SG-171 |
| TC-AC-SG-E2E-038 | Guard Bulk Delete would-empty-entity: pemblokiran total batch jika seluruh group entitas akan musnah | FE+BE | TC-AC-SG-72, TC-AC-SG-73 |
| TC-AC-SG-E2E-039 | Pemblokiran total Bulk Delete ketika seluruh baris terpilih memiliki Total Member > 0 | FE+BE | TC-AC-SG-172 |
| TC-AC-SG-E2E-040 | Pembatalan dialog Bulk Delete pada varian homogen dan varian campuran | FE+BE | TC-AC-SG-77 |
| TC-AC-SG-E2E-041 | Eksekusi Bulk Delete sukses: varian homogen, varian campuran dengan pelompataan baris, dan penanganan level 1 | FE+BE | TC-AC-SG-70, TC-AC-SG-71, TC-AC-SG-74, TC-AC-SG-76 |
| TC-AC-SG-E2E-042 | Screening popup drill-down Total User, breadcrumb full path header, dan inklusi akun Total Control | FE+BE | TC-AC-SG-79, TC-AC-SG-80, TC-AC-SG-83, TC-AC-SG-155 |
| TC-AC-SG-E2E-043 | Hirarki prioritas label kolom Group Role pada tabel popup drill-down Total User | FE+BE | TC-AC-SG-81 |
| TC-AC-SG-E2E-044 | Screening opsi dropdown filter, 5 kolom curated Setup Column, dan screening Column Visibility popup Total User | FE+BE | TC-AC-SG-161, TC-AC-SG-191, TC-AC-SG-192, TC-AC-SG-221 |
| TC-AC-SG-E2E-045 | Pencarian dan eksekusi filter granular pada popup drill-down Total User | FE+BE | TC-AC-SG-82, TC-AC-SG-168, TC-AC-SG-197, TC-AC-SG-198, TC-AC-SG-199 |
| TC-AC-SG-E2E-046 | Screening drill-down Total Member Phase 1 (Client direct only), filter, dan Column Visibility | FE+BE | TC-AC-SG-84, TC-AC-SG-85, TC-AC-SG-87, TC-AC-SG-88, TC-AC-SG-162 |
| TC-AC-SG-E2E-047 | Siklus lengkap Search Box toolbar (reveal, focus, submit Enter, clear, collapse) dan cakupan pencarian lokal | FE+BE | TC-AC-SG-89, TC-AC-SG-90, TC-AC-SG-91, TC-AC-SG-154 |
| TC-AC-SG-E2E-048 | Eksekusi filter panel tabel utama: range Min-Max, Modified By, Last Updated, dan siklus Clear Field tanpa auto-reset | FE+BE | TC-AC-SG-92, TC-AC-SG-93, TC-AC-SG-160, TC-AC-SG-177, TC-AC-SG-196 |
| TC-AC-SG-E2E-049 | Default sorting Group A-Z dan kontrol paginasi tabel utama (rows per page, page jump, independensi filter) | FE+BE | TC-AC-SG-94, TC-AC-SG-178 |
| TC-AC-SG-E2E-050 | Ekspor data tabel utama ke format CSV dan XLSX | FE+BE | TC-AC-SG-97 |
| TC-AC-SG-E2E-051 | Penanganan error saat download tabel utama gagal (500 server error) | mock | TC-AC-SG-98 |
| TC-AC-SG-E2E-052 | Setup Column tabel utama: screening modal 3 zona, toggle visibilitas kolom, dan guard minimal 1 kolom tersisa | FE+BE | TC-AC-SG-95, TC-AC-SG-204, TC-AC-SG-205, TC-AC-SG-206 |
| TC-AC-SG-E2E-053 | Setup Column tabel utama: interaksi Drag-and-Drop reorder urutan kolom dan freeze Pin scroll | FE+BE | TC-AC-SG-207, TC-AC-SG-208 |
| TC-AC-SG-E2E-054 | Setup Column tabel utama: persistensi reload F5, Reset to Default, Cancel Discard, dan isolasi cache antar tabel | FE+BE | TC-AC-SG-209, TC-AC-SG-210, TC-AC-SG-211, TC-AC-SG-212 |
| TC-AC-SG-E2E-055 | Modal Changelog: pencatatan audit trail Create/Edit/Delete, empty state, search, dan filter Action & Modified By | FE+BE | TC-AC-SG-99, TC-AC-SG-100, TC-AC-SG-101, TC-AC-SG-102, TC-AC-SG-107, TC-AC-SG-108, TC-AC-SG-186 |
| TC-AC-SG-E2E-056 | Modal Changelog: filter Date Range (termasuk single date), overlay download CSV/XLSX, dan paginasi modal | FE+BE | TC-AC-SG-200, TC-AC-SG-201, TC-AC-SG-202, TC-AC-SG-203 |
| TC-AC-SG-E2E-057 | Setup Column Modal Changelog: screening 3 zona, toggle kolom Action, dan guard minimal 1 kolom tersisa | FE+BE | TC-AC-SG-109, TC-AC-SG-213, TC-AC-SG-214, TC-AC-SG-215 |
| TC-AC-SG-E2E-058 | Setup Column Modal Changelog: interaksi Drag-and-Drop reorder urutan kolom dan freeze Pin scroll | FE+BE | TC-AC-SG-216, TC-AC-SG-217 |
| TC-AC-SG-E2E-059 | Setup Column Modal Changelog: persistensi reload F5, Reset to Default, dan Cancel Discard | FE+BE | TC-AC-SG-218, TC-AC-SG-219, TC-AC-SG-220 |
| TC-AC-SG-E2E-060 | Konkurensi 2-Aktor: Cross-action race Edit vs Delete bersamaan pada node yang sama | FE+BE | TC-AC-SG-149 |
| TC-AC-SG-E2E-061 | Konkurensi 2-Aktor: Same-action race Delete vs Delete simultan pada node yang sama | FE+BE | TC-AC-SG-150 |
| TC-AC-SG-E2E-062 | Sinkronisasi lintas modul: popup Select Group di User, kolom Group di Role, dan sidebar modul downstream | FE+BE | TC-AC-SG-124, TC-AC-SG-125, TC-AC-SG-126 |
| TC-AC-SG-E2E-063 | Aksesibilitas A11y: atribut aria-required/aria-describedby dan tooltip penjelasan pada setiap elemen disabled | mock | TC-AC-SG-139, TC-AC-SG-140 |
| TC-AC-SG-E2E-064 | Ketiadaan plan gating atau upsell pada seluruh alur fitur Settings > Group | FE+BE | TC-AC-SG-145 |

---

## 2. Daftar TC Hanya-BE (Excluded dari E2E — 23 TC)

| TC ID | Skenario | Alasan Dikecualikan dari E2E |
|---|---|---|
| TC-AC-SG-14 | Dikecualikan dari UI | Validasi query agregasi database DISTINCT backend |
| TC-AC-SG-48 | Dikecualikan dari UI | Validasi race condition level database unique constraint |
| TC-AC-SG-54 | Dikecualikan dari UI | Logika resolusi timestamp commit backend tanpa dialog konflik UI |
| TC-AC-SG-64 | Dikecualikan dari UI | Integritas baris tabel relasi database backend (user_group_managers) |
| TC-AC-SG-66 | Dikecualikan dari UI | Validasi re-evaluasi guard transaksi commit database |
| TC-AC-SG-67 | Dikecualikan dari UI | Penanganan HTTP 404 pada level handler API backend |
| TC-AC-SG-78 | Dikecualikan dari UI | Logika re-evaluasi atomik array record saat transaksi commit |
| TC-AC-SG-86 | Dikecualikan dari UI | Struktur skema database relasional backend (1:1 membership) |
| TC-AC-SG-103 | Dikecualikan dari UI | Integritas iterasi penulisan log di tingkat service BE |
| TC-AC-SG-104 | Dikecualikan dari UI | Penulisan audit record downstream ke tabel user log |
| TC-AC-SG-105 | Dikecualikan dari UI | Pemisahan penulisan record log GM di tingkat worker BE |
| TC-AC-SG-106 | Dikecualikan dari UI | Garansi integritas transaksi ACID database backend |
| TC-AC-SG-112 | Dikecualikan dari UI | Constraint keunikan (entity_id, parent_id, LOWER(name)) DB |
| TC-AC-SG-113 | Dikecualikan dari UI | Respon HTTP 404 pada request DELETE berulang |
| TC-AC-SG-114 | Dikecualikan dari UI | Penanganan idempotensi batch array ID pada API |
| TC-AC-SG-115 | Dikecualikan dari UI | Re-query status relasi record saat commit database |
| TC-AC-SG-116 | Dikecualikan dari UI | Penghitungan ulang T - E dalam transaksi database |
| TC-AC-SG-127 | Dikecualikan dari UI | Live query view database lintas modul entitas |
| TC-AC-SG-128 | Dikecualikan dari UI | Integrasi konfigurasi service runtime backend |
| TC-AC-SG-129 | Dikecualikan dari UI | Trigger lifecycle onboarding entitas backend |
| TC-AC-SG-138 | Dikecualikan dari UI | Kontrak event streaming bridge broker backend (SSE) |
| TC-AC-SG-146 | Dikecualikan dari UI | Ketiadaan batasan kuota record di skema backend |
| TC-AC-SG-147 | Dikecualikan dari UI | Validasi kedalaman rekursif pada controller API |

---

## 3. Lapisan per TC (Traceability Matrix)

| TC ID | Lapisan | Spec E2E | Mode |
|---|---|---|:---:|
| TC-AC-SG-1 | E2E | TC-AC-SG-E2E-001 | FE+BE |
| TC-AC-SG-2 | E2E | TC-AC-SG-E2E-002 | FE+BE |
| TC-AC-SG-3 | E2E | TC-AC-SG-E2E-001 | FE+BE |
| TC-AC-SG-4 | E2E | TC-AC-SG-E2E-002 | FE+BE |
| TC-AC-SG-5 | E2E | TC-AC-SG-E2E-004 | mock |
| TC-AC-SG-6 | E2E | TC-AC-SG-E2E-004 | mock |
| TC-AC-SG-7 | E2E | TC-AC-SG-E2E-001 | FE+BE |
| TC-AC-SG-163 | E2E | TC-AC-SG-E2E-005 | FE+BE |
| TC-AC-SG-164 | E2E | TC-AC-SG-E2E-005 | FE+BE |
| TC-AC-SG-222 | E2E | TC-AC-SG-E2E-016 | mock |
| TC-AC-SG-173 | E2E | TC-AC-SG-E2E-001 | FE+BE |
| TC-AC-SG-174 | E2E | TC-AC-SG-E2E-001 | FE+BE |
| TC-AC-SG-175 | E2E | TC-AC-SG-E2E-001 | FE+BE |
| TC-AC-SG-176 | E2E | TC-AC-SG-E2E-001 | FE+BE |
| TC-AC-SG-184 | E2E | TC-AC-SG-E2E-003 | FE+BE |
| TC-AC-SG-8 | E2E | TC-AC-SG-E2E-006 | FE+BE |
| TC-AC-SG-167 | E2E | TC-AC-SG-E2E-006 | FE+BE |
| TC-AC-SG-9 | E2E | TC-AC-SG-E2E-007 | FE+BE |
| TC-AC-SG-223 | E2E | TC-AC-SG-E2E-007 | FE+BE |
| TC-AC-SG-10 | E2E | TC-AC-SG-E2E-007 | FE+BE |
| TC-AC-SG-11 | E2E | TC-AC-SG-E2E-008 | FE+BE |
| TC-AC-SG-12 | E2E | TC-AC-SG-E2E-008 | FE+BE |
| TC-AC-SG-13 | E2E | TC-AC-SG-E2E-008 | FE+BE |
| TC-AC-SG-14 | Backend Only | — | — |
| TC-AC-SG-15 | E2E | TC-AC-SG-E2E-009 | FE+BE |
| TC-AC-SG-16 | E2E | TC-AC-SG-E2E-009 | FE+BE |
| TC-AC-SG-17 | E2E | TC-AC-SG-E2E-009 | FE+BE |
| TC-AC-SG-185 | E2E | TC-AC-SG-E2E-010 | FE+BE |
| TC-AC-SG-187 | E2E | TC-AC-SG-E2E-008 | FE+BE |
| TC-AC-SG-193 | E2E | TC-AC-SG-E2E-011 | FE+BE |
| TC-AC-SG-194 | E2E | TC-AC-SG-E2E-011 | FE+BE |
| TC-AC-SG-195 | E2E | TC-AC-SG-E2E-010 | FE+BE |
| TC-AC-SG-18 | E2E | TC-AC-SG-E2E-012 | FE+BE |
| TC-AC-SG-19 | E2E | TC-AC-SG-E2E-013 | FE+BE |
| TC-AC-SG-179 | E2E | TC-AC-SG-E2E-013 | FE+BE |
| TC-AC-SG-21 | E2E | TC-AC-SG-E2E-014 | FE+BE |
| TC-AC-SG-25 | E2E | TC-AC-SG-E2E-012 | FE+BE |
| TC-AC-SG-26 | E2E | TC-AC-SG-E2E-014 | FE+BE |
| TC-AC-SG-27 | E2E | TC-AC-SG-E2E-015 | FE+BE |
| TC-AC-SG-29 | E2E | TC-AC-SG-E2E-009 | FE+BE |
| TC-AC-SG-157 | E2E | TC-AC-SG-E2E-015 | FE+BE |
| TC-AC-SG-32 | E2E | TC-AC-SG-E2E-020 | FE+BE |
| TC-AC-SG-34 | E2E | TC-AC-SG-E2E-018 | FE+BE |
| TC-AC-SG-35 | E2E | TC-AC-SG-E2E-018 | FE+BE |
| TC-AC-SG-36 | E2E | TC-AC-SG-E2E-018 | FE+BE |
| TC-AC-SG-37 | E2E | TC-AC-SG-E2E-018 | FE+BE |
| TC-AC-SG-38 | E2E | TC-AC-SG-E2E-018 | FE+BE |
| TC-AC-SG-39 | E2E | TC-AC-SG-E2E-020 | FE+BE |
| TC-AC-SG-40 | E2E | TC-AC-SG-E2E-021 | mock |
| TC-AC-SG-180 | E2E | TC-AC-SG-E2E-019 | FE+BE |
| TC-AC-SG-181 | E2E | TC-AC-SG-E2E-019 | FE+BE |
| TC-AC-SG-188 | E2E | TC-AC-SG-E2E-019 | FE+BE |
| TC-AC-SG-41 | E2E | TC-AC-SG-E2E-023 | FE+BE |
| TC-AC-SG-42 | E2E | TC-AC-SG-E2E-023 | FE+BE |
| TC-AC-SG-43 | E2E | TC-AC-SG-E2E-023 | FE+BE |
| TC-AC-SG-44 | E2E | TC-AC-SG-E2E-023 | FE+BE |
| TC-AC-SG-45 | E2E | TC-AC-SG-E2E-024 | FE+BE |
| TC-AC-SG-46 | E2E | TC-AC-SG-E2E-024 | FE+BE |
| TC-AC-SG-48 | Backend Only | — | — |
| TC-AC-SG-49 | E2E | TC-AC-SG-E2E-028 | FE+BE |
| TC-AC-SG-51 | E2E | TC-AC-SG-E2E-028 | FE+BE |
| TC-AC-SG-52 | E2E | TC-AC-SG-E2E-025 | FE+BE |
| TC-AC-SG-53 | E2E | TC-AC-SG-E2E-025 | FE+BE |
| TC-AC-SG-54 | Backend Only | — | — |
| TC-AC-SG-55 | E2E | TC-AC-SG-E2E-025 | FE+BE |
| TC-AC-SG-159 | E2E | TC-AC-SG-E2E-027 | FE+BE |
| TC-AC-SG-182 | E2E | TC-AC-SG-E2E-026 | FE+BE |
| TC-AC-SG-183 | E2E | TC-AC-SG-E2E-026 | FE+BE |
| TC-AC-SG-189 | E2E | TC-AC-SG-E2E-026 | FE+BE |
| TC-AC-SG-190 | E2E | TC-AC-SG-E2E-026 | FE+BE |
| TC-AC-SG-57 | E2E | TC-AC-SG-E2E-029 | FE+BE |
| TC-AC-SG-58 | E2E | TC-AC-SG-E2E-029 | FE+BE |
| TC-AC-SG-59 | E2E | TC-AC-SG-E2E-030 | FE+BE |
| TC-AC-SG-60 | E2E | TC-AC-SG-E2E-032 | FE+BE |
| TC-AC-SG-61 | E2E | TC-AC-SG-E2E-032 | FE+BE |
| TC-AC-SG-62 | E2E | TC-AC-SG-E2E-032 | FE+BE |
| TC-AC-SG-63 | E2E | TC-AC-SG-E2E-032 | FE+BE |
| TC-AC-SG-64 | Backend Only | — | — |
| TC-AC-SG-65 | E2E | TC-AC-SG-E2E-031 | FE+BE |
| TC-AC-SG-66 | Backend Only | — | — |
| TC-AC-SG-67 | Backend Only | — | — |
| TC-AC-SG-68 | E2E | TC-AC-SG-E2E-017 | mock |
| TC-AC-SG-169 | E2E | TC-AC-SG-E2E-017 | mock |
| TC-AC-SG-153 | E2E | TC-AC-SG-E2E-033 | mock |
| TC-AC-SG-151 | E2E | TC-AC-SG-E2E-034 | mock |
| TC-AC-SG-152 | E2E | TC-AC-SG-E2E-035 | FE+BE |
| TC-AC-SG-69 | E2E | TC-AC-SG-E2E-036 | FE+BE |
| TC-AC-SG-70 | E2E | TC-AC-SG-E2E-041 | FE+BE |
| TC-AC-SG-71 | E2E | TC-AC-SG-E2E-041 | FE+BE |
| TC-AC-SG-72 | E2E | TC-AC-SG-E2E-038 | FE+BE |
| TC-AC-SG-73 | E2E | TC-AC-SG-E2E-038 | FE+BE |
| TC-AC-SG-172 | E2E | TC-AC-SG-E2E-039 | FE+BE |
| TC-AC-SG-74 | E2E | TC-AC-SG-E2E-041 | FE+BE |
| TC-AC-SG-76 | E2E | TC-AC-SG-E2E-041 | FE+BE |
| TC-AC-SG-77 | E2E | TC-AC-SG-E2E-040 | FE+BE |
| TC-AC-SG-78 | Backend Only | — | — |
| TC-AC-SG-170 | E2E | TC-AC-SG-E2E-037 | FE+BE |
| TC-AC-SG-171 | E2E | TC-AC-SG-E2E-037 | FE+BE |
| TC-AC-SG-148 | E2E | TC-AC-SG-E2E-036 | FE+BE |
| TC-AC-SG-79 | E2E | TC-AC-SG-E2E-042 | FE+BE |
| TC-AC-SG-155 | E2E | TC-AC-SG-E2E-042 | FE+BE |
| TC-AC-SG-156 | E2E | TC-AC-SG-E2E-015 | FE+BE |
| TC-AC-SG-80 | E2E | TC-AC-SG-E2E-042 | FE+BE |
| TC-AC-SG-81 | E2E | TC-AC-SG-E2E-043 | FE+BE |
| TC-AC-SG-82 | E2E | TC-AC-SG-E2E-045 | FE+BE |
| TC-AC-SG-168 | E2E | TC-AC-SG-E2E-045 | FE+BE |
| TC-AC-SG-161 | E2E | TC-AC-SG-E2E-044 | FE+BE |
| TC-AC-SG-191 | E2E | TC-AC-SG-E2E-044 | FE+BE |
| TC-AC-SG-192 | E2E | TC-AC-SG-E2E-044 | FE+BE |
| TC-AC-SG-83 | E2E | TC-AC-SG-E2E-042 | FE+BE |
| TC-AC-SG-84 | E2E | TC-AC-SG-E2E-046 | FE+BE |
| TC-AC-SG-85 | E2E | TC-AC-SG-E2E-046 | FE+BE |
| TC-AC-SG-86 | Backend Only | — | — |
| TC-AC-SG-87 | E2E | TC-AC-SG-E2E-046 | FE+BE |
| TC-AC-SG-162 | E2E | TC-AC-SG-E2E-046 | FE+BE |
| TC-AC-SG-88 | E2E | TC-AC-SG-E2E-046 | FE+BE |
| TC-AC-SG-197 | E2E | TC-AC-SG-E2E-045 | FE+BE |
| TC-AC-SG-198 | E2E | TC-AC-SG-E2E-045 | FE+BE |
| TC-AC-SG-199 | E2E | TC-AC-SG-E2E-045 | FE+BE |
| TC-AC-SG-221 | E2E | TC-AC-SG-E2E-044 | FE+BE |
| TC-AC-SG-154 | E2E | TC-AC-SG-E2E-047 | FE+BE |
| TC-AC-SG-89 | E2E | TC-AC-SG-E2E-047 | FE+BE |
| TC-AC-SG-90 | E2E | TC-AC-SG-E2E-047 | FE+BE |
| TC-AC-SG-91 | E2E | TC-AC-SG-E2E-047 | FE+BE |
| TC-AC-SG-92 | E2E | TC-AC-SG-E2E-048 | FE+BE |
| TC-AC-SG-93 | E2E | TC-AC-SG-E2E-048 | FE+BE |
| TC-AC-SG-160 | E2E | TC-AC-SG-E2E-048 | FE+BE |
| TC-AC-SG-94 | E2E | TC-AC-SG-E2E-049 | FE+BE |
| TC-AC-SG-95 | E2E | TC-AC-SG-E2E-052 | FE+BE |
| TC-AC-SG-96 | E2E | TC-AC-SG-E2E-036 | FE+BE |
| TC-AC-SG-97 | E2E | TC-AC-SG-E2E-050 | FE+BE |
| TC-AC-SG-98 | E2E | TC-AC-SG-E2E-051 | mock |
| TC-AC-SG-177 | E2E | TC-AC-SG-E2E-048 | FE+BE |
| TC-AC-SG-178 | E2E | TC-AC-SG-E2E-049 | FE+BE |
| TC-AC-SG-196 | E2E | TC-AC-SG-E2E-048 | FE+BE |
| TC-AC-SG-204 | E2E | TC-AC-SG-E2E-052 | FE+BE |
| TC-AC-SG-205 | E2E | TC-AC-SG-E2E-052 | FE+BE |
| TC-AC-SG-206 | E2E | TC-AC-SG-E2E-052 | FE+BE |
| TC-AC-SG-207 | E2E | TC-AC-SG-E2E-053 | FE+BE |
| TC-AC-SG-208 | E2E | TC-AC-SG-E2E-053 | FE+BE |
| TC-AC-SG-209 | E2E | TC-AC-SG-E2E-054 | FE+BE |
| TC-AC-SG-210 | E2E | TC-AC-SG-E2E-054 | FE+BE |
| TC-AC-SG-211 | E2E | TC-AC-SG-E2E-054 | FE+BE |
| TC-AC-SG-212 | E2E | TC-AC-SG-E2E-054 | FE+BE |
| TC-AC-SG-99 | E2E | TC-AC-SG-E2E-055 | FE+BE |
| TC-AC-SG-100 | E2E | TC-AC-SG-E2E-055 | FE+BE |
| TC-AC-SG-101 | E2E | TC-AC-SG-E2E-055 | FE+BE |
| TC-AC-SG-102 | E2E | TC-AC-SG-E2E-055 | FE+BE |
| TC-AC-SG-103 | Backend Only | — | — |
| TC-AC-SG-104 | Backend Only | — | — |
| TC-AC-SG-105 | Backend Only | — | — |
| TC-AC-SG-106 | Backend Only | — | — |
| TC-AC-SG-107 | E2E | TC-AC-SG-E2E-055 | FE+BE |
| TC-AC-SG-108 | E2E | TC-AC-SG-E2E-055 | FE+BE |
| TC-AC-SG-109 | E2E | TC-AC-SG-E2E-057 | FE+BE |
| TC-AC-SG-186 | E2E | TC-AC-SG-E2E-055 | FE+BE |
| TC-AC-SG-200 | E2E | TC-AC-SG-E2E-056 | FE+BE |
| TC-AC-SG-201 | E2E | TC-AC-SG-E2E-056 | FE+BE |
| TC-AC-SG-202 | E2E | TC-AC-SG-E2E-056 | FE+BE |
| TC-AC-SG-203 | E2E | TC-AC-SG-E2E-056 | FE+BE |
| TC-AC-SG-213 | E2E | TC-AC-SG-E2E-057 | FE+BE |
| TC-AC-SG-214 | E2E | TC-AC-SG-E2E-057 | FE+BE |
| TC-AC-SG-215 | E2E | TC-AC-SG-E2E-057 | FE+BE |
| TC-AC-SG-216 | E2E | TC-AC-SG-E2E-058 | FE+BE |
| TC-AC-SG-217 | E2E | TC-AC-SG-E2E-058 | FE+BE |
| TC-AC-SG-218 | E2E | TC-AC-SG-E2E-059 | FE+BE |
| TC-AC-SG-219 | E2E | TC-AC-SG-E2E-059 | FE+BE |
| TC-AC-SG-220 | E2E | TC-AC-SG-E2E-059 | FE+BE |
| TC-AC-SG-110 | E2E | TC-AC-SG-E2E-022 | FE+BE |
| TC-AC-SG-111 | E2E | TC-AC-SG-E2E-031 | FE+BE |
| TC-AC-SG-112 | Backend Only | — | — |
| TC-AC-SG-113 | Backend Only | — | — |
| TC-AC-SG-114 | Backend Only | — | — |
| TC-AC-SG-115 | Backend Only | — | — |
| TC-AC-SG-116 | Backend Only | — | — |
| TC-AC-SG-149 | E2E | TC-AC-SG-E2E-060 | FE+BE |
| TC-AC-SG-150 | E2E | TC-AC-SG-E2E-061 | FE+BE |
| TC-AC-SG-124 | E2E | TC-AC-SG-E2E-062 | FE+BE |
| TC-AC-SG-125 | E2E | TC-AC-SG-E2E-062 | FE+BE |
| TC-AC-SG-126 | E2E | TC-AC-SG-E2E-062 | FE+BE |
| TC-AC-SG-127 | Backend Only | — | — |
| TC-AC-SG-128 | Backend Only | — | — |
| TC-AC-SG-129 | Backend Only | — | — |
| TC-AC-SG-138 | Backend Only | — | — |
| TC-AC-SG-139 | E2E | TC-AC-SG-E2E-063 | mock |
| TC-AC-SG-140 | E2E | TC-AC-SG-E2E-063 | mock |
| TC-AC-SG-145 | E2E | TC-AC-SG-E2E-064 | FE+BE |
| TC-AC-SG-146 | Backend Only | — | — |
| TC-AC-SG-147 | Backend Only | — | — |
