# Coverage E2E — Fixed Asset > Settings > Accounting > Asset Class

Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (749 TC granular aktif). Modul tidak punya `tc-asset-class-backend.md`.
Suite: `specs/FixedAsset/AssetClass/` (beserta `suite.md`).
Prefix Modul: `FA` + `AC` (`TC-FA-FAAC-E2E-*`).
Status semua spec: `draft`.

---

## 1. Pemetaan TC Granular → Spec E2E (216 Spec)

| Spec | Isi / Judul | Mode | Langkah | TC Sumber |
|---|---|:---:|:---:|---|
| TC-FA-FAAC-E2E-001-screening-halaman-accounting-tab-asset-class-dan-navigasi | Screening Halaman Settings > Accounting Tab Asset Class dan Urutan Empat Tab | FE+BE | 31 | TC-FA-FAAC-1, TC-FA-FAAC-2 |
| TC-FA-FAAC-E2E-002-tampilan-tabel-urutan-link-asset-names-dan-format-ringkasan | Tampilan Tabel Asset Class: Loading, Empty State Search, Urutan Awal, Link Asset Names, Tooltip Accounts, dan Format Commercial | FE+BE | 31 | TC-FA-FAAC-7, TC-FA-FAAC-10, TC-FA-FAAC-11, TC-FA-FAAC-12, TC-FA-FAAC-13, TC-FA-FAAC-670, TC-FA-FAAC-671 |
| TC-FA-FAAC-E2E-003-menu-accounting-per-plan-dan-akses-url-starter | Menu Accounting per Plan Client dan Akses URL Tab Asset Class pada Plan Starter | FE+BE | 14 | TC-FA-FAAC-5, TC-FA-FAAC-646, TC-FA-FAAC-6 |
| TC-FA-FAAC-E2E-004-empty-state-tabel-dan-use-recommended-classes-blokir | Empty State Tabel Asset Class dan Dialog Use Recommended Classes: Screening, Create Tanpa Baris, Cancel, Baris Disabled, dan Blokir Batas Jumlah | FE+BE | 45 | TC-FA-FAAC-9, TC-FA-FAAC-282, TC-FA-FAAC-285, TC-FA-FAAC-293, TC-FA-FAAC-286, TC-FA-FAAC-290, TC-FA-FAAC-291 |
| TC-FA-FAAC-E2E-005-use-recommended-classes-validasi-baris-dan-tutup-dialog | Dialog Use Recommended Classes: Validasi Class Code dan Class Name per Baris, Class Code Duplikat, Klik Backdrop, dan Unsaved Changes | FE+BE | 54 | TC-FA-FAAC-288, TC-FA-FAAC-289, TC-FA-FAAC-287, TC-FA-FAAC-699, TC-FA-FAAC-710 |
| TC-FA-FAAC-E2E-006-use-recommended-classes-create-berhasil | Use Recommended Classes: Create Berhasil Satu Baris dengan Perubahan, Baris LAND Tanpa Asset Name, dan Delapan Baris Sekaligus | FE+BE | 34 | TC-FA-FAAC-284, TC-FA-FAAC-644, TC-FA-FAAC-283 |
| TC-FA-FAAC-E2E-007-guided-tooltip-otomatis-telusur-dan-selesai | Guided Tooltip Tab Asset Class: Mulai Otomatis pada Kunjungan Pertama, Telusur Delapan Step dengan Next, dan Done Menyimpan Flag | FE+BE | 36 | TC-FA-FAAC-46, TC-FA-FAAC-47, TC-FA-FAAC-48 |
| TC-FA-FAAC-E2E-008-guided-tooltip-skip-back-esc-dan-pindah-tab | Guided Tooltip Tab Asset Class: Back, Skip, Klik Overlay, Esc Menyimpan Flag, dan Pindah Halaman Tidak Menyimpan Flag | FE+BE | 50 | TC-FA-FAAC-51, TC-FA-FAAC-49, TC-FA-FAAC-50, TC-FA-FAAC-54, TC-FA-FAAC-55 |
| TC-FA-FAAC-E2E-009-guided-tooltip-replay-dan-navigasi-keyboard | Guided Tooltip Tab Asset Class: Replay Lewat Tombol [?] dan Navigasi Keyboard Enter dan Panah | FE+BE | 20 | TC-FA-FAAC-52, TC-FA-FAAC-53 |
| TC-FA-FAAC-E2E-010-screening-detail-mode-create-semua-tab | Screening Halaman Detail Mode Create: Tab General, Depreciation, Accounts, dan Asset Names | FE+BE | 59 | TC-FA-FAAC-15, TC-FA-FAAC-16, TC-FA-FAAC-17, TC-FA-FAAC-20 |
| TC-FA-FAAC-E2E-011-screening-detail-mode-edit-dan-tab-asset-names | Screening Halaman Detail Mode Edit: Badge Status dan Tab Asset Names (Berisi, Search Kosong, dan Genuinely Empty) | FE+BE | 50 | TC-FA-FAAC-18, TC-FA-FAAC-19, TC-FA-FAAC-21, TC-FA-FAAC-23, TC-FA-FAAC-22 |
| TC-FA-FAAC-E2E-012-alert-dependensi-akun-chart-of-accounts | Alert Dependensi Akun Chart of Accounts: Teks per Account Function, Posisi di Atas Banner, dan Tidak Tampil Saat Lengkap | FE+BE | 14 | TC-FA-FAAC-24, TC-FA-FAAC-31, TC-FA-FAAC-25, TC-FA-FAAC-26 |
| TC-FA-FAAC-E2E-013-banner-asset-name-tanpa-asset-class-dan-dialog-d23 | Banner Asset Name Tanpa Asset Class (0, 3, dan 1 Asset Name) serta Screening dan Penutupan Dialog Asset Names Without Asset Class | FE+BE | 35 | TC-FA-FAAC-33, TC-FA-FAAC-35, TC-FA-FAAC-270, TC-FA-FAAC-271, TC-FA-FAAC-272, TC-FA-FAAC-34 |
| TC-FA-FAAC-E2E-014-dialog-d23-search-dan-sort | Dialog Asset Names Without Asset Class: Search Hanya Mencocokkan Asset Name dan Siklus Sort Tiga Tahap Tiap Kolom | FE+BE | 30 | TC-FA-FAAC-273, TC-FA-FAAC-274, TC-FA-FAAC-275, TC-FA-FAAC-276, TC-FA-FAAC-277 |
| TC-FA-FAAC-E2E-015-dialog-d23-kolom-dan-tutup-otomatis | Dialog Asset Names Without Asset Class: Sembunyikan dan Tampilkan Kolom, serta Menutup Sendiri Saat Jumlah Menjadi 0 | FE+BE | 22 | TC-FA-FAAC-278, TC-FA-FAAC-279 |
| TC-FA-FAAC-E2E-016-aksesibilitas-keyboard-dan-fokus | Aksesibilitas Tab Asset Class: Navigasi Keyboard, Esc Menutup Modal, Fokus Terkunci di Modal Changelog, dan Tab Detail dengan Tombol Panah | FE+BE | 38 | TC-FA-FAAC-36, TC-FA-FAAC-37, TC-FA-FAAC-38, TC-FA-FAAC-39 |
| TC-FA-FAAC-E2E-017-aksesibilitas-label-dan-responsif-tablet | Aksesibilitas Label Toggle, Ikon Accounts, dan Tab Detail serta Tampilan Responsif Tabel dan Form pada Lebar Tablet | FE+BE | 33 | TC-FA-FAAC-40, TC-FA-FAAC-41, TC-FA-FAAC-42, TC-FA-FAAC-44, TC-FA-FAAC-45 |
| TC-FA-FAAC-E2E-018-alert-dependensi-akun-tidak-memblokir-link-dan-hilang-otomatis | Alert Dependensi Akun: Tidak Memblokir Aksi, Link Go to Chart of Accounts, dan Hilang Otomatis Setelah Akun Active Tersedia | FE+BE | 26 | TC-FA-FAAC-29, TC-FA-FAAC-30, TC-FA-FAAC-27, TC-FA-FAAC-28 |
| TC-FA-FAAC-E2E-019-navigasi-sidebar-tab-asset-class-dan-breadcrumb-dari-detail | Navigasi Menu Accounting di Sidebar, Klik Tab Asset Class, dan Breadcrumb dari Detail | FE+BE | 14 | TC-FA-FAAC-3, TC-FA-FAAC-4, TC-FA-FAAC-587 |
| TC-FA-FAAC-E2E-020-role-matrix-visibilitas-tabel-total-control-read-only-manage-read | Role Matrix: Visibilitas Elemen Tabel Asset Class untuk Total Control, Read Only, dan Manage Accounting (Read) | FE+BE | 32 | TC-FA-FAAC-56, TC-FA-FAAC-57, TC-FA-FAAC-58 |
| TC-FA-FAAC-E2E-021-role-matrix-visibilitas-tabel-manage-create-update-delete | Role Matrix: Visibilitas Elemen Tabel Asset Class untuk Manage Accounting (Read, Create), (Read, Update), dan (Read, Delete) | FE+BE | 38 | TC-FA-FAAC-59, TC-FA-FAAC-60, TC-FA-FAAC-61 |
| TC-FA-FAAC-E2E-022-role-matrix-visibilitas-detail-edit-total-control-read-only-manage-read | Role Matrix: Visibilitas Elemen Detail Mode Edit untuk Total Control, Read Only, dan Manage Accounting (Read) | FE+BE | 44 | TC-FA-FAAC-62, TC-FA-FAAC-63, TC-FA-FAAC-64 |
| TC-FA-FAAC-E2E-023-role-matrix-visibilitas-detail-edit-manage-create-update-delete | Role Matrix: Visibilitas Elemen Detail Mode Edit untuk Manage Accounting (Read, Create), (Read, Update), dan (Read, Delete) | FE+BE | 44 | TC-FA-FAAC-65, TC-FA-FAAC-66, TC-FA-FAAC-67 |
| TC-FA-FAAC-E2E-024-role-matrix-detail-create-manage-gabungan-dan-default-user | Role Matrix: Visibilitas Detail Mode Create, Akses Default User, dan Gabungan Elemen Manage Accounting (Read, Create, Update) | FE+BE | 33 | TC-FA-FAAC-68, TC-FA-FAAC-71, TC-FA-FAAC-672 |
| TC-FA-FAAC-E2E-025-role-matrix-menu-accounting-akses-langsung-dan-alert-per-role | Role Matrix: Menu Accounting, Akses Langsung ke Tab Asset Class, dan Alert Dependensi Akun per Role | FE+BE | 38 | TC-FA-FAAC-69, TC-FA-FAAC-70, TC-FA-FAAC-589, TC-FA-FAAC-682, TC-FA-FAAC-683 |
| TC-FA-FAAC-E2E-026-role-matrix-negatif-read-only | Role Matrix Negatif: Read Only (Tooltip Toggle Active dan Kontrol Tab Asset Names Tidak Tersedia) | FE+BE | 16 | TC-FA-FAAC-43, TC-FA-FAAC-633, TC-FA-FAAC-612 |
| TC-FA-FAAC-E2E-027-role-matrix-negatif-delete-only-create-only-dan-read-manage-tab-asset-names | Role Matrix Negatif: Deactivate Instead dan Tab Asset Names Tanpa Kontrol Tulis untuk Delete-Only, Create-Only, dan Read-Only (Manage Accounting, Huruf Read Saja) | FE+BE | 28 | TC-FA-FAAC-227, TC-FA-FAAC-615, TC-FA-FAAC-614, TC-FA-FAAC-616 |
| TC-FA-FAAC-E2E-028-role-matrix-positif-update-only-assign-move-unassign-dan-manage-delete | Role Matrix Positif: Update-Only Melihat Kontrol Assign, Move, Unassign dan Menjalankan Assign, serta Manage Accounting (Read, Delete) Menjalankan Delete | FE+BE | 27 | TC-FA-FAAC-613, TC-FA-FAAC-617, TC-FA-FAAC-86 |
| TC-FA-FAAC-E2E-029-role-matrix-positif-baca-read-only-dan-manage-read | Role Matrix Positif: Read Only dan Manage Accounting (Read) Dapat Mencari, Memfilter, Mengunduh, Membuka Changelog, dan Membuka Detail | FE+BE | 24 | TC-FA-FAAC-73, TC-FA-FAAC-74 |
| TC-FA-FAAC-E2E-030-role-matrix-positif-manage-create-create-dan-duplicate | Role Matrix Positif: Manage Accounting (Read, Create) Create dan Duplicate Asset Class Berhasil | FE+BE | 14 | TC-FA-FAAC-75, TC-FA-FAAC-76 |
| TC-FA-FAAC-E2E-031-role-matrix-positif-manage-create-use-recommended | Role Matrix Positif: Manage Accounting (Read, Create) Menjalankan Use Recommended Classes | FE+BE | 5 | TC-FA-FAAC-77 |
| TC-FA-FAAC-E2E-032-role-matrix-positif-manage-update-save-dan-status | Role Matrix Positif: Manage Accounting (Read, Update) Save Edit, Activate, Deactivate, dan Bulk Deactivate Berhasil | FE+BE | 28 | TC-FA-FAAC-78, TC-FA-FAAC-79, TC-FA-FAAC-80, TC-FA-FAAC-81 |
| TC-FA-FAAC-E2E-033-role-matrix-positif-manage-update-asset-name-dan-versi | Role Matrix Positif: Manage Accounting (Read, Update) Assign, Move, Unassign Asset Name dan Cancel Scheduled Version Berhasil | FE+BE | 33 | TC-FA-FAAC-82, TC-FA-FAAC-83, TC-FA-FAAC-84, TC-FA-FAAC-85 |
| TC-FA-FAAC-E2E-034-role-matrix-negatif-create-update-delete-only-permintaan-langsung-ke-server | Role Matrix Negatif: Create-Only, Update-Only, dan Delete-Only Tidak Dapat Menjalankan Aksi di Luar Hak (UI dan Permintaan Langsung ke Server) | FE+BE | 46 | TC-FA-FAAC-598, TC-FA-FAAC-599, TC-FA-FAAC-600 |
| TC-FA-FAAC-E2E-035-role-matrix-negatif-read-only-permintaan-langsung-ke-server | Role Matrix Negatif: Read Only Tidak Dapat Create, Edit, Deactivate, atau Delete (UI dan Permintaan Langsung ke Server) | FE+BE | 28 | TC-FA-FAAC-595, TC-FA-FAAC-596, TC-FA-FAAC-597 |
| TC-FA-FAAC-E2E-036-create-validasi-class-code | Create Asset Class: Validasi Class Code (Kosong, Batas Panjang, Karakter, Duplikat) | FE+BE | 31 | TC-FA-FAAC-97, TC-FA-FAAC-98, TC-FA-FAAC-99, TC-FA-FAAC-100 |
| TC-FA-FAAC-E2E-037-create-validasi-class-name-dan-description | Create Asset Class: Validasi Class Name dan Description (Kosong, Batas Panjang, Emoji) | FE+BE | 22 | TC-FA-FAAC-101, TC-FA-FAAC-102, TC-FA-FAAC-103, TC-FA-FAAC-104 |
| TC-FA-FAAC-E2E-038-create-validasi-method-useful-life-declining-rate | Create Asset Class: Validasi Method, Useful Life, dan Declining Rate | FE+BE | 34 | TC-FA-FAAC-105, TC-FA-FAAC-106, TC-FA-FAAC-107, TC-FA-FAAC-108, TC-FA-FAAC-109 |
| TC-FA-FAAC-E2E-039-create-validasi-units-dan-residual-value | Create Asset Class: Validasi Total Estimated Units, Unit Type, dan Residual Value | FE+BE | 26 | TC-FA-FAAC-110, TC-FA-FAAC-111, TC-FA-FAAC-112, TC-FA-FAAC-113 |
| TC-FA-FAAC-E2E-040-create-validasi-tax-method-threshold-dan-akun-ganda | Create Asset Class: Validasi Tax Depreciation Class, Tax Method, Capitalization Threshold, dan Akun Ganda | FE+BE | 27 | TC-FA-FAAC-114, TC-FA-FAAC-115, TC-FA-FAAC-116, TC-FA-FAAC-117 |
| TC-FA-FAAC-E2E-041-create-validasi-input-digit-desimal | Create Asset Class: Input Digit Desimal Ke-3 dan Pemisah Desimal Tidak Dapat Diketik | FE+BE | 27 | TC-FA-FAAC-689, TC-FA-FAAC-690, TC-FA-FAAC-691 |
| TC-FA-FAAC-E2E-042-create-validasi-tempel-teks-berpemisah-desimal | Create Asset Class: Tempel Teks Berpemisah Desimal ke Useful Life, Total Estimated Units, dan Declining Rate | FE+BE | 18 | TC-FA-FAAC-700, TC-FA-FAAC-714 |
| TC-FA-FAAC-E2E-043-create-validasi-state-berubah-setelah-form-dibuka | Create Asset Class: Submit Ditolak Saat Tax Depreciation Class, Tax Method, atau Akun Berubah Setelah Form Dibuka | FE+BE | 34 | TC-FA-FAAC-118, TC-FA-FAAC-119, TC-FA-FAAC-120 |
| TC-FA-FAAC-E2E-044-create-field-dinamis-method | Create Asset Class: Field Dinamis Depreciation Menurut Method | FE+BE | 22 | TC-FA-FAAC-121, TC-FA-FAAC-645, TC-FA-FAAC-122, TC-FA-FAAC-123, TC-FA-FAAC-124 |
| TC-FA-FAAC-E2E-045-create-tax-depreciation-class-dan-tax-method | Create Asset Class: Tax Method Mengikuti Tax Depreciation Class dan Useful Life & Rate Fiskal Read-Only | FE+BE | 23 | TC-FA-FAAC-126, TC-FA-FAAC-127 |
| TC-FA-FAAC-E2E-046-create-opsi-tax-depreciation-class-disabled-dan-inactive | Create Asset Class: Opsi Tax Depreciation Class Inactive Tidak Ditawarkan dan Select Disabled Bila Tidak Ada Class Active | FE+BE | 20 | TC-FA-FAAC-130, TC-FA-FAAC-129 |
| TC-FA-FAAC-E2E-047-create-nilai-field-tersembunyi-tidak-tersimpan-setelah-ganti-method | Create Asset Class: Nilai Field yang Disembunyikan Karena Ganti Method Tidak Ikut Tersimpan | FE+BE | 13 | TC-FA-FAAC-125 |
| TC-FA-FAAC-E2E-048-create-tax-depreciation-class-tanpa-metode | Create Asset Class: Tax Depreciation Class Tanpa Metode Membuat Tax Method Read-Only | FE+BE | 9 | TC-FA-FAAC-128 |
| TC-FA-FAAC-E2E-049-create-berhasil-straight-line-lengkap-highlight-dan-class-name-sama | Create Asset Class Berhasil: Method Straight Line Lengkap dengan Akun, Highlight Baris Baru, dan Class Name yang Sama | FE+BE | 32 | TC-FA-FAAC-14, TC-FA-FAAC-87, TC-FA-FAAC-95 |
| TC-FA-FAAC-E2E-050-create-berhasil-variasi-method-straight-line-declining-balance-dan-units-of-production | Create Asset Class Berhasil: Variasi Method Straight Line, Declining Balance, dan Units of Production | FE+BE | 29 | TC-FA-FAAC-88, TC-FA-FAAC-89, TC-FA-FAAC-90 |
| TC-FA-FAAC-E2E-051-create-berhasil-not-depreciated-akun-kosong-dan-start-rule | Create Asset Class Berhasil: Method Not Depreciated, Tab Accounts Kosong, dan Start Convention serta Start Rule Bukan Nilai Awal | FE+BE | 36 | TC-FA-FAAC-91, TC-FA-FAAC-92, TC-FA-FAAC-148 |
| TC-FA-FAAC-E2E-052-create-akun-sama-shortcut-create-account-dan-titik-peringatan-tab | Form Create Asset Class: Titik Peringatan Tab, Shortcut Create Account, dan Akun yang Sama dengan Asset Class Lain | FE+BE | 34 | TC-FA-FAAC-93, TC-FA-FAAC-94, TC-FA-FAAC-131, TC-FA-FAAC-133 |
| TC-FA-FAAC-E2E-053-unsaved-changes-form-create-breadcrumb-dan-menu-sidebar | Unsaved Changes pada Form Create: Meninggalkan Form Lewat Breadcrumb dan Menu Sidebar | FE+BE | 25 | TC-FA-FAAC-132, TC-FA-FAAC-661 |
| TC-FA-FAAC-E2E-054-unsaved-changes-form-edit-breadcrumb-dan-nilai-kembali | Unsaved Changes pada Form Edit: Breadcrumb dengan Cancel dan Leave, serta Nilai yang Dikembalikan Identik | FE+BE | 34 | TC-FA-FAAC-659, TC-FA-FAAC-660, TC-FA-FAAC-663 |
| TC-FA-FAAC-E2E-055-unsaved-changes-form-edit-back-browser-dan-clear-field-edit | Form Edit Asset Class: Unsaved Changes dengan Tombol Back Browser dan Clear Field pada Mode Edit | FE+BE | 28 | TC-FA-FAAC-662, TC-FA-FAAC-697 |
| TC-FA-FAAC-E2E-056-clear-field-detail-mode-create | Clear Field pada Detail Mode Create: Seluruh Field Dikosongkan dan Select Start Kembali ke Nilai Awal | FE+BE | 38 | TC-FA-FAAC-647, TC-FA-FAAC-696 |
| TC-FA-FAAC-E2E-057-dialog-form-backdrop-tidak-menutup-assign-move-dan-apply-changes | Klik Backdrop pada Dialog Form Assign Asset Names, Move Asset Names, dan Apply Changes Tidak Menutup Dialog | FE+BE | 37 | TC-FA-FAAC-698 |
| TC-FA-FAAC-E2E-058-dialog-form-ikon-x-dan-esc-memunculkan-unsaved-changes | Ikon ✕ dan Esc pada Dialog Form Apply Changes dan Move Asset Names Memunculkan Dialog Unsaved Changes | FE+BE | 34 | TC-FA-FAAC-708, TC-FA-FAAC-709 |
| TC-FA-FAAC-E2E-059-batas-jumlah-asset-class-master-data-count-limit | Batas Jumlah Asset Class: Dialog Blok Asset Class Limit Reached pada Master Data Count Limit | FE+BE | 58 | TC-FA-FAAC-134, TC-FA-FAAC-135, TC-FA-FAAC-136, TC-FA-FAAC-137, TC-FA-FAAC-147, TC-FA-FAAC-267 |
| TC-FA-FAAC-E2E-060-batas-method-plan-single-depreciation | Batas Method pada Plan Single Depreciation: Dialog Blok Depreciation Method Limit Reached | FE+BE | 68 | TC-FA-FAAC-138, TC-FA-FAAC-139, TC-FA-FAAC-144, TC-FA-FAAC-145, TC-FA-FAAC-183, TC-FA-FAAC-186, TC-FA-FAAC-187 |
| TC-FA-FAAC-E2E-061-batas-method-plan-multi-depreciation | Batas Method pada Plan Multi Depreciation: Max Depreciation Methods, Boundary, dan Perhitungan Method Lama | FE+BE | 51 | TC-FA-FAAC-140, TC-FA-FAAC-141, TC-FA-FAAC-142, TC-FA-FAAC-146, TC-FA-FAAC-184, TC-FA-FAAC-185 |
| TC-FA-FAAC-E2E-062-create-residual-value-unit-amount-dan-klik-ganda-submit | Create Asset Class: Residual Value Unit Amount dan Klik Ganda Submit Hanya Memproses Satu Permintaan | FE+BE | 24 | TC-FA-FAAC-96, TC-FA-FAAC-606 |
| TC-FA-FAAC-E2E-063-unsaved-changes-muat-ulang-halaman-konfirmasi-bawaan-browser | Unsaved Changes: Konfirmasi Bawaan Browser saat Muat Ulang Halaman pada Form Create dan Edit | FE+BE | 35 | TC-FA-FAAC-664, TC-FA-FAAC-665, TC-FA-FAAC-666 |
| TC-FA-FAAC-E2E-064-edit-class-name-description-dan-class-code | Edit Class Name, Description, dan Class Code Asset Class lalu Save | FE+BE | 28 | TC-FA-FAAC-171, TC-FA-FAAC-172, TC-FA-FAAC-174, TC-FA-FAAC-175 |
| TC-FA-FAAC-E2E-065-edit-depreciation-akun-dan-status-inactive | Edit Depreciation, Accounts, dan Asset Class Inactive pada Asset Class yang Belum Dipakai Aset | FE+BE | 25 | TC-FA-FAAC-176, TC-FA-FAAC-177, TC-FA-FAAC-178 |
| TC-FA-FAAC-E2E-066-assign-screening-picker-dan-validasi | Screening Dialog Assign Asset Names, Filter Picker, Search Kosong, dan Validasi Tanpa Pilihan | FE+BE | 35 | TC-FA-FAAC-149, TC-FA-FAAC-150, TC-FA-FAAC-155, TC-FA-FAAC-168, TC-FA-FAAC-169 |
| TC-FA-FAAC-E2E-067-assign-batal-tutup-dan-asset-class-inactive | Batal dan Tutup Dialog Assign Asset Names serta Assign pada Asset Class Inactive | FE+BE | 27 | TC-FA-FAAC-153, TC-FA-FAAC-154, TC-FA-FAAC-160, TC-FA-FAAC-712 |
| TC-FA-FAAC-E2E-068-assign-berhasil-satu-banyak-dan-asset-name-baru | Assign Asset Name Tanpa Asset Class Berhasil: Satu, Banyak, dan Asset Name Baru Tidak Ikut Ter-assign | FE+BE | 30 | TC-FA-FAAC-151, TC-FA-FAAC-152, TC-FA-FAAC-636 |
| TC-FA-FAAC-E2E-069-assign-klik-ganda-dan-spinner | Tombol Assign: Spinner Saat Permintaan Berjalan dan Klik Ganda Hanya Memproses Satu Permintaan | FE+BE | 20 | TC-FA-FAAC-625, TC-FA-FAAC-627 |
| TC-FA-FAAC-E2E-070-assign-sebagai-move-dan-pratinjau-dampak | Assign Asset Name yang Sudah di Asset Class Lain Diperlakukan sebagai Move dengan Effective From dan Pratinjau Dampak | FE+BE | 39 | TC-FA-FAAC-156, TC-FA-FAAC-157, TC-FA-FAAC-158 |
| TC-FA-FAAC-E2E-071-assign-campuran-effective-from-dan-pratinjau | Effective From dan Pratinjau Dampak Hanya Muncul bila Pilihan Memuat Move dengan Aset Aktif | FE+BE | 21 | TC-FA-FAAC-159, TC-FA-FAAC-688 |
| TC-FA-FAAC-E2E-072-assign-ditolak-state-berubah-setelah-dialog-dibuka | Assign Ditolak atau Dilewati saat State Berubah Setelah Dialog Dibuka | FE+BE | 42 | TC-FA-FAAC-161, TC-FA-FAAC-162, TC-FA-FAAC-163, TC-FA-FAAC-164 |
| TC-FA-FAAC-E2E-073-move-screening-dan-validasi-destination | Screening Dialog Move Asset Names dan Validasi Destination Asset Class | FE+BE | 26 | TC-FA-FAAC-188, TC-FA-FAAC-189, TC-FA-FAAC-196, TC-FA-FAAC-197 |
| TC-FA-FAAC-E2E-074-move-validasi-effective-from-dan-batal | Move: Validasi Pemilih Bulan Effective From serta Batal dan Tutup Dialog Move | FE+BE | 28 | TC-FA-FAAC-194, TC-FA-FAAC-195, TC-FA-FAAC-198, TC-FA-FAAC-199 |
| TC-FA-FAAC-E2E-075-move-batas-bawah-effective-from-last-posted-period | Move: Batas Bawah Effective From Akibat Last Posted Period | FE+BE | 19 | TC-FA-FAAC-201, TC-FA-FAAC-202 |
| TC-FA-FAAC-E2E-076-move-batas-bawah-lanjutan-dan-versi-scheduled-tujuan | Move: Batas Bawah Effective From Lanjutan dan Versi Scheduled Asset Class Tujuan | FE+BE | 35 | TC-FA-FAAC-203, TC-FA-FAAC-204, TC-FA-FAAC-205 |
| TC-FA-FAAC-E2E-077-move-berhasil-single-dan-massal | Move Asset Name Berhasil: Satu Asset Name dan Massal dengan Effective From Bulan Berjalan | FE+BE | 35 | TC-FA-FAAC-190, TC-FA-FAAC-191, TC-FA-FAAC-192 |
| TC-FA-FAAC-E2E-078-move-massal-tanpa-aset-aktif-bulan-lampau-klik-ganda-dan-spinner | Move Massal Tanpa Aset Aktif, Effective From Bulan Lampau, Klik Ganda, dan Spinner | FE+BE | 49 | TC-FA-FAAC-193, TC-FA-FAAC-206, TC-FA-FAAC-626, TC-FA-FAAC-628 |
| TC-FA-FAAC-E2E-079-move-ditolak-state-berubah-setelah-dialog-dibuka | Move Ditolak atau Dilewati saat State Berubah Setelah Dialog Dibuka | FE+BE | 32 | TC-FA-FAAC-208, TC-FA-FAAC-209, TC-FA-FAAC-210 |
| TC-FA-FAAC-E2E-080-duplicate-asset-class | Duplicate Asset Class: Pre-fill Mode Create dan Submit dengan Class Code Baru | FE+BE | 22 | TC-FA-FAAC-263, TC-FA-FAAC-264 |
| TC-FA-FAAC-E2E-081-mode-create-draft-asset-name-screening-dan-pemilihan-draft | Mode Create: Screening Tab Asset Names, Dialog Assign, dan Pemilihan Draft Asset Name | FE+BE | 20 | TC-FA-FAAC-254, TC-FA-FAAC-255, TC-FA-FAAC-256, TC-FA-FAAC-657 |
| TC-FA-FAAC-E2E-082-mode-create-draft-asset-name-hapus-satu-dan-clear-field | Mode Create: Hapus Satu Draft Asset Name dan Clear Field Membuang Seluruh Draft | FE+BE | 16 | TC-FA-FAAC-257, TC-FA-FAAC-258 |
| TC-FA-FAAC-E2E-083-mode-create-draft-asset-name-unsaved-changes-cancel-dan-leave | Mode Create: Draft Asset Name sebagai Perubahan Belum Disimpan pada Dialog Unsaved Changes | FE+BE | 17 | TC-FA-FAAC-260, TC-FA-FAAC-261 |
| TC-FA-FAAC-E2E-084-mode-create-draft-asset-name-submit | Mode Create: Submit Asset Class Baru dengan Draft Asset Name | FE+BE | 39 | TC-FA-FAAC-259, TC-FA-FAAC-654, TC-FA-FAAC-655 |
| TC-FA-FAAC-E2E-085-edit-kasus-tepi-kapitalisasi-class-code-dan-tax-depreciation-class | Edit Asset Class: Kapitalisasi Class Code dan Tax Depreciation Class yang Tidak Lagi Valid | FE+BE | 24 | TC-FA-FAAC-173, TC-FA-FAAC-179 |
| TC-FA-FAAC-E2E-086-duplicate-nilai-sumber-tidak-valid-dan-versi-scheduled | Duplicate Asset Class: Nilai Sumber Tidak Valid Dikosongkan dan Pre-fill dari Versi Terakhir | FE+BE | 22 | TC-FA-FAAC-265, TC-FA-FAAC-674 |
| TC-FA-FAAC-E2E-087-delete-guard-d05-d04-dan-deactivate-instead | Delete Guard D-05 dan D-04: Dialog Blok Asset Class yang Pernah Diposting dan Deactivate Instead | FE+BE | 22 | TC-FA-FAAC-216, TC-FA-FAAC-217, TC-FA-FAAC-218, TC-FA-FAAC-226 |
| TC-FA-FAAC-E2E-088-delete-guard-asset-name-dialog-dan-berhasil | Delete Guard D-06 Asset Name, Cancel Dialog Delete, dan Delete Berhasil | FE+BE | 33 | TC-FA-FAAC-214, TC-FA-FAAC-215, TC-FA-FAAC-219, TC-FA-FAAC-220, TC-FA-FAAC-221 |
| TC-FA-FAAC-E2E-089-delete-race-dan-halaman-terakhir | Delete: Cek Ulang Server Saat Kondisi Berubah dan Halaman Terakhir Setelah Delete | FE+BE | 26 | TC-FA-FAAC-223, TC-FA-FAAC-224, TC-FA-FAAC-703 |
| TC-FA-FAAC-E2E-090-unassign-menu-baris-dialog-dan-blokir | Unassign: Menu Baris Asset Name, Dialog Single, dan Blokir Asset Name dengan Aset Aktif | FE+BE | 30 | TC-FA-FAAC-228, TC-FA-FAAC-229, TC-FA-FAAC-230, TC-FA-FAAC-235 |
| TC-FA-FAAC-E2E-091-unassign-berhasil-dan-ditolak-state-berubah | Unassign: Berhasil Single dan Massal, serta Ditolak atau Dilewati Saat State Berubah | FE+BE | 30 | TC-FA-FAAC-231, TC-FA-FAAC-232, TC-FA-FAAC-236, TC-FA-FAAC-237 |
| TC-FA-FAAC-E2E-092-toggle-status-satu-asset-class-blokir-dan-batal | Toggle Status Satu Asset Class: Diblokir D-04, Batal, Cek Ulang Server, dan Activate Idempotent | FE+BE | 50 | TC-FA-FAAC-72, TC-FA-FAAC-295, TC-FA-FAAC-298, TC-FA-FAAC-299, TC-FA-FAAC-300, TC-FA-FAAC-301, TC-FA-FAAC-304 |
| TC-FA-FAAC-E2E-093-toggle-status-satu-asset-class-berhasil | Toggle Status Satu Asset Class: Activate dan Deactivate Berhasil | FE+BE | 31 | TC-FA-FAAC-294, TC-FA-FAAC-296, TC-FA-FAAC-297 |
| TC-FA-FAAC-E2E-094-bulk-status-blokir-batal-dan-collapse | Bulk Status: Diblokir, Batal, dan Dialog Single untuk Satu Asset Class | FE+BE | 72 | TC-FA-FAAC-246, TC-FA-FAAC-247, TC-FA-FAAC-248, TC-FA-FAAC-252, TC-FA-FAAC-667, TC-FA-FAAC-668 |
| TC-FA-FAAC-E2E-095-bulk-status-berhasil-dan-campuran | Bulk Status: Activate Berhasil, Deactivate Campuran Lolos dan Diblokir, serta Seleksi Campuran | FE+BE | 38 | TC-FA-FAAC-243, TC-FA-FAAC-244, TC-FA-FAAC-245, TC-FA-FAAC-249 |
| TC-FA-FAAC-E2E-096-aksi-form-dan-status-pada-asset-class-dihapus-pengguna-lain | Aksi Duplicate, Save Edit, Delete, Bulk, dan Toggle Status pada Asset Class yang Dihapus Pengguna Lain | FE+BE | 43 | TC-FA-FAAC-181, TC-FA-FAAC-225, TC-FA-FAAC-253, TC-FA-FAAC-268, TC-FA-FAAC-305, TC-FA-FAAC-306 |
| TC-FA-FAAC-E2E-097-aksi-asset-name-pada-asset-class-dihapus-pengguna-lain | Aksi Assign, Move, dan Unassign Asset Name pada Asset Class yang Dihapus Pengguna Lain | FE+BE | 47 | TC-FA-FAAC-170, TC-FA-FAAC-213, TC-FA-FAAC-240, TC-FA-FAAC-241 |
| TC-FA-FAAC-E2E-098-apply-changes-screening-berhasil-dan-batal | Apply Changes: Screening Dialog, Cancel, dan Apply dengan Effective From Bulan Berjalan | FE+BE | 29 | TC-FA-FAAC-307, TC-FA-FAAC-308, TC-FA-FAAC-310 |
| TC-FA-FAAC-E2E-099-apply-changes-effective-from-masa-depan-dan-pratinjau | Apply Changes: Pratinjau Assets Affected dan Effective From Masa Depan Menjadwalkan Versi | FE+BE | 24 | TC-FA-FAAC-309, TC-FA-FAAC-312 |
| TC-FA-FAAC-E2E-100-apply-changes-validasi-effective-from-dasar | Apply Changes: Validasi Effective From Kosong | FE+BE | 15 | TC-FA-FAAC-316 |
| TC-FA-FAAC-E2E-101-apply-changes-validasi-effective-from-versi-dan-last-posted | Apply Changes: Validasi Effective From terhadap Last Posted Period dan Versi Terakhir | FE+BE | 30 | TC-FA-FAAC-319, TC-FA-FAAC-320 |
| TC-FA-FAAC-E2E-102-apply-changes-alert-dampak-dan-capitalization-threshold | Apply Changes: Alert Dampak Not Depreciated dan Perubahan Capitalization Threshold Saja | FE+BE | 34 | TC-FA-FAAC-313, TC-FA-FAAC-314, TC-FA-FAAC-315 |
| TC-FA-FAAC-E2E-103-versi-scheduled-alert-dan-save-no-op | Versi Scheduled: Alert Next Version, Save No-Op, dan Validasi Effective From Perubahan Lanjutan | FE+BE | 46 | TC-FA-FAAC-321, TC-FA-FAAC-322, TC-FA-FAAC-323, TC-FA-FAAC-324, TC-FA-FAAC-325 |
| TC-FA-FAAC-E2E-104-versi-scheduled-cancel-dialog-d24 | Versi Scheduled: Dialog Cancel Scheduled Version (D-24), Konfirmasi, Back, dan Penolakan Server | FE+BE | 44 | TC-FA-FAAC-330, TC-FA-FAAC-331, TC-FA-FAAC-332, TC-FA-FAAC-333, TC-FA-FAAC-334 |
| TC-FA-FAAC-E2E-105-versi-scheduled-job-penerapan-otomatis | Versi Scheduled: Job Latar Menerapkan Versi Otomatis, Kegagalan Job, dan Pencatatan Log oleh System | FE+BE | 51 | TC-FA-FAAC-326, TC-FA-FAAC-328, TC-FA-FAAC-329, TC-FA-FAAC-533 |
| TC-FA-FAAC-E2E-106-class-code-terkunci-last-posted-period | Class Code Terkunci oleh Last Posted Period: Tooltip, Kunci Berubah Setelah Halaman Dibuka, dan Edit Class Name | FE+BE | 33 | TC-FA-FAAC-336, TC-FA-FAAC-337, TC-FA-FAAC-338, TC-FA-FAAC-339 |
| TC-FA-FAAC-E2E-107-last-posted-dan-last-exported-period | Last Posted Period dan Last Exported Period: Maju Saat Posting atau Export, Tidak Mundur | FE+BE | 29 | TC-FA-FAAC-340, TC-FA-FAAC-341, TC-FA-FAAC-342 |
| TC-FA-FAAC-E2E-108-reklasifikasi-d12-screening-dan-batal | Reklasifikasi D-12: Dialog Reclassify Balances, Cancel, Dua Akun, dan Perubahan Tanpa Dialog | FE+BE | 39 | TC-FA-FAAC-344, TC-FA-FAAC-347, TC-FA-FAAC-348, TC-FA-FAAC-349 |
| TC-FA-FAAC-E2E-109-reklasifikasi-d12-new-journals-dan-create-reclassification | Reklasifikasi D-12: Pilihan New Journals Only, Create Reclassification, dan Urutan D-11 Lalu D-12 | FE+BE | 39 | TC-FA-FAAC-345, TC-FA-FAAC-346, TC-FA-FAAC-350 |
| TC-FA-FAAC-E2E-110-unassign-massal-campuran-batal-dan-bulk-satu-item | Unassign Massal: Dialog Campuran dengan Batal, Lanjutkan Melewati Aset Aktif, dan Bulk Satu Item | FE+BE | 26 | TC-FA-FAAC-233, TC-FA-FAAC-234, TC-FA-FAAC-239 |
| TC-FA-FAAC-E2E-111-klik-ganda-apply-dan-create-recommended-hanya-satu-permintaan | Klik Ganda Apply dan Create (Recommended) Hanya Memproses Satu Permintaan | FE+BE | 26 | TC-FA-FAAC-607 |
| TC-FA-FAAC-E2E-112-search-class-code-class-name-commercial-fiscal-threshold | Search Tabel Asset Class: Class Code, Class Name, Commercial, Fiscal, Capitalization Threshold, Asset Names, dan Assets | FE+BE | 35 | TC-FA-FAAC-351, TC-FA-FAAC-352, TC-FA-FAAC-353, TC-FA-FAAC-354 |
| TC-FA-FAAC-E2E-113-search-accounts-modified-by-dan-teks-khusus | Search Tabel Asset Class: Accounts, Modified By, Nama Asset Name, dan Kolom yang Tidak Dicari | FE+BE | 31 | TC-FA-FAAC-355, TC-FA-FAAC-356, TC-FA-FAAC-357, TC-FA-FAAC-358, TC-FA-FAAC-359 |
| TC-FA-FAAC-E2E-114-search-siklus-search-box-trim-dan-nominal-berdesimal | Search Tabel Asset Class: Siklus Search Box, Pemangkasan Spasi, dan Nominal Berdesimal | FE+BE | 33 | TC-FA-FAAC-360, TC-FA-FAAC-361, TC-FA-FAAC-705 |
| TC-FA-FAAC-E2E-115-filter-panel-screening-dan-multi-select | Filter Tabel Asset Class: Screening Filter Panel, Opsi Dropdown, dan Filter Tunggal Multi-Select | FE+BE | 33 | TC-FA-FAAC-363, TC-FA-FAAC-364, TC-FA-FAAC-365 |
| TC-FA-FAAC-E2E-116-filter-range-min-max-dan-date | Filter Tabel Asset Class: Range Min dan Max Capitalization Threshold, Asset Names, Assets, dan Date Range Last Updated | FE+BE | 26 | TC-FA-FAAC-366, TC-FA-FAAC-367, TC-FA-FAAC-368 |
| TC-FA-FAAC-E2E-117-filter-logika-or-and-chip-dan-dropdown | Filter Tabel Asset Class: Logika OR dan AND, Search di Dropdown, dan Chip pada Field Multi-Select | FE+BE | 34 | TC-FA-FAAC-369, TC-FA-FAAC-370, TC-FA-FAAC-371, TC-FA-FAAC-372, TC-FA-FAAC-373 |
| TC-FA-FAAC-E2E-118-indikator-filter-aktif-dan-kombinasi-search-sort | Filter Tabel Asset Class: Indikator Filter Aktif, Pelepasan Filter, dan Kombinasi dengan Search dan Sort | FE+BE | 31 | TC-FA-FAAC-374, TC-FA-FAAC-375, TC-FA-FAAC-376, TC-FA-FAAC-377, TC-FA-FAAC-378 |
| TC-FA-FAAC-E2E-119-filter-lepas-draft-kolom-dan-kombinasi | Filter Tabel Asset Class: Draft Filter Panel, Hasil Kosong, Ganti Sort, dan Filter pada Kolom yang Disembunyikan | FE+BE | 36 | TC-FA-FAAC-379, TC-FA-FAAC-380, TC-FA-FAAC-381, TC-FA-FAAC-382 |
| TC-FA-FAAC-E2E-120-sort-3-state-kolom-teks-commercial-fiscal | Sort 3-State Tabel Asset Class: Class Code, Class Name, Modified By, Commercial, Fiscal, Asset Names, Assets, dan Capitalization Threshold | FE+BE | 10 | TC-FA-FAAC-385, TC-FA-FAAC-386, TC-FA-FAAC-387, TC-FA-FAAC-388, TC-FA-FAAC-389 |
| TC-FA-FAAC-E2E-121-sort-3-state-active-accounts-last-updated | Sort 3-State Tabel Asset Class: Active, Accounts, Last Updated, Satu Kolom Sort Aktif, dan Kolom Tanpa Ikon Sort | FE+BE | 20 | TC-FA-FAAC-390, TC-FA-FAAC-391, TC-FA-FAAC-392, TC-FA-FAAC-393, TC-FA-FAAC-394 |
| TC-FA-FAAC-E2E-122-setup-column-screening-dan-ceklis-kolom | Setup Column Tabel Asset Class: Screening Panel dan Modal, Ceklis Kolom Tampil Bawaan, dan Ceklis Kolom Tersembunyi Bawaan | FE+BE | 39 | TC-FA-FAAC-395, TC-FA-FAAC-396, TC-FA-FAAC-397, TC-FA-FAAC-398 |
| TC-FA-FAAC-E2E-123-setup-column-geser-dan-pin | Setup Column Tabel Asset Class: Geser Urutan Kolom, Pin dan Unpin Kolom, dan Tidak Memengaruhi Tabel Changelog | FE+BE | 35 | TC-FA-FAAC-399, TC-FA-FAAC-400, TC-FA-FAAC-401, TC-FA-FAAC-402, TC-FA-FAAC-407 |
| TC-FA-FAAC-E2E-124-setup-column-reset-tutup-satu-kolom-dan-persistensi | Setup Column Tabel Asset Class: Reset to Default, Tutup Modal dengan X, Satu Kolom Tersisa, dan Persistensi Konfigurasi | FE+BE | 36 | TC-FA-FAAC-403, TC-FA-FAAC-404, TC-FA-FAAC-405, TC-FA-FAAC-406 |
| TC-FA-FAAC-E2E-125-paginasi-tabel-asset-class | Paginasi Tabel Asset Class: Ukuran Halaman, Navigasi Halaman, Interaksi dengan Search, Filter, dan Sort, serta Input Nomor Halaman Tidak Valid | FE+BE | 37 | TC-FA-FAAC-383, TC-FA-FAAC-408, TC-FA-FAAC-409, TC-FA-FAAC-410, TC-FA-FAAC-411, TC-FA-FAAC-412, TC-FA-FAAC-702 |
| TC-FA-FAAC-E2E-126-state-tabel-kombinasi-dan-kembali-dari-detail | State Tabel Asset Class: Kombinasi Search, Filter, Sort, dan Ukuran Halaman, serta Dipertahankan Saat Kembali dari Detail | FE+BE | 27 | TC-FA-FAAC-384, TC-FA-FAAC-413, TC-FA-FAAC-414 |
| TC-FA-FAAC-E2E-127-state-tabel-pindah-tab-refresh-dan-reset-menu | State Tabel Asset Class: Dipertahankan Saat Pindah Tab Accounting dan Refresh, Direset Saat Menu Accounting Diklik Ulang | FE+BE | 26 | TC-FA-FAAC-415, TC-FA-FAAC-416, TC-FA-FAAC-417 |
| TC-FA-FAAC-E2E-128-download-tabel-nama-berkas-dan-cakupan-baris | Download Tabel Asset Class: Menu, Nama Berkas, Cakupan Baris dan Kolom, serta Tanpa Toast Sukses | FE+BE | 26 | TC-FA-FAAC-418, TC-FA-FAAC-419, TC-FA-FAAC-420, TC-FA-FAAC-421, TC-FA-FAAC-423, TC-FA-FAAC-424, TC-FA-FAAC-425, TC-FA-FAAC-430 |
| TC-FA-FAAC-E2E-129-download-isi-berkas-csv-xlsx | Download Tabel Asset Class: Isi Berkas CSV dan XLSX (Nilai Sel, BOM, Sheet, Urutan Baris, dan Kesamaan dengan Tabel, serta Cakupan Search dan Filter) | FE+BE | 42 | TC-FA-FAAC-422, TC-FA-FAAC-427, TC-FA-FAAC-428, TC-FA-FAAC-429, TC-FA-FAAC-432, TC-FA-FAAC-433, TC-FA-FAAC-434, TC-FA-FAAC-656 |
| TC-FA-FAAC-E2E-130-bulk-action-bar-dan-seleksi | Bulk Action Bar Tabel Asset Class: Tampil, Aksi Menurut Status Baris, Seleksi Halaman dan Lintas Halaman, serta Seleksi Dipertahankan | FE+BE | 45 | TC-FA-FAAC-435, TC-FA-FAAC-436, TC-FA-FAAC-437, TC-FA-FAAC-438, TC-FA-FAAC-439, TC-FA-FAAC-440 |
| TC-FA-FAAC-E2E-131-hover-identifier-dan-format-nominal | Tabel Asset Class: Format Nominal Berdesimal pada Capitalization Threshold dan Commercial, serta Hover Primary Identifier | FE+BE | 33 | TC-FA-FAAC-701, TC-FA-FAAC-704, TC-FA-FAAC-707, TC-FA-FAAC-716 |
| TC-FA-FAAC-E2E-132-search-kolom-tersembunyi-dan-ditampilkan-kembali | Search Tabel Asset Class: Kolom yang Disembunyikan Tidak Dicari dan Kembali Dicari Setelah Ditampilkan | FE+BE | 11 | TC-FA-FAAC-362 |
| TC-FA-FAAC-E2E-133-filter-capitalization-threshold-nominal-berdesimal | Filter Tabel Asset Class: Min dan Max pada Capitalization Threshold Membandingkan Nilai Tersimpan Termasuk Bagian Desimal | FE+BE | 15 | TC-FA-FAAC-706 |
| TC-FA-FAAC-E2E-134-tab-asset-names-search | Tab Asset Names: Search pada Kolom Asset Name, Category, Label, Assets, Assigned By, Assigned At, Debounce, dan Kolom Tersembunyi | FE+BE | 36 | TC-FA-FAAC-441, TC-FA-FAAC-442, TC-FA-FAAC-443, TC-FA-FAAC-444, TC-FA-FAAC-445, TC-FA-FAAC-446, TC-FA-FAAC-447, TC-FA-FAAC-448 |
| TC-FA-FAAC-E2E-135-tab-asset-names-filter | Tab Asset Names: Struktur Filter Panel serta Filter Category, Label, Assets Yes, dan Assets No | FE+BE | 31 | TC-FA-FAAC-449, TC-FA-FAAC-450, TC-FA-FAAC-451, TC-FA-FAAC-452, TC-FA-FAAC-453 |
| TC-FA-FAAC-E2E-136-tab-asset-names-filter-lanjutan-dan-kombinasi | Tab Asset Names: Filter Assigned At, Filter Assigned By, serta Kombinasi Search dan Filter | FE+BE | 25 | TC-FA-FAAC-454, TC-FA-FAAC-455, TC-FA-FAAC-456 |
| TC-FA-FAAC-E2E-137-tab-asset-names-sort-3-state | Tab Asset Names: Sort Tiga Tahap pada Kolom Asset Name, Category, dan Assets | FE+BE | 25 | TC-FA-FAAC-457, TC-FA-FAAC-458, TC-FA-FAAC-459 |
| TC-FA-FAAC-E2E-138-tab-asset-names-sort-lanjutan-dan-kolom-label | Tab Asset Names: Sort Tiga Tahap pada Kolom Assigned At dan Assigned By serta Kolom Label Tidak Dapat Diurutkan | FE+BE | 21 | TC-FA-FAAC-460, TC-FA-FAAC-461, TC-FA-FAAC-462 |
| TC-FA-FAAC-E2E-139-tab-asset-names-kolom-dan-persistensi | Tab Asset Names: Overlay Column Visibility, Kolom Terakhir Tidak Dapat Disembunyikan, dan Persistensi Setelah Muat Ulang | FE+BE | 21 | TC-FA-FAAC-463, TC-FA-FAAC-465, TC-FA-FAAC-466 |
| TC-FA-FAAC-E2E-140-tab-asset-names-paginasi-dan-state-tab | Tab Asset Names: Paginasi, Ukuran Halaman, Search pada Halaman 2, dan State Tabel antar Tab Detail | FE+BE | 32 | TC-FA-FAAC-467, TC-FA-FAAC-468, TC-FA-FAAC-469, TC-FA-FAAC-470, TC-FA-FAAC-471 |
| TC-FA-FAAC-E2E-141-picker-assign-search-dan-kolom | Picker Assign: Search pada Lima Kolom dan Menyembunyikan Kolom Label dan Current Class | FE+BE | 30 | TC-FA-FAAC-511, TC-FA-FAAC-512, TC-FA-FAAC-513, TC-FA-FAAC-514, TC-FA-FAAC-515, TC-FA-FAAC-525 |
| TC-FA-FAAC-E2E-142-picker-assign-filter-dan-sort-label | Picker Assign: Struktur Filter, Filter Category, Label, dan Rentang Assets, serta Kolom Label Tidak Dapat Diurutkan | FE+BE | 27 | TC-FA-FAAC-516, TC-FA-FAAC-517, TC-FA-FAAC-518, TC-FA-FAAC-519, TC-FA-FAAC-524 |
| TC-FA-FAAC-E2E-143-picker-assign-sort-kolom | Picker Assign: Sort pada Kolom Asset Name, Category, Current Class, dan Assets | FE+BE | 32 | TC-FA-FAAC-520, TC-FA-FAAC-521, TC-FA-FAAC-522, TC-FA-FAAC-523 |
| TC-FA-FAAC-E2E-144-badge-category-tab-asset-names-dan-truncate | Tab Asset Names: Badge Label dengan Chip +N more dan Badge Category dengan Pemotongan Nama Panjang | FE+BE | 21 | TC-FA-FAAC-684, TC-FA-FAAC-692, TC-FA-FAAC-693 |
| TC-FA-FAAC-E2E-145-badge-label-current-class-dan-teks-panjang | Picker Assign: Badge Label dengan Chip +N more dan Badge Current Class Terpotong, serta Teks Class Name dan Asset Name Sangat Panjang | FE+BE | 39 | TC-FA-FAAC-685, TC-FA-FAAC-694, TC-FA-FAAC-695 |
| TC-FA-FAAC-E2E-146-changelog-screening-empty-paginasi-dan-format-sel | Modal Changelog: Screening, Empty State, Hasil Search Kosong, Paginasi, dan Format Sel | FE+BE | 33 | TC-FA-FAAC-472, TC-FA-FAAC-473, TC-FA-FAAC-474, TC-FA-FAAC-475, TC-FA-FAAC-476 |
| TC-FA-FAAC-E2E-147-changelog-search-action-field-class-code-old-new-value | Modal Changelog: Search pada Kolom Action, Field, Class Code, Old Value, dan New Value | FE+BE | 33 | TC-FA-FAAC-477, TC-FA-FAAC-478, TC-FA-FAAC-479, TC-FA-FAAC-480 |
| TC-FA-FAAC-E2E-148-changelog-search-modified-by-date-siklus-dan-kolom-tersembunyi | Modal Changelog: Search pada Modified By, Kolom Date Tidak Dicari, Siklus Search Box, dan Kolom Field Tersembunyi | FE+BE | 44 | TC-FA-FAAC-481, TC-FA-FAAC-482, TC-FA-FAAC-483, TC-FA-FAAC-484 |
| TC-FA-FAAC-E2E-149-changelog-filter-struktur-opsi-dan-multi-select | Modal Changelog: Struktur Filter Panel, Isi Opsi Dropdown, Opsi Field 24 Nilai, dan Filter Tunggal Multi-Select | FE+BE | 44 | TC-FA-FAAC-485, TC-FA-FAAC-486, TC-FA-FAAC-487, TC-FA-FAAC-488 |
| TC-FA-FAAC-E2E-150-changelog-filter-range-kombinasi-dan-chip | Modal Changelog: Filter Date Range, Kombinasi AND, Logika OR, Search di Dropdown, dan Hapus Opsi lewat Chip | FE+BE | 45 | TC-FA-FAAC-489, TC-FA-FAAC-490, TC-FA-FAAC-491, TC-FA-FAAC-492, TC-FA-FAAC-493, TC-FA-FAAC-494 |
| TC-FA-FAAC-E2E-151-changelog-search-filter-kombinasi-dan-hasil-kosong | Modal Changelog: Kombinasi Search dan Filter, Hasil Kosong Pulih, dan Kombinasi Search, Filter, Sort, serta Ukuran Halaman | FE+BE | 37 | TC-FA-FAAC-495, TC-FA-FAAC-496, TC-FA-FAAC-497, TC-FA-FAAC-498 |
| TC-FA-FAAC-E2E-152-changelog-sort-3-state-dan-setup-column-screening | Modal Changelog: Sort Tiga Tahap Kolom Date dan Kolom Campuran, serta Screening Column Visibility dan Setup Column | FE+BE | 32 | TC-FA-FAAC-499, TC-FA-FAAC-501, TC-FA-FAAC-502, TC-FA-FAAC-503 |
| TC-FA-FAAC-E2E-153-changelog-setup-column-ceklis-geser-dan-pin | Modal Changelog: Setup Column Ceklis Kolom, Geser Urutan Kolom, dan Pin serta Unpin Kolom | FE+BE | 38 | TC-FA-FAAC-504, TC-FA-FAAC-505, TC-FA-FAAC-506 |
| TC-FA-FAAC-E2E-154-changelog-setup-column-reset-tutup-dan-persistensi | Modal Changelog: Setup Column Reset to Default, Tutup dengan X, Satu Kolom Tersisa, dan Tidak Memengaruhi Tabel Asset Class | FE+BE | 27 | TC-FA-FAAC-507, TC-FA-FAAC-508, TC-FA-FAAC-509, TC-FA-FAAC-510 |
| TC-FA-FAAC-E2E-155-changelog-download-csv-xlsx | Modal Changelog: Isi Berkas Download CSV dan XLSX serta Pengikutan Search, Filter, dan Kolom | FE+BE | 50 | TC-FA-FAAC-679, TC-FA-FAAC-680, TC-FA-FAAC-681, TC-FA-FAAC-718 |
| TC-FA-FAAC-E2E-156-tab-asset-names-sembunyikan-dan-tampilkan-tiap-kolom | Tab Asset Names: Menyembunyikan dan Menampilkan Tiap Kolom Satu per Satu | FE+BE | 29 | TC-FA-FAAC-464 |
| TC-FA-FAAC-E2E-157-changelog-sort-3-state-kolom-teks | Modal Changelog: Sort Tiga Tahap pada Kolom Teks Action, Class Code, Field, dan Modified By | FE+BE | 27 | TC-FA-FAAC-500 |
| TC-FA-FAAC-E2E-158-log-create-asset-class-tiga-surface-dan-use-recommended | Log Create Asset Class pada Changelog, System Log, dan Activity Log | FE+BE | 31 | TC-FA-FAAC-526, TC-FA-FAAC-527 |
| TC-FA-FAAC-E2E-159-log-edit-unit-description-dan-threshold | Log Edit: Unit Residual Value, Useful Life Berlaku Langsung, Description, dan Capitalization Threshold | FE+BE | 63 | TC-FA-FAAC-531, TC-FA-FAAC-532, TC-FA-FAAC-675, TC-FA-FAAC-676, TC-FA-FAAC-677, TC-FA-FAAC-678 |
| TC-FA-FAAC-E2E-160-log-edit-format-nominal-dan-total-estimated-units | Log Edit: Format Angka Nominal, Desimal, Persen, dan Total Estimated Units | FE+BE | 43 | TC-FA-FAAC-711, TC-FA-FAAC-713, TC-FA-FAAC-715, TC-FA-FAAC-717 |
| TC-FA-FAAC-E2E-161-log-status-delete-dan-penjadwalan-versi | Log Activate, Deactivate, Delete, dan Penjadwalan Versi Scheduled | FE+BE | 44 | TC-FA-FAAC-534, TC-FA-FAAC-535, TC-FA-FAAC-536 |
| TC-FA-FAAC-E2E-162-log-assign-unassign-asset-name-satu-per-satu | Log Assign dan Unassign Asset Name Satu per Satu pada Tiga Surface | FE+BE | 47 | TC-FA-FAAC-541, TC-FA-FAAC-542, TC-FA-FAAC-543 |
| TC-FA-FAAC-E2E-163-log-unassign-dan-move-system-activity-log | Log Unassign dan Move Asset Name pada System Log, Activity Log, dan Changelog | FE+BE | 42 | TC-FA-FAAC-544, TC-FA-FAAC-545, TC-FA-FAAC-546 |
| TC-FA-FAAC-E2E-164-log-assign-via-move-dan-assign-tiga-asset-name | Log Assign sebagai Move dan Assign Tiga Asset Name pada Changelog | FE+BE | 31 | TC-FA-FAAC-547, TC-FA-FAAC-548 |
| TC-FA-FAAC-E2E-165-log-move-massal-dan-unassign-massal-campuran | Log Move Massal dan Unassign Massal Campuran pada Changelog | FE+BE | 28 | TC-FA-FAAC-549, TC-FA-FAAC-550 |
| TC-FA-FAAC-E2E-166-log-absence-tidak-ada-entri | Log Absence: Tidak Ada Entri untuk Aksi yang Dilewati, Ditolak, atau Gagal | FE+BE | 92 | TC-FA-FAAC-538, TC-FA-FAAC-539, TC-FA-FAAC-540, TC-FA-FAAC-551, TC-FA-FAAC-578 |
| TC-FA-FAAC-E2E-167-log-request-api-langsung-tiga-surface | Log Request API Langsung Assign, Move, Unassign, Create, Edit, dan Delete pada Tiga Surface | FE+BE | 81 | TC-FA-FAAC-552, TC-FA-FAAC-553, TC-FA-FAAC-554, TC-FA-FAAC-608, TC-FA-FAAC-609, TC-FA-FAAC-610 |
| TC-FA-FAAC-E2E-168-sinkron-chart-of-accounts-alert-dan-used-by | Sinkronisasi Chart of Accounts: Alert Dependensi Akun, Used By, dan Kolom Accounts | FE+BE | 96 | TC-FA-FAAC-555, TC-FA-FAAC-556, TC-FA-FAAC-557, TC-FA-FAAC-558, TC-FA-FAAC-561, TC-FA-FAAC-567, TC-FA-FAAC-584 |
| TC-FA-FAAC-E2E-169-sinkron-tax-depreciation-class-dan-used-by | Sinkronisasi Tax Depreciation Class: Kolom Fiscal, Opsi Select, dan Modal Used By | FE+BE | 103 | TC-FA-FAAC-568, TC-FA-FAAC-569, TC-FA-FAAC-650, TC-FA-FAAC-651, TC-FA-FAAC-652 |
| TC-FA-FAAC-E2E-170-sinkron-tabel-pilihan-move-dan-used-by-a | Sinkronisasi Create, Rename, Delete Asset Class ke Tabel, Pilihan Move, dan Used By Akun | FE+BE | 142 | TC-FA-FAAC-559, TC-FA-FAAC-560, TC-FA-FAAC-565, TC-FA-FAAC-583, TC-FA-FAAC-588 |
| TC-FA-FAAC-E2E-171-sinkron-tabel-pilihan-move-dan-used-by-b | Sinkronisasi Versi, Status Active, dan Kunci Periode ke Assign, Pilihan Move, dan Log | FE+BE | 115 | TC-FA-FAAC-562, TC-FA-FAAC-563, TC-FA-FAAC-564, TC-FA-FAAC-566, TC-FA-FAAC-586 |
| TC-FA-FAAC-E2E-172-sinkron-asset-name-tabel-dan-banner-a | Sinkronisasi Assign, Move, dan Banner: Kolom Asset Names dan Assets, Badge Current Class, dan Hitungan Banner | FE+BE | 57 | TC-FA-FAAC-570, TC-FA-FAAC-571, TC-FA-FAAC-572, TC-FA-FAAC-573 |
| TC-FA-FAAC-E2E-173-sinkron-asset-name-tabel-dan-banner-b | Sinkronisasi Move, Unassign, dan Asset Name Baru: Kolom Asset Names dan Assets serta Banner | FE+BE | 64 | TC-FA-FAAC-574, TC-FA-FAAC-575, TC-FA-FAAC-576, TC-FA-FAAC-577 |
| TC-FA-FAAC-E2E-174-sinkron-asset-name-popup-dan-daftar | Sinkronisasi Asset Name: Banner, Popup Used By, Daftar Asset Name, Register Asset, dan Dampak Aset | FE+BE | 44 | TC-FA-FAAC-579, TC-FA-FAAC-580, TC-FA-FAAC-581, TC-FA-FAAC-582, TC-FA-FAAC-585 |
| TC-FA-FAAC-E2E-175-log-pembatalan-versi-scheduled-dan-last-posted-exported | Log Pembatalan Versi Scheduled dan Perubahan Last Posted dan Last Exported Period | FE+BE | 25 | TC-FA-FAAC-537, TC-FA-FAAC-538 |
| TC-FA-FAAC-E2E-176-log-edit-field-akun-dan-class-code-tiga-surface | Log Edit Asset Class: Satu Baris per Field, Format Akun, dan Class Code Baru | FE+BE | 48 | TC-FA-FAAC-528, TC-FA-FAAC-529, TC-FA-FAAC-530 |
| TC-FA-FAAC-E2E-177-state-tenant-write-lockdown-suspended-expired | State Tenant: Aksi Tulis Create, Edit, Toggle Active, dan Delete Ditolak saat Client Suspended atau Expired | FE+BE | 32 | TC-FA-FAAC-590, TC-FA-FAAC-591, TC-FA-FAAC-592, TC-FA-FAAC-593 |
| TC-FA-FAAC-E2E-178-state-tenant-baca-tetap-tersedia | State Tenant: Baca Tab Asset Class Tetap Tersedia saat Client Suspended atau Expired | FE+BE | 36 | TC-FA-FAAC-594, TC-FA-FAAC-629, TC-FA-FAAC-630, TC-FA-FAAC-631 |
| TC-FA-FAAC-E2E-179-state-tenant-aktivitas-sistem-tidak-diblokir | State Tenant: Job Sistem Penerapan Versi, Posting, dan Export Tidak Diblokir saat Client Suspended | FE+BE | 27 | TC-FA-FAAC-327, TC-FA-FAAC-343, TC-FA-FAAC-611 |
| TC-FA-FAAC-E2E-180-defense-in-depth-request-langsung-ditolak-guard-server | Defense-in-Depth: Request Langsung ke Server yang Melanggar Guard Bisnis dan Validasi Ditolak | FE+BE | 36 | TC-FA-FAAC-207, TC-FA-FAAC-242, TC-FA-FAAC-601, TC-FA-FAAC-602, TC-FA-FAAC-603, TC-FA-FAAC-604, TC-FA-FAAC-605, TC-FA-FAAC-621, TC-FA-FAAC-648, TC-FA-FAAC-649 |
| TC-FA-FAAC-E2E-181-defense-in-depth-request-langsung-tanpa-hak-update-403 | Defense-in-Depth: Request Langsung Assign, Move, Unassign, dan Cancel Scheduled Version Tanpa Hak Update Ditolak 403 | FE+BE | 17 | TC-FA-FAAC-618, TC-FA-FAAC-619, TC-FA-FAAC-620, TC-FA-FAAC-686 |
| TC-FA-FAAC-E2E-182-resilience-baca-dan-download | Resilience: Kegagalan Server saat Memuat Tabel, Alert Dependensi Akun, Banner, Dialog D-23, dan Download | FE+BE | 28 | TC-FA-FAAC-8, TC-FA-FAAC-32, TC-FA-FAAC-280, TC-FA-FAAC-281, TC-FA-FAAC-426 |
| TC-FA-FAAC-E2E-183-resilience-create-edit-duplicate | Resilience: Submit Create, Save Edit, dan Submit Duplicate Gagal karena Error Server 5xx Mempertahankan Form | FE+BE | 42 | TC-FA-FAAC-143, TC-FA-FAAC-180, TC-FA-FAAC-269 |
| TC-FA-FAAC-E2E-184-resilience-assign | Resilience: Assign Asset Name Gagal karena Error Server, Dialog Tetap Terbuka, dan Assign Diulang setelah Kegagalan Sebagian | FE+BE | 34 | TC-FA-FAAC-165, TC-FA-FAAC-166, TC-FA-FAAC-167 |
| TC-FA-FAAC-E2E-185-resilience-move-unassign-apply-changes-dan-cancel-scheduled | Resilience: Move, Unassign Massal, Apply Changes, dan Cancel Scheduled Version Gagal karena Error Server 5xx | FE+BE | 61 | TC-FA-FAAC-211, TC-FA-FAAC-212, TC-FA-FAAC-238, TC-FA-FAAC-311, TC-FA-FAAC-335 |
| TC-FA-FAAC-E2E-186-resilience-status-bulk-dan-delete | Resilience: Delete, Toggle Active, dan Bulk Activate atau Deactivate Gagal karena Error Server 5xx | FE+BE | 42 | TC-FA-FAAC-222, TC-FA-FAAC-250, TC-FA-FAAC-251, TC-FA-FAAC-302, TC-FA-FAAC-303 |
| TC-FA-FAAC-E2E-187-multi-sesi-dua-admin-race | Multi-Sesi: Dua Admin Menyimpan Edit, Create Class Code Sama, dan Cancel Scheduled Version Hampir Bersamaan | FE+BE | 45 | TC-FA-FAAC-182, TC-FA-FAAC-669, TC-FA-FAAC-687 |
| TC-FA-FAAC-E2E-188-volume-selection-limit-dan-5000-baris | Volume Data: Selection Limit pada Seleksi Tabel dan Picker Assign serta Download Lebih dari 5.000 Baris | FE+BE | 32 | TC-FA-FAAC-431, TC-FA-FAAC-632, TC-FA-FAAC-658, TC-FA-FAAC-673 |
| TC-FA-FAAC-E2E-189-siklus-hidup-asset-name-dan-deactivate | Siklus Hidup Asset Name dan Deactivate: Diblokir saat Ada Asset Name, Diizinkan setelah Dipindah, Di-Unassign, atau Dihapus, serta Aktivasi Ulang | FE+BE | 36 | TC-FA-FAAC-638, TC-FA-FAAC-639, TC-FA-FAAC-640, TC-FA-FAAC-641, TC-FA-FAAC-642 |
| TC-FA-FAAC-E2E-190-edge-destination-move-satu-class-per-asset-name-duplicate-dan-recommended | Kasus Tepi: Destination Move Hanya Asset Class Active, Satu Class per Asset Name, dan Duplicate Tidak Mengubah Data atau Menyalin Asset Name | FE+BE | 43 | TC-FA-FAAC-634, TC-FA-FAAC-635, TC-FA-FAAC-637, TC-FA-FAAC-643 |
| TC-FA-FAAC-E2E-191-resilience-submit-draft-asset-name-dan-use-recommended-classes | Resilience: Submit dengan Draft Asset Name dan Create Use Recommended Classes Gagal karena Error Server 5xx | FE+BE | 30 | TC-FA-FAAC-262, TC-FA-FAAC-292 |
| TC-FA-FAAC-E2E-192-state-tenant-write-lockdown-asset-name-suspended-expired | State Tenant: Assign, Unassign, dan Move Asset Name Ditolak saat Client Suspended atau Expired | FE+BE | 34 | TC-FA-FAAC-622, TC-FA-FAAC-623, TC-FA-FAAC-624 |
| TC-FA-FAAC-E2E-193-log-absence-request-langsung-read-only-ditolak-403 | Log Absence: Request Langsung Read Only Ditolak 403 Tidak Menulis Entri di Changelog Asset Class, System Log, dan Activity Log | FE+BE | 31 | TC-FA-FAAC-595, TC-FA-FAAC-596, TC-FA-FAAC-597, TC-FA-FAAC-618, TC-FA-FAAC-686 |
| TC-FA-FAAC-E2E-194-log-absence-request-langsung-create-update-delete-only-ditolak-403 | Log Absence: Request Langsung Create-Only, Update-Only, dan Delete-Only Ditolak 403 Tidak Menulis Entri di Changelog Asset Class, System Log, dan Activity Log | FE+BE | 34 | TC-FA-FAAC-598, TC-FA-FAAC-599, TC-FA-FAAC-600, TC-FA-FAAC-619, TC-FA-FAAC-620 |
| TC-FA-FAAC-E2E-195-log-absence-request-langsung-asset-name-ditolak-server | Log Absence: Request Langsung Move, Unassign, dan Assign Asset Name yang Ditolak Server Tidak Menulis Entri di Changelog Asset Class, System Log, dan Activity Log | FE+BE | 24 | TC-FA-FAAC-207, TC-FA-FAAC-605, TC-FA-FAAC-242, TC-FA-FAAC-621 |
| TC-FA-FAAC-E2E-196-log-absence-request-langsung-asset-class-ditolak-server | Log Absence: Request Langsung Deactivate, Delete, Edit Class Code, dan Create Melampaui Batas yang Ditolak Server Tidak Menulis Entri di Changelog Asset Class, System Log, dan Activity Log | FE+BE | 26 | TC-FA-FAAC-601, TC-FA-FAAC-602, TC-FA-FAAC-603, TC-FA-FAAC-604 |
| TC-FA-FAAC-E2E-197-tab-asset-names-caption-per-mode-dan-assign-tanpa-save | Tab Asset Names: Caption per Mode dan Assign pada Mode Edit Berlaku Tanpa Save | FE+BE | 21 | TC-FA-FAAC-737, TC-FA-FAAC-736, TC-FA-FAAC-739 |
| TC-FA-FAAC-E2E-198-role-matrix-caption-tab-asset-names-read-only | Role Matrix: Caption Tab Asset Names Tidak Tampil bagi Read Only | FE+BE | 6 | TC-FA-FAAC-738 |
| TC-FA-FAAC-E2E-199-create-tax-method-opsi-disabled-tooltip-dan-metode-hanya-scheduled-tidak-ditawarkan | Create Asset Class: Opsi Tax Method di Luar Irisan Disabled dengan Tooltip dan Metode yang Hanya Ada di Versi Scheduled Tidak Ditawarkan | FE+BE | 25 | TC-FA-FAAC-740, TC-FA-FAAC-741 |
| TC-FA-FAAC-E2E-200-create-tax-method-tooltip-versi-scheduled-paling-awal-dan-ganti-tax-depreciation-class | Create Asset Class: Tooltip Opsi Disabled Memakai Effective From Versi Scheduled Paling Awal dan Ganti Tax Depreciation Class Menghitung Ulang Tax Method | FE+BE | 29 | TC-FA-FAAC-742, TC-FA-FAAC-743 |
| TC-FA-FAAC-E2E-201-create-tax-method-irisan-kosong-semua-opsi-disabled-dan-submit-ditolak | Create Asset Class: Irisan Tax Method Kosong Membuat Semua Opsi Disabled dan Submit Ditolak | FE+BE | 24 | TC-FA-FAAC-746 |
| TC-FA-FAAC-E2E-202-use-recommended-classes-baris-tax-method-di-luar-irisan-disabled | Use Recommended Classes: Baris dengan Tax Method di Luar Irisan Disabled dengan Tooltip | FE+BE | 12 | TC-FA-FAAC-744 |
| TC-FA-FAAC-E2E-203-edit-versi-scheduled-tax-method-memakai-irisan-yang-sama | Edit Asset Class: Versi Scheduled Memakai Irisan Tax Method yang Sama | FE+BE | 18 | TC-FA-FAAC-745 |
| TC-FA-FAAC-E2E-204-defense-in-depth-request-langsung-tax-method-di-luar-irisan-ditolak-v-36 | Defense-in-Depth: Request Langsung dengan Tax Method di Luar Irisan Ditolak V-36 pada Create, Edit Versi Scheduled, dan Recommended Classes | FE+BE | 12 | TC-FA-FAAC-747 |
| TC-FA-FAAC-E2E-205-sinkron-cancel-scheduled-version-tax-depreciation-class-menghitung-ulang-opsi-tax-method | Sinkronisasi Tax Depreciation Class: Membatalkan dan Membuat Versi Scheduled Menghitung Ulang Opsi Tax Method pada Asset Class | FE+BE | 38 | TC-FA-FAAC-748 |
| TC-FA-FAAC-E2E-206-log-absence-request-langsung-tax-method-di-luar-irisan-ditolak-server | Log Absence: Request Langsung dengan Tax Method di Luar Irisan yang Ditolak Server Tidak Menulis Entri di Changelog Asset Class, System Log, dan Activity Log | FE+BE | 12 | TC-FA-FAAC-747 |
| TC-FA-FAAC-E2E-207-create-end-of-life-treatment-commercial-opsi-nilai-awal-dan-clear-field | Create Asset Class: End-of-Life Treatment Commercial Muncul pada Declining Balance dengan Tiga Opsi dan Nilai Awal, Hilang dan Pulih Lewat Clear Field | FE+BE | 21 | TC-FA-FAAC-719, TC-FA-FAAC-722 |
| TC-FA-FAAC-E2E-208-create-end-of-life-treatment-fiskal-read-only-dan-hidden-menurut-tax-method | Create Asset Class: End-of-Life Treatment Fiskal Tampil Read-Only pada Tax Method Declining Balance dan Hidden pada Kondisi Lain | FE+BE | 26 | TC-FA-FAAC-731, TC-FA-FAAC-732 |
| TC-FA-FAAC-E2E-209-create-declining-balance-menyimpan-end-of-life-treatment-dan-duplicate | Create Asset Class Declining Balance: End-of-Life Treatment Nilai Awal, Charge in Final Period, Keep Depreciating, dan Tersalin Lewat Duplicate | FE+BE | 51 | TC-FA-FAAC-720, TC-FA-FAAC-721, TC-FA-FAAC-727 |
| TC-FA-FAAC-E2E-210-edit-end-of-life-treatment-tanpa-apply-changes-ganti-method-dan-asset-class-belum-dipakai | Edit Asset Class Belum Dipakai Aset: Ganti Method Mengosongkan End-of-Life Treatment dan Edit End-of-Life Treatment Tersimpan Langsung Tanpa Apply Changes | FE+BE | 38 | TC-FA-FAAC-723, TC-FA-FAAC-725 |
| TC-FA-FAAC-E2E-211-edit-end-of-life-treatment-apply-changes-dan-versi-scheduled | Edit End-of-Life Treatment pada Asset Class yang Dipakai Aset: Apply Changes Membentuk Versi Berlaku dan Effective From Masa Depan Menjadwalkan Versi | FE+BE | 42 | TC-FA-FAAC-724, TC-FA-FAAC-726 |
| TC-FA-FAAC-E2E-212-helper-equivalent-declining-rate-pembulatan-dan-fallback | Create Asset Class: Helper Equivalent di Bawah Declining Rate, Kelipatan Tarif Garis Lurus, Pembulatan Half-Up, dan Kembali ke Helper Bawaan | FE+BE | 45 | TC-FA-FAAC-728, TC-FA-FAAC-729, TC-FA-FAAC-735, TC-FA-FAAC-730 |
| TC-FA-FAAC-E2E-213-log-edit-end-of-life-treatment-tiga-surface | Log Edit End-of-Life Treatment: Teks Opsi pada Old Value dan New Value di Changelog, System Log, dan Activity Log | FE+BE | 20 | TC-FA-FAAC-733 |
| TC-FA-FAAC-E2E-214-defense-in-depth-request-langsung-declining-balance-end-of-life-treatment-kosong-ditolak-v-39 | Defense-in-Depth: Request Langsung Create Declining Balance dengan End-of-Life Treatment Kosong Ditolak V-39 | FE+BE | 4 | TC-FA-FAAC-734 |
| TC-FA-FAAC-E2E-215-log-absence-request-langsung-declining-balance-end-of-life-treatment-kosong-ditolak-server | Log Absence: Request Langsung Create Declining Balance dengan End-of-Life Treatment Kosong yang Ditolak Server Tidak Menulis Entri di Changelog Asset Class, System Log, dan Activity Log | FE+BE | 6 | TC-FA-FAAC-734 |
| TC-FA-FAAC-E2E-216-guided-tooltip-replay-melewati-kolom-tersembunyi | Guided Tooltip Tab Asset Class: Replay Melewati Step yang Kolom Targetnya Disembunyikan | FE+BE | 24 | TC-FA-FAAC-754 |

