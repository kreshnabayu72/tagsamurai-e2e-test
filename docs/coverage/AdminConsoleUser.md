# Coverage E2E — Admin Console > Settings > User

Sumber: `admin-console/settings-user/TestCases/tc-settings-user.md` (260 TC granular aktif) dan `admin-console/settings-user/TestCases/tc-settings-user-backend.md`.
Suite: `specs/AdminConsole/User/`.
Prefix Modul: `AC` + `SU` (`TC-AC-SU-E2E-*`).
Status semua spec: `draft`.

---

## 1. Pemetaan TC Granular → Spec E2E (44 Spec Atomik)

| Spec | Isi / Judul | Mode | TC Sumber |
|---|---|:---:|---|
| TC-AC-SU-E2E-001 | Screening halaman User List, breadcrumb, header, struktur kolom tabel, baris Default User dan Self | FE+BE | TC-AC-SU-1, TC-AC-SU-2, TC-AC-SU-3, TC-AC-SU-4, TC-AC-SU-5, TC-AC-SU-6, TC-AC-SU-7, TC-AC-SU-8, TC-AC-SU-9, TC-AC-SU-12, TC-AC-SU-264, TC-AC-SU-265, TC-AC-SU-266 |
| TC-AC-SU-E2E-002 | Loading state, simulasi error fetch 500, pemulihan via Try Again, dan empty state no results found | mock | TC-AC-SU-10, TC-AC-SU-11 |
| TC-AC-SU-E2E-003 | Guided Tooltip walkthrough 5 step, auto-trigger kunjungan pertama, manual replay, dan keyboard navigation | FE+BE | TC-AC-SU-228, TC-AC-SU-229, TC-AC-SU-267, TC-AC-SU-268 |
| TC-AC-SU-E2E-004 | Setup Column User List, toggle visibilitas 4 kolom curated, render badge format, dan sorting | FE+BE | TC-AC-SU-260 |
| TC-AC-SU-E2E-005 | Pencarian toolbar User List per kolom teks dan guard kolom non-searchable | FE+BE | TC-AC-SU-13, TC-AC-SU-14, TC-AC-SU-234, TC-AC-SU-235, TC-AC-SU-236, TC-AC-SU-237, TC-AC-SU-238 |
| TC-AC-SU-E2E-006 | Filter Panel User List, multi-select searchable, populate dropdown dinamis, dan enum hardcode | FE+BE | TC-AC-SU-15, TC-AC-SU-16, TC-AC-SU-17, TC-AC-SU-18, TC-AC-SU-226, TC-AC-SU-269, TC-AC-SU-270, TC-AC-SU-272 |
| TC-AC-SU-E2E-007 | Filter rentang tanggal Last Updated dan Temporary Until serta kepatuhan format General Settings | FE+BE | TC-AC-SU-271, TC-AC-SU-273, TC-AC-SU-285 |
| TC-AC-SU-E2E-008 | Sorting 3-state pada 12 kolom sortable User List, transisi header sort, dan guard kolom non-sortable | FE+BE | TC-AC-SU-19, TC-AC-SU-274, TC-AC-SU-275, TC-AC-SU-276 |
| TC-AC-SU-E2E-009 | Navigasi Sidebar Group tree hirarki, filtering user per group, dan persistensi state collapse | FE+BE | TC-AC-SU-20, TC-AC-SU-293 |
| TC-AC-SU-E2E-010 | Export CSV dan XLSX User List, format WYSIWYG kolom terfilter, transformasi representasi teks, dan penanganan error | FE+BE | TC-AC-SU-22, TC-AC-SU-277, TC-AC-SU-278, TC-AC-SU-279, TC-AC-SU-280 |
| TC-AC-SU-E2E-011 | Modal Changelog User List, Search, Filter Panel, Column Visibility terpisah, dan export CSV | FE+BE | TC-AC-SU-23, TC-AC-SU-24, TC-AC-SU-25, TC-AC-SU-227 |
| TC-AC-SU-E2E-012 | Persistensi state filter dan search saat tab switching dan refresh F5, pagination page size, serta Clear Filter | FE+BE | TC-AC-SU-232, TC-AC-SU-233, TC-AC-SU-281, TC-AC-SU-282, TC-AC-SU-283, TC-AC-SU-284 |
| TC-AC-SU-E2E-013 | Aktivasi user baris tunggal (OFF ke ON), dialog konfirmasi info, Cancel path, dan aktivasi sukses | FE+BE | TC-AC-SU-26, TC-AC-SU-223 |
| TC-AC-SU-E2E-014 | Deaktivasi user baris tunggal (ON ke OFF), dialog konfirmasi danger, focus trap a11y, Cancel path, dan force logout | FE+BE | TC-AC-SU-27, TC-AC-SU-28, TC-AC-SU-29, TC-AC-SU-291 |
| TC-AC-SU-E2E-015 | Guard proteksi switch Active: Default User, Self-edit, entitas suspended, isActiveGlobal=false, dan tier restrictions | FE+BE | TC-AC-SU-30, TC-AC-SU-31, TC-AC-SU-32, TC-AC-SU-33, TC-AC-SU-34, TC-AC-SU-35, TC-AC-SU-36, TC-AC-SU-160 |
| TC-AC-SU-E2E-016 | Bulk Action Bar, Server Select All lintas halaman, toggle Unselect All, Bulk Activate dan Deactivate | FE+BE | TC-AC-SU-37, TC-AC-SU-38, TC-AC-SU-214, TC-AC-SU-224, TC-AC-SU-225, TC-AC-SU-249, TC-AC-SU-287, TC-AC-SU-288 |
| TC-AC-SU-E2E-017 | Bulk Action Bar dengan 1 baris terpilih collapse ke format dialog baris tunggal (tanpa bullet list) | FE+BE | TC-AC-SU-230, TC-AC-SU-231 |
| TC-AC-SU-E2E-018 | Selection Limit 1000 baris: auto-cap pada Server Select All dan live-block disabled pada centang manual ke-1001 | FE+BE | TC-AC-SU-39, TC-AC-SU-222 |
| TC-AC-SU-E2E-019 | Resiliensi error 5xx dengan optimistic rollback dan penanganan 409 Conflict pada Activate/Deactivate | mock | TC-AC-SU-41, TC-AC-SU-174, TC-AC-SU-219, TC-AC-SU-263 |
| TC-AC-SU-E2E-020 | Row action Resend Activation Email, cooldown 60 detik, proteksi klik berulang, dan verifikasi template email | FE+BE | TC-AC-SU-42, TC-AC-SU-43, TC-AC-SU-44, TC-AC-SU-47, TC-AC-SU-217, TC-AC-SU-286 |
| TC-AC-SU-E2E-021 | Bulk Resend Activation Email: partial skip non-pending, partial skip cooldown, dan sukses homogen | FE+BE | TC-AC-SU-46, TC-AC-SU-258, TC-AC-SU-289 |
| TC-AC-SU-E2E-022 | Row action Resend Confirmation Email, cooldown 60 detik, verifikasi template email baru, dan guard tidak muncul di Bulk Bar | FE+BE | TC-AC-SU-48, TC-AC-SU-49, TC-AC-SU-50, TC-AC-SU-51, TC-AC-SU-218, TC-AC-SU-292 |
| TC-AC-SU-E2E-023 | Resiliensi server error 5xx pada Resend Activation dan Confirmation Email tanpa mengonsumsi cooldown | mock | TC-AC-SU-178, TC-AC-SU-220 |
| TC-AC-SU-E2E-024 | Detail User: Header read-only, hierarki badge User Type, General Information, dan Custom Field accordion | FE+BE | TC-AC-SU-54, TC-AC-SU-55, TC-AC-SU-57, TC-AC-SU-58, TC-AC-SU-59, TC-AC-SU-60, TC-AC-SU-62, TC-AC-SU-63 |
| TC-AC-SU-E2E-025 | Tab Role Sub-tab Global Role: toggle role ON/OFF, autosave CRUD per cell, dan sinkronisasi 2-arah ke Role & Permission | FE+BE | TC-AC-SU-64, TC-AC-SU-65, TC-AC-SU-66, TC-AC-SU-67, TC-AC-SU-68 |
| TC-AC-SU-E2E-026 | Guard Sub-tab Global Role (Default User, Self-edit, target TC/RO), modal Changelog, dan rollback CRUD error 5xx | FE+BE | TC-AC-SU-69, TC-AC-SU-71, TC-AC-SU-72, TC-AC-SU-73, TC-AC-SU-161, TC-AC-SU-176, TC-AC-SU-252 |
| TC-AC-SU-E2E-027 | Tab Role Sub-tab Group Role: katalog role, Group Summary Badge, toggle ON retained vs OFF, dan cabut akses group | FE+BE | TC-AC-SU-74, TC-AC-SU-75, TC-AC-SU-76, TC-AC-SU-77, TC-AC-SU-80, TC-AC-SU-81, TC-AC-SU-82, TC-AC-SU-85 |
| TC-AC-SU-E2E-028 | Guard Sub-tab Group Role (Default User, Self-edit), popup Detail Group Assignment read-only, dan modal Changelog | FE+BE | TC-AC-SU-84, TC-AC-SU-162, TC-AC-SU-221, TC-AC-SU-261 |
| TC-AC-SU-E2E-029 | Popup Assign Group Role: hierarki tree Select Group, scope restriction already-assigned disabled, dan proteksi duplikat | FE+BE | TC-AC-SU-86, TC-AC-SU-87, TC-AC-SU-90, TC-AC-SU-91, TC-AC-SU-93, TC-AC-SU-256 |
| TC-AC-SU-E2E-030 | Assign Group Role: toggle ON kosong, Save replace PUT, toast assigned/updated, no-op, guard 0 group, dan dialog Unsaved Changes | FE+BE | TC-AC-SU-78, TC-AC-SU-79, TC-AC-SU-96, TC-AC-SU-99, TC-AC-SU-101, TC-AC-SU-250, TC-AC-SU-251, TC-AC-SU-257, TC-AC-SU-259 |
| TC-AC-SU-E2E-031 | Resiliensi error 5xx dan penanganan 409 Conflict pada popup Assign Group Role | mock | TC-AC-SU-97, TC-AC-SU-98, TC-AC-SU-177 |
| TC-AC-SU-E2E-032 | Banner tier di Tab Role (Total Control, Read Only, Group Manager) dan ketiadaan kontrol assign tier di Settings > User | FE+BE | TC-AC-SU-102, TC-AC-SU-103, TC-AC-SU-104, TC-AC-SU-105 |
| TC-AC-SU-E2E-033 | Siklus Auto-Revert tier Total Control dan Group Manager saat edit role individual menyimpang dan dialog konfirmasi | FE+BE | TC-AC-SU-70, TC-AC-SU-107, TC-AC-SU-108, TC-AC-SU-110, TC-AC-SU-112, TC-AC-SU-262, TC-AC-SU-290 |
| TC-AC-SU-E2E-034 | Detail User Tab Responsibilities: tabel Pending Approvals, default sort, badge count, Setup Column, dan export CSV | FE+BE | TC-AC-SU-116, TC-AC-SU-117, TC-AC-SU-119, TC-AC-SU-120, TC-AC-SU-121, TC-AC-SU-122, TC-AC-SU-123, TC-AC-SU-253 |
| TC-AC-SU-E2E-035 | Detail User Tab Changelog per-user: 6 kolom, Search, Filter Panel date range, Setup Column terpisah, dan export CSV | FE+BE | TC-AC-SU-124, TC-AC-SU-126, TC-AC-SU-127, TC-AC-SU-128, TC-AC-SU-129, TC-AC-SU-130, TC-AC-SU-131, TC-AC-SU-132, TC-AC-SU-133 |
| TC-AC-SU-E2E-036 | Detail User Tab System Log (aksi oleh user ini sebagai aktor): struktur kolom, scoping per-app, dan export CSV | FE+BE | TC-AC-SU-134, TC-AC-SU-135, TC-AC-SU-137, TC-AC-SU-138, TC-AC-SU-139, TC-AC-SU-141 |
| TC-AC-SU-E2E-037 | Detail User Tab User Log (riwayat sesi Admin Console): 6 kolom baku, Filter Date, event force-logout, dan export CSV | FE+BE | TC-AC-SU-240, TC-AC-SU-241, TC-AC-SU-242, TC-AC-SU-244, TC-AC-SU-245, TC-AC-SU-246 |
| TC-AC-SU-E2E-038 | Notifikasi in-app ke target user pada Remove dan Auto-Revert access, format view-only, dan guard tanpa notifikasi pada Assign | FE+BE | TC-AC-SU-204, TC-AC-SU-205, TC-AC-SU-206, TC-AC-SU-208, TC-AC-SU-209, TC-AC-SU-210, TC-AC-SU-211, TC-AC-SU-212, TC-AC-SU-247, TC-AC-SU-248 |
| TC-AC-SU-E2E-039 | Role Matrix Positif: akses menu Settings > User dan kontrol write penuh untuk Principal TC, Distributor TC, Partner TC, dan Manage user and role | FE+BE | TC-AC-SU-150 |
| TC-AC-SU-E2E-040 | Role Matrix Negatif: penolakan sidebar menu dan Direct URL 403 untuk Client, Group Manager, role lain, dan mode Read Only | FE+BE | TC-AC-SU-21, TC-AC-SU-153, TC-AC-SU-154, TC-AC-SU-239 |
| TC-AC-SU-E2E-041 | Isolasi data antar entitas Distributor dan mode blanket lock read-only pada entitas suspended | FE+BE | TC-AC-SU-40, TC-AC-SU-151, TC-AC-SU-159 |
| TC-AC-SU-E2E-042 | Resiliensi race condition 2 aktor: Deactivate vs Assign Group Role dan Deactivate vs Edit Role Auto-Revert | FE+BE | TC-AC-SU-215, TC-AC-SU-216 |
| TC-AC-SU-E2E-043 | Aksesibilitas tooltip alasan disabled, keyboard navigation, aria-live polite, dan verifikasi ketiadaan plan gating | FE+BE | TC-AC-SU-196, TC-AC-SU-197, TC-AC-SU-198, TC-AC-SU-202, TC-AC-SU-203 |
| TC-AC-SU-E2E-044 | Sinkronisasi lintas modul: pembaruan foto profil di Global Settings dan fan-out data transaksi Approvals | FE+BE | TC-AC-SU-56, TC-AC-SU-185, TC-AC-SU-186 |

