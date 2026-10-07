# Coverage Ledger — Auth > MFA (Multi-Factor Authentication)

Dokumen ini melacak keterlacakan (traceability) antara **207 Test Cases granular** pada [`auth/mfa/TestCases/tc-mfa.md`](../../auth/mfa/TestCases/tc-mfa.md) dengan **36 File Spesifikasi E2E TestSpectra** yang telah direstrukturisasi secara modular dan terisolasi.

---

## 1. Ringkasan Eksekutif

| Indikator | Nilai | Keterangan |
| :--- | :---: | :--- |
| **Total Test Case Granular Sumber** | **207** | `TC-AUTH-MFA-01` s/d `TC-AUTH-MFA-207` |
| **Total Spec E2E TestSpectra** | **36** | Tersimpan di `tagsamurai-e2e-test/specs/Auth/Mfa/` |
| **Granular TC Terpetakan** | **207 / 207** | **100.0% Coverage** |
| **Duplikasi Pemetaan** | **0** | Setiap granular TC dipetakan tepat satu kali ke 1 spec |
| **TC Tanpa Pemetaan (Uncovered)** | **0** | Tidak ada celah cakupan |
| **Status Validasi TestSpectra** | **Lolos Linter Strict** | `npx spectra lint --strict specs/Auth/Mfa` (0 error) |

---

## 2. Pemisahan Modular Berdasarkan Domain Masalah

Arsitektur 36 spec ini dirancang untuk memaksimalkan **stabilitas eksekusi otomatis** dan **kemudahan diagnosis kegagalan (failure isolation)**:

1. **Screening Visual / Layout Murni (Spec 001 - 005):**
   - Hanya menguji DOM, copy teks, tombol default/disabled, kursor Backspace, dan Tab a11y.
   - Tidak ada ketergantungan pada mail-catcher, TOTP generator, atau decoding canvas QR.
2. **Evaluasi Risiko & Logika Pemicu MFA (Spec 006 - 015):**
   - Menguji filter device, Haversine distance >100km, ISO negara, tumbling window 90 hari, dan decay 180 hari.
3. **Verifikasi & Validasi Form User (Spec 016 - 022):**
   - Format input segmented, auto-submit digit 6, smart paste, countdown timer resend 60s, kuota 5x, caption inline error.
4. **Batas Keamanan Sesi & Lifecycle User (Spec 023 - 027):**
   - Batas 5 percobaan salah akumulatif, 10m TTL pre-auth, deactivation/deletion user real-time, email alert unusual login.
5. **Audit Log Multi-Surface Terisolasi (Spec 028 - 029):**
   - Spec 028: Mutasi status Sukses & Gagal faktor-2 di Activity Log Session dan User Log.
   - Spec 029: Whitelist policy (event yang tidak boleh dicatat) & ekstraksi header `X-Forwarded-For` proxy hop.
6. **Integrasi Lintas Modul & Paritas (Spec 030 - 031):**
   - Spec 030: Fallback recovery ke OTP saat Authenticator hilang, Admin reset di GS > User.
   - Spec 031: Session Management Duplicate Login Dialog, Client Suspended/Expired, Paritas Plan Starter–Enterprise.
7. **Pengujian Teknis Khusus / High Complexity (Spec 032 - 036):**
   - **Spec 032 (QR & Secret Cryptography):** Ekstraksi dan decoding canvas/image QR Code, verifikasi URI `otpauth://`, validasi parameter SHA1, 30s period, 6 digits, secret string, dan clipboard.
   - **Spec 033 (Concurrency & Double-Submit Guards):** Balapan multi-device / multi-tab, auto-submit vs button click simultan, klik ganda cepat tombol submit.
   - **Spec 034 (Defense-in-Depth & Token Tampering):** Direct API tampering dengan token palsu/consumed dan pemisahan purpose token (`purpose='login'` vs `purpose='mfa'`).
   - **Spec 035 (Resilience & Rate Limiting):** IP Rate Limit 429, fault injection 5xx, sticky Toast T-01, ARIA live alert tags.
   - **Spec 036 (Mobile Biometric Re-login):** Pengujian khusus hardware biometrik Android pada faktor-1.

---