## 2. Daftar TC hanya-BE (Excluded dari E2E — 0 TC)

Tidak ada. Modul tidak punya TC backend; seluruh TC granular masuk spec FE+BE.

## 3. Lapisan per TC (Traceability Matrix)

| TC ID | Lapisan | Spec E2E | Mode |
|---|---|---|:---:|
| TC-FA-FAAC-1 | E2E | TC-FA-FAAC-E2E-001-screening-halaman-accounting-tab-asset-class-dan-navigasi | FE+BE |
| TC-FA-FAAC-2 | E2E | TC-FA-FAAC-E2E-001-screening-halaman-accounting-tab-asset-class-dan-navigasi | FE+BE |
| TC-FA-FAAC-3 | E2E | TC-FA-FAAC-E2E-019-navigasi-sidebar-tab-asset-class-dan-breadcrumb-dari-detail | FE+BE |
| TC-FA-FAAC-4 | E2E | TC-FA-FAAC-E2E-019-navigasi-sidebar-tab-asset-class-dan-breadcrumb-dari-detail | FE+BE |
| TC-FA-FAAC-5 | E2E | TC-FA-FAAC-E2E-003-menu-accounting-per-plan-dan-akses-url-starter | FE+BE |
| TC-FA-FAAC-6 | E2E | TC-FA-FAAC-E2E-003-menu-accounting-per-plan-dan-akses-url-starter | FE+BE |
| TC-FA-FAAC-7 | E2E | TC-FA-FAAC-E2E-002-tampilan-tabel-urutan-link-asset-names-dan-format-ringkasan | FE+BE |
| TC-FA-FAAC-8 | E2E | TC-FA-FAAC-E2E-182-resilience-baca-dan-download | FE+BE |
| TC-FA-FAAC-9 | E2E | TC-FA-FAAC-E2E-004-empty-state-tabel-dan-use-recommended-classes-blokir | FE+BE |
| TC-FA-FAAC-10 | E2E | TC-FA-FAAC-E2E-002-tampilan-tabel-urutan-link-asset-names-dan-format-ringkasan | FE+BE |
| TC-FA-FAAC-11 | E2E | TC-FA-FAAC-E2E-002-tampilan-tabel-urutan-link-asset-names-dan-format-ringkasan | FE+BE |
| TC-FA-FAAC-12 | E2E | TC-FA-FAAC-E2E-002-tampilan-tabel-urutan-link-asset-names-dan-format-ringkasan | FE+BE |
| TC-FA-FAAC-13 | E2E | TC-FA-FAAC-E2E-002-tampilan-tabel-urutan-link-asset-names-dan-format-ringkasan | FE+BE |
| TC-FA-FAAC-14 | E2E | TC-FA-FAAC-E2E-049-create-berhasil-straight-line-lengkap-highlight-dan-class-name-sama | FE+BE |
| TC-FA-FAAC-15 | E2E | TC-FA-FAAC-E2E-010-screening-detail-mode-create-semua-tab | FE+BE |
| TC-FA-FAAC-16 | E2E | TC-FA-FAAC-E2E-010-screening-detail-mode-create-semua-tab | FE+BE |
| TC-FA-FAAC-17 | E2E | TC-FA-FAAC-E2E-010-screening-detail-mode-create-semua-tab | FE+BE |
| TC-FA-FAAC-18 | E2E | TC-FA-FAAC-E2E-011-screening-detail-mode-edit-dan-tab-asset-names | FE+BE |
| TC-FA-FAAC-19 | E2E | TC-FA-FAAC-E2E-011-screening-detail-mode-edit-dan-tab-asset-names | FE+BE |
| TC-FA-FAAC-20 | E2E | TC-FA-FAAC-E2E-010-screening-detail-mode-create-semua-tab | FE+BE |
| TC-FA-FAAC-21 | E2E | TC-FA-FAAC-E2E-011-screening-detail-mode-edit-dan-tab-asset-names | FE+BE |
| TC-FA-FAAC-22 | E2E | TC-FA-FAAC-E2E-011-screening-detail-mode-edit-dan-tab-asset-names | FE+BE |
| TC-FA-FAAC-23 | E2E | TC-FA-FAAC-E2E-011-screening-detail-mode-edit-dan-tab-asset-names | FE+BE |
| TC-FA-FAAC-24 | E2E | TC-FA-FAAC-E2E-012-alert-dependensi-akun-chart-of-accounts | FE+BE |
| TC-FA-FAAC-25 | E2E | TC-FA-FAAC-E2E-012-alert-dependensi-akun-chart-of-accounts | FE+BE |
| TC-FA-FAAC-26 | E2E | TC-FA-FAAC-E2E-012-alert-dependensi-akun-chart-of-accounts | FE+BE |
| TC-FA-FAAC-27 | E2E | TC-FA-FAAC-E2E-018-alert-dependensi-akun-tidak-memblokir-link-dan-hilang-otomatis | FE+BE |
| TC-FA-FAAC-28 | E2E | TC-FA-FAAC-E2E-018-alert-dependensi-akun-tidak-memblokir-link-dan-hilang-otomatis | FE+BE |
| TC-FA-FAAC-29 | E2E | TC-FA-FAAC-E2E-018-alert-dependensi-akun-tidak-memblokir-link-dan-hilang-otomatis | FE+BE |
| TC-FA-FAAC-30 | E2E | TC-FA-FAAC-E2E-018-alert-dependensi-akun-tidak-memblokir-link-dan-hilang-otomatis | FE+BE |
| TC-FA-FAAC-31 | E2E | TC-FA-FAAC-E2E-012-alert-dependensi-akun-chart-of-accounts | FE+BE |
| TC-FA-FAAC-32 | E2E | TC-FA-FAAC-E2E-182-resilience-baca-dan-download | FE+BE |
| TC-FA-FAAC-33 | E2E | TC-FA-FAAC-E2E-013-banner-asset-name-tanpa-asset-class-dan-dialog-d23 | FE+BE |
| TC-FA-FAAC-34 | E2E | TC-FA-FAAC-E2E-013-banner-asset-name-tanpa-asset-class-dan-dialog-d23 | FE+BE |
| TC-FA-FAAC-35 | E2E | TC-FA-FAAC-E2E-013-banner-asset-name-tanpa-asset-class-dan-dialog-d23 | FE+BE |
| TC-FA-FAAC-36 | E2E | TC-FA-FAAC-E2E-016-aksesibilitas-keyboard-dan-fokus | FE+BE |
| TC-FA-FAAC-37 | E2E | TC-FA-FAAC-E2E-016-aksesibilitas-keyboard-dan-fokus | FE+BE |
| TC-FA-FAAC-38 | E2E | TC-FA-FAAC-E2E-016-aksesibilitas-keyboard-dan-fokus | FE+BE |
| TC-FA-FAAC-39 | E2E | TC-FA-FAAC-E2E-016-aksesibilitas-keyboard-dan-fokus | FE+BE |
| TC-FA-FAAC-40 | E2E | TC-FA-FAAC-E2E-017-aksesibilitas-label-dan-responsif-tablet | FE+BE |
| TC-FA-FAAC-41 | E2E | TC-FA-FAAC-E2E-017-aksesibilitas-label-dan-responsif-tablet | FE+BE |
| TC-FA-FAAC-42 | E2E | TC-FA-FAAC-E2E-017-aksesibilitas-label-dan-responsif-tablet | FE+BE |
| TC-FA-FAAC-43 | E2E | TC-FA-FAAC-E2E-026-role-matrix-negatif-read-only | FE+BE |
| TC-FA-FAAC-44 | E2E | TC-FA-FAAC-E2E-017-aksesibilitas-label-dan-responsif-tablet | FE+BE |
| TC-FA-FAAC-45 | E2E | TC-FA-FAAC-E2E-017-aksesibilitas-label-dan-responsif-tablet | FE+BE |
| TC-FA-FAAC-46 | E2E | TC-FA-FAAC-E2E-007-guided-tooltip-otomatis-telusur-dan-selesai | FE+BE |
| TC-FA-FAAC-47 | E2E | TC-FA-FAAC-E2E-007-guided-tooltip-otomatis-telusur-dan-selesai | FE+BE |
| TC-FA-FAAC-48 | E2E | TC-FA-FAAC-E2E-007-guided-tooltip-otomatis-telusur-dan-selesai | FE+BE |
| TC-FA-FAAC-49 | E2E | TC-FA-FAAC-E2E-008-guided-tooltip-skip-back-esc-dan-pindah-tab | FE+BE |
| TC-FA-FAAC-50 | E2E | TC-FA-FAAC-E2E-008-guided-tooltip-skip-back-esc-dan-pindah-tab | FE+BE |
| TC-FA-FAAC-51 | E2E | TC-FA-FAAC-E2E-008-guided-tooltip-skip-back-esc-dan-pindah-tab | FE+BE |
| TC-FA-FAAC-52 | E2E | TC-FA-FAAC-E2E-009-guided-tooltip-replay-dan-navigasi-keyboard | FE+BE |
| TC-FA-FAAC-53 | E2E | TC-FA-FAAC-E2E-009-guided-tooltip-replay-dan-navigasi-keyboard | FE+BE |
| TC-FA-FAAC-54 | E2E | TC-FA-FAAC-E2E-008-guided-tooltip-skip-back-esc-dan-pindah-tab | FE+BE |
| TC-FA-FAAC-55 | E2E | TC-FA-FAAC-E2E-008-guided-tooltip-skip-back-esc-dan-pindah-tab | FE+BE |
| TC-FA-FAAC-56 | E2E | TC-FA-FAAC-E2E-020-role-matrix-visibilitas-tabel-total-control-read-only-manage-read | FE+BE |
| TC-FA-FAAC-57 | E2E | TC-FA-FAAC-E2E-020-role-matrix-visibilitas-tabel-total-control-read-only-manage-read | FE+BE |
| TC-FA-FAAC-58 | E2E | TC-FA-FAAC-E2E-020-role-matrix-visibilitas-tabel-total-control-read-only-manage-read | FE+BE |
| TC-FA-FAAC-59 | E2E | TC-FA-FAAC-E2E-021-role-matrix-visibilitas-tabel-manage-create-update-delete | FE+BE |
| TC-FA-FAAC-60 | E2E | TC-FA-FAAC-E2E-021-role-matrix-visibilitas-tabel-manage-create-update-delete | FE+BE |
| TC-FA-FAAC-61 | E2E | TC-FA-FAAC-E2E-021-role-matrix-visibilitas-tabel-manage-create-update-delete | FE+BE |
| TC-FA-FAAC-62 | E2E | TC-FA-FAAC-E2E-022-role-matrix-visibilitas-detail-edit-total-control-read-only-manage-read | FE+BE |
| TC-FA-FAAC-63 | E2E | TC-FA-FAAC-E2E-022-role-matrix-visibilitas-detail-edit-total-control-read-only-manage-read | FE+BE |
| TC-FA-FAAC-64 | E2E | TC-FA-FAAC-E2E-022-role-matrix-visibilitas-detail-edit-total-control-read-only-manage-read | FE+BE |
| TC-FA-FAAC-65 | E2E | TC-FA-FAAC-E2E-023-role-matrix-visibilitas-detail-edit-manage-create-update-delete | FE+BE |
| TC-FA-FAAC-66 | E2E | TC-FA-FAAC-E2E-023-role-matrix-visibilitas-detail-edit-manage-create-update-delete | FE+BE |
| TC-FA-FAAC-67 | E2E | TC-FA-FAAC-E2E-023-role-matrix-visibilitas-detail-edit-manage-create-update-delete | FE+BE |
| TC-FA-FAAC-68 | E2E | TC-FA-FAAC-E2E-024-role-matrix-detail-create-manage-gabungan-dan-default-user | FE+BE |
| TC-FA-FAAC-69 | E2E | TC-FA-FAAC-E2E-025-role-matrix-menu-accounting-akses-langsung-dan-alert-per-role | FE+BE |
| TC-FA-FAAC-70 | E2E | TC-FA-FAAC-E2E-025-role-matrix-menu-accounting-akses-langsung-dan-alert-per-role | FE+BE |
| TC-FA-FAAC-71 | E2E | TC-FA-FAAC-E2E-024-role-matrix-detail-create-manage-gabungan-dan-default-user | FE+BE |
| TC-FA-FAAC-72 | E2E | TC-FA-FAAC-E2E-092-toggle-status-satu-asset-class-blokir-dan-batal | FE+BE |
| TC-FA-FAAC-73 | E2E | TC-FA-FAAC-E2E-029-role-matrix-positif-baca-read-only-dan-manage-read | FE+BE |
| TC-FA-FAAC-74 | E2E | TC-FA-FAAC-E2E-029-role-matrix-positif-baca-read-only-dan-manage-read | FE+BE |
| TC-FA-FAAC-75 | E2E | TC-FA-FAAC-E2E-030-role-matrix-positif-manage-create-create-dan-duplicate | FE+BE |
| TC-FA-FAAC-76 | E2E | TC-FA-FAAC-E2E-030-role-matrix-positif-manage-create-create-dan-duplicate | FE+BE |
| TC-FA-FAAC-77 | E2E | TC-FA-FAAC-E2E-031-role-matrix-positif-manage-create-use-recommended | FE+BE |
| TC-FA-FAAC-78 | E2E | TC-FA-FAAC-E2E-032-role-matrix-positif-manage-update-save-dan-status | FE+BE |
| TC-FA-FAAC-79 | E2E | TC-FA-FAAC-E2E-032-role-matrix-positif-manage-update-save-dan-status | FE+BE |
| TC-FA-FAAC-80 | E2E | TC-FA-FAAC-E2E-032-role-matrix-positif-manage-update-save-dan-status | FE+BE |
| TC-FA-FAAC-81 | E2E | TC-FA-FAAC-E2E-032-role-matrix-positif-manage-update-save-dan-status | FE+BE |
| TC-FA-FAAC-82 | E2E | TC-FA-FAAC-E2E-033-role-matrix-positif-manage-update-asset-name-dan-versi | FE+BE |
| TC-FA-FAAC-83 | E2E | TC-FA-FAAC-E2E-033-role-matrix-positif-manage-update-asset-name-dan-versi | FE+BE |
| TC-FA-FAAC-84 | E2E | TC-FA-FAAC-E2E-033-role-matrix-positif-manage-update-asset-name-dan-versi | FE+BE |
| TC-FA-FAAC-85 | E2E | TC-FA-FAAC-E2E-033-role-matrix-positif-manage-update-asset-name-dan-versi | FE+BE |
| TC-FA-FAAC-86 | E2E | TC-FA-FAAC-E2E-028-role-matrix-positif-update-only-assign-move-unassign-dan-manage-delete | FE+BE |
| TC-FA-FAAC-87 | E2E | TC-FA-FAAC-E2E-049-create-berhasil-straight-line-lengkap-highlight-dan-class-name-sama | FE+BE |
| TC-FA-FAAC-88 | E2E | TC-FA-FAAC-E2E-050-create-berhasil-variasi-method-straight-line-declining-balance-dan-units-of-production | FE+BE |
| TC-FA-FAAC-89 | E2E | TC-FA-FAAC-E2E-050-create-berhasil-variasi-method-straight-line-declining-balance-dan-units-of-production | FE+BE |
| TC-FA-FAAC-90 | E2E | TC-FA-FAAC-E2E-050-create-berhasil-variasi-method-straight-line-declining-balance-dan-units-of-production | FE+BE |
| TC-FA-FAAC-91 | E2E | TC-FA-FAAC-E2E-051-create-berhasil-not-depreciated-akun-kosong-dan-start-rule | FE+BE |
| TC-FA-FAAC-92 | E2E | TC-FA-FAAC-E2E-051-create-berhasil-not-depreciated-akun-kosong-dan-start-rule | FE+BE |
| TC-FA-FAAC-93 | E2E | TC-FA-FAAC-E2E-052-create-akun-sama-shortcut-create-account-dan-titik-peringatan-tab | FE+BE |
| TC-FA-FAAC-94 | E2E | TC-FA-FAAC-E2E-052-create-akun-sama-shortcut-create-account-dan-titik-peringatan-tab | FE+BE |
| TC-FA-FAAC-95 | E2E | TC-FA-FAAC-E2E-049-create-berhasil-straight-line-lengkap-highlight-dan-class-name-sama | FE+BE |
| TC-FA-FAAC-96 | E2E | TC-FA-FAAC-E2E-062-create-residual-value-unit-amount-dan-klik-ganda-submit | FE+BE |
| TC-FA-FAAC-97 | E2E | TC-FA-FAAC-E2E-036-create-validasi-class-code | FE+BE |
| TC-FA-FAAC-98 | E2E | TC-FA-FAAC-E2E-036-create-validasi-class-code | FE+BE |
| TC-FA-FAAC-99 | E2E | TC-FA-FAAC-E2E-036-create-validasi-class-code | FE+BE |
| TC-FA-FAAC-100 | E2E | TC-FA-FAAC-E2E-036-create-validasi-class-code | FE+BE |
| TC-FA-FAAC-101 | E2E | TC-FA-FAAC-E2E-037-create-validasi-class-name-dan-description | FE+BE |
| TC-FA-FAAC-102 | E2E | TC-FA-FAAC-E2E-037-create-validasi-class-name-dan-description | FE+BE |
| TC-FA-FAAC-103 | E2E | TC-FA-FAAC-E2E-037-create-validasi-class-name-dan-description | FE+BE |
| TC-FA-FAAC-104 | E2E | TC-FA-FAAC-E2E-037-create-validasi-class-name-dan-description | FE+BE |
| TC-FA-FAAC-105 | E2E | TC-FA-FAAC-E2E-038-create-validasi-method-useful-life-declining-rate | FE+BE |
| TC-FA-FAAC-106 | E2E | TC-FA-FAAC-E2E-038-create-validasi-method-useful-life-declining-rate | FE+BE |
| TC-FA-FAAC-107 | E2E | TC-FA-FAAC-E2E-038-create-validasi-method-useful-life-declining-rate | FE+BE |
| TC-FA-FAAC-108 | E2E | TC-FA-FAAC-E2E-038-create-validasi-method-useful-life-declining-rate | FE+BE |
| TC-FA-FAAC-109 | E2E | TC-FA-FAAC-E2E-038-create-validasi-method-useful-life-declining-rate | FE+BE |
| TC-FA-FAAC-110 | E2E | TC-FA-FAAC-E2E-039-create-validasi-units-dan-residual-value | FE+BE |
| TC-FA-FAAC-111 | E2E | TC-FA-FAAC-E2E-039-create-validasi-units-dan-residual-value | FE+BE |
| TC-FA-FAAC-112 | E2E | TC-FA-FAAC-E2E-039-create-validasi-units-dan-residual-value | FE+BE |
| TC-FA-FAAC-113 | E2E | TC-FA-FAAC-E2E-039-create-validasi-units-dan-residual-value | FE+BE |
| TC-FA-FAAC-114 | E2E | TC-FA-FAAC-E2E-040-create-validasi-tax-method-threshold-dan-akun-ganda | FE+BE |
| TC-FA-FAAC-115 | E2E | TC-FA-FAAC-E2E-040-create-validasi-tax-method-threshold-dan-akun-ganda | FE+BE |
| TC-FA-FAAC-116 | E2E | TC-FA-FAAC-E2E-040-create-validasi-tax-method-threshold-dan-akun-ganda | FE+BE |
| TC-FA-FAAC-117 | E2E | TC-FA-FAAC-E2E-040-create-validasi-tax-method-threshold-dan-akun-ganda | FE+BE |
| TC-FA-FAAC-118 | E2E | TC-FA-FAAC-E2E-043-create-validasi-state-berubah-setelah-form-dibuka | FE+BE |
| TC-FA-FAAC-119 | E2E | TC-FA-FAAC-E2E-043-create-validasi-state-berubah-setelah-form-dibuka | FE+BE |
| TC-FA-FAAC-120 | E2E | TC-FA-FAAC-E2E-043-create-validasi-state-berubah-setelah-form-dibuka | FE+BE |
| TC-FA-FAAC-121 | E2E | TC-FA-FAAC-E2E-044-create-field-dinamis-method | FE+BE |
| TC-FA-FAAC-122 | E2E | TC-FA-FAAC-E2E-044-create-field-dinamis-method | FE+BE |
| TC-FA-FAAC-123 | E2E | TC-FA-FAAC-E2E-044-create-field-dinamis-method | FE+BE |
| TC-FA-FAAC-124 | E2E | TC-FA-FAAC-E2E-044-create-field-dinamis-method | FE+BE |
| TC-FA-FAAC-125 | E2E | TC-FA-FAAC-E2E-047-create-nilai-field-tersembunyi-tidak-tersimpan-setelah-ganti-method | FE+BE |
| TC-FA-FAAC-126 | E2E | TC-FA-FAAC-E2E-045-create-tax-depreciation-class-dan-tax-method | FE+BE |
| TC-FA-FAAC-127 | E2E | TC-FA-FAAC-E2E-045-create-tax-depreciation-class-dan-tax-method | FE+BE |
| TC-FA-FAAC-128 | E2E | TC-FA-FAAC-E2E-048-create-tax-depreciation-class-tanpa-metode | FE+BE |
| TC-FA-FAAC-129 | E2E | TC-FA-FAAC-E2E-046-create-opsi-tax-depreciation-class-disabled-dan-inactive | FE+BE |
| TC-FA-FAAC-130 | E2E | TC-FA-FAAC-E2E-046-create-opsi-tax-depreciation-class-disabled-dan-inactive | FE+BE |
| TC-FA-FAAC-131 | E2E | TC-FA-FAAC-E2E-052-create-akun-sama-shortcut-create-account-dan-titik-peringatan-tab | FE+BE |
| TC-FA-FAAC-132 | E2E | TC-FA-FAAC-E2E-053-unsaved-changes-form-create-breadcrumb-dan-menu-sidebar | FE+BE |
| TC-FA-FAAC-133 | E2E | TC-FA-FAAC-E2E-052-create-akun-sama-shortcut-create-account-dan-titik-peringatan-tab | FE+BE |
| TC-FA-FAAC-134 | E2E | TC-FA-FAAC-E2E-059-batas-jumlah-asset-class-master-data-count-limit | FE+BE |
| TC-FA-FAAC-135 | E2E | TC-FA-FAAC-E2E-059-batas-jumlah-asset-class-master-data-count-limit | FE+BE |
| TC-FA-FAAC-136 | E2E | TC-FA-FAAC-E2E-059-batas-jumlah-asset-class-master-data-count-limit | FE+BE |
| TC-FA-FAAC-137 | E2E | TC-FA-FAAC-E2E-059-batas-jumlah-asset-class-master-data-count-limit | FE+BE |
| TC-FA-FAAC-138 | E2E | TC-FA-FAAC-E2E-060-batas-method-plan-single-depreciation | FE+BE |
| TC-FA-FAAC-139 | E2E | TC-FA-FAAC-E2E-060-batas-method-plan-single-depreciation | FE+BE |
| TC-FA-FAAC-140 | E2E | TC-FA-FAAC-E2E-061-batas-method-plan-multi-depreciation | FE+BE |
| TC-FA-FAAC-141 | E2E | TC-FA-FAAC-E2E-061-batas-method-plan-multi-depreciation | FE+BE |
| TC-FA-FAAC-142 | E2E | TC-FA-FAAC-E2E-061-batas-method-plan-multi-depreciation | FE+BE |
| TC-FA-FAAC-143 | E2E | TC-FA-FAAC-E2E-183-resilience-create-edit-duplicate | FE+BE |
| TC-FA-FAAC-144 | E2E | TC-FA-FAAC-E2E-060-batas-method-plan-single-depreciation | FE+BE |
| TC-FA-FAAC-145 | E2E | TC-FA-FAAC-E2E-060-batas-method-plan-single-depreciation | FE+BE |
| TC-FA-FAAC-146 | E2E | TC-FA-FAAC-E2E-061-batas-method-plan-multi-depreciation | FE+BE |
| TC-FA-FAAC-147 | E2E | TC-FA-FAAC-E2E-059-batas-jumlah-asset-class-master-data-count-limit | FE+BE |
| TC-FA-FAAC-148 | E2E | TC-FA-FAAC-E2E-051-create-berhasil-not-depreciated-akun-kosong-dan-start-rule | FE+BE |
| TC-FA-FAAC-149 | E2E | TC-FA-FAAC-E2E-066-assign-screening-picker-dan-validasi | FE+BE |
| TC-FA-FAAC-150 | E2E | TC-FA-FAAC-E2E-066-assign-screening-picker-dan-validasi | FE+BE |
| TC-FA-FAAC-151 | E2E | TC-FA-FAAC-E2E-068-assign-berhasil-satu-banyak-dan-asset-name-baru | FE+BE |
| TC-FA-FAAC-152 | E2E | TC-FA-FAAC-E2E-068-assign-berhasil-satu-banyak-dan-asset-name-baru | FE+BE |
| TC-FA-FAAC-153 | E2E | TC-FA-FAAC-E2E-067-assign-batal-tutup-dan-asset-class-inactive | FE+BE |
| TC-FA-FAAC-154 | E2E | TC-FA-FAAC-E2E-067-assign-batal-tutup-dan-asset-class-inactive | FE+BE |
| TC-FA-FAAC-155 | E2E | TC-FA-FAAC-E2E-066-assign-screening-picker-dan-validasi | FE+BE |
| TC-FA-FAAC-156 | E2E | TC-FA-FAAC-E2E-070-assign-sebagai-move-dan-pratinjau-dampak | FE+BE |
| TC-FA-FAAC-157 | E2E | TC-FA-FAAC-E2E-070-assign-sebagai-move-dan-pratinjau-dampak | FE+BE |
| TC-FA-FAAC-158 | E2E | TC-FA-FAAC-E2E-070-assign-sebagai-move-dan-pratinjau-dampak | FE+BE |
| TC-FA-FAAC-159 | E2E | TC-FA-FAAC-E2E-071-assign-campuran-effective-from-dan-pratinjau | FE+BE |
| TC-FA-FAAC-160 | E2E | TC-FA-FAAC-E2E-067-assign-batal-tutup-dan-asset-class-inactive | FE+BE |
| TC-FA-FAAC-161 | E2E | TC-FA-FAAC-E2E-072-assign-ditolak-state-berubah-setelah-dialog-dibuka | FE+BE |
| TC-FA-FAAC-162 | E2E | TC-FA-FAAC-E2E-072-assign-ditolak-state-berubah-setelah-dialog-dibuka | FE+BE |
| TC-FA-FAAC-163 | E2E | TC-FA-FAAC-E2E-072-assign-ditolak-state-berubah-setelah-dialog-dibuka | FE+BE |
| TC-FA-FAAC-164 | E2E | TC-FA-FAAC-E2E-072-assign-ditolak-state-berubah-setelah-dialog-dibuka | FE+BE |
| TC-FA-FAAC-165 | E2E | TC-FA-FAAC-E2E-184-resilience-assign | FE+BE |
| TC-FA-FAAC-166 | E2E | TC-FA-FAAC-E2E-184-resilience-assign | FE+BE |
| TC-FA-FAAC-167 | E2E | TC-FA-FAAC-E2E-184-resilience-assign | FE+BE |
| TC-FA-FAAC-168 | E2E | TC-FA-FAAC-E2E-066-assign-screening-picker-dan-validasi | FE+BE |
| TC-FA-FAAC-169 | E2E | TC-FA-FAAC-E2E-066-assign-screening-picker-dan-validasi | FE+BE |
| TC-FA-FAAC-170 | E2E | TC-FA-FAAC-E2E-097-aksi-asset-name-pada-asset-class-dihapus-pengguna-lain | FE+BE |
| TC-FA-FAAC-171 | E2E | TC-FA-FAAC-E2E-064-edit-class-name-description-dan-class-code | FE+BE |
| TC-FA-FAAC-172 | E2E | TC-FA-FAAC-E2E-064-edit-class-name-description-dan-class-code | FE+BE |
| TC-FA-FAAC-173 | E2E | TC-FA-FAAC-E2E-085-edit-kasus-tepi-kapitalisasi-class-code-dan-tax-depreciation-class | FE+BE |
| TC-FA-FAAC-174 | E2E | TC-FA-FAAC-E2E-064-edit-class-name-description-dan-class-code | FE+BE |
| TC-FA-FAAC-175 | E2E | TC-FA-FAAC-E2E-064-edit-class-name-description-dan-class-code | FE+BE |
| TC-FA-FAAC-176 | E2E | TC-FA-FAAC-E2E-065-edit-depreciation-akun-dan-status-inactive | FE+BE |
| TC-FA-FAAC-177 | E2E | TC-FA-FAAC-E2E-065-edit-depreciation-akun-dan-status-inactive | FE+BE |
| TC-FA-FAAC-178 | E2E | TC-FA-FAAC-E2E-065-edit-depreciation-akun-dan-status-inactive | FE+BE |
| TC-FA-FAAC-179 | E2E | TC-FA-FAAC-E2E-085-edit-kasus-tepi-kapitalisasi-class-code-dan-tax-depreciation-class | FE+BE |
| TC-FA-FAAC-180 | E2E | TC-FA-FAAC-E2E-183-resilience-create-edit-duplicate | FE+BE |
| TC-FA-FAAC-181 | E2E | TC-FA-FAAC-E2E-096-aksi-form-dan-status-pada-asset-class-dihapus-pengguna-lain | FE+BE |
| TC-FA-FAAC-182 | E2E | TC-FA-FAAC-E2E-187-multi-sesi-dua-admin-race | FE+BE |
| TC-FA-FAAC-183 | E2E | TC-FA-FAAC-E2E-060-batas-method-plan-single-depreciation | FE+BE |
| TC-FA-FAAC-184 | E2E | TC-FA-FAAC-E2E-061-batas-method-plan-multi-depreciation | FE+BE |
| TC-FA-FAAC-185 | E2E | TC-FA-FAAC-E2E-061-batas-method-plan-multi-depreciation | FE+BE |
| TC-FA-FAAC-186 | E2E | TC-FA-FAAC-E2E-060-batas-method-plan-single-depreciation | FE+BE |
| TC-FA-FAAC-187 | E2E | TC-FA-FAAC-E2E-060-batas-method-plan-single-depreciation | FE+BE |
| TC-FA-FAAC-188 | E2E | TC-FA-FAAC-E2E-073-move-screening-dan-validasi-destination | FE+BE |
| TC-FA-FAAC-189 | E2E | TC-FA-FAAC-E2E-073-move-screening-dan-validasi-destination | FE+BE |
| TC-FA-FAAC-190 | E2E | TC-FA-FAAC-E2E-077-move-berhasil-single-dan-massal | FE+BE |
| TC-FA-FAAC-191 | E2E | TC-FA-FAAC-E2E-077-move-berhasil-single-dan-massal | FE+BE |
| TC-FA-FAAC-192 | E2E | TC-FA-FAAC-E2E-077-move-berhasil-single-dan-massal | FE+BE |
| TC-FA-FAAC-193 | E2E | TC-FA-FAAC-E2E-078-move-massal-tanpa-aset-aktif-bulan-lampau-klik-ganda-dan-spinner | FE+BE |
| TC-FA-FAAC-194 | E2E | TC-FA-FAAC-E2E-074-move-validasi-effective-from-dan-batal | FE+BE |
| TC-FA-FAAC-195 | E2E | TC-FA-FAAC-E2E-074-move-validasi-effective-from-dan-batal | FE+BE |
| TC-FA-FAAC-196 | E2E | TC-FA-FAAC-E2E-073-move-screening-dan-validasi-destination | FE+BE |
| TC-FA-FAAC-197 | E2E | TC-FA-FAAC-E2E-073-move-screening-dan-validasi-destination | FE+BE |
| TC-FA-FAAC-198 | E2E | TC-FA-FAAC-E2E-074-move-validasi-effective-from-dan-batal | FE+BE |
| TC-FA-FAAC-199 | E2E | TC-FA-FAAC-E2E-074-move-validasi-effective-from-dan-batal | FE+BE |
| TC-FA-FAAC-201 | E2E | TC-FA-FAAC-E2E-075-move-batas-bawah-effective-from-last-posted-period | FE+BE |
| TC-FA-FAAC-202 | E2E | TC-FA-FAAC-E2E-075-move-batas-bawah-effective-from-last-posted-period | FE+BE |
| TC-FA-FAAC-203 | E2E | TC-FA-FAAC-E2E-076-move-batas-bawah-lanjutan-dan-versi-scheduled-tujuan | FE+BE |
| TC-FA-FAAC-204 | E2E | TC-FA-FAAC-E2E-076-move-batas-bawah-lanjutan-dan-versi-scheduled-tujuan | FE+BE |
| TC-FA-FAAC-205 | E2E | TC-FA-FAAC-E2E-076-move-batas-bawah-lanjutan-dan-versi-scheduled-tujuan | FE+BE |
| TC-FA-FAAC-206 | E2E | TC-FA-FAAC-E2E-078-move-massal-tanpa-aset-aktif-bulan-lampau-klik-ganda-dan-spinner | FE+BE |
| TC-FA-FAAC-207 | E2E | TC-FA-FAAC-E2E-180-defense-in-depth-request-langsung-ditolak-guard-server | FE+BE |
| TC-FA-FAAC-207 | E2E | TC-FA-FAAC-E2E-195-log-absence-request-langsung-asset-name-ditolak-server | FE+BE |
| TC-FA-FAAC-208 | E2E | TC-FA-FAAC-E2E-079-move-ditolak-state-berubah-setelah-dialog-dibuka | FE+BE |
| TC-FA-FAAC-209 | E2E | TC-FA-FAAC-E2E-079-move-ditolak-state-berubah-setelah-dialog-dibuka | FE+BE |
| TC-FA-FAAC-210 | E2E | TC-FA-FAAC-E2E-079-move-ditolak-state-berubah-setelah-dialog-dibuka | FE+BE |
| TC-FA-FAAC-211 | E2E | TC-FA-FAAC-E2E-185-resilience-move-unassign-apply-changes-dan-cancel-scheduled | FE+BE |
| TC-FA-FAAC-212 | E2E | TC-FA-FAAC-E2E-185-resilience-move-unassign-apply-changes-dan-cancel-scheduled | FE+BE |
| TC-FA-FAAC-213 | E2E | TC-FA-FAAC-E2E-097-aksi-asset-name-pada-asset-class-dihapus-pengguna-lain | FE+BE |
| TC-FA-FAAC-214 | E2E | TC-FA-FAAC-E2E-088-delete-guard-asset-name-dialog-dan-berhasil | FE+BE |
| TC-FA-FAAC-215 | E2E | TC-FA-FAAC-E2E-088-delete-guard-asset-name-dialog-dan-berhasil | FE+BE |
| TC-FA-FAAC-216 | E2E | TC-FA-FAAC-E2E-087-delete-guard-d05-d04-dan-deactivate-instead | FE+BE |
| TC-FA-FAAC-217 | E2E | TC-FA-FAAC-E2E-087-delete-guard-d05-d04-dan-deactivate-instead | FE+BE |
| TC-FA-FAAC-218 | E2E | TC-FA-FAAC-E2E-087-delete-guard-d05-d04-dan-deactivate-instead | FE+BE |
| TC-FA-FAAC-219 | E2E | TC-FA-FAAC-E2E-088-delete-guard-asset-name-dialog-dan-berhasil | FE+BE |
| TC-FA-FAAC-220 | E2E | TC-FA-FAAC-E2E-088-delete-guard-asset-name-dialog-dan-berhasil | FE+BE |
| TC-FA-FAAC-221 | E2E | TC-FA-FAAC-E2E-088-delete-guard-asset-name-dialog-dan-berhasil | FE+BE |
| TC-FA-FAAC-222 | E2E | TC-FA-FAAC-E2E-186-resilience-status-bulk-dan-delete | FE+BE |
| TC-FA-FAAC-223 | E2E | TC-FA-FAAC-E2E-089-delete-race-dan-halaman-terakhir | FE+BE |
| TC-FA-FAAC-224 | E2E | TC-FA-FAAC-E2E-089-delete-race-dan-halaman-terakhir | FE+BE |
| TC-FA-FAAC-225 | E2E | TC-FA-FAAC-E2E-096-aksi-form-dan-status-pada-asset-class-dihapus-pengguna-lain | FE+BE |
| TC-FA-FAAC-226 | E2E | TC-FA-FAAC-E2E-087-delete-guard-d05-d04-dan-deactivate-instead | FE+BE |
| TC-FA-FAAC-227 | E2E | TC-FA-FAAC-E2E-027-role-matrix-negatif-delete-only-create-only-dan-read-manage-tab-asset-names | FE+BE |
| TC-FA-FAAC-228 | E2E | TC-FA-FAAC-E2E-090-unassign-menu-baris-dialog-dan-blokir | FE+BE |
| TC-FA-FAAC-229 | E2E | TC-FA-FAAC-E2E-090-unassign-menu-baris-dialog-dan-blokir | FE+BE |
| TC-FA-FAAC-230 | E2E | TC-FA-FAAC-E2E-090-unassign-menu-baris-dialog-dan-blokir | FE+BE |
| TC-FA-FAAC-231 | E2E | TC-FA-FAAC-E2E-091-unassign-berhasil-dan-ditolak-state-berubah | FE+BE |
| TC-FA-FAAC-232 | E2E | TC-FA-FAAC-E2E-091-unassign-berhasil-dan-ditolak-state-berubah | FE+BE |
| TC-FA-FAAC-233 | E2E | TC-FA-FAAC-E2E-110-unassign-massal-campuran-batal-dan-bulk-satu-item | FE+BE |
| TC-FA-FAAC-234 | E2E | TC-FA-FAAC-E2E-110-unassign-massal-campuran-batal-dan-bulk-satu-item | FE+BE |
| TC-FA-FAAC-235 | E2E | TC-FA-FAAC-E2E-090-unassign-menu-baris-dialog-dan-blokir | FE+BE |
| TC-FA-FAAC-236 | E2E | TC-FA-FAAC-E2E-091-unassign-berhasil-dan-ditolak-state-berubah | FE+BE |
| TC-FA-FAAC-237 | E2E | TC-FA-FAAC-E2E-091-unassign-berhasil-dan-ditolak-state-berubah | FE+BE |
| TC-FA-FAAC-238 | E2E | TC-FA-FAAC-E2E-185-resilience-move-unassign-apply-changes-dan-cancel-scheduled | FE+BE |
| TC-FA-FAAC-239 | E2E | TC-FA-FAAC-E2E-110-unassign-massal-campuran-batal-dan-bulk-satu-item | FE+BE |
| TC-FA-FAAC-240 | E2E | TC-FA-FAAC-E2E-097-aksi-asset-name-pada-asset-class-dihapus-pengguna-lain | FE+BE |
| TC-FA-FAAC-241 | E2E | TC-FA-FAAC-E2E-097-aksi-asset-name-pada-asset-class-dihapus-pengguna-lain | FE+BE |
| TC-FA-FAAC-242 | E2E | TC-FA-FAAC-E2E-180-defense-in-depth-request-langsung-ditolak-guard-server | FE+BE |
| TC-FA-FAAC-242 | E2E | TC-FA-FAAC-E2E-195-log-absence-request-langsung-asset-name-ditolak-server | FE+BE |
| TC-FA-FAAC-243 | E2E | TC-FA-FAAC-E2E-095-bulk-status-berhasil-dan-campuran | FE+BE |
| TC-FA-FAAC-244 | E2E | TC-FA-FAAC-E2E-095-bulk-status-berhasil-dan-campuran | FE+BE |
| TC-FA-FAAC-245 | E2E | TC-FA-FAAC-E2E-095-bulk-status-berhasil-dan-campuran | FE+BE |
| TC-FA-FAAC-246 | E2E | TC-FA-FAAC-E2E-094-bulk-status-blokir-batal-dan-collapse | FE+BE |
| TC-FA-FAAC-247 | E2E | TC-FA-FAAC-E2E-094-bulk-status-blokir-batal-dan-collapse | FE+BE |
| TC-FA-FAAC-248 | E2E | TC-FA-FAAC-E2E-094-bulk-status-blokir-batal-dan-collapse | FE+BE |
| TC-FA-FAAC-249 | E2E | TC-FA-FAAC-E2E-095-bulk-status-berhasil-dan-campuran | FE+BE |
| TC-FA-FAAC-250 | E2E | TC-FA-FAAC-E2E-186-resilience-status-bulk-dan-delete | FE+BE |
| TC-FA-FAAC-251 | E2E | TC-FA-FAAC-E2E-186-resilience-status-bulk-dan-delete | FE+BE |
| TC-FA-FAAC-252 | E2E | TC-FA-FAAC-E2E-094-bulk-status-blokir-batal-dan-collapse | FE+BE |
| TC-FA-FAAC-253 | E2E | TC-FA-FAAC-E2E-096-aksi-form-dan-status-pada-asset-class-dihapus-pengguna-lain | FE+BE |
| TC-FA-FAAC-254 | E2E | TC-FA-FAAC-E2E-081-mode-create-draft-asset-name-screening-dan-pemilihan-draft | FE+BE |
| TC-FA-FAAC-255 | E2E | TC-FA-FAAC-E2E-081-mode-create-draft-asset-name-screening-dan-pemilihan-draft | FE+BE |
| TC-FA-FAAC-256 | E2E | TC-FA-FAAC-E2E-081-mode-create-draft-asset-name-screening-dan-pemilihan-draft | FE+BE |
| TC-FA-FAAC-257 | E2E | TC-FA-FAAC-E2E-082-mode-create-draft-asset-name-hapus-satu-dan-clear-field | FE+BE |
| TC-FA-FAAC-258 | E2E | TC-FA-FAAC-E2E-082-mode-create-draft-asset-name-hapus-satu-dan-clear-field | FE+BE |
| TC-FA-FAAC-259 | E2E | TC-FA-FAAC-E2E-084-mode-create-draft-asset-name-submit | FE+BE |
| TC-FA-FAAC-260 | E2E | TC-FA-FAAC-E2E-083-mode-create-draft-asset-name-unsaved-changes-cancel-dan-leave | FE+BE |
| TC-FA-FAAC-261 | E2E | TC-FA-FAAC-E2E-083-mode-create-draft-asset-name-unsaved-changes-cancel-dan-leave | FE+BE |
| TC-FA-FAAC-262 | E2E | TC-FA-FAAC-E2E-191-resilience-submit-draft-asset-name-dan-use-recommended-classes | FE+BE |
| TC-FA-FAAC-263 | E2E | TC-FA-FAAC-E2E-080-duplicate-asset-class | FE+BE |
| TC-FA-FAAC-264 | E2E | TC-FA-FAAC-E2E-080-duplicate-asset-class | FE+BE |
| TC-FA-FAAC-265 | E2E | TC-FA-FAAC-E2E-086-duplicate-nilai-sumber-tidak-valid-dan-versi-scheduled | FE+BE |
| TC-FA-FAAC-267 | E2E | TC-FA-FAAC-E2E-059-batas-jumlah-asset-class-master-data-count-limit | FE+BE |
| TC-FA-FAAC-268 | E2E | TC-FA-FAAC-E2E-096-aksi-form-dan-status-pada-asset-class-dihapus-pengguna-lain | FE+BE |
| TC-FA-FAAC-269 | E2E | TC-FA-FAAC-E2E-183-resilience-create-edit-duplicate | FE+BE |
| TC-FA-FAAC-270 | E2E | TC-FA-FAAC-E2E-013-banner-asset-name-tanpa-asset-class-dan-dialog-d23 | FE+BE |
| TC-FA-FAAC-271 | E2E | TC-FA-FAAC-E2E-013-banner-asset-name-tanpa-asset-class-dan-dialog-d23 | FE+BE |
| TC-FA-FAAC-272 | E2E | TC-FA-FAAC-E2E-013-banner-asset-name-tanpa-asset-class-dan-dialog-d23 | FE+BE |
| TC-FA-FAAC-273 | E2E | TC-FA-FAAC-E2E-014-dialog-d23-search-dan-sort | FE+BE |
| TC-FA-FAAC-274 | E2E | TC-FA-FAAC-E2E-014-dialog-d23-search-dan-sort | FE+BE |
| TC-FA-FAAC-275 | E2E | TC-FA-FAAC-E2E-014-dialog-d23-search-dan-sort | FE+BE |
| TC-FA-FAAC-276 | E2E | TC-FA-FAAC-E2E-014-dialog-d23-search-dan-sort | FE+BE |
| TC-FA-FAAC-277 | E2E | TC-FA-FAAC-E2E-014-dialog-d23-search-dan-sort | FE+BE |
| TC-FA-FAAC-278 | E2E | TC-FA-FAAC-E2E-015-dialog-d23-kolom-dan-tutup-otomatis | FE+BE |
| TC-FA-FAAC-279 | E2E | TC-FA-FAAC-E2E-015-dialog-d23-kolom-dan-tutup-otomatis | FE+BE |
| TC-FA-FAAC-280 | E2E | TC-FA-FAAC-E2E-182-resilience-baca-dan-download | FE+BE |
| TC-FA-FAAC-281 | E2E | TC-FA-FAAC-E2E-182-resilience-baca-dan-download | FE+BE |
| TC-FA-FAAC-282 | E2E | TC-FA-FAAC-E2E-004-empty-state-tabel-dan-use-recommended-classes-blokir | FE+BE |
| TC-FA-FAAC-283 | E2E | TC-FA-FAAC-E2E-006-use-recommended-classes-create-berhasil | FE+BE |
| TC-FA-FAAC-284 | E2E | TC-FA-FAAC-E2E-006-use-recommended-classes-create-berhasil | FE+BE |
| TC-FA-FAAC-285 | E2E | TC-FA-FAAC-E2E-004-empty-state-tabel-dan-use-recommended-classes-blokir | FE+BE |
| TC-FA-FAAC-286 | E2E | TC-FA-FAAC-E2E-004-empty-state-tabel-dan-use-recommended-classes-blokir | FE+BE |
| TC-FA-FAAC-287 | E2E | TC-FA-FAAC-E2E-005-use-recommended-classes-validasi-baris-dan-tutup-dialog | FE+BE |
| TC-FA-FAAC-288 | E2E | TC-FA-FAAC-E2E-005-use-recommended-classes-validasi-baris-dan-tutup-dialog | FE+BE |
| TC-FA-FAAC-289 | E2E | TC-FA-FAAC-E2E-005-use-recommended-classes-validasi-baris-dan-tutup-dialog | FE+BE |
| TC-FA-FAAC-290 | E2E | TC-FA-FAAC-E2E-004-empty-state-tabel-dan-use-recommended-classes-blokir | FE+BE |
| TC-FA-FAAC-291 | E2E | TC-FA-FAAC-E2E-004-empty-state-tabel-dan-use-recommended-classes-blokir | FE+BE |
| TC-FA-FAAC-292 | E2E | TC-FA-FAAC-E2E-191-resilience-submit-draft-asset-name-dan-use-recommended-classes | FE+BE |
| TC-FA-FAAC-293 | E2E | TC-FA-FAAC-E2E-004-empty-state-tabel-dan-use-recommended-classes-blokir | FE+BE |
| TC-FA-FAAC-294 | E2E | TC-FA-FAAC-E2E-093-toggle-status-satu-asset-class-berhasil | FE+BE |
| TC-FA-FAAC-295 | E2E | TC-FA-FAAC-E2E-092-toggle-status-satu-asset-class-blokir-dan-batal | FE+BE |
| TC-FA-FAAC-296 | E2E | TC-FA-FAAC-E2E-093-toggle-status-satu-asset-class-berhasil | FE+BE |
| TC-FA-FAAC-297 | E2E | TC-FA-FAAC-E2E-093-toggle-status-satu-asset-class-berhasil | FE+BE |
| TC-FA-FAAC-298 | E2E | TC-FA-FAAC-E2E-092-toggle-status-satu-asset-class-blokir-dan-batal | FE+BE |
| TC-FA-FAAC-299 | E2E | TC-FA-FAAC-E2E-092-toggle-status-satu-asset-class-blokir-dan-batal | FE+BE |
| TC-FA-FAAC-300 | E2E | TC-FA-FAAC-E2E-092-toggle-status-satu-asset-class-blokir-dan-batal | FE+BE |
| TC-FA-FAAC-301 | E2E | TC-FA-FAAC-E2E-092-toggle-status-satu-asset-class-blokir-dan-batal | FE+BE |
| TC-FA-FAAC-302 | E2E | TC-FA-FAAC-E2E-186-resilience-status-bulk-dan-delete | FE+BE |
| TC-FA-FAAC-303 | E2E | TC-FA-FAAC-E2E-186-resilience-status-bulk-dan-delete | FE+BE |
| TC-FA-FAAC-304 | E2E | TC-FA-FAAC-E2E-092-toggle-status-satu-asset-class-blokir-dan-batal | FE+BE |
| TC-FA-FAAC-305 | E2E | TC-FA-FAAC-E2E-096-aksi-form-dan-status-pada-asset-class-dihapus-pengguna-lain | FE+BE |
| TC-FA-FAAC-306 | E2E | TC-FA-FAAC-E2E-096-aksi-form-dan-status-pada-asset-class-dihapus-pengguna-lain | FE+BE |
| TC-FA-FAAC-307 | E2E | TC-FA-FAAC-E2E-098-apply-changes-screening-berhasil-dan-batal | FE+BE |
| TC-FA-FAAC-308 | E2E | TC-FA-FAAC-E2E-098-apply-changes-screening-berhasil-dan-batal | FE+BE |
| TC-FA-FAAC-309 | E2E | TC-FA-FAAC-E2E-099-apply-changes-effective-from-masa-depan-dan-pratinjau | FE+BE |
| TC-FA-FAAC-310 | E2E | TC-FA-FAAC-E2E-098-apply-changes-screening-berhasil-dan-batal | FE+BE |
| TC-FA-FAAC-311 | E2E | TC-FA-FAAC-E2E-185-resilience-move-unassign-apply-changes-dan-cancel-scheduled | FE+BE |
| TC-FA-FAAC-312 | E2E | TC-FA-FAAC-E2E-099-apply-changes-effective-from-masa-depan-dan-pratinjau | FE+BE |
| TC-FA-FAAC-313 | E2E | TC-FA-FAAC-E2E-102-apply-changes-alert-dampak-dan-capitalization-threshold | FE+BE |
| TC-FA-FAAC-314 | E2E | TC-FA-FAAC-E2E-102-apply-changes-alert-dampak-dan-capitalization-threshold | FE+BE |
| TC-FA-FAAC-315 | E2E | TC-FA-FAAC-E2E-102-apply-changes-alert-dampak-dan-capitalization-threshold | FE+BE |
| TC-FA-FAAC-316 | E2E | TC-FA-FAAC-E2E-100-apply-changes-validasi-effective-from-dasar | FE+BE |
| TC-FA-FAAC-319 | E2E | TC-FA-FAAC-E2E-101-apply-changes-validasi-effective-from-versi-dan-last-posted | FE+BE |
| TC-FA-FAAC-320 | E2E | TC-FA-FAAC-E2E-101-apply-changes-validasi-effective-from-versi-dan-last-posted | FE+BE |
| TC-FA-FAAC-321 | E2E | TC-FA-FAAC-E2E-103-versi-scheduled-alert-dan-save-no-op | FE+BE |
| TC-FA-FAAC-322 | E2E | TC-FA-FAAC-E2E-103-versi-scheduled-alert-dan-save-no-op | FE+BE |
| TC-FA-FAAC-323 | E2E | TC-FA-FAAC-E2E-103-versi-scheduled-alert-dan-save-no-op | FE+BE |
| TC-FA-FAAC-324 | E2E | TC-FA-FAAC-E2E-103-versi-scheduled-alert-dan-save-no-op | FE+BE |
| TC-FA-FAAC-325 | E2E | TC-FA-FAAC-E2E-103-versi-scheduled-alert-dan-save-no-op | FE+BE |
| TC-FA-FAAC-326 | E2E | TC-FA-FAAC-E2E-105-versi-scheduled-job-penerapan-otomatis | FE+BE |
| TC-FA-FAAC-327 | E2E | TC-FA-FAAC-E2E-179-state-tenant-aktivitas-sistem-tidak-diblokir | FE+BE |
| TC-FA-FAAC-328 | E2E | TC-FA-FAAC-E2E-105-versi-scheduled-job-penerapan-otomatis | FE+BE |
| TC-FA-FAAC-329 | E2E | TC-FA-FAAC-E2E-105-versi-scheduled-job-penerapan-otomatis | FE+BE |
| TC-FA-FAAC-330 | E2E | TC-FA-FAAC-E2E-104-versi-scheduled-cancel-dialog-d24 | FE+BE |
| TC-FA-FAAC-331 | E2E | TC-FA-FAAC-E2E-104-versi-scheduled-cancel-dialog-d24 | FE+BE |
| TC-FA-FAAC-332 | E2E | TC-FA-FAAC-E2E-104-versi-scheduled-cancel-dialog-d24 | FE+BE |
| TC-FA-FAAC-333 | E2E | TC-FA-FAAC-E2E-104-versi-scheduled-cancel-dialog-d24 | FE+BE |
| TC-FA-FAAC-334 | E2E | TC-FA-FAAC-E2E-104-versi-scheduled-cancel-dialog-d24 | FE+BE |
| TC-FA-FAAC-335 | E2E | TC-FA-FAAC-E2E-185-resilience-move-unassign-apply-changes-dan-cancel-scheduled | FE+BE |
| TC-FA-FAAC-336 | E2E | TC-FA-FAAC-E2E-106-class-code-terkunci-last-posted-period | FE+BE |
| TC-FA-FAAC-337 | E2E | TC-FA-FAAC-E2E-106-class-code-terkunci-last-posted-period | FE+BE |
| TC-FA-FAAC-338 | E2E | TC-FA-FAAC-E2E-106-class-code-terkunci-last-posted-period | FE+BE |
| TC-FA-FAAC-339 | E2E | TC-FA-FAAC-E2E-106-class-code-terkunci-last-posted-period | FE+BE |
| TC-FA-FAAC-340 | E2E | TC-FA-FAAC-E2E-107-last-posted-dan-last-exported-period | FE+BE |
| TC-FA-FAAC-341 | E2E | TC-FA-FAAC-E2E-107-last-posted-dan-last-exported-period | FE+BE |
| TC-FA-FAAC-342 | E2E | TC-FA-FAAC-E2E-107-last-posted-dan-last-exported-period | FE+BE |
| TC-FA-FAAC-343 | E2E | TC-FA-FAAC-E2E-179-state-tenant-aktivitas-sistem-tidak-diblokir | FE+BE |
| TC-FA-FAAC-344 | E2E | TC-FA-FAAC-E2E-108-reklasifikasi-d12-screening-dan-batal | FE+BE |
| TC-FA-FAAC-345 | E2E | TC-FA-FAAC-E2E-109-reklasifikasi-d12-new-journals-dan-create-reclassification | FE+BE |
| TC-FA-FAAC-346 | E2E | TC-FA-FAAC-E2E-109-reklasifikasi-d12-new-journals-dan-create-reclassification | FE+BE |
| TC-FA-FAAC-347 | E2E | TC-FA-FAAC-E2E-108-reklasifikasi-d12-screening-dan-batal | FE+BE |
| TC-FA-FAAC-348 | E2E | TC-FA-FAAC-E2E-108-reklasifikasi-d12-screening-dan-batal | FE+BE |
| TC-FA-FAAC-349 | E2E | TC-FA-FAAC-E2E-108-reklasifikasi-d12-screening-dan-batal | FE+BE |
| TC-FA-FAAC-350 | E2E | TC-FA-FAAC-E2E-109-reklasifikasi-d12-new-journals-dan-create-reclassification | FE+BE |
| TC-FA-FAAC-351 | E2E | TC-FA-FAAC-E2E-112-search-class-code-class-name-commercial-fiscal-threshold | FE+BE |
| TC-FA-FAAC-352 | E2E | TC-FA-FAAC-E2E-112-search-class-code-class-name-commercial-fiscal-threshold | FE+BE |
| TC-FA-FAAC-353 | E2E | TC-FA-FAAC-E2E-112-search-class-code-class-name-commercial-fiscal-threshold | FE+BE |
| TC-FA-FAAC-354 | E2E | TC-FA-FAAC-E2E-112-search-class-code-class-name-commercial-fiscal-threshold | FE+BE |
| TC-FA-FAAC-355 | E2E | TC-FA-FAAC-E2E-113-search-accounts-modified-by-dan-teks-khusus | FE+BE |
| TC-FA-FAAC-356 | E2E | TC-FA-FAAC-E2E-113-search-accounts-modified-by-dan-teks-khusus | FE+BE |
| TC-FA-FAAC-357 | E2E | TC-FA-FAAC-E2E-113-search-accounts-modified-by-dan-teks-khusus | FE+BE |
| TC-FA-FAAC-358 | E2E | TC-FA-FAAC-E2E-113-search-accounts-modified-by-dan-teks-khusus | FE+BE |
| TC-FA-FAAC-359 | E2E | TC-FA-FAAC-E2E-113-search-accounts-modified-by-dan-teks-khusus | FE+BE |
| TC-FA-FAAC-360 | E2E | TC-FA-FAAC-E2E-114-search-siklus-search-box-trim-dan-nominal-berdesimal | FE+BE |
| TC-FA-FAAC-361 | E2E | TC-FA-FAAC-E2E-114-search-siklus-search-box-trim-dan-nominal-berdesimal | FE+BE |
| TC-FA-FAAC-362 | E2E | TC-FA-FAAC-E2E-132-search-kolom-tersembunyi-dan-ditampilkan-kembali | FE+BE |
| TC-FA-FAAC-363 | E2E | TC-FA-FAAC-E2E-115-filter-panel-screening-dan-multi-select | FE+BE |
| TC-FA-FAAC-364 | E2E | TC-FA-FAAC-E2E-115-filter-panel-screening-dan-multi-select | FE+BE |
| TC-FA-FAAC-365 | E2E | TC-FA-FAAC-E2E-115-filter-panel-screening-dan-multi-select | FE+BE |
| TC-FA-FAAC-366 | E2E | TC-FA-FAAC-E2E-116-filter-range-min-max-dan-date | FE+BE |
| TC-FA-FAAC-367 | E2E | TC-FA-FAAC-E2E-116-filter-range-min-max-dan-date | FE+BE |
| TC-FA-FAAC-368 | E2E | TC-FA-FAAC-E2E-116-filter-range-min-max-dan-date | FE+BE |
| TC-FA-FAAC-369 | E2E | TC-FA-FAAC-E2E-117-filter-logika-or-and-chip-dan-dropdown | FE+BE |
| TC-FA-FAAC-370 | E2E | TC-FA-FAAC-E2E-117-filter-logika-or-and-chip-dan-dropdown | FE+BE |
| TC-FA-FAAC-371 | E2E | TC-FA-FAAC-E2E-117-filter-logika-or-and-chip-dan-dropdown | FE+BE |
| TC-FA-FAAC-372 | E2E | TC-FA-FAAC-E2E-117-filter-logika-or-and-chip-dan-dropdown | FE+BE |
| TC-FA-FAAC-373 | E2E | TC-FA-FAAC-E2E-117-filter-logika-or-and-chip-dan-dropdown | FE+BE |
| TC-FA-FAAC-374 | E2E | TC-FA-FAAC-E2E-118-indikator-filter-aktif-dan-kombinasi-search-sort | FE+BE |
| TC-FA-FAAC-375 | E2E | TC-FA-FAAC-E2E-118-indikator-filter-aktif-dan-kombinasi-search-sort | FE+BE |
| TC-FA-FAAC-376 | E2E | TC-FA-FAAC-E2E-118-indikator-filter-aktif-dan-kombinasi-search-sort | FE+BE |
| TC-FA-FAAC-377 | E2E | TC-FA-FAAC-E2E-118-indikator-filter-aktif-dan-kombinasi-search-sort | FE+BE |
| TC-FA-FAAC-378 | E2E | TC-FA-FAAC-E2E-118-indikator-filter-aktif-dan-kombinasi-search-sort | FE+BE |
| TC-FA-FAAC-379 | E2E | TC-FA-FAAC-E2E-119-filter-lepas-draft-kolom-dan-kombinasi | FE+BE |
| TC-FA-FAAC-380 | E2E | TC-FA-FAAC-E2E-119-filter-lepas-draft-kolom-dan-kombinasi | FE+BE |
| TC-FA-FAAC-381 | E2E | TC-FA-FAAC-E2E-119-filter-lepas-draft-kolom-dan-kombinasi | FE+BE |
| TC-FA-FAAC-382 | E2E | TC-FA-FAAC-E2E-119-filter-lepas-draft-kolom-dan-kombinasi | FE+BE |
| TC-FA-FAAC-383 | E2E | TC-FA-FAAC-E2E-125-paginasi-tabel-asset-class | FE+BE |
| TC-FA-FAAC-384 | E2E | TC-FA-FAAC-E2E-126-state-tabel-kombinasi-dan-kembali-dari-detail | FE+BE |
| TC-FA-FAAC-385 | E2E | TC-FA-FAAC-E2E-120-sort-3-state-kolom-teks-commercial-fiscal | FE+BE |
| TC-FA-FAAC-386 | E2E | TC-FA-FAAC-E2E-120-sort-3-state-kolom-teks-commercial-fiscal | FE+BE |
| TC-FA-FAAC-387 | E2E | TC-FA-FAAC-E2E-120-sort-3-state-kolom-teks-commercial-fiscal | FE+BE |
| TC-FA-FAAC-388 | E2E | TC-FA-FAAC-E2E-120-sort-3-state-kolom-teks-commercial-fiscal | FE+BE |
| TC-FA-FAAC-389 | E2E | TC-FA-FAAC-E2E-120-sort-3-state-kolom-teks-commercial-fiscal | FE+BE |
| TC-FA-FAAC-390 | E2E | TC-FA-FAAC-E2E-121-sort-3-state-active-accounts-last-updated | FE+BE |
| TC-FA-FAAC-391 | E2E | TC-FA-FAAC-E2E-121-sort-3-state-active-accounts-last-updated | FE+BE |
| TC-FA-FAAC-392 | E2E | TC-FA-FAAC-E2E-121-sort-3-state-active-accounts-last-updated | FE+BE |
| TC-FA-FAAC-393 | E2E | TC-FA-FAAC-E2E-121-sort-3-state-active-accounts-last-updated | FE+BE |
| TC-FA-FAAC-394 | E2E | TC-FA-FAAC-E2E-121-sort-3-state-active-accounts-last-updated | FE+BE |
| TC-FA-FAAC-395 | E2E | TC-FA-FAAC-E2E-122-setup-column-screening-dan-ceklis-kolom | FE+BE |
| TC-FA-FAAC-396 | E2E | TC-FA-FAAC-E2E-122-setup-column-screening-dan-ceklis-kolom | FE+BE |
| TC-FA-FAAC-397 | E2E | TC-FA-FAAC-E2E-122-setup-column-screening-dan-ceklis-kolom | FE+BE |
| TC-FA-FAAC-398 | E2E | TC-FA-FAAC-E2E-122-setup-column-screening-dan-ceklis-kolom | FE+BE |
| TC-FA-FAAC-399 | E2E | TC-FA-FAAC-E2E-123-setup-column-geser-dan-pin | FE+BE |
| TC-FA-FAAC-400 | E2E | TC-FA-FAAC-E2E-123-setup-column-geser-dan-pin | FE+BE |
| TC-FA-FAAC-401 | E2E | TC-FA-FAAC-E2E-123-setup-column-geser-dan-pin | FE+BE |
| TC-FA-FAAC-402 | E2E | TC-FA-FAAC-E2E-123-setup-column-geser-dan-pin | FE+BE |
| TC-FA-FAAC-403 | E2E | TC-FA-FAAC-E2E-124-setup-column-reset-tutup-satu-kolom-dan-persistensi | FE+BE |
| TC-FA-FAAC-404 | E2E | TC-FA-FAAC-E2E-124-setup-column-reset-tutup-satu-kolom-dan-persistensi | FE+BE |
| TC-FA-FAAC-405 | E2E | TC-FA-FAAC-E2E-124-setup-column-reset-tutup-satu-kolom-dan-persistensi | FE+BE |
| TC-FA-FAAC-406 | E2E | TC-FA-FAAC-E2E-124-setup-column-reset-tutup-satu-kolom-dan-persistensi | FE+BE |
| TC-FA-FAAC-407 | E2E | TC-FA-FAAC-E2E-123-setup-column-geser-dan-pin | FE+BE |
| TC-FA-FAAC-408 | E2E | TC-FA-FAAC-E2E-125-paginasi-tabel-asset-class | FE+BE |
| TC-FA-FAAC-409 | E2E | TC-FA-FAAC-E2E-125-paginasi-tabel-asset-class | FE+BE |
| TC-FA-FAAC-410 | E2E | TC-FA-FAAC-E2E-125-paginasi-tabel-asset-class | FE+BE |
| TC-FA-FAAC-411 | E2E | TC-FA-FAAC-E2E-125-paginasi-tabel-asset-class | FE+BE |
| TC-FA-FAAC-412 | E2E | TC-FA-FAAC-E2E-125-paginasi-tabel-asset-class | FE+BE |
| TC-FA-FAAC-413 | E2E | TC-FA-FAAC-E2E-126-state-tabel-kombinasi-dan-kembali-dari-detail | FE+BE |
| TC-FA-FAAC-414 | E2E | TC-FA-FAAC-E2E-126-state-tabel-kombinasi-dan-kembali-dari-detail | FE+BE |
| TC-FA-FAAC-415 | E2E | TC-FA-FAAC-E2E-127-state-tabel-pindah-tab-refresh-dan-reset-menu | FE+BE |
| TC-FA-FAAC-416 | E2E | TC-FA-FAAC-E2E-127-state-tabel-pindah-tab-refresh-dan-reset-menu | FE+BE |
| TC-FA-FAAC-417 | E2E | TC-FA-FAAC-E2E-127-state-tabel-pindah-tab-refresh-dan-reset-menu | FE+BE |
| TC-FA-FAAC-418 | E2E | TC-FA-FAAC-E2E-128-download-tabel-nama-berkas-dan-cakupan-baris | FE+BE |
| TC-FA-FAAC-419 | E2E | TC-FA-FAAC-E2E-128-download-tabel-nama-berkas-dan-cakupan-baris | FE+BE |
| TC-FA-FAAC-420 | E2E | TC-FA-FAAC-E2E-128-download-tabel-nama-berkas-dan-cakupan-baris | FE+BE |
| TC-FA-FAAC-421 | E2E | TC-FA-FAAC-E2E-128-download-tabel-nama-berkas-dan-cakupan-baris | FE+BE |
| TC-FA-FAAC-422 | E2E | TC-FA-FAAC-E2E-129-download-isi-berkas-csv-xlsx | FE+BE |
| TC-FA-FAAC-423 | E2E | TC-FA-FAAC-E2E-128-download-tabel-nama-berkas-dan-cakupan-baris | FE+BE |
| TC-FA-FAAC-424 | E2E | TC-FA-FAAC-E2E-128-download-tabel-nama-berkas-dan-cakupan-baris | FE+BE |
| TC-FA-FAAC-425 | E2E | TC-FA-FAAC-E2E-128-download-tabel-nama-berkas-dan-cakupan-baris | FE+BE |
| TC-FA-FAAC-426 | E2E | TC-FA-FAAC-E2E-182-resilience-baca-dan-download | FE+BE |
| TC-FA-FAAC-427 | E2E | TC-FA-FAAC-E2E-129-download-isi-berkas-csv-xlsx | FE+BE |
| TC-FA-FAAC-428 | E2E | TC-FA-FAAC-E2E-129-download-isi-berkas-csv-xlsx | FE+BE |
| TC-FA-FAAC-429 | E2E | TC-FA-FAAC-E2E-129-download-isi-berkas-csv-xlsx | FE+BE |
| TC-FA-FAAC-430 | E2E | TC-FA-FAAC-E2E-128-download-tabel-nama-berkas-dan-cakupan-baris | FE+BE |
| TC-FA-FAAC-431 | E2E | TC-FA-FAAC-E2E-188-volume-selection-limit-dan-5000-baris | FE+BE |
| TC-FA-FAAC-432 | E2E | TC-FA-FAAC-E2E-129-download-isi-berkas-csv-xlsx | FE+BE |
| TC-FA-FAAC-433 | E2E | TC-FA-FAAC-E2E-129-download-isi-berkas-csv-xlsx | FE+BE |
| TC-FA-FAAC-434 | E2E | TC-FA-FAAC-E2E-129-download-isi-berkas-csv-xlsx | FE+BE |
| TC-FA-FAAC-435 | E2E | TC-FA-FAAC-E2E-130-bulk-action-bar-dan-seleksi | FE+BE |
| TC-FA-FAAC-436 | E2E | TC-FA-FAAC-E2E-130-bulk-action-bar-dan-seleksi | FE+BE |
| TC-FA-FAAC-437 | E2E | TC-FA-FAAC-E2E-130-bulk-action-bar-dan-seleksi | FE+BE |
| TC-FA-FAAC-438 | E2E | TC-FA-FAAC-E2E-130-bulk-action-bar-dan-seleksi | FE+BE |
| TC-FA-FAAC-439 | E2E | TC-FA-FAAC-E2E-130-bulk-action-bar-dan-seleksi | FE+BE |
| TC-FA-FAAC-440 | E2E | TC-FA-FAAC-E2E-130-bulk-action-bar-dan-seleksi | FE+BE |
| TC-FA-FAAC-441 | E2E | TC-FA-FAAC-E2E-134-tab-asset-names-search | FE+BE |
| TC-FA-FAAC-442 | E2E | TC-FA-FAAC-E2E-134-tab-asset-names-search | FE+BE |
| TC-FA-FAAC-443 | E2E | TC-FA-FAAC-E2E-134-tab-asset-names-search | FE+BE |
| TC-FA-FAAC-444 | E2E | TC-FA-FAAC-E2E-134-tab-asset-names-search | FE+BE |
| TC-FA-FAAC-445 | E2E | TC-FA-FAAC-E2E-134-tab-asset-names-search | FE+BE |
| TC-FA-FAAC-446 | E2E | TC-FA-FAAC-E2E-134-tab-asset-names-search | FE+BE |
| TC-FA-FAAC-447 | E2E | TC-FA-FAAC-E2E-134-tab-asset-names-search | FE+BE |
| TC-FA-FAAC-448 | E2E | TC-FA-FAAC-E2E-134-tab-asset-names-search | FE+BE |
| TC-FA-FAAC-449 | E2E | TC-FA-FAAC-E2E-135-tab-asset-names-filter | FE+BE |
| TC-FA-FAAC-450 | E2E | TC-FA-FAAC-E2E-135-tab-asset-names-filter | FE+BE |
| TC-FA-FAAC-451 | E2E | TC-FA-FAAC-E2E-135-tab-asset-names-filter | FE+BE |
| TC-FA-FAAC-452 | E2E | TC-FA-FAAC-E2E-135-tab-asset-names-filter | FE+BE |
| TC-FA-FAAC-453 | E2E | TC-FA-FAAC-E2E-135-tab-asset-names-filter | FE+BE |
| TC-FA-FAAC-454 | E2E | TC-FA-FAAC-E2E-136-tab-asset-names-filter-lanjutan-dan-kombinasi | FE+BE |
| TC-FA-FAAC-455 | E2E | TC-FA-FAAC-E2E-136-tab-asset-names-filter-lanjutan-dan-kombinasi | FE+BE |
| TC-FA-FAAC-456 | E2E | TC-FA-FAAC-E2E-136-tab-asset-names-filter-lanjutan-dan-kombinasi | FE+BE |
| TC-FA-FAAC-457 | E2E | TC-FA-FAAC-E2E-137-tab-asset-names-sort-3-state | FE+BE |
| TC-FA-FAAC-458 | E2E | TC-FA-FAAC-E2E-137-tab-asset-names-sort-3-state | FE+BE |
| TC-FA-FAAC-459 | E2E | TC-FA-FAAC-E2E-137-tab-asset-names-sort-3-state | FE+BE |
| TC-FA-FAAC-460 | E2E | TC-FA-FAAC-E2E-138-tab-asset-names-sort-lanjutan-dan-kolom-label | FE+BE |
| TC-FA-FAAC-461 | E2E | TC-FA-FAAC-E2E-138-tab-asset-names-sort-lanjutan-dan-kolom-label | FE+BE |
| TC-FA-FAAC-462 | E2E | TC-FA-FAAC-E2E-138-tab-asset-names-sort-lanjutan-dan-kolom-label | FE+BE |
| TC-FA-FAAC-463 | E2E | TC-FA-FAAC-E2E-139-tab-asset-names-kolom-dan-persistensi | FE+BE |
| TC-FA-FAAC-464 | E2E | TC-FA-FAAC-E2E-156-tab-asset-names-sembunyikan-dan-tampilkan-tiap-kolom | FE+BE |
| TC-FA-FAAC-465 | E2E | TC-FA-FAAC-E2E-139-tab-asset-names-kolom-dan-persistensi | FE+BE |
| TC-FA-FAAC-466 | E2E | TC-FA-FAAC-E2E-139-tab-asset-names-kolom-dan-persistensi | FE+BE |
| TC-FA-FAAC-467 | E2E | TC-FA-FAAC-E2E-140-tab-asset-names-paginasi-dan-state-tab | FE+BE |
| TC-FA-FAAC-468 | E2E | TC-FA-FAAC-E2E-140-tab-asset-names-paginasi-dan-state-tab | FE+BE |
| TC-FA-FAAC-469 | E2E | TC-FA-FAAC-E2E-140-tab-asset-names-paginasi-dan-state-tab | FE+BE |
| TC-FA-FAAC-470 | E2E | TC-FA-FAAC-E2E-140-tab-asset-names-paginasi-dan-state-tab | FE+BE |
| TC-FA-FAAC-471 | E2E | TC-FA-FAAC-E2E-140-tab-asset-names-paginasi-dan-state-tab | FE+BE |
| TC-FA-FAAC-472 | E2E | TC-FA-FAAC-E2E-146-changelog-screening-empty-paginasi-dan-format-sel | FE+BE |
| TC-FA-FAAC-473 | E2E | TC-FA-FAAC-E2E-146-changelog-screening-empty-paginasi-dan-format-sel | FE+BE |
| TC-FA-FAAC-474 | E2E | TC-FA-FAAC-E2E-146-changelog-screening-empty-paginasi-dan-format-sel | FE+BE |
| TC-FA-FAAC-475 | E2E | TC-FA-FAAC-E2E-146-changelog-screening-empty-paginasi-dan-format-sel | FE+BE |
| TC-FA-FAAC-476 | E2E | TC-FA-FAAC-E2E-146-changelog-screening-empty-paginasi-dan-format-sel | FE+BE |
| TC-FA-FAAC-477 | E2E | TC-FA-FAAC-E2E-147-changelog-search-action-field-class-code-old-new-value | FE+BE |
| TC-FA-FAAC-478 | E2E | TC-FA-FAAC-E2E-147-changelog-search-action-field-class-code-old-new-value | FE+BE |
| TC-FA-FAAC-479 | E2E | TC-FA-FAAC-E2E-147-changelog-search-action-field-class-code-old-new-value | FE+BE |
| TC-FA-FAAC-480 | E2E | TC-FA-FAAC-E2E-147-changelog-search-action-field-class-code-old-new-value | FE+BE |
| TC-FA-FAAC-481 | E2E | TC-FA-FAAC-E2E-148-changelog-search-modified-by-date-siklus-dan-kolom-tersembunyi | FE+BE |
| TC-FA-FAAC-482 | E2E | TC-FA-FAAC-E2E-148-changelog-search-modified-by-date-siklus-dan-kolom-tersembunyi | FE+BE |
| TC-FA-FAAC-483 | E2E | TC-FA-FAAC-E2E-148-changelog-search-modified-by-date-siklus-dan-kolom-tersembunyi | FE+BE |
| TC-FA-FAAC-484 | E2E | TC-FA-FAAC-E2E-148-changelog-search-modified-by-date-siklus-dan-kolom-tersembunyi | FE+BE |
| TC-FA-FAAC-485 | E2E | TC-FA-FAAC-E2E-149-changelog-filter-struktur-opsi-dan-multi-select | FE+BE |
| TC-FA-FAAC-486 | E2E | TC-FA-FAAC-E2E-149-changelog-filter-struktur-opsi-dan-multi-select | FE+BE |
| TC-FA-FAAC-487 | E2E | TC-FA-FAAC-E2E-149-changelog-filter-struktur-opsi-dan-multi-select | FE+BE |
| TC-FA-FAAC-488 | E2E | TC-FA-FAAC-E2E-149-changelog-filter-struktur-opsi-dan-multi-select | FE+BE |
| TC-FA-FAAC-489 | E2E | TC-FA-FAAC-E2E-150-changelog-filter-range-kombinasi-dan-chip | FE+BE |
| TC-FA-FAAC-490 | E2E | TC-FA-FAAC-E2E-150-changelog-filter-range-kombinasi-dan-chip | FE+BE |
| TC-FA-FAAC-491 | E2E | TC-FA-FAAC-E2E-150-changelog-filter-range-kombinasi-dan-chip | FE+BE |
| TC-FA-FAAC-492 | E2E | TC-FA-FAAC-E2E-150-changelog-filter-range-kombinasi-dan-chip | FE+BE |
| TC-FA-FAAC-493 | E2E | TC-FA-FAAC-E2E-150-changelog-filter-range-kombinasi-dan-chip | FE+BE |
| TC-FA-FAAC-494 | E2E | TC-FA-FAAC-E2E-150-changelog-filter-range-kombinasi-dan-chip | FE+BE |
| TC-FA-FAAC-495 | E2E | TC-FA-FAAC-E2E-151-changelog-search-filter-kombinasi-dan-hasil-kosong | FE+BE |
| TC-FA-FAAC-496 | E2E | TC-FA-FAAC-E2E-151-changelog-search-filter-kombinasi-dan-hasil-kosong | FE+BE |
| TC-FA-FAAC-497 | E2E | TC-FA-FAAC-E2E-151-changelog-search-filter-kombinasi-dan-hasil-kosong | FE+BE |
| TC-FA-FAAC-498 | E2E | TC-FA-FAAC-E2E-151-changelog-search-filter-kombinasi-dan-hasil-kosong | FE+BE |
| TC-FA-FAAC-499 | E2E | TC-FA-FAAC-E2E-152-changelog-sort-3-state-dan-setup-column-screening | FE+BE |
| TC-FA-FAAC-500 | E2E | TC-FA-FAAC-E2E-157-changelog-sort-3-state-kolom-teks | FE+BE |
| TC-FA-FAAC-501 | E2E | TC-FA-FAAC-E2E-152-changelog-sort-3-state-dan-setup-column-screening | FE+BE |
| TC-FA-FAAC-502 | E2E | TC-FA-FAAC-E2E-152-changelog-sort-3-state-dan-setup-column-screening | FE+BE |
| TC-FA-FAAC-503 | E2E | TC-FA-FAAC-E2E-152-changelog-sort-3-state-dan-setup-column-screening | FE+BE |
| TC-FA-FAAC-504 | E2E | TC-FA-FAAC-E2E-153-changelog-setup-column-ceklis-geser-dan-pin | FE+BE |
| TC-FA-FAAC-505 | E2E | TC-FA-FAAC-E2E-153-changelog-setup-column-ceklis-geser-dan-pin | FE+BE |
| TC-FA-FAAC-506 | E2E | TC-FA-FAAC-E2E-153-changelog-setup-column-ceklis-geser-dan-pin | FE+BE |
| TC-FA-FAAC-507 | E2E | TC-FA-FAAC-E2E-154-changelog-setup-column-reset-tutup-dan-persistensi | FE+BE |
| TC-FA-FAAC-508 | E2E | TC-FA-FAAC-E2E-154-changelog-setup-column-reset-tutup-dan-persistensi | FE+BE |
| TC-FA-FAAC-509 | E2E | TC-FA-FAAC-E2E-154-changelog-setup-column-reset-tutup-dan-persistensi | FE+BE |
| TC-FA-FAAC-510 | E2E | TC-FA-FAAC-E2E-154-changelog-setup-column-reset-tutup-dan-persistensi | FE+BE |
| TC-FA-FAAC-511 | E2E | TC-FA-FAAC-E2E-141-picker-assign-search-dan-kolom | FE+BE |
| TC-FA-FAAC-512 | E2E | TC-FA-FAAC-E2E-141-picker-assign-search-dan-kolom | FE+BE |
| TC-FA-FAAC-513 | E2E | TC-FA-FAAC-E2E-141-picker-assign-search-dan-kolom | FE+BE |
| TC-FA-FAAC-514 | E2E | TC-FA-FAAC-E2E-141-picker-assign-search-dan-kolom | FE+BE |
| TC-FA-FAAC-515 | E2E | TC-FA-FAAC-E2E-141-picker-assign-search-dan-kolom | FE+BE |
| TC-FA-FAAC-516 | E2E | TC-FA-FAAC-E2E-142-picker-assign-filter-dan-sort-label | FE+BE |
| TC-FA-FAAC-517 | E2E | TC-FA-FAAC-E2E-142-picker-assign-filter-dan-sort-label | FE+BE |
| TC-FA-FAAC-518 | E2E | TC-FA-FAAC-E2E-142-picker-assign-filter-dan-sort-label | FE+BE |
| TC-FA-FAAC-519 | E2E | TC-FA-FAAC-E2E-142-picker-assign-filter-dan-sort-label | FE+BE |
| TC-FA-FAAC-520 | E2E | TC-FA-FAAC-E2E-143-picker-assign-sort-kolom | FE+BE |
| TC-FA-FAAC-521 | E2E | TC-FA-FAAC-E2E-143-picker-assign-sort-kolom | FE+BE |
| TC-FA-FAAC-522 | E2E | TC-FA-FAAC-E2E-143-picker-assign-sort-kolom | FE+BE |
| TC-FA-FAAC-523 | E2E | TC-FA-FAAC-E2E-143-picker-assign-sort-kolom | FE+BE |
| TC-FA-FAAC-524 | E2E | TC-FA-FAAC-E2E-142-picker-assign-filter-dan-sort-label | FE+BE |
| TC-FA-FAAC-525 | E2E | TC-FA-FAAC-E2E-141-picker-assign-search-dan-kolom | FE+BE |
| TC-FA-FAAC-526 | E2E | TC-FA-FAAC-E2E-158-log-create-asset-class-tiga-surface-dan-use-recommended | FE+BE |
| TC-FA-FAAC-527 | E2E | TC-FA-FAAC-E2E-158-log-create-asset-class-tiga-surface-dan-use-recommended | FE+BE |
| TC-FA-FAAC-528 | E2E | TC-FA-FAAC-E2E-176-log-edit-field-akun-dan-class-code-tiga-surface | FE+BE |
| TC-FA-FAAC-529 | E2E | TC-FA-FAAC-E2E-176-log-edit-field-akun-dan-class-code-tiga-surface | FE+BE |
| TC-FA-FAAC-530 | E2E | TC-FA-FAAC-E2E-176-log-edit-field-akun-dan-class-code-tiga-surface | FE+BE |
| TC-FA-FAAC-531 | E2E | TC-FA-FAAC-E2E-159-log-edit-unit-description-dan-threshold | FE+BE |
| TC-FA-FAAC-532 | E2E | TC-FA-FAAC-E2E-159-log-edit-unit-description-dan-threshold | FE+BE |
| TC-FA-FAAC-533 | E2E | TC-FA-FAAC-E2E-105-versi-scheduled-job-penerapan-otomatis | FE+BE |
| TC-FA-FAAC-534 | E2E | TC-FA-FAAC-E2E-161-log-status-delete-dan-penjadwalan-versi | FE+BE |
| TC-FA-FAAC-535 | E2E | TC-FA-FAAC-E2E-161-log-status-delete-dan-penjadwalan-versi | FE+BE |
| TC-FA-FAAC-536 | E2E | TC-FA-FAAC-E2E-161-log-status-delete-dan-penjadwalan-versi | FE+BE |
| TC-FA-FAAC-537 | E2E | TC-FA-FAAC-E2E-175-log-pembatalan-versi-scheduled-dan-last-posted-exported | FE+BE |
| TC-FA-FAAC-538 | E2E | TC-FA-FAAC-E2E-166-log-absence-tidak-ada-entri | FE+BE |
| TC-FA-FAAC-538 | E2E | TC-FA-FAAC-E2E-175-log-pembatalan-versi-scheduled-dan-last-posted-exported | FE+BE |
| TC-FA-FAAC-539 | E2E | TC-FA-FAAC-E2E-166-log-absence-tidak-ada-entri | FE+BE |
| TC-FA-FAAC-540 | E2E | TC-FA-FAAC-E2E-166-log-absence-tidak-ada-entri | FE+BE |
| TC-FA-FAAC-541 | E2E | TC-FA-FAAC-E2E-162-log-assign-unassign-asset-name-satu-per-satu | FE+BE |
| TC-FA-FAAC-542 | E2E | TC-FA-FAAC-E2E-162-log-assign-unassign-asset-name-satu-per-satu | FE+BE |
| TC-FA-FAAC-543 | E2E | TC-FA-FAAC-E2E-162-log-assign-unassign-asset-name-satu-per-satu | FE+BE |
| TC-FA-FAAC-544 | E2E | TC-FA-FAAC-E2E-163-log-unassign-dan-move-system-activity-log | FE+BE |
| TC-FA-FAAC-545 | E2E | TC-FA-FAAC-E2E-163-log-unassign-dan-move-system-activity-log | FE+BE |
| TC-FA-FAAC-546 | E2E | TC-FA-FAAC-E2E-163-log-unassign-dan-move-system-activity-log | FE+BE |
| TC-FA-FAAC-547 | E2E | TC-FA-FAAC-E2E-164-log-assign-via-move-dan-assign-tiga-asset-name | FE+BE |
| TC-FA-FAAC-548 | E2E | TC-FA-FAAC-E2E-164-log-assign-via-move-dan-assign-tiga-asset-name | FE+BE |
| TC-FA-FAAC-549 | E2E | TC-FA-FAAC-E2E-165-log-move-massal-dan-unassign-massal-campuran | FE+BE |
| TC-FA-FAAC-550 | E2E | TC-FA-FAAC-E2E-165-log-move-massal-dan-unassign-massal-campuran | FE+BE |
| TC-FA-FAAC-551 | E2E | TC-FA-FAAC-E2E-166-log-absence-tidak-ada-entri | FE+BE |
| TC-FA-FAAC-552 | E2E | TC-FA-FAAC-E2E-167-log-request-api-langsung-tiga-surface | FE+BE |
| TC-FA-FAAC-553 | E2E | TC-FA-FAAC-E2E-167-log-request-api-langsung-tiga-surface | FE+BE |
| TC-FA-FAAC-554 | E2E | TC-FA-FAAC-E2E-167-log-request-api-langsung-tiga-surface | FE+BE |
| TC-FA-FAAC-555 | E2E | TC-FA-FAAC-E2E-168-sinkron-chart-of-accounts-alert-dan-used-by | FE+BE |
| TC-FA-FAAC-556 | E2E | TC-FA-FAAC-E2E-168-sinkron-chart-of-accounts-alert-dan-used-by | FE+BE |
| TC-FA-FAAC-557 | E2E | TC-FA-FAAC-E2E-168-sinkron-chart-of-accounts-alert-dan-used-by | FE+BE |
| TC-FA-FAAC-558 | E2E | TC-FA-FAAC-E2E-168-sinkron-chart-of-accounts-alert-dan-used-by | FE+BE |
| TC-FA-FAAC-559 | E2E | TC-FA-FAAC-E2E-170-sinkron-tabel-pilihan-move-dan-used-by-a | FE+BE |
| TC-FA-FAAC-560 | E2E | TC-FA-FAAC-E2E-170-sinkron-tabel-pilihan-move-dan-used-by-a | FE+BE |
| TC-FA-FAAC-561 | E2E | TC-FA-FAAC-E2E-168-sinkron-chart-of-accounts-alert-dan-used-by | FE+BE |
| TC-FA-FAAC-562 | E2E | TC-FA-FAAC-E2E-171-sinkron-tabel-pilihan-move-dan-used-by-b | FE+BE |
| TC-FA-FAAC-563 | E2E | TC-FA-FAAC-E2E-171-sinkron-tabel-pilihan-move-dan-used-by-b | FE+BE |
| TC-FA-FAAC-564 | E2E | TC-FA-FAAC-E2E-171-sinkron-tabel-pilihan-move-dan-used-by-b | FE+BE |
| TC-FA-FAAC-565 | E2E | TC-FA-FAAC-E2E-170-sinkron-tabel-pilihan-move-dan-used-by-a | FE+BE |
| TC-FA-FAAC-566 | E2E | TC-FA-FAAC-E2E-171-sinkron-tabel-pilihan-move-dan-used-by-b | FE+BE |
| TC-FA-FAAC-567 | E2E | TC-FA-FAAC-E2E-168-sinkron-chart-of-accounts-alert-dan-used-by | FE+BE |
| TC-FA-FAAC-568 | E2E | TC-FA-FAAC-E2E-169-sinkron-tax-depreciation-class-dan-used-by | FE+BE |
| TC-FA-FAAC-569 | E2E | TC-FA-FAAC-E2E-169-sinkron-tax-depreciation-class-dan-used-by | FE+BE |
| TC-FA-FAAC-570 | E2E | TC-FA-FAAC-E2E-172-sinkron-asset-name-tabel-dan-banner-a | FE+BE |
| TC-FA-FAAC-571 | E2E | TC-FA-FAAC-E2E-172-sinkron-asset-name-tabel-dan-banner-a | FE+BE |
| TC-FA-FAAC-572 | E2E | TC-FA-FAAC-E2E-172-sinkron-asset-name-tabel-dan-banner-a | FE+BE |
| TC-FA-FAAC-573 | E2E | TC-FA-FAAC-E2E-172-sinkron-asset-name-tabel-dan-banner-a | FE+BE |
| TC-FA-FAAC-574 | E2E | TC-FA-FAAC-E2E-173-sinkron-asset-name-tabel-dan-banner-b | FE+BE |
| TC-FA-FAAC-575 | E2E | TC-FA-FAAC-E2E-173-sinkron-asset-name-tabel-dan-banner-b | FE+BE |
| TC-FA-FAAC-576 | E2E | TC-FA-FAAC-E2E-173-sinkron-asset-name-tabel-dan-banner-b | FE+BE |
| TC-FA-FAAC-577 | E2E | TC-FA-FAAC-E2E-173-sinkron-asset-name-tabel-dan-banner-b | FE+BE |
| TC-FA-FAAC-578 | E2E | TC-FA-FAAC-E2E-166-log-absence-tidak-ada-entri | FE+BE |
| TC-FA-FAAC-579 | E2E | TC-FA-FAAC-E2E-174-sinkron-asset-name-popup-dan-daftar | FE+BE |
| TC-FA-FAAC-580 | E2E | TC-FA-FAAC-E2E-174-sinkron-asset-name-popup-dan-daftar | FE+BE |
| TC-FA-FAAC-581 | E2E | TC-FA-FAAC-E2E-174-sinkron-asset-name-popup-dan-daftar | FE+BE |
| TC-FA-FAAC-582 | E2E | TC-FA-FAAC-E2E-174-sinkron-asset-name-popup-dan-daftar | FE+BE |
| TC-FA-FAAC-583 | E2E | TC-FA-FAAC-E2E-170-sinkron-tabel-pilihan-move-dan-used-by-a | FE+BE |
| TC-FA-FAAC-584 | E2E | TC-FA-FAAC-E2E-168-sinkron-chart-of-accounts-alert-dan-used-by | FE+BE |
| TC-FA-FAAC-585 | E2E | TC-FA-FAAC-E2E-174-sinkron-asset-name-popup-dan-daftar | FE+BE |
| TC-FA-FAAC-586 | E2E | TC-FA-FAAC-E2E-171-sinkron-tabel-pilihan-move-dan-used-by-b | FE+BE |
| TC-FA-FAAC-587 | E2E | TC-FA-FAAC-E2E-019-navigasi-sidebar-tab-asset-class-dan-breadcrumb-dari-detail | FE+BE |
| TC-FA-FAAC-588 | E2E | TC-FA-FAAC-E2E-170-sinkron-tabel-pilihan-move-dan-used-by-a | FE+BE |
| TC-FA-FAAC-589 | E2E | TC-FA-FAAC-E2E-025-role-matrix-menu-accounting-akses-langsung-dan-alert-per-role | FE+BE |
| TC-FA-FAAC-590 | E2E | TC-FA-FAAC-E2E-177-state-tenant-write-lockdown-suspended-expired | FE+BE |
| TC-FA-FAAC-591 | E2E | TC-FA-FAAC-E2E-177-state-tenant-write-lockdown-suspended-expired | FE+BE |
| TC-FA-FAAC-592 | E2E | TC-FA-FAAC-E2E-177-state-tenant-write-lockdown-suspended-expired | FE+BE |
| TC-FA-FAAC-593 | E2E | TC-FA-FAAC-E2E-177-state-tenant-write-lockdown-suspended-expired | FE+BE |
| TC-FA-FAAC-594 | E2E | TC-FA-FAAC-E2E-178-state-tenant-baca-tetap-tersedia | FE+BE |
| TC-FA-FAAC-595 | E2E | TC-FA-FAAC-E2E-035-role-matrix-negatif-read-only-permintaan-langsung-ke-server | FE+BE |
| TC-FA-FAAC-595 | E2E | TC-FA-FAAC-E2E-193-log-absence-request-langsung-read-only-ditolak-403 | FE+BE |
| TC-FA-FAAC-596 | E2E | TC-FA-FAAC-E2E-035-role-matrix-negatif-read-only-permintaan-langsung-ke-server | FE+BE |
| TC-FA-FAAC-596 | E2E | TC-FA-FAAC-E2E-193-log-absence-request-langsung-read-only-ditolak-403 | FE+BE |
| TC-FA-FAAC-597 | E2E | TC-FA-FAAC-E2E-035-role-matrix-negatif-read-only-permintaan-langsung-ke-server | FE+BE |
| TC-FA-FAAC-597 | E2E | TC-FA-FAAC-E2E-193-log-absence-request-langsung-read-only-ditolak-403 | FE+BE |
| TC-FA-FAAC-598 | E2E | TC-FA-FAAC-E2E-034-role-matrix-negatif-create-update-delete-only-permintaan-langsung-ke-server | FE+BE |
| TC-FA-FAAC-598 | E2E | TC-FA-FAAC-E2E-194-log-absence-request-langsung-create-update-delete-only-ditolak-403 | FE+BE |
| TC-FA-FAAC-599 | E2E | TC-FA-FAAC-E2E-034-role-matrix-negatif-create-update-delete-only-permintaan-langsung-ke-server | FE+BE |
| TC-FA-FAAC-599 | E2E | TC-FA-FAAC-E2E-194-log-absence-request-langsung-create-update-delete-only-ditolak-403 | FE+BE |
| TC-FA-FAAC-600 | E2E | TC-FA-FAAC-E2E-034-role-matrix-negatif-create-update-delete-only-permintaan-langsung-ke-server | FE+BE |
| TC-FA-FAAC-600 | E2E | TC-FA-FAAC-E2E-194-log-absence-request-langsung-create-update-delete-only-ditolak-403 | FE+BE |
| TC-FA-FAAC-601 | E2E | TC-FA-FAAC-E2E-180-defense-in-depth-request-langsung-ditolak-guard-server | FE+BE |
| TC-FA-FAAC-601 | E2E | TC-FA-FAAC-E2E-196-log-absence-request-langsung-asset-class-ditolak-server | FE+BE |
| TC-FA-FAAC-602 | E2E | TC-FA-FAAC-E2E-180-defense-in-depth-request-langsung-ditolak-guard-server | FE+BE |
| TC-FA-FAAC-602 | E2E | TC-FA-FAAC-E2E-196-log-absence-request-langsung-asset-class-ditolak-server | FE+BE |
| TC-FA-FAAC-603 | E2E | TC-FA-FAAC-E2E-180-defense-in-depth-request-langsung-ditolak-guard-server | FE+BE |
| TC-FA-FAAC-603 | E2E | TC-FA-FAAC-E2E-196-log-absence-request-langsung-asset-class-ditolak-server | FE+BE |
| TC-FA-FAAC-604 | E2E | TC-FA-FAAC-E2E-180-defense-in-depth-request-langsung-ditolak-guard-server | FE+BE |
| TC-FA-FAAC-604 | E2E | TC-FA-FAAC-E2E-196-log-absence-request-langsung-asset-class-ditolak-server | FE+BE |
| TC-FA-FAAC-605 | E2E | TC-FA-FAAC-E2E-180-defense-in-depth-request-langsung-ditolak-guard-server | FE+BE |
| TC-FA-FAAC-605 | E2E | TC-FA-FAAC-E2E-195-log-absence-request-langsung-asset-name-ditolak-server | FE+BE |
| TC-FA-FAAC-606 | E2E | TC-FA-FAAC-E2E-062-create-residual-value-unit-amount-dan-klik-ganda-submit | FE+BE |
| TC-FA-FAAC-607 | E2E | TC-FA-FAAC-E2E-111-klik-ganda-apply-dan-create-recommended-hanya-satu-permintaan | FE+BE |
| TC-FA-FAAC-608 | E2E | TC-FA-FAAC-E2E-167-log-request-api-langsung-tiga-surface | FE+BE |
| TC-FA-FAAC-609 | E2E | TC-FA-FAAC-E2E-167-log-request-api-langsung-tiga-surface | FE+BE |
| TC-FA-FAAC-610 | E2E | TC-FA-FAAC-E2E-167-log-request-api-langsung-tiga-surface | FE+BE |
| TC-FA-FAAC-611 | E2E | TC-FA-FAAC-E2E-179-state-tenant-aktivitas-sistem-tidak-diblokir | FE+BE |
| TC-FA-FAAC-612 | E2E | TC-FA-FAAC-E2E-026-role-matrix-negatif-read-only | FE+BE |
| TC-FA-FAAC-613 | E2E | TC-FA-FAAC-E2E-028-role-matrix-positif-update-only-assign-move-unassign-dan-manage-delete | FE+BE |
| TC-FA-FAAC-614 | E2E | TC-FA-FAAC-E2E-027-role-matrix-negatif-delete-only-create-only-dan-read-manage-tab-asset-names | FE+BE |
| TC-FA-FAAC-615 | E2E | TC-FA-FAAC-E2E-027-role-matrix-negatif-delete-only-create-only-dan-read-manage-tab-asset-names | FE+BE |
| TC-FA-FAAC-616 | E2E | TC-FA-FAAC-E2E-027-role-matrix-negatif-delete-only-create-only-dan-read-manage-tab-asset-names | FE+BE |
| TC-FA-FAAC-617 | E2E | TC-FA-FAAC-E2E-028-role-matrix-positif-update-only-assign-move-unassign-dan-manage-delete | FE+BE |
| TC-FA-FAAC-618 | E2E | TC-FA-FAAC-E2E-181-defense-in-depth-request-langsung-tanpa-hak-update-403 | FE+BE |
| TC-FA-FAAC-618 | E2E | TC-FA-FAAC-E2E-193-log-absence-request-langsung-read-only-ditolak-403 | FE+BE |
| TC-FA-FAAC-619 | E2E | TC-FA-FAAC-E2E-181-defense-in-depth-request-langsung-tanpa-hak-update-403 | FE+BE |
| TC-FA-FAAC-619 | E2E | TC-FA-FAAC-E2E-194-log-absence-request-langsung-create-update-delete-only-ditolak-403 | FE+BE |
| TC-FA-FAAC-620 | E2E | TC-FA-FAAC-E2E-181-defense-in-depth-request-langsung-tanpa-hak-update-403 | FE+BE |
| TC-FA-FAAC-620 | E2E | TC-FA-FAAC-E2E-194-log-absence-request-langsung-create-update-delete-only-ditolak-403 | FE+BE |
| TC-FA-FAAC-621 | E2E | TC-FA-FAAC-E2E-180-defense-in-depth-request-langsung-ditolak-guard-server | FE+BE |
| TC-FA-FAAC-621 | E2E | TC-FA-FAAC-E2E-195-log-absence-request-langsung-asset-name-ditolak-server | FE+BE |
| TC-FA-FAAC-622 | E2E | TC-FA-FAAC-E2E-192-state-tenant-write-lockdown-asset-name-suspended-expired | FE+BE |
| TC-FA-FAAC-623 | E2E | TC-FA-FAAC-E2E-192-state-tenant-write-lockdown-asset-name-suspended-expired | FE+BE |
| TC-FA-FAAC-624 | E2E | TC-FA-FAAC-E2E-192-state-tenant-write-lockdown-asset-name-suspended-expired | FE+BE |
| TC-FA-FAAC-625 | E2E | TC-FA-FAAC-E2E-069-assign-klik-ganda-dan-spinner | FE+BE |
| TC-FA-FAAC-626 | E2E | TC-FA-FAAC-E2E-078-move-massal-tanpa-aset-aktif-bulan-lampau-klik-ganda-dan-spinner | FE+BE |
| TC-FA-FAAC-627 | E2E | TC-FA-FAAC-E2E-069-assign-klik-ganda-dan-spinner | FE+BE |
| TC-FA-FAAC-628 | E2E | TC-FA-FAAC-E2E-078-move-massal-tanpa-aset-aktif-bulan-lampau-klik-ganda-dan-spinner | FE+BE |
| TC-FA-FAAC-629 | E2E | TC-FA-FAAC-E2E-178-state-tenant-baca-tetap-tersedia | FE+BE |
| TC-FA-FAAC-630 | E2E | TC-FA-FAAC-E2E-178-state-tenant-baca-tetap-tersedia | FE+BE |
| TC-FA-FAAC-631 | E2E | TC-FA-FAAC-E2E-178-state-tenant-baca-tetap-tersedia | FE+BE |
| TC-FA-FAAC-632 | E2E | TC-FA-FAAC-E2E-188-volume-selection-limit-dan-5000-baris | FE+BE |
| TC-FA-FAAC-633 | E2E | TC-FA-FAAC-E2E-026-role-matrix-negatif-read-only | FE+BE |
| TC-FA-FAAC-634 | E2E | TC-FA-FAAC-E2E-190-edge-destination-move-satu-class-per-asset-name-duplicate-dan-recommended | FE+BE |
| TC-FA-FAAC-635 | E2E | TC-FA-FAAC-E2E-190-edge-destination-move-satu-class-per-asset-name-duplicate-dan-recommended | FE+BE |
| TC-FA-FAAC-636 | E2E | TC-FA-FAAC-E2E-068-assign-berhasil-satu-banyak-dan-asset-name-baru | FE+BE |
| TC-FA-FAAC-637 | E2E | TC-FA-FAAC-E2E-190-edge-destination-move-satu-class-per-asset-name-duplicate-dan-recommended | FE+BE |
| TC-FA-FAAC-638 | E2E | TC-FA-FAAC-E2E-189-siklus-hidup-asset-name-dan-deactivate | FE+BE |
| TC-FA-FAAC-639 | E2E | TC-FA-FAAC-E2E-189-siklus-hidup-asset-name-dan-deactivate | FE+BE |
| TC-FA-FAAC-640 | E2E | TC-FA-FAAC-E2E-189-siklus-hidup-asset-name-dan-deactivate | FE+BE |
| TC-FA-FAAC-641 | E2E | TC-FA-FAAC-E2E-189-siklus-hidup-asset-name-dan-deactivate | FE+BE |
| TC-FA-FAAC-642 | E2E | TC-FA-FAAC-E2E-189-siklus-hidup-asset-name-dan-deactivate | FE+BE |
| TC-FA-FAAC-643 | E2E | TC-FA-FAAC-E2E-190-edge-destination-move-satu-class-per-asset-name-duplicate-dan-recommended | FE+BE |
| TC-FA-FAAC-644 | E2E | TC-FA-FAAC-E2E-006-use-recommended-classes-create-berhasil | FE+BE |
| TC-FA-FAAC-645 | E2E | TC-FA-FAAC-E2E-044-create-field-dinamis-method | FE+BE |
| TC-FA-FAAC-646 | E2E | TC-FA-FAAC-E2E-003-menu-accounting-per-plan-dan-akses-url-starter | FE+BE |
| TC-FA-FAAC-647 | E2E | TC-FA-FAAC-E2E-056-clear-field-detail-mode-create | FE+BE |
| TC-FA-FAAC-648 | E2E | TC-FA-FAAC-E2E-180-defense-in-depth-request-langsung-ditolak-guard-server | FE+BE |
| TC-FA-FAAC-649 | E2E | TC-FA-FAAC-E2E-180-defense-in-depth-request-langsung-ditolak-guard-server | FE+BE |
| TC-FA-FAAC-650 | E2E | TC-FA-FAAC-E2E-169-sinkron-tax-depreciation-class-dan-used-by | FE+BE |
| TC-FA-FAAC-651 | E2E | TC-FA-FAAC-E2E-169-sinkron-tax-depreciation-class-dan-used-by | FE+BE |
| TC-FA-FAAC-652 | E2E | TC-FA-FAAC-E2E-169-sinkron-tax-depreciation-class-dan-used-by | FE+BE |
| TC-FA-FAAC-654 | E2E | TC-FA-FAAC-E2E-084-mode-create-draft-asset-name-submit | FE+BE |
| TC-FA-FAAC-655 | E2E | TC-FA-FAAC-E2E-084-mode-create-draft-asset-name-submit | FE+BE |
| TC-FA-FAAC-656 | E2E | TC-FA-FAAC-E2E-129-download-isi-berkas-csv-xlsx | FE+BE |
| TC-FA-FAAC-657 | E2E | TC-FA-FAAC-E2E-081-mode-create-draft-asset-name-screening-dan-pemilihan-draft | FE+BE |
| TC-FA-FAAC-658 | E2E | TC-FA-FAAC-E2E-188-volume-selection-limit-dan-5000-baris | FE+BE |
| TC-FA-FAAC-659 | E2E | TC-FA-FAAC-E2E-054-unsaved-changes-form-edit-breadcrumb-dan-nilai-kembali | FE+BE |
| TC-FA-FAAC-660 | E2E | TC-FA-FAAC-E2E-054-unsaved-changes-form-edit-breadcrumb-dan-nilai-kembali | FE+BE |
| TC-FA-FAAC-661 | E2E | TC-FA-FAAC-E2E-053-unsaved-changes-form-create-breadcrumb-dan-menu-sidebar | FE+BE |
| TC-FA-FAAC-662 | E2E | TC-FA-FAAC-E2E-055-unsaved-changes-form-edit-back-browser-dan-clear-field-edit | FE+BE |
| TC-FA-FAAC-663 | E2E | TC-FA-FAAC-E2E-054-unsaved-changes-form-edit-breadcrumb-dan-nilai-kembali | FE+BE |
| TC-FA-FAAC-664 | E2E | TC-FA-FAAC-E2E-063-unsaved-changes-muat-ulang-halaman-konfirmasi-bawaan-browser | FE+BE |
| TC-FA-FAAC-665 | E2E | TC-FA-FAAC-E2E-063-unsaved-changes-muat-ulang-halaman-konfirmasi-bawaan-browser | FE+BE |
| TC-FA-FAAC-666 | E2E | TC-FA-FAAC-E2E-063-unsaved-changes-muat-ulang-halaman-konfirmasi-bawaan-browser | FE+BE |
| TC-FA-FAAC-667 | E2E | TC-FA-FAAC-E2E-094-bulk-status-blokir-batal-dan-collapse | FE+BE |
| TC-FA-FAAC-668 | E2E | TC-FA-FAAC-E2E-094-bulk-status-blokir-batal-dan-collapse | FE+BE |
| TC-FA-FAAC-669 | E2E | TC-FA-FAAC-E2E-187-multi-sesi-dua-admin-race | FE+BE |
| TC-FA-FAAC-670 | E2E | TC-FA-FAAC-E2E-002-tampilan-tabel-urutan-link-asset-names-dan-format-ringkasan | FE+BE |
| TC-FA-FAAC-671 | E2E | TC-FA-FAAC-E2E-002-tampilan-tabel-urutan-link-asset-names-dan-format-ringkasan | FE+BE |
| TC-FA-FAAC-672 | E2E | TC-FA-FAAC-E2E-024-role-matrix-detail-create-manage-gabungan-dan-default-user | FE+BE |
| TC-FA-FAAC-673 | E2E | TC-FA-FAAC-E2E-188-volume-selection-limit-dan-5000-baris | FE+BE |
| TC-FA-FAAC-674 | E2E | TC-FA-FAAC-E2E-086-duplicate-nilai-sumber-tidak-valid-dan-versi-scheduled | FE+BE |
| TC-FA-FAAC-675 | E2E | TC-FA-FAAC-E2E-159-log-edit-unit-description-dan-threshold | FE+BE |
| TC-FA-FAAC-676 | E2E | TC-FA-FAAC-E2E-159-log-edit-unit-description-dan-threshold | FE+BE |
| TC-FA-FAAC-677 | E2E | TC-FA-FAAC-E2E-159-log-edit-unit-description-dan-threshold | FE+BE |
| TC-FA-FAAC-678 | E2E | TC-FA-FAAC-E2E-159-log-edit-unit-description-dan-threshold | FE+BE |
| TC-FA-FAAC-679 | E2E | TC-FA-FAAC-E2E-155-changelog-download-csv-xlsx | FE+BE |
| TC-FA-FAAC-680 | E2E | TC-FA-FAAC-E2E-155-changelog-download-csv-xlsx | FE+BE |
| TC-FA-FAAC-681 | E2E | TC-FA-FAAC-E2E-155-changelog-download-csv-xlsx | FE+BE |
| TC-FA-FAAC-682 | E2E | TC-FA-FAAC-E2E-025-role-matrix-menu-accounting-akses-langsung-dan-alert-per-role | FE+BE |
| TC-FA-FAAC-683 | E2E | TC-FA-FAAC-E2E-025-role-matrix-menu-accounting-akses-langsung-dan-alert-per-role | FE+BE |
| TC-FA-FAAC-684 | E2E | TC-FA-FAAC-E2E-144-badge-category-tab-asset-names-dan-truncate | FE+BE |
| TC-FA-FAAC-685 | E2E | TC-FA-FAAC-E2E-145-badge-label-current-class-dan-teks-panjang | FE+BE |
| TC-FA-FAAC-686 | E2E | TC-FA-FAAC-E2E-181-defense-in-depth-request-langsung-tanpa-hak-update-403 | FE+BE |
| TC-FA-FAAC-686 | E2E | TC-FA-FAAC-E2E-193-log-absence-request-langsung-read-only-ditolak-403 | FE+BE |
| TC-FA-FAAC-687 | E2E | TC-FA-FAAC-E2E-187-multi-sesi-dua-admin-race | FE+BE |
| TC-FA-FAAC-688 | E2E | TC-FA-FAAC-E2E-071-assign-campuran-effective-from-dan-pratinjau | FE+BE |
| TC-FA-FAAC-689 | E2E | TC-FA-FAAC-E2E-041-create-validasi-input-digit-desimal | FE+BE |
| TC-FA-FAAC-690 | E2E | TC-FA-FAAC-E2E-041-create-validasi-input-digit-desimal | FE+BE |
| TC-FA-FAAC-691 | E2E | TC-FA-FAAC-E2E-041-create-validasi-input-digit-desimal | FE+BE |
| TC-FA-FAAC-692 | E2E | TC-FA-FAAC-E2E-144-badge-category-tab-asset-names-dan-truncate | FE+BE |
| TC-FA-FAAC-693 | E2E | TC-FA-FAAC-E2E-144-badge-category-tab-asset-names-dan-truncate | FE+BE |
| TC-FA-FAAC-694 | E2E | TC-FA-FAAC-E2E-145-badge-label-current-class-dan-teks-panjang | FE+BE |
| TC-FA-FAAC-695 | E2E | TC-FA-FAAC-E2E-145-badge-label-current-class-dan-teks-panjang | FE+BE |
| TC-FA-FAAC-696 | E2E | TC-FA-FAAC-E2E-056-clear-field-detail-mode-create | FE+BE |
| TC-FA-FAAC-697 | E2E | TC-FA-FAAC-E2E-055-unsaved-changes-form-edit-back-browser-dan-clear-field-edit | FE+BE |
| TC-FA-FAAC-698 | E2E | TC-FA-FAAC-E2E-057-dialog-form-backdrop-tidak-menutup-assign-move-dan-apply-changes | FE+BE |
| TC-FA-FAAC-699 | E2E | TC-FA-FAAC-E2E-005-use-recommended-classes-validasi-baris-dan-tutup-dialog | FE+BE |
| TC-FA-FAAC-700 | E2E | TC-FA-FAAC-E2E-042-create-validasi-tempel-teks-berpemisah-desimal | FE+BE |
| TC-FA-FAAC-701 | E2E | TC-FA-FAAC-E2E-131-hover-identifier-dan-format-nominal | FE+BE |
| TC-FA-FAAC-702 | E2E | TC-FA-FAAC-E2E-125-paginasi-tabel-asset-class | FE+BE |
| TC-FA-FAAC-703 | E2E | TC-FA-FAAC-E2E-089-delete-race-dan-halaman-terakhir | FE+BE |
| TC-FA-FAAC-704 | E2E | TC-FA-FAAC-E2E-131-hover-identifier-dan-format-nominal | FE+BE |
| TC-FA-FAAC-705 | E2E | TC-FA-FAAC-E2E-114-search-siklus-search-box-trim-dan-nominal-berdesimal | FE+BE |
| TC-FA-FAAC-706 | E2E | TC-FA-FAAC-E2E-133-filter-capitalization-threshold-nominal-berdesimal | FE+BE |
| TC-FA-FAAC-707 | E2E | TC-FA-FAAC-E2E-131-hover-identifier-dan-format-nominal | FE+BE |
| TC-FA-FAAC-708 | E2E | TC-FA-FAAC-E2E-058-dialog-form-ikon-x-dan-esc-memunculkan-unsaved-changes | FE+BE |
| TC-FA-FAAC-709 | E2E | TC-FA-FAAC-E2E-058-dialog-form-ikon-x-dan-esc-memunculkan-unsaved-changes | FE+BE |
| TC-FA-FAAC-710 | E2E | TC-FA-FAAC-E2E-005-use-recommended-classes-validasi-baris-dan-tutup-dialog | FE+BE |
| TC-FA-FAAC-711 | E2E | TC-FA-FAAC-E2E-160-log-edit-format-nominal-dan-total-estimated-units | FE+BE |
| TC-FA-FAAC-712 | E2E | TC-FA-FAAC-E2E-067-assign-batal-tutup-dan-asset-class-inactive | FE+BE |
| TC-FA-FAAC-713 | E2E | TC-FA-FAAC-E2E-160-log-edit-format-nominal-dan-total-estimated-units | FE+BE |
| TC-FA-FAAC-714 | E2E | TC-FA-FAAC-E2E-042-create-validasi-tempel-teks-berpemisah-desimal | FE+BE |
| TC-FA-FAAC-715 | E2E | TC-FA-FAAC-E2E-160-log-edit-format-nominal-dan-total-estimated-units | FE+BE |
| TC-FA-FAAC-716 | E2E | TC-FA-FAAC-E2E-131-hover-identifier-dan-format-nominal | FE+BE |
| TC-FA-FAAC-717 | E2E | TC-FA-FAAC-E2E-160-log-edit-format-nominal-dan-total-estimated-units | FE+BE |
| TC-FA-FAAC-718 | E2E | TC-FA-FAAC-E2E-155-changelog-download-csv-xlsx | FE+BE |
| TC-FA-FAAC-719 | E2E | TC-FA-FAAC-E2E-207-create-end-of-life-treatment-commercial-opsi-nilai-awal-dan-clear-field | FE+BE |
| TC-FA-FAAC-720 | E2E | TC-FA-FAAC-E2E-209-create-declining-balance-menyimpan-end-of-life-treatment-dan-duplicate | FE+BE |
| TC-FA-FAAC-721 | E2E | TC-FA-FAAC-E2E-209-create-declining-balance-menyimpan-end-of-life-treatment-dan-duplicate | FE+BE |
| TC-FA-FAAC-722 | E2E | TC-FA-FAAC-E2E-207-create-end-of-life-treatment-commercial-opsi-nilai-awal-dan-clear-field | FE+BE |
| TC-FA-FAAC-723 | E2E | TC-FA-FAAC-E2E-210-edit-end-of-life-treatment-tanpa-apply-changes-ganti-method-dan-asset-class-belum-dipakai | FE+BE |
| TC-FA-FAAC-724 | E2E | TC-FA-FAAC-E2E-211-edit-end-of-life-treatment-apply-changes-dan-versi-scheduled | FE+BE |
| TC-FA-FAAC-725 | E2E | TC-FA-FAAC-E2E-210-edit-end-of-life-treatment-tanpa-apply-changes-ganti-method-dan-asset-class-belum-dipakai | FE+BE |
| TC-FA-FAAC-726 | E2E | TC-FA-FAAC-E2E-211-edit-end-of-life-treatment-apply-changes-dan-versi-scheduled | FE+BE |
| TC-FA-FAAC-727 | E2E | TC-FA-FAAC-E2E-209-create-declining-balance-menyimpan-end-of-life-treatment-dan-duplicate | FE+BE |
| TC-FA-FAAC-728 | E2E | TC-FA-FAAC-E2E-212-helper-equivalent-declining-rate-pembulatan-dan-fallback | FE+BE |
| TC-FA-FAAC-729 | E2E | TC-FA-FAAC-E2E-212-helper-equivalent-declining-rate-pembulatan-dan-fallback | FE+BE |
| TC-FA-FAAC-730 | E2E | TC-FA-FAAC-E2E-212-helper-equivalent-declining-rate-pembulatan-dan-fallback | FE+BE |
| TC-FA-FAAC-731 | E2E | TC-FA-FAAC-E2E-208-create-end-of-life-treatment-fiskal-read-only-dan-hidden-menurut-tax-method | FE+BE |
| TC-FA-FAAC-732 | E2E | TC-FA-FAAC-E2E-208-create-end-of-life-treatment-fiskal-read-only-dan-hidden-menurut-tax-method | FE+BE |
| TC-FA-FAAC-733 | E2E | TC-FA-FAAC-E2E-213-log-edit-end-of-life-treatment-tiga-surface | FE+BE |
| TC-FA-FAAC-734 | E2E | TC-FA-FAAC-E2E-214-defense-in-depth-request-langsung-declining-balance-end-of-life-treatment-kosong-ditolak-v-39 | FE+BE |
| TC-FA-FAAC-734 | E2E | TC-FA-FAAC-E2E-215-log-absence-request-langsung-declining-balance-end-of-life-treatment-kosong-ditolak-server | FE+BE |
| TC-FA-FAAC-735 | E2E | TC-FA-FAAC-E2E-212-helper-equivalent-declining-rate-pembulatan-dan-fallback | FE+BE |
| TC-FA-FAAC-736 | E2E | TC-FA-FAAC-E2E-197-tab-asset-names-caption-per-mode-dan-assign-tanpa-save | FE+BE |
| TC-FA-FAAC-737 | E2E | TC-FA-FAAC-E2E-197-tab-asset-names-caption-per-mode-dan-assign-tanpa-save | FE+BE |
| TC-FA-FAAC-738 | E2E | TC-FA-FAAC-E2E-198-role-matrix-caption-tab-asset-names-read-only | FE+BE |
| TC-FA-FAAC-739 | E2E | TC-FA-FAAC-E2E-197-tab-asset-names-caption-per-mode-dan-assign-tanpa-save | FE+BE |
| TC-FA-FAAC-740 | E2E | TC-FA-FAAC-E2E-199-create-tax-method-opsi-disabled-tooltip-dan-metode-hanya-scheduled-tidak-ditawarkan | FE+BE |
| TC-FA-FAAC-741 | E2E | TC-FA-FAAC-E2E-199-create-tax-method-opsi-disabled-tooltip-dan-metode-hanya-scheduled-tidak-ditawarkan | FE+BE |
| TC-FA-FAAC-742 | E2E | TC-FA-FAAC-E2E-200-create-tax-method-tooltip-versi-scheduled-paling-awal-dan-ganti-tax-depreciation-class | FE+BE |
| TC-FA-FAAC-743 | E2E | TC-FA-FAAC-E2E-200-create-tax-method-tooltip-versi-scheduled-paling-awal-dan-ganti-tax-depreciation-class | FE+BE |
| TC-FA-FAAC-744 | E2E | TC-FA-FAAC-E2E-202-use-recommended-classes-baris-tax-method-di-luar-irisan-disabled | FE+BE |
| TC-FA-FAAC-745 | E2E | TC-FA-FAAC-E2E-203-edit-versi-scheduled-tax-method-memakai-irisan-yang-sama | FE+BE |
| TC-FA-FAAC-746 | E2E | TC-FA-FAAC-E2E-201-create-tax-method-irisan-kosong-semua-opsi-disabled-dan-submit-ditolak | FE+BE |
| TC-FA-FAAC-747 | E2E | TC-FA-FAAC-E2E-204-defense-in-depth-request-langsung-tax-method-di-luar-irisan-ditolak-v-36 | FE+BE |
| TC-FA-FAAC-747 | E2E | TC-FA-FAAC-E2E-206-log-absence-request-langsung-tax-method-di-luar-irisan-ditolak-server | FE+BE |
| TC-FA-FAAC-748 | E2E | TC-FA-FAAC-E2E-205-sinkron-cancel-scheduled-version-tax-depreciation-class-menghitung-ulang-opsi-tax-method | FE+BE |
| TC-FA-FAAC-754 | E2E | TC-FA-FAAC-E2E-216-guided-tooltip-replay-melewati-kolom-tersembunyi | FE+BE |

