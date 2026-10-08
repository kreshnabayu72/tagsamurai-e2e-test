# Coverage E2E — Auth > Account Activation

Sumber: `auth/account-activation/TestCases/tc-account-activation.md` (134 TC, `TC-AUTH-ACT-01`–`134`). Suite: `specs/Auth/AccountActivation/`. Status semua spec: `draft`, belum ada script.

Seleksi sesuai `docs/e2e-conventions.md` bagian 2: 130 TC masuk spec, 4 TC hanya-BE. Setiap TC terpetakan tepat ke satu spec. Asersi absence pencatatan dari TC-01 dan TC-74 diuji di spec 017, dari TC-11 dan TC-98 di spec 029 (dicatat di `## Notes` spec 001, 009, 010, 023, 017, dan 029). Spec 015 dihapus; TC-129 dan TC-130 pindah ke spec 020 (kelas defense-in-depth).

## TC granular → spec e2e

| Spec | Judul | TC sumber |
|---|---|---|
| TC-AUTH-ACT-E2E-001-screening-set-password-valid-link | Screening Halaman Set Password dari Link Aktivasi Valid | 01, 07, 08 |
| TC-AUTH-ACT-E2E-002-active-session-in-browser | Link Aktivasi dan Go to Login saat Browser Memiliki Sesi Login Aktif | 10, 78 |
| TC-AUTH-ACT-E2E-003-toggle-show-hide-a11y | Toggle Show/Hide Password dan Aksesibilitas Form Set Password | 19, 20, 21, 60, 61, 62 |
| TC-AUTH-ACT-E2E-004-password-policy-checklist | Checklist Password Policy Real-time | 22, 23, 24, 25, 26, 27, 28, 29, 30, 31 |
| TC-AUTH-ACT-E2E-005-max-length-72 | Batas Panjang 72 Karakter pada Password dan Confirm Password | 32, 33, 34, 35, 36, 37 |
| TC-AUTH-ACT-E2E-006-empty-and-mismatch-validation | Validasi Field Kosong dan Confirm Password Tidak Sama | 38, 39, 40, 41, 42, 43, 44, 53, 54, 55, 56 |
| TC-AUTH-ACT-E2E-007-policy-blocked-submit | Submit Diblokir saat Password Tidak Memenuhi Policy | 45, 46, 47, 48, 49, 50, 51, 52 |
| TC-AUTH-ACT-E2E-008-no-captcha-no-unsaved-dialog | Halaman Set Password Tanpa CAPTCHA dan Tanpa Dialog Unsaved Changes | 57, 58, 59 |
| TC-AUTH-ACT-E2E-009-activation-success-and-navigation | Aktivasi Berhasil, Halaman Activation Success, dan Navigasi | 63, 65, 70, 71, 73, 74, 75, 76, 77 |
| TC-AUTH-ACT-E2E-010-status-reflection-and-login | Refleksi Status Activated dan Login Setelah Aktivasi | 98, 106, 107, 108 |
| TC-AUTH-ACT-E2E-011-active-toggle-off | Aktivasi pada User dengan Toggle Active OFF | 72, 89, 109, 126 |
| TC-AUTH-ACT-E2E-012-invalid-link-unknown-token | Halaman Invalid Link untuk Token Tidak Dikenal atau Salah Bentuk | 09, 79, 80, 81, 82 |
| TC-AUTH-ACT-E2E-013-invalid-link-used | Halaman Invalid Link Varian Used untuk Token yang Sudah Dipakai | 83, 84, 127 |
| TC-AUTH-ACT-E2E-014-invalid-link-deleted-user | Link Aktivasi Milik User yang Dihapus | 88, 125 |
| TC-AUTH-ACT-E2E-016-entity-and-plan-dimensions | Aktivasi pada Client Suspended, Expired, dan Berbagai Plan | 110, 111, 112 |
| TC-AUTH-ACT-E2E-017-zero-logging-absence | Tidak Ada Pencatatan oleh Auth Account Activation dari Halaman Publik | 90, 91, 92, 93, 94, 95 |
| TC-AUTH-ACT-E2E-018-resilience-validate-and-submit | Ketahanan Validate Link terhadap Error Server dan Timeout | 02, 03, 04, 05, 06 |
| TC-AUTH-ACT-E2E-019-server-response-422-400-404 | Tampilan Set Password untuk Respons Server 422 dan 400 | 117, 118 |
| TC-AUTH-ACT-E2E-020-defense-in-depth-token | Cakupan Token, Pola Injeksi, dan Request Langsung ke Server | 119, 120, 129, 130, 131, 132, 113 |
| TC-AUTH-ACT-E2E-021-multi-tab-same-token | Submit dari Dua Tab dan Resend saat Form Terbuka | 121, 122, 123 |
| TC-AUTH-ACT-E2E-022-rate-limit-429 | Penolakan IP Rate Limit 429 pada Validate Link dan Set Password | 133, 134 |
| TC-AUTH-ACT-E2E-023-email-trigger-global-settings | Activation Email dari Pembuatan User di Global Settings | 11, 13, 14, 15, 16 |
| TC-AUTH-ACT-E2E-024-email-send-failure-and-resend | Kegagalan Pengiriman Activation Email dan Pemulihan lewat Resend | 17, 18 |
| TC-AUTH-ACT-E2E-025-email-trigger-admin-console | Activation Email dari Admin Console dan Resend | 12, 100 |
| TC-AUTH-ACT-E2E-026-resend-invalidation | Resend Activation Email Menggantikan Link Lama: Single dan Bulk Resend | 85, 99, 101 |
| TC-AUTH-ACT-E2E-027-token-ttl-time-travel | Masa Berlaku Token 24 Jam | 86, 87, 105, 124 |
| TC-AUTH-ACT-E2E-028-resilience-set-password-submit | Ketahanan Submit Set Password terhadap Error Server dan Timeout | 64, 66, 67, 68, 69 |
| TC-AUTH-ACT-E2E-029-zero-logging-absence-admin-triggers | Tidak Ada Pencatatan oleh Auth Account Activation dari Aksi Admin dan Login | 96, 97 |
| TC-AUTH-ACT-E2E-030-resend-repeat-status-email-change | Resend Berulang, Status Setelah Resend, dan Perubahan Email User Pending Activation | 102, 103, 104 |

