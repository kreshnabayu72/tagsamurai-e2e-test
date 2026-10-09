---
id: TC-GS-GSET-E2E-040-security-bypass-client-dom-error-inline-per-field
title: "Bypass Client: injeksi nilai tidak valid via DOM pada kelima Select memunculkan error inline, tanpa toast sukses, dan nilai tersimpan tidak berubah"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-GSET-164
  - TC-GS-GSET-165
  - TC-GS-GSET-166
  - TC-GS-GSET-167
  - TC-GS-GSET-168
  - TC-GS-GSET-169
  - TC-GS-GSET-170
  - TC-GS-GSET-171
  - TC-GS-GSET-172
  - TC-GS-GSET-173
coverage:
  web: automated
---

# Bypass Client: injeksi nilai tidak valid via DOM pada kelima Select memunculkan error inline, tanpa toast sukses, dan nilai tersimpan tidak berubah

## Prerequisites

- Login sebagai Role: Total Control
- Record General Settings entitas tersimpan: Currency Code `IDR`, Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `Asia/Jakarta`, Session Idle Timeout `30 minutes`
- Kemampuan injeksi nilai langsung ke elemen Select via DOM (bypass pilihan dropdown FE)

## Test Steps

### Currency Code

1. Injeksi nilai kosong ke Select "Currency Code" lewat DOM, klik `[Save]`, lalu `[Change Currency]`
2. Verifikasi error inline di bawah field "Currency Code": "Currency Code must not be empty" (field bergaya error), tidak ada toast sukses, form tetap unsaved; refresh (F5) dan nilai tersimpan tidak berubah
3. Injeksi nilai `ZZZ` (di luar enum) ke Select "Currency Code" lewat DOM, klik `[Save]`, lalu `[Change Currency]`
4. Verifikasi error inline "Invalid currency code", tidak ada toast sukses, form tetap unsaved; refresh (F5) dan nilai tersimpan tidak berubah

### Time Zone

5. Injeksi nilai kosong ke Select "Time Zone" lewat DOM, klik `[Save]`
6. Verifikasi error inline "Time Zone must not be empty", tanpa toast sukses, form tetap unsaved; refresh (F5) dan nilai tersimpan tidak berubah
7. Injeksi nilai `Mars/Olympus` (bukan IANA kurasi) ke Select "Time Zone" lewat DOM, klik `[Save]`
8. Verifikasi error inline "Invalid time zone", tanpa toast sukses, form tetap unsaved; refresh (F5) dan nilai tersimpan tidak berubah

### Date Format

9. Injeksi nilai kosong ke Select "Date Format" lewat DOM, klik `[Save]`
10. Verifikasi error inline "Date Format must not be empty", tanpa toast sukses, form tetap unsaved; refresh (F5) dan nilai tersimpan tidak berubah
11. Injeksi nilai `YYYY-MM-DD` (di luar enum) ke Select "Date Format" lewat DOM, klik `[Save]`
12. Verifikasi error inline "Invalid date format", tanpa toast sukses, form tetap unsaved; refresh (F5) dan nilai tersimpan tidak berubah

### Time Format

13. Injeksi nilai kosong ke Select "Time Format" lewat DOM, klik `[Save]`
14. Verifikasi error inline "Time Format must not be empty", tanpa toast sukses, form tetap unsaved; refresh (F5) dan nilai tersimpan tidak berubah
15. Injeksi nilai `h:mm a` (di luar enum) ke Select "Time Format" lewat DOM, klik `[Save]`
16. Verifikasi error inline "Invalid time format", tanpa toast sukses, form tetap unsaved; refresh (F5) dan nilai tersimpan tidak berubah

### Session Idle Timeout

17. Injeksi nilai kosong ke Select "Session Idle Timeout" lewat DOM, klik `[Save]`
18. Verifikasi error inline "Session Idle Timeout must not be empty", tanpa toast sukses, form tetap unsaved; refresh (F5) dan nilai tersimpan tidak berubah
19. Injeksi nilai `45` (di luar enum) ke Select "Session Idle Timeout" lewat DOM, klik `[Save]`
20. Verifikasi error inline "Invalid session idle timeout value", tanpa toast sukses, form tetap unsaved; refresh (F5) dan nilai tersimpan tidak berubah

## Notes

- Spec FE+BE: injeksi via DOM di UI, namun error inline berasal dari validasi server dan nilai tersimpan di backend turut diasersi. Menggabungkan TC-GS-GSET-164 s.d. 173. Salah satu spec terbesar; bila step > 35, pecah per field.