## 4. Pertanyaan terbuka dan Temuan untuk QA

Spec yang memuat butir "Temuan untuk QA" di Notes: 191 dari seluruh spec. Temuan ditulis di Notes tiap spec; TC sumber tidak ditambal diam-diam. Status keputusan: D-1 (klausa log kelas g) dan D-2 (breadcrumb untuk form halaman penuh) diputuskan 2026-11-04 dan diterapkan di konvensi serta fix pass 1; butir lain di bawah belum diputuskan.

### 4.1 Pertanyaan terbuka (butuh keputusan QA/FE)

1. Fixture dan kemampuan BE tak bernama: periode Closed/Last Posted/Exported, versi Scheduled, job penerapan versi, plan, status entitas, tabel kosong, volume besar, sesi API aktor kedua, dan pembaca Changelog/System Log/Activity Log ditulis "disediakan tim FE/BE" tanpa endpoint karangan.
2. Nama env password `FA_TC_PASSWORD` dan `FA_AC_<KODE>_PASSWORD` (usulan) belum terdaftar di `spectra.config.ts` dan `.env.example`; akun "role lain tanpa Manage accounting" (TC-70, 589) dan akun client seed khusus (TC-129, 607) belum ada di Pre-setup TC.
3. Klausa "tidak ada log": spec absence 166 hanya memuat TC-538, 539, 540, 551, 578. TC lain (antara lain 100, 163, 164, 170, 209, 213, 225, 237, 240, 241, 253, 293, 305, 306, 595-600) di-assert di spec asalnya dengan baseline selisih atau hanya dirujuk di Notes; S-05 ketat meminta kelas g.
4. Changelog absolut: TC-472 sampai 510 dan 679 sampai 681 meng-assert total dari seed (19 entri), bentrok dengan S-12 karena Changelog bertambah dari spec lain; bergantung fixture BE yang menjamin keadaan itu.
5. Seed literal (B-FREE*, B-IN*, B-DEL*, HEAVY-EQ, B-ANCHOR, B-DEC, B-HID, B-TANAH) dipakai apa adanya sebagai pengecualian beralasan S-06/S-12 (batas Class Code 15 karakter). Spec yang membuat kode sendiri memakai suffix run.
6. State bersama antar TC: TC-9 dan 282 sampai 293 mengasumsikan tabel kosong, TC-1 sampai 13 mengasumsikan 9 Asset Class; TC-208 vs 190, TC-168 vs 149-155, TC-87 vs spec lain (B-ANCHOR) memakai fixture untuk berpindah state.
7. Tidak ada spec mode `mock`; kelas c (dua sesi UI) hanya TC-182, 669, 687, lainnya memakai sesi API.
8. `executionOrder: 7.0` di `suite.md` (1.0 sampai 6.0 dipakai suite lain).