## Lapisan per TC

| TC | Spec | Mode |
|---|---|---|
| TC-AUTH-ACT-01 | TC-AUTH-ACT-E2E-001 | FE+BE |
| TC-AUTH-ACT-07 | TC-AUTH-ACT-E2E-001 | FE+BE |
| TC-AUTH-ACT-08 | TC-AUTH-ACT-E2E-001 | FE+BE |
| TC-AUTH-ACT-10 | TC-AUTH-ACT-E2E-002 | FE+BE |
| TC-AUTH-ACT-78 | TC-AUTH-ACT-E2E-002 | FE+BE |
| TC-AUTH-ACT-19 | TC-AUTH-ACT-E2E-003 | FE+BE |
| TC-AUTH-ACT-20 | TC-AUTH-ACT-E2E-003 | FE+BE |
| TC-AUTH-ACT-21 | TC-AUTH-ACT-E2E-003 | FE+BE |
| TC-AUTH-ACT-60 | TC-AUTH-ACT-E2E-003 | FE+BE |
| TC-AUTH-ACT-61 | TC-AUTH-ACT-E2E-003 | FE+BE |
| TC-AUTH-ACT-62 | TC-AUTH-ACT-E2E-003 | FE+BE |
| TC-AUTH-ACT-22 | TC-AUTH-ACT-E2E-004 | FE+BE |
| TC-AUTH-ACT-23 | TC-AUTH-ACT-E2E-004 | FE+BE |
| TC-AUTH-ACT-24 | TC-AUTH-ACT-E2E-004 | FE+BE |
| TC-AUTH-ACT-25 | TC-AUTH-ACT-E2E-004 | FE+BE |
| TC-AUTH-ACT-26 | TC-AUTH-ACT-E2E-004 | FE+BE |
| TC-AUTH-ACT-27 | TC-AUTH-ACT-E2E-004 | FE+BE |
| TC-AUTH-ACT-28 | TC-AUTH-ACT-E2E-004 | FE+BE |
| TC-AUTH-ACT-29 | TC-AUTH-ACT-E2E-004 | FE+BE |
| TC-AUTH-ACT-30 | TC-AUTH-ACT-E2E-004 | FE+BE |
| TC-AUTH-ACT-31 | TC-AUTH-ACT-E2E-004 | FE+BE |
| TC-AUTH-ACT-32 | TC-AUTH-ACT-E2E-005 | FE+BE |
| TC-AUTH-ACT-33 | TC-AUTH-ACT-E2E-005 | FE+BE |
| TC-AUTH-ACT-34 | TC-AUTH-ACT-E2E-005 | FE+BE |
| TC-AUTH-ACT-35 | TC-AUTH-ACT-E2E-005 | FE+BE |
| TC-AUTH-ACT-36 | TC-AUTH-ACT-E2E-005 | FE+BE |
| TC-AUTH-ACT-37 | TC-AUTH-ACT-E2E-005 | FE+BE |
| TC-AUTH-ACT-38 | TC-AUTH-ACT-E2E-006 | FE+BE |
| TC-AUTH-ACT-39 | TC-AUTH-ACT-E2E-006 | FE+BE |
| TC-AUTH-ACT-40 | TC-AUTH-ACT-E2E-006 | FE+BE |
| TC-AUTH-ACT-41 | TC-AUTH-ACT-E2E-006 | FE+BE |
| TC-AUTH-ACT-42 | TC-AUTH-ACT-E2E-006 | FE+BE |
| TC-AUTH-ACT-43 | TC-AUTH-ACT-E2E-006 | FE+BE |
| TC-AUTH-ACT-44 | TC-AUTH-ACT-E2E-006 | FE+BE |
| TC-AUTH-ACT-53 | TC-AUTH-ACT-E2E-006 | FE+BE |
| TC-AUTH-ACT-54 | TC-AUTH-ACT-E2E-006 | FE+BE |
| TC-AUTH-ACT-55 | TC-AUTH-ACT-E2E-006 | FE+BE |
| TC-AUTH-ACT-56 | TC-AUTH-ACT-E2E-006 | FE+BE |
| TC-AUTH-ACT-45 | TC-AUTH-ACT-E2E-007 | FE+BE |
| TC-AUTH-ACT-46 | TC-AUTH-ACT-E2E-007 | FE+BE |
| TC-AUTH-ACT-47 | TC-AUTH-ACT-E2E-007 | FE+BE |
| TC-AUTH-ACT-48 | TC-AUTH-ACT-E2E-007 | FE+BE |
| TC-AUTH-ACT-49 | TC-AUTH-ACT-E2E-007 | FE+BE |
| TC-AUTH-ACT-50 | TC-AUTH-ACT-E2E-007 | FE+BE |
| TC-AUTH-ACT-51 | TC-AUTH-ACT-E2E-007 | FE+BE |
| TC-AUTH-ACT-52 | TC-AUTH-ACT-E2E-007 | FE+BE |
| TC-AUTH-ACT-57 | TC-AUTH-ACT-E2E-008 | FE+BE |
| TC-AUTH-ACT-58 | TC-AUTH-ACT-E2E-008 | FE+BE |
| TC-AUTH-ACT-59 | TC-AUTH-ACT-E2E-008 | FE+BE |
| TC-AUTH-ACT-63 | TC-AUTH-ACT-E2E-009 | FE+BE |
| TC-AUTH-ACT-64 | TC-AUTH-ACT-E2E-028 | FE+BE |
| TC-AUTH-ACT-65 | TC-AUTH-ACT-E2E-009 | FE+BE |
| TC-AUTH-ACT-70 | TC-AUTH-ACT-E2E-009 | FE+BE |
| TC-AUTH-ACT-71 | TC-AUTH-ACT-E2E-009 | FE+BE |
| TC-AUTH-ACT-73 | TC-AUTH-ACT-E2E-009 | FE+BE |
| TC-AUTH-ACT-74 | TC-AUTH-ACT-E2E-009 | FE+BE |
| TC-AUTH-ACT-75 | TC-AUTH-ACT-E2E-009 | FE+BE |
| TC-AUTH-ACT-76 | TC-AUTH-ACT-E2E-009 | FE+BE |
| TC-AUTH-ACT-77 | TC-AUTH-ACT-E2E-009 | FE+BE |
| TC-AUTH-ACT-98 | TC-AUTH-ACT-E2E-010 | FE+BE |
| TC-AUTH-ACT-106 | TC-AUTH-ACT-E2E-010 | FE+BE |
| TC-AUTH-ACT-107 | TC-AUTH-ACT-E2E-010 | FE+BE |
| TC-AUTH-ACT-108 | TC-AUTH-ACT-E2E-010 | FE+BE |
| TC-AUTH-ACT-72 | TC-AUTH-ACT-E2E-011 | FE+BE |
| TC-AUTH-ACT-89 | TC-AUTH-ACT-E2E-011 | FE+BE |
| TC-AUTH-ACT-109 | TC-AUTH-ACT-E2E-011 | FE+BE |
| TC-AUTH-ACT-126 | TC-AUTH-ACT-E2E-011 | FE+BE |
| TC-AUTH-ACT-09 | TC-AUTH-ACT-E2E-012 | FE+BE |
| TC-AUTH-ACT-79 | TC-AUTH-ACT-E2E-012 | FE+BE |
| TC-AUTH-ACT-80 | TC-AUTH-ACT-E2E-012 | FE+BE |
| TC-AUTH-ACT-81 | TC-AUTH-ACT-E2E-012 | FE+BE |
| TC-AUTH-ACT-82 | TC-AUTH-ACT-E2E-012 | FE+BE |
| TC-AUTH-ACT-83 | TC-AUTH-ACT-E2E-013 | FE+BE |
| TC-AUTH-ACT-84 | TC-AUTH-ACT-E2E-013 | FE+BE |
| TC-AUTH-ACT-127 | TC-AUTH-ACT-E2E-013 | FE+BE |
| TC-AUTH-ACT-88 | TC-AUTH-ACT-E2E-014 | FE+BE |
| TC-AUTH-ACT-125 | TC-AUTH-ACT-E2E-014 | FE+BE |
| TC-AUTH-ACT-129 | TC-AUTH-ACT-E2E-020 | FE+BE |
| TC-AUTH-ACT-130 | TC-AUTH-ACT-E2E-020 | FE+BE |
| TC-AUTH-ACT-110 | TC-AUTH-ACT-E2E-016 | FE+BE |
| TC-AUTH-ACT-111 | TC-AUTH-ACT-E2E-016 | FE+BE |
| TC-AUTH-ACT-112 | TC-AUTH-ACT-E2E-016 | FE+BE |
| TC-AUTH-ACT-90 | TC-AUTH-ACT-E2E-017 | FE+BE |
| TC-AUTH-ACT-91 | TC-AUTH-ACT-E2E-017 | FE+BE |
| TC-AUTH-ACT-92 | TC-AUTH-ACT-E2E-017 | FE+BE |
| TC-AUTH-ACT-93 | TC-AUTH-ACT-E2E-017 | FE+BE |
| TC-AUTH-ACT-94 | TC-AUTH-ACT-E2E-017 | FE+BE |
| TC-AUTH-ACT-95 | TC-AUTH-ACT-E2E-017 | FE+BE |
| TC-AUTH-ACT-96 | TC-AUTH-ACT-E2E-029 | FE+BE |
| TC-AUTH-ACT-97 | TC-AUTH-ACT-E2E-029 | FE+BE |
| TC-AUTH-ACT-02 | TC-AUTH-ACT-E2E-018 | FE+BE |
| TC-AUTH-ACT-03 | TC-AUTH-ACT-E2E-018 | FE+BE |
| TC-AUTH-ACT-04 | TC-AUTH-ACT-E2E-018 | FE+BE |
| TC-AUTH-ACT-05 | TC-AUTH-ACT-E2E-018 | FE+BE |
| TC-AUTH-ACT-06 | TC-AUTH-ACT-E2E-018 | FE+BE |
| TC-AUTH-ACT-66 | TC-AUTH-ACT-E2E-028 | FE+BE |
| TC-AUTH-ACT-67 | TC-AUTH-ACT-E2E-028 | FE+BE |
| TC-AUTH-ACT-68 | TC-AUTH-ACT-E2E-028 | FE+BE |
| TC-AUTH-ACT-69 | TC-AUTH-ACT-E2E-028 | FE+BE |
| TC-AUTH-ACT-117 | TC-AUTH-ACT-E2E-019 | FE+BE |
| TC-AUTH-ACT-118 | TC-AUTH-ACT-E2E-019 | FE+BE |
| TC-AUTH-ACT-131 | TC-AUTH-ACT-E2E-020 | FE+BE |
| TC-AUTH-ACT-132 | TC-AUTH-ACT-E2E-020 | FE+BE |
| TC-AUTH-ACT-113 | TC-AUTH-ACT-E2E-020 | FE+BE |
| TC-AUTH-ACT-119 | TC-AUTH-ACT-E2E-020 | FE+BE |
| TC-AUTH-ACT-120 | TC-AUTH-ACT-E2E-020 | FE+BE |
| TC-AUTH-ACT-121 | TC-AUTH-ACT-E2E-021 | FE+BE |
| TC-AUTH-ACT-122 | TC-AUTH-ACT-E2E-021 | FE+BE |
| TC-AUTH-ACT-133 | TC-AUTH-ACT-E2E-022 | FE+BE |
| TC-AUTH-ACT-134 | TC-AUTH-ACT-E2E-022 | FE+BE |
| TC-AUTH-ACT-11 | TC-AUTH-ACT-E2E-023 | FE+BE |
| TC-AUTH-ACT-13 | TC-AUTH-ACT-E2E-023 | FE+BE |
| TC-AUTH-ACT-14 | TC-AUTH-ACT-E2E-023 | FE+BE |
| TC-AUTH-ACT-15 | TC-AUTH-ACT-E2E-023 | FE+BE |
| TC-AUTH-ACT-16 | TC-AUTH-ACT-E2E-023 | FE+BE |
| TC-AUTH-ACT-17 | TC-AUTH-ACT-E2E-024 | FE+BE |
| TC-AUTH-ACT-18 | TC-AUTH-ACT-E2E-024 | FE+BE |
| TC-AUTH-ACT-12 | TC-AUTH-ACT-E2E-025 | FE+BE |
| TC-AUTH-ACT-100 | TC-AUTH-ACT-E2E-025 | FE+BE |
| TC-AUTH-ACT-85 | TC-AUTH-ACT-E2E-026 | FE+BE |
| TC-AUTH-ACT-99 | TC-AUTH-ACT-E2E-026 | FE+BE |
| TC-AUTH-ACT-101 | TC-AUTH-ACT-E2E-026 | FE+BE |
| TC-AUTH-ACT-102 | TC-AUTH-ACT-E2E-030 | FE+BE |
| TC-AUTH-ACT-103 | TC-AUTH-ACT-E2E-030 | FE+BE |
| TC-AUTH-ACT-104 | TC-AUTH-ACT-E2E-030 | FE+BE |
| TC-AUTH-ACT-123 | TC-AUTH-ACT-E2E-021 | FE+BE |
| TC-AUTH-ACT-86 | TC-AUTH-ACT-E2E-027 | FE+BE |
| TC-AUTH-ACT-87 | TC-AUTH-ACT-E2E-027 | FE+BE |
| TC-AUTH-ACT-105 | TC-AUTH-ACT-E2E-027 | FE+BE |
| TC-AUTH-ACT-124 | TC-AUTH-ACT-E2E-027 | FE+BE |

## TC hanya-BE (tidak masuk spec)

| TC | Alasan |
|---|---|
| TC-AUTH-ACT-114 | Request langsung ke server dengan password kurang dari 8 karakter ditolak server: request langsung ke server, asersinya kontrak validasi server; dicakup `tc-account-activation-backend.md`. |
| TC-AUTH-ACT-115 | Request langsung ke server dengan password 73 karakter ditolak server: request langsung ke server, asersinya kontrak validasi server; dicakup `tc-account-activation-backend.md`. |
| TC-AUTH-ACT-116 | Request langsung ke server dengan password berisi spasi ditolak server tanpa di-trim: request langsung ke server, asersinya kontrak validasi server; dicakup `tc-account-activation-backend.md`. |
| TC-AUTH-ACT-128 | Request langsung ke server dengan Confirm Password berbeda ditolak server: request langsung ke server, asersinya kontrak validasi server; dicakup `tc-account-activation-backend.md`. |