## 3. Matriks Pemetaan Lengkap (36 Specs)

| No | ID Spec E2E | Jumlah TC | Granular TC yang Dicakup | Platform |
| :---: | :--- | :---: | :--- | :--- |
| 001 | `TC-AUTH-MFA-E2E-001-screening-choose-verification-method` | 8 | TC-AUTH-MFA-01, TC-AUTH-MFA-02, TC-AUTH-MFA-03, TC-AUTH-MFA-13, TC-AUTH-MFA-53, TC-AUTH-MFA-59, TC-AUTH-MFA-60, TC-AUTH-MFA-61 | Web |
| 002 | `TC-AUTH-MFA-E2E-002-screening-halaman-otp-verification` | 6 | TC-AUTH-MFA-04, TC-AUTH-MFA-14, TC-AUTH-MFA-56, TC-AUTH-MFA-65, TC-AUTH-MFA-67, TC-AUTH-MFA-87 | Web |
| 003 | `TC-AUTH-MFA-E2E-003-screening-authenticator-verification` | 8 | TC-AUTH-MFA-05, TC-AUTH-MFA-06, TC-AUTH-MFA-08, TC-AUTH-MFA-15, TC-AUTH-MFA-55, TC-AUTH-MFA-57, TC-AUTH-MFA-63, TC-AUTH-MFA-92 | Web |
| 004 | `TC-AUTH-MFA-E2E-004-screening-enrollment-authenticator` | 7 | TC-AUTH-MFA-07, TC-AUTH-MFA-16, TC-AUTH-MFA-58, TC-AUTH-MFA-113, TC-AUTH-MFA-114, TC-AUTH-MFA-115, TC-AUTH-MFA-116 | Web |
| 005 | `TC-AUTH-MFA-E2E-005-mobile-native-layout-responsif` | 2 | TC-AUTH-MFA-17, TC-AUTH-MFA-18 | Mobile Native |
| 006 | `TC-AUTH-MFA-E2E-006-akses-publik-dan-direct-url` | 3 | TC-AUTH-MFA-19, TC-AUTH-MFA-20, TC-AUTH-MFA-21 | Web |
| 007 | `TC-AUTH-MFA-E2E-007-evaluasi-single-step-tanpa-mfa` | 4 | TC-AUTH-MFA-22, TC-AUTH-MFA-23, TC-AUTH-MFA-34, TC-AUTH-MFA-148 | Web |
| 008 | `TC-AUTH-MFA-E2E-008-pemicu-mfa-login-pertama` | 3 | TC-AUTH-MFA-24, TC-AUTH-MFA-25, TC-AUTH-MFA-149 | Web |
| 009 | `TC-AUTH-MFA-E2E-009-pemicu-mfa-idle-dan-independensi-platform` | 4 | TC-AUTH-MFA-26, TC-AUTH-MFA-27, TC-AUTH-MFA-28, TC-AUTH-MFA-29 | Web |
| 010 | `TC-AUTH-MFA-E2E-010-deteksi-device-baru-dan-reset-storage` | 4 | TC-AUTH-MFA-30, TC-AUTH-MFA-31, TC-AUTH-MFA-32, TC-AUTH-MFA-50 | Web |
| 011 | `TC-AUTH-MFA-E2E-011-deteksi-lokasi-jarak-dan-baseline-user` | 2 | TC-AUTH-MFA-33, TC-AUTH-MFA-51 | Web |
| 012 | `TC-AUTH-MFA-E2E-012-deteksi-beda-negara-dan-tumbling-window` | 6 | TC-AUTH-MFA-35, TC-AUTH-MFA-36, TC-AUTH-MFA-37, TC-AUTH-MFA-38, TC-AUTH-MFA-39, TC-AUTH-MFA-40 | Web |
| 013 | `TC-AUTH-MFA-E2E-013-decay-pasangan-negara-dan-single-step-refresh` | 4 | TC-AUTH-MFA-41, TC-AUTH-MFA-42, TC-AUTH-MFA-43, TC-AUTH-MFA-44 | Web |
| 014 | `TC-AUTH-MFA-E2E-014-fail-open-geo-ip-dan-kombinasi-alert` | 3 | TC-AUTH-MFA-45, TC-AUTH-MFA-46, TC-AUTH-MFA-52 | Web |
| 015 | `TC-AUTH-MFA-E2E-015-sekuensialitas-agreement-gate-dan-mfa` | 3 | TC-AUTH-MFA-47, TC-AUTH-MFA-48, TC-AUTH-MFA-49 | Web |
| 016 | `TC-AUTH-MFA-E2E-016-verifikasi-otp-auto-submit-dan-paste` | 6 | TC-AUTH-MFA-62, TC-AUTH-MFA-66, TC-AUTH-MFA-68, TC-AUTH-MFA-69, TC-AUTH-MFA-88, TC-AUTH-MFA-89 | Web |
| 017 | `TC-AUTH-MFA-E2E-017-validasi-input-otp-error-dan-expiry` | 7 | TC-AUTH-MFA-70, TC-AUTH-MFA-71, TC-AUTH-MFA-72, TC-AUTH-MFA-73, TC-AUTH-MFA-74, TC-AUTH-MFA-76, TC-AUTH-MFA-86 | Web |
| 018 | `TC-AUTH-MFA-E2E-018-siklus-resend-otp-cooldown-dan-kuota` | 8 | TC-AUTH-MFA-77, TC-AUTH-MFA-78, TC-AUTH-MFA-79, TC-AUTH-MFA-80, TC-AUTH-MFA-81, TC-AUTH-MFA-82, TC-AUTH-MFA-85, TC-AUTH-MFA-200 | Web |
| 019 | `TC-AUTH-MFA-E2E-019-verifikasi-authenticator-drift-dan-anti-replay` | 6 | TC-AUTH-MFA-90, TC-AUTH-MFA-91, TC-AUTH-MFA-96, TC-AUTH-MFA-97, TC-AUTH-MFA-98, TC-AUTH-MFA-99 | Web |
| 020 | `TC-AUTH-MFA-E2E-020-validasi-input-authenticator-dan-paste` | 9 | TC-AUTH-MFA-09, TC-AUTH-MFA-10, TC-AUTH-MFA-93, TC-AUTH-MFA-94, TC-AUTH-MFA-95, TC-AUTH-MFA-101, TC-AUTH-MFA-102, TC-AUTH-MFA-103, TC-AUTH-MFA-104 | Web |
| 021 | `TC-AUTH-MFA-E2E-021-enrollment-authenticator-lengkap` | 6 | TC-AUTH-MFA-11, TC-AUTH-MFA-106, TC-AUTH-MFA-107, TC-AUTH-MFA-108, TC-AUTH-MFA-121, TC-AUTH-MFA-122 | Web |
| 022 | `TC-AUTH-MFA-E2E-022-validasi-input-enrollment-authenticator` | 4 | TC-AUTH-MFA-110, TC-AUTH-MFA-111, TC-AUTH-MFA-112, TC-AUTH-MFA-124 | Web |
| 023 | `TC-AUTH-MFA-E2E-023-batas-percobaan-salah-lintas-metode` | 7 | TC-AUTH-MFA-129, TC-AUTH-MFA-130, TC-AUTH-MFA-131, TC-AUTH-MFA-132, TC-AUTH-MFA-133, TC-AUTH-MFA-134, TC-AUTH-MFA-135 | Web |
| 024 | `TC-AUTH-MFA-E2E-024-ttl-sesi-pre-auth-dan-navigasi-browser` | 5 | TC-AUTH-MFA-125, TC-AUTH-MFA-126, TC-AUTH-MFA-127, TC-AUTH-MFA-128, TC-AUTH-MFA-136 | Web |
| 025 | `TC-AUTH-MFA-E2E-025-pembatalan-sesi-user-deactivated-dan-deleted` | 5 | TC-AUTH-MFA-138, TC-AUTH-MFA-139, TC-AUTH-MFA-140, TC-AUTH-MFA-141, TC-AUTH-MFA-142 | Web |
| 026 | `TC-AUTH-MFA-E2E-026-pembentukan-trust-device-dan-pasca-login` | 7 | TC-AUTH-MFA-143, TC-AUTH-MFA-144, TC-AUTH-MFA-145, TC-AUTH-MFA-146, TC-AUTH-MFA-147, TC-AUTH-MFA-150, TC-AUTH-MFA-151 | Web |
| 027 | `TC-AUTH-MFA-E2E-027-email-alert-login-tak-biasa-dan-reset-password` | 6 | TC-AUTH-MFA-152, TC-AUTH-MFA-153, TC-AUTH-MFA-154, TC-AUTH-MFA-155, TC-AUTH-MFA-156, TC-AUTH-MFA-157 | Web |
| 028 | `TC-AUTH-MFA-E2E-028-audit-log-mutasi-status-sukses-dan-gagal` | 11 | TC-AUTH-MFA-158, TC-AUTH-MFA-159, TC-AUTH-MFA-160, TC-AUTH-MFA-161, TC-AUTH-MFA-162, TC-AUTH-MFA-163, TC-AUTH-MFA-164, TC-AUTH-MFA-165, TC-AUTH-MFA-166, TC-AUTH-MFA-178, TC-AUTH-MFA-207 | Web |
| 029 | `TC-AUTH-MFA-E2E-029-audit-log-whitelist-policy-dan-ip-proxy-hop` | 8 | TC-AUTH-MFA-167, TC-AUTH-MFA-168, TC-AUTH-MFA-169, TC-AUTH-MFA-170, TC-AUTH-MFA-171, TC-AUTH-MFA-172, TC-AUTH-MFA-173, TC-AUTH-MFA-174 | Web |
| 030 | `TC-AUTH-MFA-E2E-030-mfa-recovery-dan-admin-reset-authenticator` | 7 | TC-AUTH-MFA-64, TC-AUTH-MFA-75, TC-AUTH-MFA-100, TC-AUTH-MFA-105, TC-AUTH-MFA-175, TC-AUTH-MFA-176, TC-AUTH-MFA-177 | Web |
| 031 | `TC-AUTH-MFA-E2E-031-session-management-dan-paritas-subscription-plan` | 9 | TC-AUTH-MFA-179, TC-AUTH-MFA-180, TC-AUTH-MFA-181, TC-AUTH-MFA-182, TC-AUTH-MFA-183, TC-AUTH-MFA-184, TC-AUTH-MFA-185, TC-AUTH-MFA-186, TC-AUTH-MFA-187 | Web |
| 032 | `TC-AUTH-MFA-E2E-032-verifikasi-isi-qr-code-dan-secret-key` | 4 | TC-AUTH-MFA-109, TC-AUTH-MFA-117, TC-AUTH-MFA-120, TC-AUTH-MFA-123 | Web |
| 033 | `TC-AUTH-MFA-E2E-033-konkurensi-multi-tab-dan-guard-double-submit` | 7 | TC-AUTH-MFA-118, TC-AUTH-MFA-119, TC-AUTH-MFA-137, TC-AUTH-MFA-191, TC-AUTH-MFA-194, TC-AUTH-MFA-195, TC-AUTH-MFA-196 | Web |
| 034 | `TC-AUTH-MFA-E2E-034-security-defense-token-tampering` | 4 | TC-AUTH-MFA-188, TC-AUTH-MFA-189, TC-AUTH-MFA-190, TC-AUTH-MFA-206 | Web |
| 035 | `TC-AUTH-MFA-E2E-035-rate-limiting-resilience-dan-toast-sticky` | 13 | TC-AUTH-MFA-12, TC-AUTH-MFA-83, TC-AUTH-MFA-84, TC-AUTH-MFA-192, TC-AUTH-MFA-193, TC-AUTH-MFA-197, TC-AUTH-MFA-198, TC-AUTH-MFA-199, TC-AUTH-MFA-201, TC-AUTH-MFA-202, TC-AUTH-MFA-203, TC-AUTH-MFA-204, TC-AUTH-MFA-205 | Web |
| 036 | `TC-AUTH-MFA-E2E-036-mobile-biometric-relogin-trigger` | 1 | TC-AUTH-MFA-54 | Mobile Native |

---

## 4. Verifikasi Integritas Data

- **Total Granular TCs:** 207
- **Unique Granular TCs:** 207
- **Missing TCs:** Tidak ada
- **Duplikasi:** Tidak ada