### 4.2 Spec di atas ~35 langkah (alasan di Notes tiap spec)

Nomor cadangan tiap slice habis. Terbesar: 170 (127), 123 (~100 terekspansi), 171 (105), 168 (88), 169 (85), 166 (83), 167 (78), 060 (63), 185 (60), 010 (59), 159 (57), 005 (54), 059 (54), 105 (50), 155 (50), 180 (50), 205 (38). Memecahnya butuh nomor spec tambahan atau fix pass; audit bisa menolak alasan pada spec seperti 155, 148/149, 185.

### 4.3 Temuan TC sumber utama

- TC-100, 129, 118-120 (Manual Only (d)), 125, 128, 179, 265: pengamatan atau langkah tidak lengkap; spec memakai kemampuan BE atau teks PRD §6.
- TC-144 vs 145 (B-PE6/B-PE7), TC-401 (refresh), TC-434 (urutan Z-A), TC-439 (judul Filter, langkah Search), TC-705/706 (bergantung TC-704), TC-611 (judul Suspended atau Expired, hanya Suspended diuji), TC-607 (judul klik ganda Save, langkah Apply dan Create).
- TC-40: spec hanya memeriksa fokus keyboard pada toggle Active.

### 4.4 Fix pass 1 (2026-11-04)

Spec absence kelas g baru 193–196 memuat klausa log request langsung ditolak (TC-595–600, 601–605, 207, 242, 618–621, 686). TC itu juga tetap di sourceTc spec asalnya (check-suite [REVIEW] C2, diharapkan). Klausa log pada aksi UI kelas b (TC-143, 180, 222, 302, 303, 311, 335, 635) tetap `Verifikasi` berbaseline di spec asal; belum ada keputusan apakah ini cukup.

