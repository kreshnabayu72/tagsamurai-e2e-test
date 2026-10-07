---
id: TC-GS-ACTLOG-E2E-049-sinkronisasi-real-time-sse-isolasi-keamanan-lintas-tenant
title: "Isolasi Keamanan Real-Time SSE: Pencegahan Kebocoran Event Streaming Lintas-Tenant (Alfa vs Beta)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ACTLOG-198
coverage:
  web: automated
---

# Isolasi Keamanan Real-Time SSE: Pencegahan Kebocoran Event Streaming Lintas-Tenant (Alfa vs Beta)

## Prerequisites

- Dua sesi browser terpisah dengan kredensial berbeda: Sesi 1 pada Client Alfa, Sesi 2 pada Client Beta
- Koneksi SSE aktif pada kedua tenant

## Test Steps

### Pengujian Kebocoran Stream SSE Antar-Tenant
1. Pada Sesi Browser 1, login sebagai Total Control pada Client Alfa dan buka Activity Log > User Action.
2. Pastikan tabel Tab User Action Client Alfa dalam keadaan idle tanpa filter.
3. Pada Sesi Browser 2, login sebagai Total Control pada Client Beta dan buat data Brand 'Beta Corp'.
4. Amati layar Sesi Browser 1 (Client Alfa) secara real-time.
5. Verifikasi event pembuatan Brand 'Beta Corp' milik Client Beta TIDAK PERNAH muncul di layar Client Alfa.
6. Lakukan refresh manual (F5) pada Client Alfa, verifikasi event milik Client Beta tetap tidak pernah tercampur ke data Client Alfa.

## Notes

- Saluran SSE wajib diisolasi secara ketat per tenant ID untuk mencegah kebocoran data sensitif.
