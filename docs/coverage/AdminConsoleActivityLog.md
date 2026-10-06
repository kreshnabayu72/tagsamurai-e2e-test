# Coverage E2E — Admin Console > Activity Log

Sumber: `admin-console/activity-log/TestCases/tc-activity-log.md` (238 TC granular aktif) dan `admin-console/activity-log/TestCases/tc-activity-log-backend.md`.
Referensi: `admin-console/activity-log/TestCases/tc-activity-log-frontend.md`.
Suite: `specs/AdminConsole/ActivityLog/`.
Prefix Modul: `AC` + `ACAL` (`TC-AC-ACAL-E2E-*`).
Status semua spec: `draft`.

---

## 1. Pemetaan TC Granular → Spec E2E (42 Spec Atomik)

| Spec | Isi / Judul | Mode | TC Sumber |
|---|---|:---:|---|
| TC-AC-ACAL-E2E-001 | Screening halaman Activity Log, breadcrumb, 2 tab, toolbar, dan navigasi tab independen | FE+BE | TC-AC-ACAL-01, 02, 03, 20, 21, 22, 263 |
| TC-AC-ACAL-E2E-002 | Loading state, simulasi error fetch 500, dan pemulihan tabel via tombol Try Again | mock | TC-AC-ACAL-06, 07, 12, 13, 14, 15 |
| TC-AC-ACAL-E2E-003 | Empty state genuinely kosong pada Tab Session dan Tab User Action untuk entitas baru | FE+BE | TC-AC-ACAL-08, 09 |
| TC-AC-ACAL-E2E-004 | Tampilan empty state no results found saat pencarian tidak menemukan hasil pada kedua tab | FE+BE | TC-AC-ACAL-10, 11, 44, 136 |
| TC-AC-ACAL-E2E-005 | Default sort Date newest first dan format tanggal sesuai General Settings pada kedua tab | FE+BE | TC-AC-ACAL-04, 05, 231, 232 |
| TC-AC-ACAL-E2E-006 | Hover tooltip teks panjang terpotong dan siklus lengkap Guided Tooltip Walkthrough | FE+BE | TC-AC-ACAL-257, 258, 264 |
| TC-AC-ACAL-E2E-007 | Role Matrix Positif — Akses menu dan kontrol penuh untuk Principal, Distributor, dan Partner | FE+BE | TC-AC-ACAL-23, 24, 25, 27, 28 |
| TC-AC-ACAL-E2E-008 | Role Matrix Negatif — Penolakan menu sidebar dan Direct URL 403 untuk Client dan Group Manager | FE+BE | TC-AC-ACAL-26, 29, 30, 31, 32 |
| TC-AC-ACAL-E2E-009 | Entity Scoping — Isolasi visibilitas log riwayat antar Distributor, Partner, dan Principal | FE+BE | TC-AC-ACAL-234, 235, 236, 237 |
| TC-AC-ACAL-E2E-010 | Tab Session — Search toolbar per kolom dan guard kolom Date yang tidak tercakup search text | FE+BE | TC-AC-ACAL-33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43 |
| TC-AC-ACAL-E2E-011 | Tab Session — Siklus interaksi Search Box (reveal, clear, submit, collapse) | FE+BE | TC-AC-ACAL-45 |
| TC-AC-ACAL-E2E-012 | Tab Session — Screening struktur Filter Panel 4 field dan fungsi filter individual | FE+BE | TC-AC-ACAL-46, 47, 48, 49, 50, 268 |
| TC-AC-ACAL-E2E-013 | Tab Session — Populasi opsi dropdown filter User, Position, dan Division terisi secara dinamis dari log | FE+BE | TC-AC-ACAL-51, 52, 53 |
| TC-AC-ACAL-E2E-014 | Tab Session — Search dalam dropdown filter, logika OR multi-select, penambahan dan penghapusan chip | FE+BE | TC-AC-ACAL-54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 269, 270, 271 |
| TC-AC-ACAL-E2E-015 | Tab Session — Kombinasi penuh 4 kontrol, pelepasan filter parsial, dan pemulihan recovery data | FE+BE | TC-AC-ACAL-77, 78, 79, 80, 81 |
| TC-AC-ACAL-E2E-016 | Tab Session — Sorting 3-state pada 9 kolom sortable dan guard kolom Status tidak sortable | FE+BE | TC-AC-ACAL-68, 69, 70, 71, 72, 73, 74, 75, 76 |
| TC-AC-ACAL-E2E-017 | Tab Session — Screening Dropdown Overlay Quick Panel dan struktur Popup Modal Setup Column 3 Zona | FE+BE | TC-AC-ACAL-83, 84 |
| TC-AC-ACAL-E2E-018 | Tab Session — Check/Uncheck visibilitas 10 kolom, Live Preview, dan persistensi reload F5 | FE+BE | TC-AC-ACAL-85, 86, 87, 88, 89, 90, 91, 92, 93, 94 |
| TC-AC-ACAL-E2E-019 | Tab Session — Drag and drop reordering urutan 10 kolom dan persistensi reload F5 | FE+BE | TC-AC-ACAL-95, 96, 97, 98, 99, 100, 101, 102, 103, 104 |
| TC-AC-ACAL-E2E-020 | Tab Session — Pin freeze kolom sticky, Reset to Default, Cancel Discard, dan isolasi cache antar tab | FE+BE | TC-AC-ACAL-105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117 |
| TC-AC-ACAL-E2E-021 | Tab Session — Export CSV/XLSX seluruh data, data terfilter, filter kosong, dan penanganan error | FE+BE | TC-AC-ACAL-118, 119, 120, 121, 123 |
| TC-AC-ACAL-E2E-022 | Tab Session — Pengalihan ke Background Download untuk dataset besar (>5.000 baris) | FE+BE | TC-AC-ACAL-122 |
| TC-AC-ACAL-E2E-023 | Tab Session — Penggantian Page Size, navigasi Next/Prev, dan retensi state filter saat reload F5 | FE+BE | TC-AC-ACAL-16, 124, 125, 126, 127, 265 |
| TC-AC-ACAL-E2E-024 | Tab User Action — Search toolbar per kolom untuk seluruh field teks | FE+BE | TC-AC-ACAL-128, 129, 130, 131, 132, 133, 134, 135 |
| TC-AC-ACAL-E2E-025 | Tab User Action — Siklus interaksi Search Box (reveal, clear, submit, collapse) | FE+BE | TC-AC-ACAL-137 |
| TC-AC-ACAL-E2E-026 | Tab User Action — Screening struktur Filter Panel 4 field dan fungsi filter individual | FE+BE | TC-AC-ACAL-138, 139, 140, 141, 142, 272 |
| TC-AC-ACAL-E2E-027 | Tab User Action — Populasi opsi dropdown filter Action, Object, dan Modified By secara dinamis | FE+BE | TC-AC-ACAL-143, 144, 145 |
| TC-AC-ACAL-E2E-028 | Tab User Action — Search dalam dropdown filter, logika OR multi-select, dan manajemen chip | FE+BE | TC-AC-ACAL-146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 273, 274, 275 |
| TC-AC-ACAL-E2E-029 | Tab User Action — Kombinasi penuh 4 kontrol, pelepasan filter parsial, dan pemulihan recovery data | FE+BE | TC-AC-ACAL-168, 169, 170, 171, 172 |
| TC-AC-ACAL-E2E-030 | Tab User Action — Sorting 3-state pada 6 kolom sortable dan guard kolom Old/New Value tidak sortable | FE+BE | TC-AC-ACAL-160, 161, 162, 163, 164, 165, 166, 167 |
| TC-AC-ACAL-E2E-031 | Tab User Action — Screening Dropdown Overlay Quick Panel dan Popup Modal Setup Column 8 Kolom | FE+BE | TC-AC-ACAL-174, 175 |
| TC-AC-ACAL-E2E-032 | Tab User Action — Check/Uncheck visibilitas 8 kolom, Live Preview, dan persistensi reload F5 | FE+BE | TC-AC-ACAL-176, 177, 178, 179, 180, 181, 182, 183 |
| TC-AC-ACAL-E2E-033 | Tab User Action — Drag and drop reordering urutan 8 kolom dan persistensi reload F5 | FE+BE | TC-AC-ACAL-184, 185, 186, 187, 188, 189, 190, 191 |
| TC-AC-ACAL-E2E-034 | Tab User Action — Pin freeze kolom sticky, Reset to Default, Cancel Discard, dan isolasi cache | FE+BE | TC-AC-ACAL-192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202 |
| TC-AC-ACAL-E2E-035 | Tab User Action — Export CSV/XLSX seluruh data, data terfilter, filter kosong, dan penanganan error | FE+BE | TC-AC-ACAL-203, 204, 205, 206, 208 |
| TC-AC-ACAL-E2E-036 | Tab User Action — Pengalihan ke Background Download untuk dataset besar (>5.000 baris) | FE+BE | TC-AC-ACAL-207 |
| TC-AC-ACAL-E2E-037 | Tab User Action — Penggantian Page Size, navigasi Next/Prev, dan retensi state filter saat reload F5 | FE+BE | TC-AC-ACAL-17, 209, 210, 211, 266 |
| TC-AC-ACAL-E2E-038 | Sinkronisasi Real-time SSE — Entri baru otomatis muncul di atas tabel dan filter guard | FE+BE | TC-AC-ACAL-18, 19, 82, 173 |
| TC-AC-ACAL-E2E-039 | Keamanan & Format — Sanitasi XSS script injection pada Search toolbar dan format IP Address | FE+BE | TC-AC-ACAL-238, 239 |
| TC-AC-ACAL-E2E-040 | Integritas Data — Snapshot immutability data historis log terhadap mutasi nama master data | FE+BE | TC-AC-ACAL-240 |
| TC-AC-ACAL-E2E-041 | Tab User Action — Mutasi multi-field menghasilkan N entri baris terpisah dengan timestamp identik | FE+BE | TC-AC-ACAL-241 |
| TC-AC-ACAL-E2E-042 | Plan Gating — Ketiadaan plan gating dan fungsionalitas identik lintas seluruh tier langganan | FE+BE | TC-AC-ACAL-242 |