### 4.5 Fix pass 2 (2026-11-05)

Menutup N-1..N-10 delta recheck 1 (tiga surface log di 004/054/059/060, keadaan awal dinamis di 134/172/173/182, M+2 di 146, Search di 029/079/113, breadcrumb di 102/109, penanda job sinkron di 105, "Tunggu aksi selesai"). Total Changelog 19 entri di spec 146-157 sah menurut Lampiran A-19 (konvensi) dengan fixture BE reset. Spec 105 menuntut pemicu job sinkron dari tim FE/BE.

### 4.6 Fix pass 3 (2026-11-05)

Menutup N2-1 (097), N2-2 (094), N2-3 (174) dan TC TS2-1/TS2-2. Klik link Class Code B-* tanpa Search di ±18 spec (N2-R1) diterima sebagai Ringan.

### 4.7 Fix pass 4 (2026-11-05)

Menutup temuan audit penuh ke-2 (F-1..F-17 + Ringan di spec yang sama) dan perbaikan TC T-1..T-8, T-12. TC-422 pindah dari spec 128 ke 129 (sourceTc berubah). T-11 (Manual Only) dibiarkan: kriteria (d) dua sesi paralel sah menurut foundation testcase-conventions. Spec di atas 35 langkah bertambah (070, 119, 122, 124, 129, 130, 166-173 dst.) dengan alasan di Notes.