---

## 2. TC Granular Hanya-BE (Pure Backend Contract — Tidak Masuk Spec E2E UI)

| TC ID | Skenario | Alasan Pengecualian E2E UI |
|---|---|---|
| TC-AC-SU-53 | Email Confirmed tidak menghasilkan log di modul ini | Event konfirmasi email dicatat penuh di Global Settings, AC tidak menulis log redundan |
| TC-AC-SU-83 | Multi-group CRUD resolution exact match tanpa pewarisan | Logika resolusi query otorisasi database level backend |
| TC-AC-SU-106 | Assign Total Control dari Role & Permission bulk-write peran | Penugasan tier via backend batch write ke tabel peran |
| TC-AC-SU-109 | Remove Total Control reset peran individual | Logika cascade reset peran di tingkat database backend |
| TC-AC-SU-111 | Assign GM materialize Group Role di group target | Materialisasi role assignment di tingkat database backend |
| TC-AC-SU-113 | Mutual-exclusive Total Control/Read Only vs Group Manager | Validasi constraint entitas di backend API validator |
| TC-AC-SU-115 | Remove GM otomatis saat Group dihapus | Database cascade trigger penghapusan group di Settings > Group |
| TC-AC-SU-118 | Sumber baris Pending Approvals target user | Resolusi query backend untuk approver eligibility |
| TC-AC-SU-125 | 1 write tersinkronisasi ke modal dan tab | Integritas database single source of truth |
| TC-AC-SU-136 | System Log per-app tidak dikonsolidasikan | Isolasi scoping database per aplikasi backend |
| TC-AC-SU-142..149 | Logging 6-Surface Sync | Komitmen transaksi atomik database 6 surface logging |
| TC-AC-SU-152 | 1 email = 1 akun = 1 entitas | Model constraint level database backend |
| TC-AC-SU-175 | Bulk Activate/Deactivate partial commit | Logika commit parsial transaksi database |
| TC-AC-SU-180 | GS cabut App Access hapus baris user_module_status | Sinkronisasi grant modul pada skema database backend |
| TC-AC-SU-181 | GS guard tidak bisa cabut App Access AC Default User | Guard pencegahan di sisi modul Global Settings |
| TC-AC-SU-182 | GS hapus user cascade hard-delete role tables | Database cascade trigger saat soft-delete user di GS |
| TC-AC-SU-183 | Settings > Group hapus group cascade assignment | Database cascade trigger penghapusan role assignment |
| TC-AC-SU-184 | Onboarding Default User otomatis Total Control | Seeding data inisialisasi entitas baru di backend |
| TC-AC-SU-187 | Schema migration penambahan role di masa depan | Script migrasi database skema platform |
| TC-AC-SU-207 | Auto-Revert TC dipicu dari Role & Permission | Notifikasi trigger event origin Role & Permission |
| TC-AC-SU-213 | Auto-Revert GM multi-group boundary notifikasi | Logika percabangan notifikasi multi-group di backend |
| TC-AC-SU-243 | User Log per-app tidak dikonsolidasikan ke GS | Isolasi scoping database sesi per aplikasi backend |

---

## 3. TC Superseded / Dicabut

- **TC-AC-SU-52:** Superseded (Bulk Resend Confirmation Email dihapus, disamakan dengan GS).
- **TC-AC-SU-92:** Superseded (Model aktor group scope dihapus).
- **TC-AC-SU-140:** Superseded (Session Log digantikan Tab User Log Kategori X).
- **TC-AC-SU-155, 157, 158:** Superseded (Global Role entity-wide, dialog safeguard dihapus).
- **TC-AC-SU-199, 200, 201, 254, 255:** Dicabut (Skenario mobile/responsive dihapus sesuai konvensi web-only).