### 4.8 Fix pass 5 (2026-11-05)

Menutup temuan delta 1 atas baseline ke-2 (G1-1..G1-6, G2-1..G2-5, Ringan terkait) dengan cakupan diperluas ke spec di luar daftar (disetujui user): Class Code `{runId}` >15 karakter diganti literal <=15 karakter di 15 spec, Search sebelum klik baris non-B-* di 162-174, keadaan awal fixture di 141-143/162/166/172/173/184, bulan relatif di 100/101/147. TC-211 dan TC-479 diperbaiki. Asumsi UI yang belum terbukti: kotak Search/Filter tetap terisi setelah kembali ke tabel; seleksi bertahan saat page size berubah; panel Filter dibuka ulang per blok.

### 4.9 Fix pass 6 (2026-11-05)

Menutup H1-1, H1-2, H2-1..H2-3 (rujukan langkah 084, pemulihan Meeting Table 072, Search bertahan antar-tab 169/170, Search sebelum hapus Asset Name 166/174, seed Climate Probe 145) dan TC-479 (butir seed M+2). Seed Climate Probe di 145 bersumber dari precondition TC-692.

### 4.10 Fix pass 7 (2026-11-05)

Menutup J-1 (169) dan J-2 (169, 170, 190: Create/Submit dan aksi di Detail tetap di Detail; kembali ke tabel lewat breadcrumb), R3-a (147 zona waktu) dan TC-569/650-652 (T-S5). Save tanpa versi Scheduled kembali ke tabel (PRD asset-class.md ~L373-375), jadi Save lalu Search di tabel (170) tidak diubah. Tanpa audit atau delta lanjutan atas permintaan user. Asumsi UI yang belum terbukti: Search bertahan lewat breadcrumb (170 langkah 14, 190 langkah 27), Search bertahan antar-tab (TC-415).


### 4.11 Sinkron perubahan TC 2026-11-20 (irisan Tax Method)

Tax Method dibatasi irisan metode versi Current dan semua versi Scheduled Tax Depreciation Class. TC-653 dihapus (spec 085 kehilangan blok keadaan Tax Method tersimpan yang tidak diizinkan; langkah dan trace dinomori ulang). TC-266 dihapus (aturan Duplicate yang mengosongkan Tax Method di luar irisan dicabut; spec 086 kehilangan blok TC-266 dan seed `B-DUPTM`); TC-119 dan TC-126/127 (spec 043, 045) hanya menambah rujukan FAAC-LOGIC-02l. TC baru 740-748 masuk spec 199-206: 199 (740, 741), 200 (742, 743), 201 (746), 202 (744), 203 (745), 204 (747 respons dan state data), 205 (748, di atas 35 langkah dengan alasan di Notes), 206 (747 klausa tidak ada log, pasangan S-05 dengan 204). Seed baru: `Seed Irisan A` sampai `D` dan `B-IRISAN` (nama literal tanpa suffix, disediakan fixture BE di bawah suite serial). Asumsi yang belum terbukti: cara pembuatan versi Scheduled `Seed Irisan A` pada tab Tax Depreciation Class (spec 205) dan nilai field wajib lain permintaan Create TC-747 (spec 204, 206).

### 4.12 TC End-of-Life Treatment Declining Balance dan helper Equivalent (TC-719 sampai 735)

TC-719 sampai 735 masuk spec 207 sampai 215: 207 (719, 722), 208 (731, 732), 209 (720, 721, 727), 210 (723, 725), 211 (724, 726), 212 (728, 729, 730, 735), 213 (733), 214 (734 respons dan state data), 215 (734 klausa tidak ada log, pasangan S-05 dengan 214). Tidak ada TC hanya-BE: TC-734 bertanda BE di tabel TC tetapi berkelas defense-in-depth dengan Expected respons API, sehingga masuk spec FE+BE menurut K-1 (pola TC-747 di spec 204 dan 206). Seed baru: `B-EOLSWAP`, `B-EOLUSED`, `B-EOLFREE`, `B-EOLSCHED`, `B-EOLDUP`, `B-EOLLOG` (nama literal, disediakan fixture BE di bawah suite serial); `B-EOLDEF`, `B-EOLCHG`, `B-EOLKEEP`, `B-EOLDUP2` dibuat spec 209 dan dihapus fixture BE. Spec 209 sampai 212 di atas 35 langkah dengan alasan di Notes. Asumsi yang belum terbukti dan perlu konfirmasi tim FE: nilai End-of-Life Treatment fiskal pada master `Bukan bangunan – Kelompok 3` (TC-731 tidak menyebut nilainya), bentuk visual indikator wajib pada label End-of-Life Treatment (TC-719), label tombol dialog Apply Changes (TC-724, 726), dan status respons HTTP penolakan V-39 (TC-734).

### 4.13 Sinkron perubahan TC 2026-11-24

TC-754 (Guided Tooltip melewati step yang kolom targetnya disembunyikan; `guided-tooltip.md` §16.3 baris Target tersembunyi) masuk spec 216. TC-749 sampai 753 (pengecualian Unpost pada `FAAC-LOGIC-09c`) belum punya spec dan belum dipetakan di sini.
